/* ═══════════════════════════════════════════════════
   CoursePath — dashboard.js
   Lógica completa do dashboard: artigos, filtros,
   modal, resumo com IA, quiz, favoritos, lidos.
═══════════════════════════════════════════════════ */

// ── Estado global ──────────────────────────────────
let state = {
  user: null,
  allArticles: [],
  filteredArticles: [],
  currentView: 'todos',
  activeSubject: null,
  currentArticle: null,
  currentSummary: '',
  summaryGenerated: false,
  quizData: null,
  quizAnswers: [],
};

// ── Init ───────────────────────────────────────────
(async () => {
  // Verifica autenticação
const saved = sessionStorage.getItem('cp_user');
if (!saved) { window.location.href = '../index.html'; return; }
state.user = JSON.parse(saved);

  // Preenche UI do usuário
  const initials = (state.user.name || '?').split(' ').map(w => w[0]).slice(0,2).join('').toUpperCase();
  document.getElementById('user-name').textContent = state.user.name || 'Usuário';
  document.getElementById('user-avatar').textContent = initials;

  await carregarArtigos();
})();

// ── Trocar tema claro/escuro ────────────────────────

function trocar_tema() {
  const html = document.documentElement;
  const btn  = document.querySelector('.changetheme-btn');

  if (html.classList.contains('dark')) {
    // Voltar ao tema escuro (padrão)
    html.classList.remove('dark');
    localStorage.setItem('theme', 'dark');
    if (btn) btn.title = 'Modo claro';
  } else {
    // Ativar tema claro
    html.classList.add('dark');
    localStorage.setItem('theme', 'light');
    if (btn) btn.title = 'Modo escuro';
  }
}

// Aplica o tema salvo assim que o script carrega
(function aplicarTemaSalvo() {
  const tema = localStorage.getItem('theme');
  const btn  = document.querySelector('.changetheme-btn');
  if (tema === 'light') {
    document.documentElement.classList.add('dark');
    if (btn) btn.title = 'Modo escuro';
  } else {
    document.documentElement.classList.remove('dark');
    if (btn) btn.title = 'Modo claro';
  }
})();


// ── Carregamento de artigos ─────────────────────────
async function carregarArtigos(semester = null) {
  mostrarLoading();

  try {
    let res;
    if (state.currentView === 'lidos') {
      res = await Api.getReadArticles();
    } else if (state.currentView === 'favoritos') {
      res = await Api.getFavorites();
    } else {
      res = await Api.getArticles(semester);
    }

    if (!res.ok) throw new Error(res.data.error);
    state.allArticles = res.data;
    state.filteredArticles = [...state.allArticles];

    buildFilterTags();
    renderArticles();
    updateStats();
  } catch (e) {
    document.getElementById('articles-grid').innerHTML = `
      <div class="empty-state">
        <span class="empty-icon">⚠</span>
        <p>Erro ao carregar artigos. Verifique se o servidor está rodando.</p>
        <small style="color:var(--err)">${e.message}</small>
      </div>`;
  }
}

function mostrarLoading() {
  document.getElementById('articles-grid').innerHTML = `
    <div class="loading-state">
      <div class="spinner"></div>
      <p>Carregando artigos…</p>
    </div>`;
}

// ── Filtros de disciplina (tags) ───────────────────
function buildFilterTags() {
  const subjects = [...new Set(state.allArticles.map(a => a.subject))];
  const bar = document.getElementById('filter-tags');
  bar.innerHTML = '';

  const allBtn = criarTag('Todas', null);
  allBtn.classList.add('active');
  bar.appendChild(allBtn);

  subjects.forEach(s => bar.appendChild(criarTag(s, s)));
}

function criarTag(label, value) {
  const btn = document.createElement('button');
  btn.className = 'filter-tag';
  btn.textContent = label;
  btn.onclick = () => {
    document.querySelectorAll('.filter-tag').forEach(t => t.classList.remove('active'));
    btn.classList.add('active');
    state.activeSubject = value;
    filtrarArtigos();
  };
  return btn;
}

