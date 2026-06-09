/* ═══════════════════════════════════════════════════
   CoursePath — profile.js
   Gerenciamento do perfil do usuário (Read/Update/Delete)
═══════════════════════════════════════════════════ */

// ── Abrir / Fechar modal ───────────────────────────

async function abrirPerfil() {
  const overlay = document.getElementById('profile-overlay');
  overlay.style.display = 'flex';
  voltarPerfil();
  _clearProfileErrors();

  // Pré-carrega dados do usuário
  try {
    const { ok, data } = await Api.getUser();
    if (ok) {
      document.getElementById('p-name').value  = data.user.name  || '';
      document.getElementById('p-email').value = data.user.email || '';
    }
  } catch {
    // falha silenciosa; campos ficam vazios
  }
}

function fecharPerfil(e) {
  if (e && e.target !== document.getElementById('profile-overlay')) return;
  document.getElementById('profile-overlay').style.display = 'none';
}

function voltarPerfil() {
  document.getElementById('profile-view').style.display   = 'block';
  document.getElementById('profile-delete').style.display = 'none';
  _clearProfileErrors();
}

function abrirExcluirConta() {
  document.getElementById('profile-view').style.display   = 'none';
  document.getElementById('profile-delete').style.display = 'block';
  document.getElementById('p-del-password').value = '';
  _clearProfileErrors();
}

// ── Validações locais ──────────────────────────────

function _clearProfileErrors() {
  ['err-p-name','err-p-email','err-p-password','err-p-password2',
   'err-p-global','err-p-del'].forEach(id => {
    const el = document.getElementById(id);
    if (el) el.textContent = '';
  });
}

function _setProfileErr(id, msg) {
  const el = document.getElementById(id);
  if (el) el.textContent = msg;
}

function _validarEmail(email) {
  return /^[a-zA-Z]+\.[a-zA-Z]+@ufrpe\.br$/i.test(email);
}

function _validarSenha(senha) {
  return senha.length >= 8
    && /[A-Z]/.test(senha)
    && /[a-z]/.test(senha)
    && /\d/.test(senha)
    && /[!@#$%^&*()_+\-=\[\]{}|;':",./<>?]/.test(senha);
}

// ── Salvar alterações (Update) ─────────────────────

async function salvarPerfil() {
  _clearProfileErrors();

  const name     = document.getElementById('p-name').value.trim();
  const email    = document.getElementById('p-email').value.trim().toLowerCase();
  const password = document.getElementById('p-password').value;
  const password2= document.getElementById('p-password2').value;

  let hasErr = false;

  if (!name || !/^[A-Za-zÀ-ÿ ]+$/.test(name)) {
    _setProfileErr('err-p-name', 'Use apenas letras e espaços.');
    hasErr = true;
  }
  if (!_validarEmail(email)) {
    _setProfileErr('err-p-email', 'Formato: nome.sobrenome@ufrpe.br');
    hasErr = true;
  }
  if (password && !_validarSenha(password)) {
    _setProfileErr('err-p-password', '≥8 chars, maiúscula, minúscula, número e símbolo.');
    hasErr = true;
  }
  if (password && password !== password2) {
    _setProfileErr('err-p-password2', 'As senhas não coincidem.');
    hasErr = true;
  }
  if (hasErr) return;

  const btn = document.getElementById('btn-save-profile');
  btn.disabled = true;
  btn.textContent = 'Salvando…';

  const payload = { name, email };
  if (password) payload.password = password;

  try {
    const { ok, data } = await Api.updateUser(payload);
    if (!ok) {
      _setProfileErr('err-p-global', data.error || 'Erro ao salvar.');
    } else {
      // Atualiza sessionStorage e UI
      const saved = JSON.parse(sessionStorage.getItem('cp_user') || '{}');
      saved.name  = data.user.name;
      saved.email = data.user.email;
      sessionStorage.setItem('cp_user', JSON.stringify(saved));

      // Atualiza sidebar
      const nameEl   = document.getElementById('user-name');
      const avatarEl = document.getElementById('user-avatar');
      if (nameEl)   nameEl.textContent   = data.user.name;
      if (avatarEl) avatarEl.textContent = data.user.name.charAt(0).toUpperCase();

      document.getElementById('p-password').value  = '';
      document.getElementById('p-password2').value = '';

      showToast('Perfil atualizado com sucesso ✓', 'ok');
      fecharPerfil();
    }
  } catch {
    _setProfileErr('err-p-global', 'Erro de conexão com o servidor.');
  } finally {
    btn.disabled = false;
    btn.textContent = '💾 Salvar alterações';
  }
}

// ── Confirmar exclusão (Delete) ────────────────────

async function confirmarExclusao() {
  _clearProfileErrors();
  const password = document.getElementById('p-del-password').value;

  if (!password) {
    _setProfileErr('err-p-del', 'Digite sua senha para confirmar.');
    return;
  }

  const btn = document.getElementById('btn-confirm-delete');
  btn.disabled = true;
  btn.textContent = 'Excluindo…';

  try {
    const { ok, data } = await Api.deleteUser(password);
    if (!ok) {
      _setProfileErr('err-p-del', data.error || 'Erro ao excluir conta.');
    } else {
      showToast('Conta excluída. Até mais! 👋', 'ok');
      sessionStorage.removeItem('cp_user');
      setTimeout(() => {
        window.location.href = '../../frontend/index.html';
      }, 1500);
    }
  } catch {
    _setProfileErr('err-p-del', 'Erro de conexão com o servidor.');
  } finally {
    btn.disabled = false;
    btn.textContent = 'Excluir minha conta';
  }
}
