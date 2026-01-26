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

## Referencial Metodológico: Benchmarking e o Modelo de Gestão de Minas Gerais (IEPHA)

A estruturação do **Sistema Estadual de Informações sobre Unidades de Conservação do Pará (SEINUC/PA)**, embora fundamentada em base legal própria, demanda a adoção de parâmetros de governança que garantam eficiência administrativa e segurança jurídica. Nesse contexto, a análise de modelos de gestão consolidados em outros estados apresenta-se como uma estratégia de mitigação de riscos e otimização de fluxos.

O modelo desenvolvido pelo **Instituto Estadual do Patrimônio Histórico e Artístico de Minas Gerais (IEPHA/MG)**, embora voltado ao patrimônio cultural, oferece uma arquitetura sistêmica de alta maturidade para a gestão de dados descentralizados. A metodologia mineira destaca-se pela robustez na integração entre o ente estadual e os municípios, servindo como referencial acadêmico e técnico para a implementação do SEINUC/PA, especialmente no que tange à sistematização de requisitos e ao monitoramento de repasses financeiros.

### 1. Requisitos Legais do SEINUC/PA e a Necessidade de Sistematização

A **Lei Estadual nº 10.306/2023** estabelece as diretrizes para a criação de um banco de dados padronizado. A conformidade com o Art. 67 exige que o sistema contemple:

* **Inventário Biótico e Abiótico:** Dados sobre fauna, flora, recursos hídricos e pedologia.
* **Geotecnologias:** Georreferenciamento e zoneamento ambiental.
* **Dados Socioeconômicos:** Situação fundiária e caracterização antropológica e turística.
* **Interoperabilidade:** Integração obrigatória com o Cadastro Nacional de Unidades de Conservação (CNUC).

### 2. A Organização Metodológica do Modelo Mineiro como Paradigma

A eficácia do modelo do IEPHA/MG reside na sua organização lógica, passível de transposição para o contexto ambiental paraense através dos seguintes eixos:

#### A. Estruturação em Eixos Temáticos (Quadros)

A metodologia de Minas Gerais segmenta a informação em "Quadros", o que permite uma visão modular da gestão:

* **Gestão e Governança:** Foco em conselhos e instrumentos de planejamento.
* **Proteção e Inventário:** Sistematização de dados técnicos e diagnósticos.
* **Salvaguarda e Promoção:** Avaliação de resultados e educação ambiental/patrimonial.
* **Aplicação ao SEINUC:** Esta estrutura possibilita ao Pará organizar os dados exigidos pela lei em módulos de fácil alimentação e auditoria, como o Módulo de Biodiversidade e o Módulo de Caracterização Fundiária.

#### B. Padronização de Fluxos Documentais e Validação Técnica

O referencial metodológico de Minas Gerais estabelece um ciclo anual previsível, que abrange desde o envio de arquivos digitais via protocolos seguros (FTP) até a análise técnica e a fase recursal.

* **Critérios Objetivos:** A utilização de checklists de admissibilidade e fichas de avaliação padronizadas minimiza a subjetividade na análise técnica.
* **Transparência e Controle Social:** O processo culmina na publicação de pontuações e relatórios, atendendo ao princípio da publicidade e permitindo o acompanhamento pela sociedade civil.

### 3. Síntese da Transposição de Modelos

A adoção dessa arquitetura administrativa para o SEINUC/PA permite que o estado avance além do cumprimento formal da lei, estabelecendo um sistema de monitoramento dinâmico. A sistematização inspirada no benchmarking mineiro provê:

1. **Segurança Jurídica:** Prazos e critérios de avaliação claramente definidos em atos normativos.
2. **Qualidade de Dados:** Exigência de nomenclaturas estritas, formatos vetoriais e declarações de veracidade.
3. **Eficiência na Gestão Territorial:** Integração efetiva entre a SEMAS, o IDEFLOR-Bio e os municípios, facilitando a atualização do banco de dados estadual e federal.

Esta abordagem metodológica assegura que a implementação do SEINUC/PA não ocorra de forma isolada, mas sim integrada às melhores práticas de gestão pública estadual no Brasil.