function filtrarArtigos() {
  const q = (document.getElementById('search-input').value || '').toLowerCase();
  state.filteredArticles = state.allArticles.filter(a => {
    const matchSearch = !q
      || a.title.toLowerCase().includes(q)
      || a.authors.toLowerCase().includes(q)
      || a.subject.toLowerCase().includes(q)
      || a.introduction.toLowerCase().includes(q);
    const matchSubject = !state.activeSubject || a.subject === state.activeSubject;
    return matchSearch && matchSubject;
  });
  renderArticles();
}

// ── Render grid ────────────────────────────────────
function renderArticles() {
  const grid = document.getElementById('articles-grid');

  if (!state.filteredArticles.length) {
    grid.innerHTML = `
      <div class="empty-state">
        <span class="empty-icon">◌</span>
        <p>Nenhum artigo encontrado.</p>
      </div>`;
    return;
  }

  grid.innerHTML = '';
  state.filteredArticles.forEach((a, i) => {
    const card = document.createElement('div');
    card.className = 'article-card';
    card.style.animationDelay = `${i * 0.04}s`;
    card.innerHTML = buildCardHTML(a);
    card.addEventListener('click', (e) => {
      // Evita abrir modal ao clicar nos botões de ação
      if (e.target.closest('.card-action-btn') || e.target.closest('.card-read-link')) return;
      abrirModal(a.id);
    });
    grid.appendChild(card);
  });
}

function buildCardHTML(a) {
  const semLabel = `${a.semester}º Semestre`;
  const readBadge = a.is_read ? `<span class="badge badge-read">✓ Lido</span>` : '';
  const favBadge  = a.is_favorite ? `<span class="badge badge-fav">♥ Favorito</span>` : '';

  return `
    <div class="card-badges">
      <span class="badge badge-semester">${semLabel}</span>
      <span class="badge badge-subject">${a.subject}</span>
      ${readBadge}${favBadge}
    </div>
    <h3 class="card-title">${a.title}</h3>
    <p class="card-authors">${a.authors}</p>
    <p class="card-intro">${a.introduction}</p>
    <div class="card-footer">
      <a class="card-read-link" href="${a.link}" target="_blank" rel="noopener" onclick="event.stopPropagation()">
        🔗 Abrir artigo
      </a>
      <div class="card-actions">
        <button class="card-action-btn ${a.is_read ? 'is-read' : ''}"
          title="${a.is_read ? 'Lido' : 'Marcar como lido'}"
          onclick="event.stopPropagation(); quickMarkRead(${a.id}, this)">✓</button>
        <button class="card-action-btn ${a.is_favorite ? 'is-fav' : ''}"
          title="${a.is_favorite ? 'Remover favorito' : 'Favoritar'}"
          onclick="event.stopPropagation(); quickFav(${a.id}, this)">♥</button>
      </div>
    </div>`;
}

// ── Ações rápidas no card ──────────────────────────
async function quickMarkRead(id, btn) {
  await Api.markRead(id);
  btn.classList.add('is-read');
  btn.title = 'Lido';
  const a = state.allArticles.find(x => x.id === id);
  if (a) a.is_read = true;
  showToast('Marcado como lido ✓', 'ok');
  // Adiciona badge lido ao card
  const badges = btn.closest('.article-card').querySelector('.card-badges');
  if (!badges.querySelector('.badge-read')) {
    const b = document.createElement('span');
    b.className = 'badge badge-read';
    b.textContent = '✓ Lido';
    badges.appendChild(b);
  }
}

async function quickFav(id, btn) {
  const { ok, data } = await Api.toggleFavorite(id);
  if (!ok) return;
  const a = state.allArticles.find(x => x.id === id);
  if (data.favorited) {
    btn.classList.add('is-fav');
    btn.title = 'Remover favorito';
    if (a) a.is_favorite = true;
    showToast('Adicionado aos favoritos ♥', 'ok');
    const badges = btn.closest('.article-card').querySelector('.card-badges');
    if (!badges.querySelector('.badge-fav')) {
      const b = document.createElement('span');
      b.className = 'badge badge-fav';
      b.textContent = '♥ Favorito';
      badges.appendChild(b);
    }
  } else {
    btn.classList.remove('is-fav');
    btn.title = 'Favoritar';
    if (a) a.is_favorite = false;
    showToast('Removido dos favoritos', '');
    const fBadge = btn.closest('.article-card').querySelector('.badge-fav');
    if (fBadge) fBadge.remove();
  }
}

