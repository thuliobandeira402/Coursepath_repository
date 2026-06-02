const API_BASE = 'http://localhost:5000/api';

function _getUserId() {
  const saved = sessionStorage.getItem('cp_user');
  if (!saved) return null;
  return JSON.parse(saved).id;
}

const Api = {
  async _req(method, path, body = null) {
    const userId = _getUserId();
    const opts = {
      method,
      headers: {
        'Content-Type': 'application/json',
        ...(userId ? { 'X-User-Id': String(userId) } : {})
      },
    };
    if (body) opts.body = JSON.stringify(body);
    const res = await fetch(API_BASE + path, opts);
    const data = await res.json();
    return { ok: res.ok, status: res.status, data };
  },

  register: (name, email, password) =>
    Api._req('POST', '/register', { name, email, password }),
  login: (email, password) =>
    Api._req('POST', '/login', { email, password }),
  logout: () => { sessionStorage.removeItem('cp_user'); return Promise.resolve({ ok: true }); },
  me: () => Api._req('GET', '/me'),

  getArticles: (semester = null) =>
    Api._req('GET', semester ? `/articles?semester=${semester}` : '/articles'),
  getArticle: (id) => Api._req('GET', `/articles/${id}`),
  markRead: (id) => Api._req('POST', `/articles/${id}/read`),
  getReadArticles: () => Api._req('GET', '/articles/read'),
  toggleFavorite: (id) => Api._req('POST', `/articles/${id}/favorite`),
  getFavorites: () => Api._req('GET', '/articles/favorites'),
  getSummary: (id) => Api._req('GET', `/articles/${id}/summary`),
  generateQuiz: (id, summary = '') =>
    Api._req('POST', `/articles/${id}/quiz`, { summary }),
};

function showToast(msg, type = '') {
  let t = document.getElementById('__toast');
  if (!t) {
    t = document.createElement('div');
    t.id = '__toast';
    t.className = 'toast';
    document.body.appendChild(t);
  }
  t.textContent = msg;
  t.className = 'toast ' + type;
  void t.offsetWidth;
  t.classList.add('show');
  clearTimeout(t._timer);
  t._timer = setTimeout(() => t.classList.remove('show'), 2800);
}