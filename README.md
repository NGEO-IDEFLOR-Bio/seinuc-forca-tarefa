# 🎯 SEINUC - Força-Tarefa | Sprint Kanban

Sistema de gerenciamento de sprints com Kanban Board e Gantt Chart para o projeto SertanAI - IDEFLOR.

## 🚀 Deploy no Cloudflare Pages

### **Passo 1: Push para GitHub**

```bash
git add -A
git commit -m "Initial commit: Estrutura inicial do projeto"
git push -u origin main --force
```

### **Passo 2: Conectar ao Cloudflare Pages**

1. Acesse [dash.cloudflare.com](https://dash.cloudflare.com)
2. Vá em **Pages** → **Create a project**
3. Conecte sua conta do GitHub
4. Selecione o repositório `NGEO-IDEFLOR-Bio/seinuc-forca-tarefa`
5. Configure o build:
   - **Build command**: (deixe vazio)
   - **Build output directory**: `/`
   - **Root directory**: `/`
6. Clique em **Save and Deploy**

### **Passo 3: Configurar Variáveis de Ambiente**

Após o primeiro deploy, configure as variáveis de ambiente:

1. Vá em **Settings** → **Environment variables**
2. Adicione as seguintes variáveis:

```
GITHUB_TOKEN = seu_personal_access_token_aqui
GITHUB_OWNER = NGEO-IDEFLOR-Bio
GITHUB_REPO = seinuc-forca-tarefa
```

#### Como criar o GitHub Personal Access Token:

1. GitHub → **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)**
2. **Generate new token (classic)**
3. Selecione o escopo: `repo` (Full control of private repositories)
4. Copie o token e cole na variável `GITHUB_TOKEN` do Cloudflare

### **Passo 4: Redeploy**

Após configurar as variáveis, faça um redeploy:

1. **Deployments** → Selecione o último deploy
2. **Manage deployment** → **Retry deployment**

---

## 📁 Estrutura do Projeto

```
.
├── functions/              # Cloudflare Pages Functions (API)
│   └── api/
│       └── save-tasks.js   # Endpoint para salvar tarefas via GitHub API
├── kanban.html             # Kanban Board interativo
├── gantt.html              # Gantt Chart timeline
├── tasks.json              # Database de tarefas (JSON)
├── _headers                # Configuração de CORS e cache
└── wrangler.toml           # Configuração Cloudflare (opcional)
```

---

## 🎨 Features

### 📊 Kanban Board (`kanban.html`)
- ✅ Drag & Drop entre colunas
- ✅ Colunas: Backlog, Em Andamento, Review, Concluído
- ✅ Edição de cards (duplo-clique)
- ✅ Criação de novos cards
- ✅ Priorização (P0, P1, P2)
- ✅ Tags de tipo (Doc, Decisão, Execução, Ritual)
- ✅ Gates de projeto
- ✅ Estatísticas em tempo real

### 📅 Gantt Chart (`gantt.html`)
- ✅ Timeline visual das tarefas
- ✅ Dependências entre tarefas
- ✅ Marcos (milestones)
- ✅ Zoom e navegação
- ✅ Cores por prioridade

---

## 🔧 Desenvolvimento Local

### Requisitos
- Node.js (opcional, para usar Wrangler CLI)

### Rodando localmente com Wrangler

```bash
# Instalar Wrangler CLI
npm install -g wrangler

# Rodar servidor local
wrangler pages dev .
```

### Ou usar um servidor HTTP simples

```bash
# Python
python -m http.server 8000

# Node.js
npx serve .
```

Acesse: `http://localhost:8000/kanban.html`

---

## 📝 Como Usar

### Editar Tarefas

1. **Via Interface**: Duplo-clique em qualquer card no Kanban
2. **Via JSON**: Edite `tasks.json` diretamente e faça commit

### Adicionar Novas Tarefas

1. Clique em **"+ Adicionar Card"** em qualquer coluna
2. Preencha o formulário
3. Salvar → Commit automático no GitHub

### Mover Tarefas

- Arraste e solte cards entre as colunas
- Salvar → Atualiza `tasks.json` automaticamente

---

## 🌐 Stack Tecnológica

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Icons**: Lucide Icons
- **Hosting**: Cloudflare Pages
- **API**: Cloudflare Pages Functions (Workers)
- **Database**: JSON File + GitHub API
- **CI/CD**: GitHub Actions (automático via Cloudflare)

---

## 👥 Equipe

**Desenvolvedor**: Samuel Santos  
**Email**: samuelsantosambiental@gmail.com  
**Organização**: NGEO-IDEFLOR-Bio

---

## 📄 Licença

Este projeto é de uso interno da IDEFLOR.

---

## 🆘 Suporte

Para dúvidas ou problemas:
1. Abra uma issue no repositório
2. Entre em contato com a equipe de desenvolvimento

---

**✨ Happy Coding!**