// ── Stats no topbar ────────────────────────────────
function updateStats() {
  const total = state.allArticles.length;
  const lidos = state.allArticles.filter(a => a.is_read).length;
  const favs  = state.allArticles.filter(a => a.is_favorite).length;

  if (state.currentView === 'todos' || state.currentView.startsWith('semestre')) {
    document.getElementById('topbar-stats').innerHTML = `
      <span class="stat-chip">📖 <span class="stat-num">${lidos}</span>/${total} lidos</span>
      <span class="stat-chip">♥ <span class="stat-num">${favs}</span> favoritos</span>`;
  } else {
    document.getElementById('topbar-stats').innerHTML =
      `<span class="stat-chip"><span class="stat-num">${total}</span> artigos</span>`;
  }
}

// ── Navegação de views ─────────────────────────────
const VIEW_TITLES = {
  todos:     'Todos os Artigos',
  semestre1: '1º Semestre',
  semestre2: '2º Semestre',
  lidos:     'Artigos Lidos',
  favoritos: 'Favoritos',
};

async function setView(view) {
  state.currentView = view;
  state.activeSubject = null;
  document.getElementById('search-input').value = '';

  // Nav active
  document.querySelectorAll('.nav-item').forEach(b => {
    b.classList.toggle('active', b.dataset.view === view);
  });
  document.getElementById('topbar-title').textContent = VIEW_TITLES[view] || view;

  // Sidebar mobile fecha
  document.getElementById('sidebar').classList.remove('open');

  let semester = null;
  if (view === 'semestre1') semester = 1;
  if (view === 'semestre2') semester = 2;

  await carregarArtigos(semester);
}

// ── Sidebar mobile ─────────────────────────────────
function toggleSidebar() {
  document.getElementById('sidebar').classList.toggle('open');
}

// ── Logout ─────────────────────────────────────────
async function logout() {
  await Api.logout();
  sessionStorage.removeItem('cp_user');
  window.location.href = '../index.html';
}

// ══════════════════════════════════════════════════
// MODAL
// ══════════════════════════════════════════════════

async function abrirModal(id) {
  // Reset estado do modal
  state.currentArticle = null;
  state.currentSummary = '';
  state.summaryGenerated = false;
  state.quizData = null;
  state.quizAnswers = [];

  // Reseta conteúdo
  document.getElementById('resumo-body').innerHTML =
    `<p class="resumo-placeholder">Clique em "Gerar Resumo" para criar um resumo inteligente deste artigo.</p>`;
  document.getElementById('quiz-body').innerHTML = '';
  document.getElementById('section-quiz').style.display = 'none';
  document.getElementById('section-translate').style.display = 'none';
  document.getElementById('translate-body').innerHTML = '';
  document.getElementById('btn-quiz').textContent = 'Iniciar Quiz';
  document.getElementById('btn-resumo').disabled = false;
  document.getElementById('btn-resumo').textContent = 'Gerar Resumo';
  const btnCopiar = document.getElementById('btn-copiar-resumo');
  if (btnCopiar) btnCopiar.style.display = 'none';

  // Busca artigo
  const { ok, data } = await Api.getArticle(id);
  if (!ok) { showToast('Erro ao abrir artigo', 'err'); return; }
  state.currentArticle = data;

  // Preenche header
  document.getElementById('m-semester').textContent = `${data.semester}º Semestre`;
  document.getElementById('m-subject').textContent = data.subject;
  document.getElementById('m-title').textContent = data.title;
  document.getElementById('m-authors').textContent = data.authors;
  document.getElementById('m-intro').textContent = data.introduction;
  document.getElementById('m-link').href = data.link;

  // Botões de status
  const btnRead = document.getElementById('btn-mark-read');
  const btnFav  = document.getElementById('btn-fav');

  if (data.is_read) {
    btnRead.textContent = '✓ Já lido';
    btnRead.classList.add('active-read');
  } else {
    btnRead.textContent = '✓ Marcar como lido';
    btnRead.classList.remove('active-read');
  }

  if (data.is_favorite) {
    btnFav.textContent = '♥ Favoritado';
    btnFav.classList.add('active-fav');
  } else {
    btnFav.textContent = '♡ Favoritar';
    btnFav.classList.remove('active-fav');
  }

  // Se já está lido, mostra botão de quiz
  if (data.is_read) {
    document.getElementById('section-quiz').style.display = 'block';
  }

  // Abre overlay
  const overlay = document.getElementById('modal-overlay');
  overlay.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function fecharModal(event) {
  if (event && event.target !== document.getElementById('modal-overlay') && !event.target.classList.contains('modal-close')) {
    if (event.target !== document.getElementById('modal-overlay')) return;
  }
  document.getElementById('modal-overlay').classList.remove('open');
  document.body.style.overflow = '';
}

// Fecha modal com Escape
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') fecharModal({ target: document.getElementById('modal-overlay') });
});

