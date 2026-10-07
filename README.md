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

* **Matriz de Acompanhamento (`EPICOS.md`):** Apresenta o detalhamento dos 4 eixos estratégicos do projeto e o estado atual de cada entrega.
* **Documentação de Tarefas (`tarefas/`):** Contém as especificações técnicas, parâmetros regulatórios e fluxos de cada tarefa individual (`EPIC1-T1.md` a `EPIC4-T12.md`).
* **Acervo Normativo e Referências (`documentos/referencias/`):** Reúne a legislação federal, estadual comparada, diretrizes do CONAMA e estudos técnicos, catalogados em `INDEX.md`.
* **Produtos Consolidados (`producao/docs/`):** Armazena as minutas de atos normativos e documentos regulamentares finalizados.

---

## 3. Estrutura de Épicos do Projeto

### Épico 1: Regulamentação e Base Normativa
Abrange a elaboração do Decreto Regulamentador do SEINUC/PA (Concluído), a fixação do calendário operacional de Ano-Base e Ano de Exercício (Concluído) e a publicação da Portaria de Diretrizes Técnicas.

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
├── EPICOS.md                      # Painel central de Épicos e Status de Tarefas
├── README.md                      # Documento descritivo do repositório
├── tarefas/                       # Especificações e documentos de tarefas (.md)
│   ├── EPIC1-T1.md                # Minuta do Decreto de Regulamentação [Concluído]
│   ├── EPIC1-T2.md                # Ciclo Anual de Gestão (Cronograma) [Concluído]
│   ├── EPIC1-T3.md                # Portaria de Diretrizes Técnicas
│   ├── EPIC2-T4.md                # Módulo de Caracterização Ambiental (Quadro I)
│   ├── EPIC2-T5.md                # Módulo Georreferenciado e Fundiário (Quadro II)
│   ├── EPIC2-T6.md                # Módulo de Gestão e Socioeconomia (Quadro III)
│   ├── EPIC2-T7.md                # Protocolo de Integração com o CNUC, ITERPA e SEMAS [Concluído]
│   ├── EPIC3-T8.md                # Fluxo de Envio e Protocolo Digital
│   ├── EPIC3-T9.md                # Checklist de Triagem e Admissibilidade
│   ├── EPIC3-T10.md               # Ciclo de Análise Técnica e Fase Recursal [Concluído]
│   ├── EPIC4-T11.md               # Portal de Transparência e Serviços de Mapas (OGC)
│   └── EPIC4-T12.md               # Relatórios de Efetividade da Gestão (Art. 113) [Concluído]
├── producao/
│   └── docs/
│       └── minuta-decreto-seinuc.md # Minuta do Decreto Regulamentador (Texto Final)
└── documentos/
    └── referencias/               # Base legal, resoluções e estudos técnicos (PDFs)
        └── INDEX.md               # Catálogo sistematizado do acervo de referência
```
