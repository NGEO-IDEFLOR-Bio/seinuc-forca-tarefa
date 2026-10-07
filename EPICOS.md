# Projeto de Implementação do SEINUC/PA

Este repositório contém o planejamento, a estrutura normativa e a arquitetura de dados do **Sistema Estadual de Informações sobre Unidades de Conservação do Estado do Pará (SEINUC/PA)**, em cumprimento ao **Art. 67 da Lei Estadual nº 10.306/2023**.

---

## Épico 1: Regulamentação e Base Normativa
**Objetivo:** Estabelecer o arcabouço legal, os cronogramas operacionais e as diretrizes técnicas para o funcionamento oficial do SEINUC/PA.

### Critérios de Conclusão (DoD):
1. **Minuta do Decreto Regulamentador [Concluído]:** Texto legal regulamentando a governança, eixos, rito recursal e integração do SEINUC ([`minuta-decreto-seinuc.md`](file:///H:/Meu%20Drive/IDEFLOR/SEINUC/producao/docs/minuta-decreto-seinuc.md)).
2. **Ciclo Anual de Gestão [Concluído]:** Definição dos prazos operacionais para o Ano-Base, Ano de Exercício e publicação do ICMS Ecológico ([`minuta-decreto-seinuc.md`](file:///H:/Meu%20Drive/IDEFLOR/SEINUC/producao/docs/minuta-decreto-seinuc.md)).
3. **Minuta da Portaria Técnica [Concluído]:** Diretrizes formais de apresentação (PDF/Shapefile), nomenclatura e Declaração de Veracidade ([`minuta-portaria-diretrizes-tecnicas.md`](file:///H:/Meu%20Drive/IDEFLOR/SEINUC/producao/docs/minuta-portaria-diretrizes-tecnicas.md)).

### Lista de Tarefas
| ID | Tarefa | Status | Documento de Trabalho / Produto Oficial |
| :--- | :--- | :---: | :--- |
| **T1** | Minutar o Decreto de Regulamentação do SEINUC | Concluído | [minuta-decreto-seinuc.md](file:///H:/Meu%20Drive/IDEFLOR/SEINUC/producao/docs/minuta-decreto-seinuc.md) |
| **T2** | Definir o Ciclo Anual de Gestão (Cronograma Operacional) | Concluído | [minuta-decreto-seinuc.md](file:///H:/Meu%20Drive/IDEFLOR/SEINUC/producao/docs/minuta-decreto-seinuc.md) |
| **T3** | Criar a Portaria de Diretrizes Técnicas | Concluído | [minuta-portaria-diretrizes-tecnicas.md](file:///H:/Meu%20Drive/IDEFLOR/SEINUC/producao/docs/minuta-portaria-diretrizes-tecnicas.md) |

---

## Épico 2: Arquitetura de Dados e Módulos do Sistema
**Objetivo:** Estruturar as fichas, formulários e padrões geográficos do sistema, assegurando conformidade com a legislação estadual e integração com sistemas parceiros (CNUC, ITERPA e SEMAS).

### Critérios de Conclusão (DoD):
1. **Módulo Ambiental (Quadro I) [Concluído]:** Estrutura de campos para dados bióticos, abióticos, espécies ameaçadas e exóticas ([`especificacao-modulos-dados-seinuc.md`](file:///H:/Meu%20Drive/IDEFLOR/SEINUC/producao/docs/especificacao-modulos-dados-seinuc.md)).
2. **Módulo Georreferenciado e Fundiário (Quadro II) [Concluído]:** Atributos oficiais do Shapefile do IDEFLOR-Bio (SIRGAS 2000), dominialidade e RPPNs ([`especificacao-modulos-dados-seinuc.md`](file:///H:/Meu%20Drive/IDEFLOR/SEINUC/producao/docs/especificacao-modulos-dados-seinuc.md)).
3. **Módulo de Gestão e Socioeconomia (Quadro III) [Concluído]:** Cadastro de Conselhos, Planos de Manejo, visitação e rastreamento de UCs legadas ([`especificacao-modulos-dados-seinuc.md`](file:///H:/Meu%20Drive/IDEFLOR/SEINUC/producao/docs/especificacao-modulos-dados-seinuc.md)).
4. **Mapa de Integração CNUC, ITERPA e SEMAS [Concluído]:** Protocolo de exportação e repasse trienal regulamentado ([`especificacao-modulos-dados-seinuc.md`](file:///H:/Meu%20Drive/IDEFLOR/SEINUC/producao/docs/especificacao-modulos-dados-seinuc.md)).

### Lista de Tarefas
| ID | Tarefa | Status | Documento de Trabalho / Produto Oficial |
| :--- | :--- | :---: | :--- |
| **T4** | Estruturar Módulo de Caracterização Ambiental | Concluído | [especificacao-modulos-dados-seinuc.md](file:///H:/Meu%20Drive/IDEFLOR/SEINUC/producao/docs/especificacao-modulos-dados-seinuc.md) |
| **T5** | Estruturar Módulo de Georreferenciamento e Fundiário | Concluído | [especificacao-modulos-dados-seinuc.md](file:///H:/Meu%20Drive/IDEFLOR/SEINUC/producao/docs/especificacao-modulos-dados-seinuc.md) |
| **T6** | Estruturar Módulo de Gestão e Socioeconomia | Concluído | [especificacao-modulos-dados-seinuc.md](file:///H:/Meu%20Drive/IDEFLOR/SEINUC/producao/docs/especificacao-modulos-dados-seinuc.md) |
| **T7** | Definir Protocolo de Integração com o CNUC, ITERPA e SEMAS | Concluído | [especificacao-modulos-dados-seinuc.md](file:///H:/Meu%20Drive/IDEFLOR/SEINUC/producao/docs/especificacao-modulos-dados-seinuc.md) |

---

## Épico 3: Fluxo Operacional e Validação Processual
**Objetivo:** Desenhar o rito administrativo e digital desde o protocolo das informações até a análise técnica, pontuação e fase recursal.

### Critérios de Conclusão (DoD):
1. **Protocolo de Envio e Nomenclatura [Concluído]:** Padrão de transmissão digital, nomeação de arquivos e recibos de protocolo ([`manual-fluxo-envio-e-triagem.md`](file:///H:/Meu%20Drive/IDEFLOR/SEINUC/producao/docs/manual-fluxo-envio-e-triagem.md)).
2. **Checklist de Triagem (Admissibilidade) [Concluído]:** Critérios formais eliminatórios para aceitação prévia de documentos ([`manual-fluxo-envio-e-triagem.md`](file:///H:/Meu%20Drive/IDEFLOR/SEINUC/producao/docs/manual-fluxo-envio-e-triagem.md)).
3. **Fase de Análise Técnica e Recursos [Concluído]:** Regras para atribuição de notas, ressalvas, Comissão Técnica (CT-SEINUC) e prazo recursal de 15 dias ([`minuta-decreto-seinuc.md`](file:///H:/Meu%20Drive/IDEFLOR/SEINUC/producao/docs/minuta-decreto-seinuc.md)).

### Lista de Tarefas
| ID | Tarefa | Status | Documento de Trabalho / Produto Oficial |
| :--- | :--- | :---: | :--- |
| **T8** | Desenhar o Fluxo de Envio de Documentos (Upload) | Concluído | [manual-fluxo-envio-e-triagem.md](file:///H:/Meu%20Drive/IDEFLOR/SEINUC/producao/docs/manual-fluxo-envio-e-triagem.md) |
| **T9** | Criar o Checklist de Validação (Triagem) | Concluído | [manual-fluxo-envio-e-triagem.md](file:///H:/Meu%20Drive/IDEFLOR/SEINUC/producao/docs/manual-fluxo-envio-e-triagem.md) |
| **T10** | Estabelecer o Ciclo de Análise Técnica e Fase Recursal | Concluído | [minuta-decreto-seinuc.md](file:///H:/Meu%20Drive/IDEFLOR/SEINUC/producao/docs/minuta-decreto-seinuc.md) |

---

## Épico 4: Transparência e Efetividade da Gestão
**Objetivo:** Regulamentar a publicidade dos dados no Portal SEINUC, a integração cartográfica oficial e a prestação de contas periódica.

### Critérios de Conclusão (DoD):
1. **Portal de Transparência do SEINUC e Geoserviços [Concluído]:** Diretrizes de publicação pública e serviços OGC (WMS/WFS) para a Cartografia Oficial do Estado ([`especificacao-portal-transparencia-ogc.md`](file:///H:/Meu%20Drive/IDEFLOR/SEINUC/producao/docs/especificacao-portal-transparencia-ogc.md)).
2. **Relatórios de Efetividade da Gestão [Concluído]:** Regulamentação do relatório anual e do relatório quadrienal de efetividade da gestão ([`minuta-decreto-seinuc.md`](file:///H:/Meu%20Drive/IDEFLOR/SEINUC/producao/docs/minuta-decreto-seinuc.md)).

### Lista de Tarefas
| ID | Tarefa | Status | Documento de Trabalho / Produto Oficial |
| :--- | :--- | :---: | :--- |
| **T11** | Projetar o Portal de Transparência e Serviços de Mapas (OGC) | Concluído | [especificacao-portal-transparencia-ogc.md](file:///H:/Meu%20Drive/IDEFLOR/SEINUC/producao/docs/especificacao-portal-transparencia-ogc.md) |
| **T12** | Definir a Publicação do Relatório de Efetividade da Gestão | Concluído | [minuta-decreto-seinuc.md](file:///H:/Meu%20Drive/IDEFLOR/SEINUC/producao/docs/minuta-decreto-seinuc.md) |

---
*SEINUC/PA - Sistema Estadual de Informações sobre Unidades de Conservação do Estado do Pará.*
