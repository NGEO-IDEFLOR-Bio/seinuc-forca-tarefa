# SEINUC/PA - Sistema Estadual de Informações sobre Unidades de Conservação do Estado do Pará

Este repositório reúne a documentação técnica, legal e institucional para o planejamento e estruturação do **Sistema Estadual de Informações sobre Unidades de Conservação do Estado do Pará (SEINUC/PA)**, instituído pela **Lei Estadual nº 10.306, de 22 de dezembro de 2023**.

---

## 1. Contexto e Objetivos

O SEINUC/PA constitui o banco de dados oficial e padronizado com as informações relativas às Unidades de Conservação (UCs) estaduais e municipais localizadas no Estado do Pará. Suas finalidades principais compreendem:

1. Subsidiar a gestão do Sistema Estadual de Unidades de Conservação da Natureza (SEUC/PA) nas etapas de criação, planejamento, monitoramento e fiscalização.
2. Servir de base técnica para a apuração dos critérios de cálculo e distribuição da parcela correspondente ao ICMS Ecológico aos municípios, conforme a Lei Estadual nº 7.638/2012 e suas alterações.
3. Garantir a transparência ativa e o controle social da gestão do patrimônio natural estadual, nos termos da Lei Federal nº 12.527/2011 (Lei de Acesso à Informação).
4. Assegurar a interoperabilidade e integração dos dados estaduais com o Cadastro Nacional de Unidades de Conservação (CNUC), mantido pelo Ministério do Meio Ambiente e Mudança do Clima.

---

## 2. Metodologia e Estrutura de Documentação

A documentação do projeto está estruturada em formato Markdown (.md) de modo modular e padronizado, visando à auditabilidade e à manutenção contínua das informações:

* **Roadmap do Projeto (`ROADMAP.md`):** Trajetória cronológica por Fases, Milestones e percentual de progresso.
* **Matriz de Acompanhamento (`EPICOS.md`):** Apresenta o detalhamento dos 4 eixos estratégicos do projeto e o estado atual de cada entrega.
* **Documentação de Tarefas (`tarefas/`):** Contém as especificações técnicas, parâmetros regulatórios e fluxos de cada tarefa individual (`EPIC1-T1.md` a `EPIC4-T12.md`).
* **Acervo Normativo e Referências (`documentos/referencias/`):** Reúne a legislação federal, estadual comparada, diretrizes do CONAMA e estudos técnicos, catalogados em `INDEX.md`.
* **Auditoria e Conformidade (`documentos/auditoria-conformidade-seinuc.md`):** Relatório de auditoria técnica e jurídica do acervo, consolidado em 4 rodadas de reavaliação (Partes I a IV).
* **Produtos Consolidados (`producao/docs/`):** Armazena as minutas de atos normativos e documentos regulamentares finalizados (Texto Final Sanado).
* **Arquivados (`producao/arquivados/`):** Versões superadas de documentos produzidos durante o processo (ex.: minuta anterior em `.docx`).

---

## 3. Estrutura de Épicos do Projeto

### Épico 1: Regulamentação e Base Normativa
Abrange a elaboração do Decreto Regulamentador do SEINUC/PA (Concluído), a fixação do calendário operacional de Ano-Base e Ano de Exercício (Concluído) e a publicação da Portaria Conjunta de Diretrizes Técnicas (Concluído).

### Épico 2: Arquitetura de Dados e Módulos do Sistema
Compreende o dicionário de dados dos Módulos Ambiental (Quadro I), Georreferenciado e Fundiário (Quadro II) e de Gestão e Socioeconomia (Quadro III), além dos protocolos de integração com o CNUC, ITERPA e SEMAS (Concluído).

### Épico 3: Fluxo Operacional e Validação Processual
Regulamenta os procedimentos digitais de recepção documental, os checklists de triagem e admissibilidade formal, e os ritos de análise técnica e fase recursal (Concluído).

### Épico 4: Transparência e Avaliação de Efetividade
Define os parâmetros para o Portal de Transparência do SEINUC, a disponibilização de geoserviços OGC (WMS/WFS) para a Cartografia Oficial do Estado e os relatórios anuais e quadrienais de avaliação de efetividade da gestão (Concluído).

---

## 4. Estrutura do Repositório

```
.
├── ROADMAP.md                      # Trajetória de Fases, Milestones e Progresso (100% Concluído)
├── EPICOS.md                      # Painel central de Épicos e Status de Tarefas (100% Concluído)
├── README.md                      # Documento descritivo do repositório
├── tarefas/                       # Especificações e documentos de tarefas (.md)
│   ├── EPIC1-T1.md                # Minuta do Decreto de Regulamentação [Concluído]
│   ├── EPIC1-T2.md                # Ciclo Anual de Gestão (Cronograma) [Concluído]
│   ├── EPIC1-T3.md                # Portaria de Diretrizes Técnicas [Concluído]
│   ├── EPIC2-T4.md                # Módulo de Caracterização Ambiental (Quadro I) [Concluído]
│   ├── EPIC2-T5.md                # Módulo Georreferenciado e Fundiário (Quadro II) [Concluído]
│   ├── EPIC2-T6.md                # Módulo de Gestão e Socioeconomia (Quadro III) [Concluído]
│   ├── EPIC2-T7.md                # Protocolo de Integração com o CNUC, ITERPA e SEMAS [Concluído]
│   ├── EPIC3-T8.md                # Fluxo de Envio e Protocolo Digital [Concluído]
│   ├── EPIC3-T9.md                # Checklist de Triagem e Admissibilidade [Concluído]
│   ├── EPIC3-T10.md               # Ciclo de Análise Técnica e Fase Recursal [Concluído]
│   ├── EPIC4-T11.md               # Portal de Transparência e Serviços de Mapas (OGC) [Concluído]
│   └── EPIC4-T12.md               # Relatórios de Efetividade da Gestão (Art. 113) [Concluído]
├── producao/
│   ├── docs/
│   │   ├── minuta-decreto-seinuc.md            # Minuta do Decreto Regulamentador (Texto Final Sanado)
│   │   ├── minuta-portaria-diretrizes-tecnicas.md # Portaria Conjunta SEMAS/IDEFLOR-Bio (Texto Final Sanado)
│   │   ├── especificacao-modulos-dados-seinuc.md # Especificação Técnica dos Módulos I a IV (SIRGAS 2000)
│   │   ├── manual-fluxo-envio-e-triagem.md       # Manual de Protocolo Digital, Envio e Triagem
│   │   ├── especificacao-portal-transparencia-ogc.md # Portal de Transparência e Geoserviços OGC (WMS/WFS)
│   │   └── docx/                               # Arquivos Finais em Word (.docx) Formatados em ABNT
│   │       ├── minuta-decreto-seinuc.docx
│   │       ├── minuta-portaria-diretrizes-tecnicas.docx
│   │       ├── especificacao-modulos-dados-seinuc.docx
│   │       ├── manual-fluxo-envio-e-triagem.docx
│   │       └── especificacao-portal-transparencia-ogc.docx
│   └── arquivados/
│       └── minuta-elberth.docx                # Versão anterior da minuta do Decreto (arquivada)
└── documentos/
    ├── referencias/               # Base legal, resoluções e estudos técnicos (PDFs)
    │   └── INDEX.md               # Catálogo sistematizado do acervo de referência
    └── auditoria-conformidade-seinuc.md # Relatório de Auditoria Técnica e Jurídica (4 rodadas)
```
