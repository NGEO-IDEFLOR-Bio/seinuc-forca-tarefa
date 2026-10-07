# Roadmap de Implementação do SEINUC/PA

Este documento apresenta a trajetória cronológica e sequencial para o desenvolvimento e consolidação da documentação técnica, legal e cadastral do **Sistema Estadual de Informações sobre Unidades de Conservação do Estado do Pará (SEINUC/PA)**.

---

## Visão Geral das Fases

```
[FASE 1: BASE REGULAMENTAR] 🟢 (Concluído - 100%)
Decreto Regulamentador (T1), Ciclo Anual (T2) e Governança Recursal (T10)
       │
       ▼
[FASE 2: ARQUITETURA DE DADOS] 🟢 (Concluído - 100%)
Módulos de Dados: Ambiental (T4), Geo/Fundiário (T5), Gestão (T6) e Integração (T7)
       │
       ▼
[FASE 3: ESTEIRA OPERACIONAL] 🟢 (Concluído - 100%)
Portaria Técnica (T3), Protocolo de Envio (T8) e Checklist de Triagem (T9)
       │
       ▼
[FASE 4: TRANSPARÊNCIA E SERVIÇOS] 🟢 (Concluído - 100%)
Portal do SEINUC e Geoserviços OGC (T11)
```

---

## Detalhamento das Fases e Entregáveis

### Fase 1: Arcabouço Normativo Fundamental
**Status:** Concluído (100%)  
**Objetivo:** Normatizar a governança legal do SEINUC/PA, o ciclo de avaliação do ICMS Ecológico e as garantias processuais.

* [x] **Milestone 1.1:** Minuta do Decreto Regulamentador ([`minuta-decreto-seinuc.md`](producao/docs/minuta-decreto-seinuc.md)) — `T1`
* [x] **Milestone 1.2:** Definição do Ciclo Anual de Gestão e Cronograma de Prazos — `T2`
* [x] **Milestone 1.3:** Regulamentação da Comissão Técnica (CT-SEINUC) e Rito Recursal de 15 Dias — `T10`
* [x] **Milestone 1.4:** Normatização da Integração Trienal com ITERPA e SEMAS Licenciamento — `T7`
* [x] **Milestone 1.5:** Regulamentação do Relatório Quadrienal de Efetividade (Art. 113 da Lei nº 10.306/2023) — `T12`

---

### Fase 2: Arquitetura e Dicionário de Dados dos Módulos
**Status:** Concluído (100%)  
**Objetivo:** Especificar o Dicionário de Dados, esquemas JSON e regras de validação dos Módulos do SEINUC/PA com base nos padrões oficiais do IDEFLOR-Bio.

* [x] **Milestone 2.1:** Módulo I - Caracterização Ambiental e Biodiversidade ([`especificacao-modulos-dados-seinuc.md`](producao/docs/especificacao-modulos-dados-seinuc.md)) — `T4`
* [x] **Milestone 2.2:** Módulo II - Georreferenciamento, Fundiário e RPPNs ([`especificacao-modulos-dados-seinuc.md`](producao/docs/especificacao-modulos-dados-seinuc.md)) — `T5`
* [x] **Milestone 2.3:** Módulo III - Gestão, Socioeconomia e UCs Legadas ([`especificacao-modulos-dados-seinuc.md`](producao/docs/especificacao-modulos-dados-seinuc.md)) — `T6`
* [x] **Milestone 2.4:** Protocolo de Integração CNUC, ITERPA e SEMAS ([`especificacao-modulos-dados-seinuc.md`](producao/docs/especificacao-modulos-dados-seinuc.md)) — `T7`

---

### Fase 3: Regras Técnicas, Envio e Triagem
**Status:** Concluído (100%)  
**Objetivo:** Traduzir os módulos de dados em minuta de Portaria Técnica e instrumentos formais de recebimento e triagem.

* [x] **Milestone 3.1:** Minuta da Portaria de Diretrizes Técnicas ([`minuta-portaria-diretrizes-tecnicas.md`](producao/docs/minuta-portaria-diretrizes-tecnicas.md)) — `T3`
* [x] **Milestone 3.2:** Protocolo Digital de Transmissão, Nomenclatura e FTP ([`manual-fluxo-envio-e-triagem.md`](producao/docs/manual-fluxo-envio-e-triagem.md)) — `T8`
* [x] **Milestone 3.3:** Checklist de Triagem e Ficha de Admissibilidade Formal ([`manual-fluxo-envio-e-triagem.md`](producao/docs/manual-fluxo-envio-e-triagem.md)) — `T9`

---

### Fase 4: Transparência, Serviços OGC e Divulgação
**Status:** Concluído (100%)  
**Objetivo:** Regulamentar os serviços de publicação de dados abertos e interoperabilidade cartográfica estadual.

* [x] **Milestone 4.1:** Requisitos do Portal de Transparência e Geoserviços OGC (WMS/WFS) ([`especificacao-portal-transparencia-ogc.md`](producao/docs/especificacao-portal-transparencia-ogc.md)) — `T11`
* [x] **Milestone 4.2:** Consolidação e Fechamento da Documentação de Produção.

---
*Roadmap finalizado em conformidade integral com a Lei Estadual nº 10.306/2023.*
