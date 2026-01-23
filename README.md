# SEINUC/PA - Sistema Estadual de Informações sobre Unidades de Conservação do Pará

## Sobre o Projeto

O **SEINUC/PA** (Sistema Estadual de Informações sobre Unidades de Conservação do Estado do Pará) está legalmente instituído pela **Lei Estadual nº 10.306/2023**, mas ainda em fase de estruturação prática.

Este repositório documenta o planejamento e desenvolvimento do sistema, utilizando metodologia ágil com **Kanban Board** e **Gantt Chart** para gestão das tarefas.

### Objetivo

Criar o sistema de informações que permitirá:
- Gestão integrada das Unidades de Conservação do Pará
- Transparência e controle social da gestão ambiental
- Integração com o Cadastro Nacional de Unidades de Conservação (CNUC)
- Subsidiar repasses de ICMS Ecológico

---

## Glossário de Termos do Projeto

### Organização das Tarefas

#### **Épicos**
Grandes áreas temáticas que agrupam tarefas relacionadas. O projeto está dividido em 4 épicos:

| Épico | Descrição | Foco |
|-------|-----------|------|
| **Épico 1** | Regulamentação e Base Normativa | Decretos, portarias e cronograma |
| **Épico 2** | Arquitetura de Dados | Módulos de informação (Ambiental, Geo, Gestão) |
| **Épico 3** | Fluxo Operacional | Processos de envio, validação e recursos |
| **Épico 4** | Transparência e Controle Social | Portal público e relatórios |

**Ver detalhamento completo**: [EPICOS.md](EPICOS.md)

#### **Prioridades (P0, P1, P2)**

| Prioridade | Nome | Significado | Cor |
|------------|------|-------------|-----|
| **P0** | Crítico | Bloqueante. Sem isso, nada funciona. | Vermelho |
| **P1** | Alto | Importante para o MVP. Deve ser feito logo. | Laranja |
| **P2** | Normal | Melhoria. Pode ser adiado se necessário. | Azul |

#### **Gates (Portões de Controle)**

Referem-se aos **épicos** aos quais a tarefa pertence. Funcionam como marcos de validação:
- **Épico 1**: Base legal deve estar pronta antes de seguir
- **Épico 2**: Dados estruturados antes de criar interface
- **Épico 3**: Fluxos validados antes de abrir ao público
- **Épico 4**: Sistema transparente e acessível

#### **Tipos de Tarefas**

| Tipo | Descrição | Cor |
|------|-----------|-----|
| **Doc** | Criação de documentos normativos (decretos, portarias, manuais) | Verde |
| **Decisão** | Definições estratégicas ou escolhas técnicas | Amarelo |
| **Execução** | Desenvolvimento técnico (código, formulários, integrações) | Vermelho |
| **Ritual** | Reuniões, apresentações, validações com stakeholders | Roxo |

#### **Status das Tarefas**

| Status | Descrição |
|--------|-----------|
| **Backlog** | Tarefa mapeada, aguardando início |
| **Em Andamento** | Tarefa sendo executada ativamente |
| **Review** | Aguardando revisão ou aprovação |
| **Concluído** | Tarefa finalizada e validada |

---

## Estrutura do Repositório

```
.
├── documentos/                    # Documentos de referência
│   └── Lei-10.306-2023.pdf        # Lei que institui o SEINUC/PA
├── documentacao-do-repo/          # Documentação técnica do repositório
│   ├── SETUP_GUIDE.md             # Guia de configuração
│   └── INDEX.md                   # Índice da documentação
├── functions/api/                 # API Serverless (Cloudflare Workers)
│   └── save-tasks.js              # Endpoint para salvar tarefas
├── kanban.html                    # Interface Kanban interativa
├── gantt.html                     # Diagrama de Gantt
├── tasks.json                     # Base de dados das tarefas
└── README.md                      # Este arquivo
```

---

## Acesso ao Sistema

**Kanban Board**: https://seinuc-forca-tarefa.pages.dev/kanban.html  
**Gantt Chart**: https://seinuc-forca-tarefa.pages.dev/gantt.html

---

## Benchmarking: Modelo de Minas Gerais (IEPHA)

Dado que o **SEINUC/PA** está legalmente instituído mas ainda em fase de estruturação prática, é estratégico observar modelos de gestão de outros estados.

Embora as fontes fornecidas não detalhem o sistema *ambiental* de Minas Gerais (SISEMA), elas oferecem um **modelo estrutural de gestão estadual extremamente detalhado** referente ao **Patrimônio Cultural (IEPHA/MG)**. A estrutura administrativa, documental e de financiamento deste sistema mineiro serve como um excelente "estudo de caso" (benchmark) para desenhar a arquitetura do SEINUC/PA, especialmente no que tange à integração com municípios e repasse de recursos (ICMS).

Abaixo, apresento uma análise comparativa entre o que a lei do Pará exige para o SEINUC e como a estrutura de Minas Gerais (no âmbito cultural) opera, o que pode servir de inspiração para a criação do sistema paraense.

