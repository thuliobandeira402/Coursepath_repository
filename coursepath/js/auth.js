/* ═══════════════════════════════════════════════════
   CoursePath — auth.js
   Lógica de login e cadastro.
═══════════════════════════════════════════════════ */

// ── Utilitários ────────────────────────────────────
function clearErrors() {
  document.querySelectorAll('.field-err').forEach(el => el.textContent = '');
  document.querySelectorAll('.field input').forEach(el => el.classList.remove('invalid'));
}

function setErr(id, msg) {
  const el = document.getElementById(id);
  if (el) { el.textContent = msg; }
  // marca input inválido
  const inputId = id.replace('err-', '');
  const input = document.getElementById(inputId);
  if (input) input.classList.add('invalid');
}

function irParaCadastro() {
  clearErrors();
  document.getElementById('sec-login').classList.remove('active');
  document.getElementById('sec-cadastro').classList.add('active');
}

function irParaLogin() {
  clearErrors();
  document.getElementById('sec-cadastro').classList.remove('active');
  document.getElementById('sec-login').classList.add('active');
}

// Validações locais
function validarEmail(email) {
  return /^[a-zA-Z]+\.[a-zA-Z]+@ufrpe\.br$/i.test(email);
}
function validarSenha(senha) {
  return senha.length >= 8
    && /[A-Z]/.test(senha)
    && /[a-z]/.test(senha)
    && /\d/.test(senha)
    && /[!@#$%^&*()_+\-=\[\]{}|;':",.\/<>?]/.test(senha);
}

// ── LOGIN ──────────────────────────────────────────
document.getElementById('btn-login').addEventListener('click', async () => {
  clearErrors();

  const email = document.getElementById('login-email').value.trim().toLowerCase();
  const senha = document.getElementById('login-senha').value;
  let hasErr = false;

  if (!validarEmail(email)) {
    setErr('err-login-email', 'Formato: nome.sobrenome@ufrpe.br');
    hasErr = true;
  }
  if (!senha) {
    setErr('err-login-senha', 'Digite sua senha.');
    hasErr = true;
  }
  if (hasErr) return;

  const btn = document.getElementById('btn-login');
  btn.disabled = true;
  btn.textContent = 'Entrando…';

  try {
    const { ok, data } = await Api.login(email, senha);
    if (!ok) {
      setErr('err-login-global', data.error || 'Falha no login.');
    } else {
      showToast('Login realizado! ✓', 'ok');
      // Guarda nome localmente para uso imediato no dashboard
      sessionStorage.setItem('cp_user', JSON.stringify(data.user));
      setTimeout(() => {
        window.location.href = 'pages/dashboard.html';
      }, 500);
    }
  } catch {
    setErr('err-login-global', 'Erro de conexão com o servidor.');
  } finally {
    btn.disabled = false;
    btn.textContent = 'Entrar';
  }
});

// Enter no campo de senha faz login
document.getElementById('login-senha').addEventListener('keydown', e => {
  if (e.key === 'Enter') document.getElementById('btn-login').click();
});

// ── CADASTRO ───────────────────────────────────────
document.getElementById('btn-cadastro').addEventListener('click', async () => {
  clearErrors();

  const nome     = document.getElementById('cad-nome').value.trim();
  const email    = document.getElementById('cad-email').value.trim().toLowerCase();
  const senha    = document.getElementById('cad-senha').value;
  const confirma = document.getElementById('cad-confirma').value;
  let hasErr = false;

  if (!nome || !/^[A-Za-zÀ-ÿ ]+$/.test(nome)) {
    setErr('err-cad-nome', 'Use apenas letras e espaços.');
    hasErr = true;
  }
  if (!validarEmail(email)) {
    setErr('err-cad-email', 'Formato: nome.sobrenome@ufrpe.br');
    hasErr = true;
  }
  if (!validarSenha(senha)) {
    setErr('err-cad-senha', '≥8 chars, maiúscula, minúscula, número e símbolo.');
    hasErr = true;
  }
  if (senha !== confirma) {
    setErr('err-cad-confirma', 'As senhas não coincidem.');
    hasErr = true;
  }
  if (hasErr) return;

  const btn = document.getElementById('btn-cadastro');
  btn.disabled = true;
  btn.textContent = 'Criando conta…';

  try {
    const { ok, data } = await Api.register(nome, email, senha);
    if (!ok) {
      setErr('err-cad-global', data.error || 'Erro ao criar conta.');
    } else {
      showToast('Conta criada! Faça login ✓', 'ok');
      setTimeout(() => irParaLogin(), 1200);
    }
  } catch {
    setErr('err-cad-global', 'Erro de conexão com o servidor.');
  } finally {
    btn.disabled = false;
    btn.textContent = 'Criar conta';
  }
});

// ── Verifica se já está logado e redireciona ────────
(async () => {
  try {
    const { ok } = await Api.me();
    if (ok) window.location.href = 'pages/dashboard.html';
  } catch { /* não logado, fica na tela */ }
})();