// ── Marcar lido (do modal) ─────────────────────────
async function marcarLido() {
  if (!state.currentArticle) return;
  const id = state.currentArticle.id;

  await Api.markRead(id);
  state.currentArticle.is_read = true;

  const btn = document.getElementById('btn-mark-read');
  btn.textContent = '✓ Já lido';
  btn.classList.add('active-read');

  // Mostra quiz
  document.getElementById('section-quiz').style.display = 'block';

  // Atualiza card no grid
  const a = state.allArticles.find(x => x.id === id);
  if (a) { a.is_read = true; renderArticles(); }

  showToast('Marcado como lido ✓', 'ok');
}

// ── Toggle favorito (do modal) ─────────────────────
async function toggleFavorito() {
  if (!state.currentArticle) return;
  const id = state.currentArticle.id;

  const { ok, data } = await Api.toggleFavorite(id);
  if (!ok) { showToast('Erro ao favoritar', 'err'); return; }

  const btn = document.getElementById('btn-fav');
  const a = state.allArticles.find(x => x.id === id);

  if (data.favorited) {
    state.currentArticle.is_favorite = true;
    btn.textContent = '♥ Favoritado';
    btn.classList.add('active-fav');
    if (a) a.is_favorite = true;
    showToast('Adicionado aos favoritos ♥', 'ok');
  } else {
    state.currentArticle.is_favorite = false;
    btn.textContent = '♡ Favoritar';
    btn.classList.remove('active-fav');
    if (a) a.is_favorite = false;
    showToast('Removido dos favoritos', '');
  }

  if (state.currentView === 'favoritos') { await carregarArtigos(); }
  else renderArticles();
}

// ══════════════════════════════════════════════════
// RESUMO COM IA
// ══════════════════════════════════════════════════

async function gerarResumo() {
  if (!state.currentArticle) return;

  const btn = document.getElementById('btn-resumo');
  const body = document.getElementById('resumo-body');

  btn.disabled = true;
  btn.textContent = 'Gerando…';

  body.innerHTML = `
    <div class="resumo-loading">
      <div class="spinner"></div>
      Gerando resumo com IA… isso pode levar alguns segundos.
    </div>`;

  try {
    const { ok, data } = await Api.getSummary(state.currentArticle.id);
    if (!ok) throw new Error(data.error);

    state.currentSummary = data.summary;
    state.summaryGenerated = true;

    // Renderiza markdown simples
    body.innerHTML = renderMarkdown(data.summary);

    btn.textContent = '↺ Gerar novamente';
    btn.disabled = false;

    // Mostra botão de copiar
    const btnCopiar = document.getElementById('btn-copiar-resumo');
    if (btnCopiar) btnCopiar.style.display = 'inline-flex';

    // Libera quiz se já lido
    if (state.currentArticle.is_read) {
      document.getElementById('section-quiz').style.display = 'block';
      showToast('Resumo gerado! Agora você pode fazer o quiz ◎', 'ok');
    }

  } catch (e) {
    body.innerHTML = `<p style="color:var(--err)">Erro ao gerar resumo:  IA temporariamente indisponível, tente novamente</p>`;
    btn.disabled = false;
    btn.textContent = 'Tentar novamente';
  }
}