### 1. O que a Lei do Pará exige para o SEINUC/PA
A Lei Estadual nº 10.306/2023 define a estrutura legal que o sistema deve ter:

*   **Definição:** Um banco de dados padronizado com informações das Unidades de Conservação (UCs) estaduais.
*   **Conteúdo Obrigatório:** O sistema deve conter, no mínimo:
    *   Características ambientais (fauna, flora, recursos hídricos, clima, solo).
    *   Georreferenciamento (incluindo zoneamento).
    *   Situação fundiária.
    *   Aspectos sociais, econômicos, culturais, antropológicos e turísticos.
*   **Gestão:** O órgão central (SEMAS) organiza e mantém o sistema, com colaboração do IDEFLOR-Bio.
*   **Integração:** Deve ser integrado ao Cadastro Nacional de Unidades de Conservação (CNUC).
*   **Objetivo Estratégico:** Subsidiar a gestão, controle, fiscalização e permitir o acompanhamento pela sociedade.

### 2. Modelo de Estruturação: O Exemplo de Minas Gerais (IEPHA)
Para "criar" o SEINUC na prática, você pode analisar a estrutura administrativa utilizada por Minas Gerais para gerir dados municipais e estaduais visando o repasse de ICMS (neste caso, Cultural). Esta estrutura pode ser adaptada para o ICMS Ecológico ou gestão ambiental no Pará:

#### A. Base Normativa e Critérios de Pontuação
Minas Gerais utiliza uma **Deliberação Normativa** (do conselho estadual, CONEP) para estabelecer diretrizes anuais e tabelas de pontuação. Isso cria um ciclo previsível de gestão.
*   **Aplicação para o SEINUC:** O Pará poderia criar resoluções anuais definindo quais dados do SEINUC são prioritários para o cálculo de índices de qualidade ou repasse de recursos (como o ICMS Verde).

#### B. Estrutura de Coleta de Dados ("Quadros")
O sistema mineiro organiza a informação em "Quadros" ou eixos temáticos, o que facilita a alimentação do banco de dados:
*   **Quadro I (Gestão):** Política municipal, fundos de preservação, conselhos atuantes.
*   **Quadro II (Proteção):** Inventários, tombamentos e registros.
*   **Quadro III (Salvaguarda):** Laudos técnicos de conservação e educação patrimonial.
*   **Aplicação para o SEINUC:** O sistema do Pará poderia ser estruturado em módulos similares: Módulo de Gestão (Conselhos das UCs, Plano de Manejo), Módulo de Biodiversidade (inventários de fauna/flora exigidos no art. 67 da lei) e Módulo Fundiário.

#### C. Mecanismo de Envio e Validação (FTP e Digitalização)
Para operacionalizar o sistema, MG utiliza protocolos de transferência de arquivos (FTP) e exige documentos digitais (PDF), eliminando papel e facilitando a criação do banco de dados.
*   **Validação:** O município ou gestor da UC envia a documentação, que passa por análise técnica do estado. Se aprovada, gera pontuação e alimenta o sistema.
*   **Aplicação para o SEINUC:** O SEINUC pode ser a interface web onde os gestores das UCs (estaduais e municipais) fazem o *upload* dos Planos de Gestão, shapefiles do zoneamento e relatórios de fiscalização, conforme exige a Lei 10.306/2023.

#### D. Transparência e Recurso
O modelo mineiro prevê a publicação de pontuações provisórias e definitivas em site oficial, com prazos claros para impugnação e recurso pelos municípios.
*   **Aplicação para o SEINUC:** Como o art. 67 da lei do Pará menciona permitir o "acompanhamento pela sociedade", o sistema deve ter um portal público que exiba os dados validados (semelhante ao portal do IEPHA), permitindo controle social sobre a efetividade da gestão das UCs.

### 3. Passos Práticos para Criação (Baseado na análise comparativa)

Para tirar o SEINUC do papel, baseando-se na lei aprovada e nas experiências de estruturação analisadas:

1.  **Regulamentação:** O Art. 67, §5º da Lei 10.306/2023 define que o SEINUC será regulamentado por ato do Chefe do Poder Executivo. É necessário minutar este decreto, possivelmente inspirando-se na organização lógica das portarias do IEPHA/MG (definição de prazos, formatos de arquivos e responsabilidades).
2.  **Padronização de Dados:** Definir o "dicionário de dados" (o que exatamente é exigido em "características ambientais" ou "aspectos antropológicos" mencionados na lei).
3.  **Plataforma Tecnológica:** Desenvolver ou contratar uma ferramenta que permita o envio descentralizado de informações (pelos chefes de UC e municípios) e a validação centralizada pela SEMAS/IDEFLOR-Bio, integrando esses dados ao CNUC federal.
4.  **Inventário Inicial:** Realizar o levantamento das terras devolutas e arrecadadas pelo ITERPA (prazo de 5 anos estipulado na lei) para alimentar a base fundiária do sistema.

Esta análise estrutural do sistema de Minas Gerais, embora de outra área temática, oferece um roteiro administrativo robusto (fluxo de documentos, prazos, validação e publicidade) que pode acelerar a implementação do SEINUC no Pará.