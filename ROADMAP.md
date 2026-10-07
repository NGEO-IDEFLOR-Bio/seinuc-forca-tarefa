# Roadmap de Implementação do SEINUC/PA

Este documento apresenta a trajetória cronológica e sequencial para o desenvolvimento e consolidação da documentação técnica, legal e cadastral do **Sistema Estadual de Informações sobre Unidades de Conservação do Estado do Pará (SEINUC/PA)**.

---

## Visão Geral das Fases

```
[FASE 1: BASE REGULAMENTAR] 🟢 (Concluído)
Decreto Regulamentador (T1), Ciclo Anual (T2) e Governança Recursal (T10)
       │
       ▼
[FASE 2: ARQUITETURA DE DADOS] 🟡 (Em Andamento)
Módulos de Dados: Ambiental (T4), Geo/Fundiário (T5) e Gestão (T6)
       │
       ▼
[FASE 3: ESTEIRA OPERACIONAL] ⚪ (Pendente)
Portaria Técnica (T3), Protocolo de Envio (T8) e Checklist de Triagem (T9)
       │
       ▼
[FASE 4: TRANSPARÊNCIA E SERVIÇOS] ⚪ (Pendente)
Portal do SEINUC, Geoserviços OGC (T11) e Relatório Quadrienal (T12)
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
**Status:** Em Andamento (0% de 3 tarefas)  
**Objetivo:** Especificar o Dicionário de Dados, esquemas JSON e regras de validação dos 4 Módulos do SEINUC/PA.

* [ ] **Milestone 2.1 (Próximo Passo):** Módulo I - Caracterização Ambiental e Biodiversidade ([`EPIC2-T4.md`](tarefas/EPIC2-T4.md))
* [ ] **Milestone 2.2:** Módulo II - Georreferenciamento, Fundiário e RPPNs ([`EPIC2-T5.md`](tarefas/EPIC2-T5.md))
* [ ] **Milestone 2.3:** Módulo III - Gestão, Socioeconomia e UCs Legadas ([`EPIC2-T6.md`](tarefas/EPIC2-T6.md))

---

### Fase 3: Regras Técnicas, Envio e Triagem
**Status:** Pendente  
**Objetivo:** Traduzir os módulos de dados em minuta de Portaria Técnica e instrumentos formais de recebimento e triagem.

* [ ] **Milestone 3.1:** Minuta da Portaria de Diretrizes Técnicas ([`EPIC1-T3.md`](tarefas/EPIC1-T3.md))
* [ ] **Milestone 3.2:** Protocolo Digital de Transmissão, Nomenclatura e FTP ([`EPIC3-T8.md`](tarefas/EPIC3-T8.md))
* [ ] **Milestone 3.3:** Checklist de Triagem e Ficha de Admissibilidade Formal ([`EPIC3-T9.md`](tarefas/EPIC3-T9.md))

---

### Fase 4: Transparência, Serviços OGC e Divulgação
**Status:** Pendente  
**Objetivo:** Regulamentar os serviços de publicação de dados abertos e interoperabilidade cartográfica estadual.

* [ ] **Milestone 4.1:** Requisitos do Portal de Transparência e Geoserviços OGC (WMS/WFS) ([`EPIC4-T11.md`](tarefas/EPIC4-T11.md))
* [ ] **Milestone 4.2:** Consolidação e Fechamento da Documentação de Produção.

---
*Roadmap atualizado em consonância com a Lei Estadual nº 10.306/2023.*
