// Serverless function para salvar tasks.json via GitHub API
export default async function handler(req, res) {
    // CORS headers
    res.setHeader('Access-Control-Allow-Credentials', true);
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT');
    res.setHeader('Access-Control-Allow-Headers', 'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version');

    // Handle preflight
    if (req.method === 'OPTIONS') {
        res.status(200).end();
        return;
    }

    if (req.method !== 'POST') {
        return res.status(405).json({ error: 'Método não permitido' });
    }

    try {
        // Validar dados
        if (!req.body || !req.body.sprint || !req.body.tasks) {
            return res.status(400).json({ error: 'Dados inválidos' });
        }

        // Configuração do GitHub
        const GITHUB_TOKEN = process.env.GITHUB_TOKEN;
        const GITHUB_OWNER = process.env.GITHUB_OWNER || 'Sertan-AI';
        const GITHUB_REPO = process.env.GITHUB_REPO || 'app-sprint-1';
        const FILE_PATH = 'docs/sprints/tasks.json';

        if (!GITHUB_TOKEN) {
            console.error('❌ GITHUB_TOKEN não configurado');
            return res.status(500).json({ error: 'GitHub token não configurado' });
        }

        // 1. Buscar SHA atual do arquivo
        const getFileResponse = await fetch(
            `https://api.github.com/repos/${GITHUB_OWNER}/${GITHUB_REPO}/contents/${FILE_PATH}`,
            {
                headers: {
                    'Authorization': `token ${GITHUB_TOKEN}`,
                    'Accept': 'application/vnd.github.v3+json',
                    'User-Agent': 'Sprint-Kanban-App'
                }
            }
        );

        if (!getFileResponse.ok) {
            throw new Error(`Erro ao buscar arquivo: ${getFileResponse.status}`);
        }

        const fileData = await getFileResponse.json();
        const currentSHA = fileData.sha;

        // 2. Preparar conteúdo atualizado
        const content = JSON.stringify(req.body, null, 2);
        const contentBase64 = Buffer.from(content).toString('base64');

        // 3. Fazer commit via GitHub API
        const updateResponse = await fetch(
            `https://api.github.com/repos/${GITHUB_OWNER}/${GITHUB_REPO}/contents/${FILE_PATH}`,
            {
                method: 'PUT',
                headers: {
                    'Authorization': `token ${GITHUB_TOKEN}`,
                    'Accept': 'application/vnd.github.v3+json',
                    'Content-Type': 'application/json',
                    'User-Agent': 'Sprint-Kanban-App'
                },
                body: JSON.stringify({
                    message: `🔄 Auto-save: Kanban atualizado via web`,
                    content: contentBase64,
                    sha: currentSHA,
                    branch: 'main'
                })
            }
        );

        if (!updateResponse.ok) {
            const errorData = await updateResponse.json();
            throw new Error(`Erro ao fazer commit: ${JSON.stringify(errorData)}`);
        }

        const result = await updateResponse.json();

        console.log(`✅ Commit realizado: ${result.commit.sha}`);

        res.status(200).json({
            success: true,
            message: 'Tarefas salvas com sucesso!',
            commit: result.commit.sha,
            timestamp: new Date().toISOString()
        });
    } catch (error) {
        console.error('❌ Erro ao salvar:', error);
        res.status(500).json({
            error: 'Erro ao salvar tarefas',
            details: error.message
        });
    }
}
