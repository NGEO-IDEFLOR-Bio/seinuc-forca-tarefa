# 📊 Sprint Kanban + Gantt Template

Sistema completo de gestão de sprints com Kanban interativo e visualização Gantt, com salvamento automático via GitHub API.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Vercel](https://img.shields.io/badge/deploy-Vercel-black.svg)

## ✨ Features

- ✅ **Kanban Interativo**: Drag-and-drop entre colunas
- ✅ **Criação/Edição de Cards**: Modal completo com todos os campos
- ✅ **Visualização Gantt**: Timeline visual das tarefas
- ✅ **Salvamento Automático**: Commits direto no GitHub via API
- ✅ **Deploy Automático**: Vercel redesenha a cada commit
- ✅ **Tema Dark Premium**: Design moderno com paleta profissional
- ✅ **Zero Dependências**: HTML/CSS/JS puro

## 🚀 Quick Start

### 1. Copiar Template

```bash
# Copie esta pasta para seu novo repositório
cp -r sprint-kanban-template/* seu-repo/
cd seu-repo
```

### 2. Personalizar `tasks.json`

Edite `tasks.json` com suas tarefas:

```json
{
  "sprint": {
    "name": "Sprint 1",
    "startDate": "2026-01-19",
    "endDate": "2026-01-23"
  },
  "tasks": [
    {
      "id": "T001",
      "title": "Sua tarefa aqui",
      "description": "Descrição detalhada",
      "status": "todo",
      "priority": "p0",
      ...
    }
  ]
}
```

### 3. Deploy no Vercel

```bash
npm install -g vercel
vercel login
vercel
```

### 4. Configurar GitHub Token

**Criar token**:
1. https://github.com/settings/tokens
2. "Generate new token (classic)"
3. Scope: `repo` ✅
4. Copiar token

**Adicionar no Vercel**:
1. Dashboard → Settings → Environment Variables
2. Adicionar:
   - `GITHUB_TOKEN` = seu_token
   - `GITHUB_OWNER` = seu_usuario
   - `GITHUB_REPO` = nome_do_repo
3. Save

**Redeploy**:
```bash
vercel --prod
```

### 5. Conectar Repositório

1. Vercel Dashboard → Settings → Git
2. Connect Git Repository
3. Selecionar seu repo
4. ✅ Deploy automático ativado!

## 📁 Estrutura

```
sprint-kanban-template/
├── api/
│   └── save-tasks.js          # Serverless function para salvar
├── kanban.html                # Interface Kanban
├── gantt.html                 # Visualização Gantt
├── tasks.json                 # Dados das tarefas (source of truth)
├── vercel.json                # Configuração Vercel
├── package.json               # Scripts NPM
└── README.md                  # Este arquivo
```

## 🎨 Personalização

### Cores

Edite as variáveis CSS em `kanban.html` e `gantt.html`:

```css
:root {
    --primary: #2563eb;        /* Cor principal */
    --success: #10b981;        /* Verde (sucesso) */
    --warning: #f59e0b;        /* Amarelo (alerta) */
    --danger: #ef4444;         /* Vermelho (crítico) */
    /* ... */
}
```

### Colunas do Kanban

Edite a estrutura em `kanban.html` (linhas ~620-660):

```html
<div class="kanban-column" data-status="todo">
    <div class="column-header">
        <i data-lucide="inbox"></i>
        <h2>Sua Coluna</h2>
        <span class="task-count">0</span>
    </div>
    <!-- ... -->
</div>
```

### Campos das Tarefas

Edite o modal e a estrutura de dados em `tasks.json`:

```json
{
  "id": "T001",
  "title": "Título",
  "description": "Descrição",
  "status": "todo | in-progress | in-review | done",
  "priority": "p0 | p1 | p2",
  "type": "feat | fix | docs",
  "gate": "Gate opcional",
  "startDate": "2026-01-19",
  "duration": 3,
  "responsible": "Nome"
}
```

## 🔧 Como Funciona

### Fluxo de Salvamento

1. Usuário arrasta card ou cria/edita tarefa
2. Frontend chama `/api/save-tasks` (POST)
3. Serverless function:
   - Autentica com GitHub via token
   - Busca SHA atual do `tasks.json`
   - Faz commit com novo conteúdo
4. Vercel detecta commit → Redeploy automático (~30s)
5. Próximo carregamento: frontend lê arquivo atualizado

### Segurança

- ✅ Token em variável de ambiente (nunca no código)
- ✅ CORS configurado
- ✅ Validação de dados na API
- ✅ HTTPS automático (Vercel)

## 📖 Uso

### Kanban

**Mover tarefa**: Arraste o card entre colunas

**Criar tarefa**:
1. Clique em "Adicionar Card" na coluna desejada
2. Preencha os campos
3. Salvar

**Editar tarefa**:
1. Duplo-clique no card
2. Edite os campos
3. Salvar

### Gantt

- Visualização read-only
- Barras coloridas por prioridade
- Animação para tarefas em andamento
- Tooltip com descrição

## 🐛 Troubleshooting

### Erro 500 ao salvar

**Causa**: Token inválido ou variáveis não configuradas

**Solução**:
1. Verificar variáveis de ambiente no Vercel
2. Gerar novo token
3. Redeploy

### Mudanças não refletem

**Causa**: Repo não conectado ao Vercel

**Solução**:
1. Settings → Git → Connect Repository
2. Aguardar deploy automático (~30-60s)
3. Hard refresh: `Ctrl + Shift + R`

### Cards desaparecem

**Causa**: `tasks.json` vazio ou inválido

**Solução**:
1. Verificar sintaxe JSON
2. Garantir que há tarefas no array
3. Verificar console do navegador (F12)

## 📦 Deploy em Outras Plataformas

### Netlify

```bash
# netlify.toml
[build]
  publish = "."
  
[functions]
  directory = "api"
```

### Cloudflare Pages

Similar ao Vercel - adicionar variáveis de ambiente e conectar repo.

## 🤝 Contribuindo

Este é um template! Sinta-se livre para:

- Adicionar novas features
- Customizar o design
- Criar novos campos
- Integrar com outras ferramentas

## 📄 Licença

MIT License - Use como quiser!

## 💡 Créditos

Template criado para facilitar gestão ágil de sprints com persistência real via Git.

---

**Precisa de ajuda?** Abra uma issue ou consulte a documentação do Vercel.

**Gostou?** ⭐ Dê uma estrela no repo!
