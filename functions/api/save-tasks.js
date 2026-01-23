// Cloudflare Pages Function para salvar tasks.json via GitHub API
export async function onRequestPost(context) {
    const { request, env } = context;

    // CORS headers
    const corsHeaders = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET,OPTIONS,PATCH,DELETE,POST,PUT',
        'Access-Control-Allow-Headers': 'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version',
        'Content-Type': 'application/json'
    };

    try {
        // Validar dados
        const body = await request.json();
        
        if (!body || !body.sprint || !body.tasks) {
            return new Response(
                JSON.stringify({ error: 'Dados inválidos' }), 
                { status: 400, headers: corsHeaders }
            );
        }

        // Configuração do GitHub
        const GITHUB_TOKEN = env.GITHUB_TOKEN;
        const GITHUB_OWNER = env.GITHUB_OWNER || 'NGEO-IDEFLOR-Bio';
        const GITHUB_REPO = env.GITHUB_REPO || 'seinuc-forca-tarefa';
        const FILE_PATH = 'tasks.json';

        if (!GITHUB_TOKEN) {
            console.error('❌ GITHUB_TOKEN não configurado');
            return new Response(
                JSON.stringify({ error: 'GitHub token não configurado' }), 
                { status: 500, headers: corsHeaders }
            );
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
        const content = JSON.stringify(body, null, 2);
        // Cloudflare Workers não tem Buffer global, usamos btoa
        const contentBase64 = btoa(unescape(encodeURIComponent(content)));

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

        return new Response(
            JSON.stringify({
                success: true,
                message: 'Tarefas salvas com sucesso!',
                commit: result.commit.sha,
                timestamp: new Date().toISOString()
            }),
            { status: 200, headers: corsHeaders }
        );
    } catch (error) {
        console.error('❌ Erro ao salvar:', error);
        return new Response(
            JSON.stringify({
                error: 'Erro ao salvar tarefas',
                details: error.message
            }),
            { status: 500, headers: corsHeaders }
        );
    }
}

// Handle OPTIONS (preflight)
export async function onRequestOptions() {
    return new Response(null, {
        status: 200,
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET,OPTIONS,PATCH,DELETE,POST,PUT',
            'Access-Control-Allow-Headers': 'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version'
        }
    });
}
