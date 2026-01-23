# Guia de Uso Rápido

## Checklist de Setup (10 minutos)

> **IMPORTANTE**: Este template requer integração GitHub para funcionar!
> O salvamento automático faz commits direto no repositório.

### Passo 1: Criar Novo Repositório

1. Vá em: https://github.com/new
2. Nome: `meu-sprint-kanban` (ou qualquer nome)
3. Privado ou Público (sua escolha)
4. **NÃO** adicione README, .gitignore ou license
5. Create repository

### Passo 2: Copiar Template

```bash
# Na pasta onde está o template
cd sprint-kanban-template

# Inicializar Git
git init
git add .
git commit -m "feat: Initial commit from template"

# Conectar ao seu repo
git remote add origin https://github.com/SEU-USUARIO/meu-sprint-kanban.git
git branch -M main
git push -u origin main
```

### Passo 3: Customizar Tasks

Edite `tasks.json` com suas tarefas reais:

```json
{
  "sprint": {
    "name": "Minha Sprint",
    "startDate": "2026-01-27",  // Segunda-feira
    "endDate": "2026-01-31",     // Sexta-feira
    "goal": "Entregar MVP do produto"
  },
  "tasks": [
    {
      "id": "T001",
      "title": "Minha primeira tarefa",
      // ... seus campos
    }
  ]
}
```

### Passo 4: Deploy no Vercel via GitHub

**Opção A: Via Dashboard (Recomendado)**

1. Acesse: https://vercel.com/new
2. Clique em "Import Git Repository"
3. Selecione seu repositório `meu-sprint-kanban`
4. Framework Preset: Other
5. Deploy

**Opção B: Via CLI** (se preferir)

```bash
npm install -g vercel
vercel login
vercel
```

### Passo 5: Conectar Repositório (OBRIGATÓRIO)

> **CRÍTICO**: Sem esta etapa, o salvamento automático **NÃO funciona**!

1. Vercel Dashboard → Seu Projeto → Settings → Git
2. **Connect Git Repository**
3. Autorize o Vercel a acessar o GitHub
4. Selecione o repositório
5. Branch: `main`

✅ Agora cada `git push` = deploy automático!

### Passo 6: Configurar GitHub Token

**Criar Token**:
1. https://github.com/settings/tokens
2. "Generate new token (classic)"
3. Note: `Vercel Sprint Kanban`
4. Expiration: 90 dias (ou No expiration)
5. Scope: **repo** (marque apenas este)
6. Generate → **COPIE O TOKEN**

**Adicionar no Vercel**:

Via Dashboard:
1. Acesse seu projeto no Vercel
2. Settings → Environment Variables
3. Adicione 3 variáveis:

| Name | Value | Environments |
|------|-------|--------------|
| `GITHUB_TOKEN` | `ghp_seu_token_aqui` | Production, Preview, Development |
| `GITHUB_OWNER` | `seu_usuario_github` | Production, Preview, Development |
| `GITHUB_REPO` | `meu-sprint-kanban` | Production, Preview, Development |

4. Save

**Aplicar variáveis**:

1. Vercel Dashboard → Deployments
2. Latest Deployment → ⋯ → Redeploy
3. Aguardar conclusão

---

## Testando o Salvamento Automático

1. Acesse: `https://seu-projeto.vercel.app/kanban.html`
2. Arraste um card para outra coluna
3. Veja notificação: "Salvo automaticamente!"
4. Verifique no GitHub:
   - Vá no seu repositório
   - Veja que foi criado um commit automático!
5. Aguarde ~30 segundos (Vercel redeploy)
6. Recarregue a página (F5)
7. **Mudança persistiu!** 

> **Como funciona**: A API faz commit → GitHub trigger → Vercel redeploy → Mudança salva!

---

## URLs do Seu Projeto

Após deploy:

- **Kanban**: `https://seu-projeto.vercel.app/kanban.html`
- **Gantt**: `https://seu-projeto.vercel.app/gantt.html`
- **Dashboard Vercel**: `https://vercel.com/seu-usuario/seu-projeto`

---

## Personalizações Comuns

### Mudar Nome da Sprint

Edite `tasks.json`:
```json
{
  "sprint": {
    "name": "Sprint 2 - Backend"  // <-- Aqui
  }
}
```

### Adicionar Nova Coluna no Kanban

Edite `kanban.html` (~linha 620):

```html
<!-- Copie esta estrutura -->
<div class="kanban-column" data-status="seu-status">
    <div class="column-header">
        <i data-lucide="icon-name"></i>
        <h2>Nova Coluna</h2>
        <span class="task-count">0</span>
    </div>
    <div class="tasks-container">
        <!-- Cards vão aqui -->
    </div>
    <button class="add-task-btn">
        <i data-lucide="plus"></i>
        Adicionar Card
    </button>
</div>
```

Depois, adicione esse status no dropdown do modal (~linha 500).

### Mudar Cores

Edite variáveis CSS em `kanban.html` e `gantt.html` (~linha 15):

```css
:root {
    --primary: #6366f1;        /* Roxo (em vez de azul) */
    --success: #22c55e;        /* Verde mais vibrante */
    /* ... */
}
```

---

## Problemas Comuns

### "Failed to connect repository"

**Solução**: 
- Repo está privado? Dê permissão ao Vercel via: https://github.com/settings/installations
- Ou transfira repo para sua conta pessoal

### Erro 500 ao arrastar card

**Causa**: Token ou variáveis erradas

**Solução**:
1. Vercel → Logs → Ver erro detalhado
2. Conferir se as 3 variáveis estão corretas
3. Gerar novo token se necessário

### Cards voltam ao recarregar

**Causa**: Repo não conectado

**Solução**:
1. Conectar repo (Passo 6 acima)
2. Aguardar deploy automático (~30-60s)
3. Hard refresh: `Ctrl + Shift + R`

---

## Dicas

**Deploy automático**: Cada `git push` dispara deploy. Não use `vercel --prod` manualmente!

**Commits automáticos**: Quando você move cards, a API cria commits como `Auto-save: Kanban atualizado via web`

**Monitore deployments**: Aba Deployments no Vercel mostra cada build em tempo real

**Histórico completo**: Como tudo é versionado no Git, você pode reverter mudanças se necessário!

**Desenvolvimento local**: Edite `tasks.json` localmente e dê push - deploy automático acontece

---

**Precisa de mais ajuda?** Consulte o README.md principal ou a documentação do Vercel.

**Dúvidas sobre GitHub API?** https://docs.github.com/en/rest/repos/contents