// Renderizador de markdown simples (sem dependências)
function renderMarkdown(text) {
  // Escapa HTML para evitar XSS
  const esc = s => s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
  
  const lines = text.split('\n');
  const out = [];
  let inUl = false;

  for (let line of lines) {
    // Separador horizontal (--- ou ***) — ignora, não renderiza nada
    if (/^[-*]{3,}\s*$/.test(line.trim())) {
      if (inUl) { out.push('</ul>'); inUl = false; }
      // apenas pula, sem adicionar nada
      continue;
    // Headers
    } else if (/^### /.test(line)) {
      if (inUl) { out.push('</ul>'); inUl = false; }
      out.push(`<h3>${esc(line.slice(4))}</h3>`);
    } else if (/^## /.test(line)) {
      if (inUl) { out.push('</ul>'); inUl = false; }
      out.push(`<h3>${esc(line.slice(3))}</h3>`);
    } else if (/^# /.test(line)) {
      if (inUl) { out.push('</ul>'); inUl = false; }
      out.push(`<h3>${esc(line.slice(2))}</h3>`);
    // Listas (só entra aqui se NÃO for separador)
    } else if (/^\s*[-*] /.test(line)) {
      if (!inUl) { out.push('<ul>'); inUl = true; }
      const content = line.replace(/^\s*[-*] /, '');
      out.push(`<li>${esc(content).replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')}</li>`);
    // Linha vazia
    } else if (line.trim() === '') {
      if (inUl) { out.push('</ul>'); inUl = false; }
      out.push('<br>');
    // Parágrafo normal
    } else {
      if (inUl) { out.push('</ul>'); inUl = false; }
      const formatted = esc(line).replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
      out.push(`<p>${formatted}</p>`);
    }
  }
  if (inUl) out.push('</ul>');
  return out.join('\n');
}

// ══════════════════════════════════════════════════
// QUIZ
// ══════════════════════════════════════════════════

async function iniciarQuiz() {
  if (!state.currentArticle) return;
  if (!state.currentArticle.is_read) {
    showToast('Marque o artigo como lido primeiro', 'err');
    return;
  }

  const btn = document.getElementById('btn-quiz');
  const body = document.getElementById('quiz-body');

  btn.disabled = true;
  btn.textContent = 'Gerando quiz…';

  body.innerHTML = `
    <div class="resumo-loading">
      <div class="spinner"></div>
      Gerando quiz personalizado… aguarde.
    </div>`;

  try {
    const { ok, data } = await Api.generateQuiz(state.currentArticle.id, state.currentSummary);
    if (!ok) throw new Error(data.error);

    state.quizData = data;
    state.quizAnswers = new Array(data.questions.length).fill(null);

    renderQuiz();

    btn.textContent = '↺ Novo Quiz';
    btn.disabled = false;
  } catch (e) {
    body.innerHTML = `<p style="color:var(--err)">Erro ao gerar quiz:  IA temporariamente indisponível, tente novamente</p>`;
    btn.disabled = false;
    btn.textContent = 'Tentar novamente';
  }
}

