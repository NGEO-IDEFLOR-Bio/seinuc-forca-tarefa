# Guia de Uso Rápido

## Checklist de Setup (5 minutos)

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

### Passo 4: Deploy no Vercel

```bash
# Se não tem Vercel CLI instalado
npm install -g vercel

# Login
vercel login

# Deploy
vercel

# Quando perguntar "Link to existing project?": NO
# Nome do projeto: aceite ou altere
# Directory: ./ (enter)
# Override settings: NO (enter)
```

### Passo 5: Configurar GitHub Token

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

**Redeploy**:
```bash
vercel --prod
```

### Passo 6: Conectar Repositório (Deploy Automático)

1. Vercel Dashboard → Seu Projeto → Settings → Git
2. "Connect Git Repository"
3. Selecione `seu_usuario/meu-sprint-kanban`
4. Branch: `main`
5. Save

**Pronto!** Agora cada commit = deploy automático!

---

## Testando

1. Acesse: `https://seu-projeto.vercel.app/kanban.html`
2. Arraste um card para outra coluna
3. Veja notificação: "Salvo automaticamente!"
4. Aguarde ~30 segundos
5. Recarregue a página (F5)
6. **Mudança persistiu!**

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

**Use commits descritivos**: Os commits automáticos aparecem como `Auto-save: Kanban atualizado via web`

**Monitore deployments**: Aba Deployments no Vercel mostra cada build em tempo real

**Backup regular**: `tasks.json` é versionado = histórico completo no Git!

**Branch para experimentos**: Teste mudanças em branch separada antes de mergear

---

**Precisa de mais ajuda?** Consulte o README.md principal ou a documentação do Vercel.

**Dúvidas sobre GitHub API?** https://docs.github.com/en/rest/repos/contents
