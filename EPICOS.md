# Projeto de Implementação do SEINUC/PA

Este repositório contém o planejamento e a estruturação do **Sistema Estadual de Informações sobre Unidades de Conservação do Estado do Pará (SEINUC/PA)**. 

O projeto visa cumprir o **Art. 67 da Lei Estadual nº 10.306/2023**, utilizando como *benchmark* de fluxo processual e documental o sistema de gestão do **IEPHA/MG** (Minas Gerais).

---

## Épico 1: Regulamentação e Base Normativa
**Objetivo:** Estabelecer o arcabouço jurídico e o cronograma que darão validade legal ao sistema e aos dados coletados.

### O que teremos ao final deste Épico (DoD):
1.  **Minuta do Decreto Regulamentador:** Texto legal definindo a governança do SEINUC, em cumprimento ao Art. 67, §5º da Lei 10.306/2023.
2.  **Minuta da Portaria Técnica:** Documento detalhando as regras de formatação (PDF/Shapefile), responsabilidades e critérios de pontuação/validação, baseado na *Portaria IEPHA nº 34/2024 (Modelo de Processo)*.
3.  **Calendário de Gestão:** Definição clara dos prazos de "Ano-Base" (ação) e "Ano de Exercício" (validação/repasse).

### Lista de Tarefas
| ID | Tarefa | Link |
| :--- | :--- | :--- |
| **T1** | Minutar o Decreto de Regulamentação do SEINUC | [Acessar Tarefa](tarefas/EPIC1-T1.md) |
| **T2** | Definição do Ciclo Anual de Gestão (Cronograma) | [Acessar Tarefa](tarefas/EPIC1-T2.md) |
| **T3** | Criar a Portaria de Diretrizes Técnicas | [Acessar Tarefa](tarefas/EPIC1-T3.md) |

---

## Épico 2: Arquitetura de Dados e Conteúdo
**Objetivo:** Definir o "Dicionário de Dados" e os módulos temáticos que compõem o sistema, garantindo a padronização das informações exigidas por lei.

### O que teremos ao final deste Épico (DoD):
1.  **Estrutura do Módulo Ambiental:** Campos definidos para fauna, flora e recursos hídricos (Art. 67, §2º, I).
2.  **Estrutura do Módulo Fundiário/Geo:** Padrões para *upload* de vetores (zoneamento/limites) e cadastro de situação fundiária (Art. 67, §2º, II e III).
3.  **Estrutura do Módulo de Gestão:** Campos para dados de conselhos, planos de manejo e aspectos sociais/turísticos.
4.  **Mapa de Integração CNUC:** Tabela "De-Para" garantindo que os dados do SEINUC sejam compatíveis com o Cadastro Nacional (Art. 67, §3º).

### Lista de Tarefas
| ID | Tarefa | Link |
| :--- | :--- | :--- |
| **T4** | Estruturar o Módulo de "Caracterização Ambiental" | [Acessar Tarefa](tarefas/EPIC2-T4.md) |
| **T5** | Estruturar o Módulo de "Georreferenciamento e Fundiário" | [Acessar Tarefa](tarefas/EPIC2-T5.md) |
| **T6** | Estruturar o Módulo de "Gestão e Socioeconomia" | [Acessar Tarefa](tarefas/EPIC2-T6.md) |
| **T7** | Definir Protocolo de Integração com o CNUC | [Acessar Tarefa](tarefas/EPIC2-T7.md) |

---

## Épico 3: Fluxo Operacional e Validação
**Objetivo:** Desenhar a "esteira de produção" da informação, desde o envio pelo gestor da UC até a validação final pelo Estado.

### O que teremos ao final deste Épico (DoD):
1.  **Protocolo de Envio:** Definição da ferramenta (FTP ou Web) e regras de nomenclatura de arquivos, baseado no modelo eficiente de MG.
2.  **Checklist de Triagem:** Lista de verificação automática para aceite inicial da documentação (ex: assinaturas, legibilidade).
3.  **Fluxo de Análise e Recurso:** Regras claras para impugnação de notas ou recusa de documentos, com prazos definidos (ex: 10 a 15 dias) para garantir ampla defesa.
4.  **Rotina de Homologação:** Processo de publicação da "Pontuação Definitiva" e oficialização dos dados no sistema.

### Lista de Tarefas
| ID | Tarefa | Link |
| :--- | :--- | :--- |
| **T8** | Desenhar o Fluxo de Envio de Documentos (Upload) | [Acessar Tarefa](tarefas/EPIC3-T8.md) |
| **T9** | Criar o Checklist de Validação (Triagem) | [Acessar Tarefa](tarefas/EPIC3-T9.md) |
| **T10** | Estabelecer o Ciclo de Análise Técnica | [Acessar Tarefa](tarefas/EPIC3-T10.md) |
| **T11** | Estruturar a Fase Recursal | [Acessar Tarefa](tarefas/EPIC3-T11.md) |
| **T12** | Homologação e Integração | [Acessar Tarefa](tarefas/EPIC3-T12.md) |

---
*Documento gerado com base na Lei PA nº 10.306/2023 e Benchmark IEPHA/MG.*