function renderQuiz() {
  if (!state.quizData) return;
  const body = document.getElementById('quiz-body');
  body.innerHTML = '';

  state.quizData.questions.forEach((q, qi) => {
    const div = document.createElement('div');
    div.className = 'quiz-question';
    div.style.animationDelay = `${qi * 0.07}s`;
    div.innerHTML = `
      <p class="quiz-q-num">QUESTÃO ${qi + 1} de ${state.quizData.questions.length}</p>
      <p class="quiz-q-text">${q.question}</p>
      <div class="quiz-options" id="opts-${qi}">
        ${q.options.map((opt, oi) => `
          <button class="quiz-option" data-qi="${qi}" data-oi="${oi}" onclick="responderQuiz(${qi}, ${oi})">
            ${opt}
          </button>`).join('')}
      </div>
      <div class="quiz-explanation" id="exp-${qi}">${q.explanation}</div>`;
    body.appendChild(div);
  });
}

function responderQuiz(qi, oi) {
  if (state.quizAnswers[qi] !== null) return; // já respondeu
  const q = state.quizData.questions[qi];
  state.quizAnswers[qi] = oi;

  // Marca respostas
  const opts = document.querySelectorAll(`#opts-${qi} .quiz-option`);
  opts.forEach((btn, i) => {
    btn.disabled = true;
    if (i === q.correct) btn.classList.add('correct');
    else if (i === oi) btn.classList.add('wrong');
  });

  // Mostra explicação
  document.getElementById(`exp-${qi}`).classList.add('show');

  // Verifica se respondeu tudo
  if (state.quizAnswers.every(a => a !== null)) {
    setTimeout(mostrarResultadoQuiz, 600);
  }
}

function mostrarResultadoQuiz() {
  const total = state.quizData.questions.length;
  const acertos = state.quizAnswers.filter((a, i) =>
    a === state.quizData.questions[i].correct
  ).length;

  const pct = Math.round((acertos / total) * 100);
  const msg = pct === 100 ? '🎉 Perfeito! Você dominou o assunto!'
    : pct >= 80 ? '✨ Excelente! Você entendeu muito bem o artigo.'
    : pct >= 60 ? '📖 Bom trabalho! Revise os pontos errados.'
    : '💡 Vale reler o artigo e o resumo antes de refazer.';

  const resultDiv = document.createElement('div');
  resultDiv.className = 'quiz-result';
  resultDiv.innerHTML = `
    <span class="result-score">${acertos}/${total}</span>
    <span class="result-label">${pct}% de acerto</span>
    <p class="result-msg">${msg}</p>`;

  document.getElementById('quiz-body').appendChild(resultDiv);
  resultDiv.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

// ── Tradução de introdução ─────────────────────────

async function traduzirIntroducao() {
  const secao = document.getElementById('section-translate');
  const corpo = document.getElementById('translate-body');
  const lang  = document.getElementById('lang-select')?.value || 'pt';

  if (!state.currentArticle) return;

  secao.style.display = 'block';
  corpo.innerHTML = '<div style="display:flex;align-items:center;gap:8px;color:var(--muted,#888);"><div class="spinner" style="width:18px;height:18px;border-width:2px;"></div> Traduzindo…</div>';

  try {
    const { ok, data } = await Api.translateIntroduction(state.currentArticle.id, lang);
    if (!ok) {
      corpo.innerHTML = `<p style="color:#f38ba8;">⚠️ ${data.error || 'Erro na tradução.'}</p>`;
    } else {
      corpo.innerHTML = `<p style="line-height:1.7;font-size:14px;">${data.translated}</p>`;
    }
  } catch {
    corpo.innerHTML = '<p style="color:#f38ba8;">⚠️ Erro de conexão.</p>';
  }
}

// ══════════════════════════════════════════════════
// COPIAR RESUMO
// ══════════════════════════════════════════════════
async function copiarResumo() {
  if (!state.currentSummary) return;

  const btn = document.getElementById('btn-copiar-resumo');
  try {
    await navigator.clipboard.writeText(state.currentSummary);
    btn.textContent = '✓ Copiado!';
    setTimeout(() => { btn.textContent = '📋 Copiar'; }, 2000);
    showToast('Resumo copiado para a área de transferência ✓', 'ok');
  } catch {
    // Fallback para navegadores mais antigos
    const ta = document.createElement('textarea');
    ta.value = state.currentSummary;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    document.body.removeChild(ta);
    btn.textContent = '✓ Copiado!';
    setTimeout(() => { btn.textContent = '📋 Copiar'; }, 2000);
    showToast('Resumo copiado! ✓', 'ok');
  }
}

// ══════════════════════════════════════════════════
// MODAL — ADICIONAR ARTIGO
// ══════════════════════════════════════════════════

function abrirModalAdicionar() {
  // Limpa campos
  ['add-title','add-authors','add-subject','add-link','add-introduction'].forEach(id => {
    const el = document.getElementById(id);
    if (el) el.value = '';
  });
  document.getElementById('add-semester').value = '';
  ['err-add-title','err-add-authors','err-add-subject','err-add-semester',
   'err-add-intro','err-add-link','err-add-global'].forEach(id => {
    const el = document.getElementById(id);
    if (el) el.textContent = '';
  });
  const btn = document.getElementById('btn-add-submit');
  if (btn) { btn.disabled = false; btn.textContent = '＋ Adicionar Artigo'; }

  // Fecha sidebar mobile
  document.getElementById('sidebar').classList.remove('open');

  const overlay = document.getElementById('add-article-overlay');
  overlay.style.display = 'flex';
  document.body.style.overflow = 'hidden';
}

function fecharModalAdicionar(event) {
  if (event && event.target !== document.getElementById('add-article-overlay')) return;
  document.getElementById('add-article-overlay').style.display = 'none';
  document.body.style.overflow = '';
}

async function submeterNovoArtigo() {
  // Limpa erros
  ['err-add-title','err-add-authors','err-add-subject','err-add-semester',
   'err-add-intro','err-add-link','err-add-global'].forEach(id => {
    const el = document.getElementById(id);
    if (el) el.textContent = '';
  });

  const title        = document.getElementById('add-title').value.trim();
  const authors      = document.getElementById('add-authors').value.trim();
  const subject      = document.getElementById('add-subject').value.trim();
  const semesterVal  = document.getElementById('add-semester').value;
  const introduction = document.getElementById('add-introduction').value.trim();
  const link         = document.getElementById('add-link').value.trim();

  let valid = true;
  if (!title) { document.getElementById('err-add-title').textContent = 'Título obrigatório.'; valid = false; }
  if (!authors) { document.getElementById('err-add-authors').textContent = 'Autores obrigatórios.'; valid = false; }
  if (!subject) { document.getElementById('err-add-subject').textContent = 'Disciplina obrigatória.'; valid = false; }
  if (!semesterVal) { document.getElementById('err-add-semester').textContent = 'Selecione o semestre.'; valid = false; }
  if (!introduction) { document.getElementById('err-add-intro').textContent = 'Introdução obrigatória.'; valid = false; }
  if (!link) { document.getElementById('err-add-link').textContent = 'Link obrigatório.'; valid = false; }
  if (!valid) return;

  const btn = document.getElementById('btn-add-submit');
  btn.disabled = true;
  btn.textContent = 'Salvando…';

  try {
    const res = await fetch('http://localhost:5000/api/articles', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-User-Id': state.user?.id || ''
      },
      body: JSON.stringify({
        title, authors, subject,
        semester: parseInt(semesterVal),
        introduction, link
      })
    });
    const data = await res.json();

    if (!res.ok) {
      document.getElementById('err-add-global').textContent = data.error || 'Erro ao salvar artigo.';
      btn.disabled = false;
      btn.textContent = '＋ Adicionar Artigo';
      return;
    }

    showToast('Artigo adicionado com sucesso! ✓', 'ok');
    fecharModalAdicionar();
    // Recarrega lista
    await carregarArtigos();
  } catch (e) {
    document.getElementById('err-add-global').textContent = 'Erro de conexão com o servidor.';
    btn.disabled = false;
    btn.textContent = '＋ Adicionar Artigo';
  }
}

// Fecha modal adicionar com Escape
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') {
    const overlay = document.getElementById('add-article-overlay');
    if (overlay && overlay.style.display === 'flex') fecharModalAdicionar();
  }
});
