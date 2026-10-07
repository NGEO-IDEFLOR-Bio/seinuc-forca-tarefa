# SEINUC/PA - Sistema Estadual de Informações sobre Unidades de Conservação do Pará

Este repositório contém a documentação técnica, legal e operacional para a implementação prática do **SEINUC/PA**, instituído pela **Lei Estadual nº 10.306/2023**.

---

## 🎯 Estrutura de Trabalho (Zero Distrações)

O repositório é mantido em **Markdown puro (`.md`)**, sem intermediários, sem interfaces HTML ou pipelines automatizados. A estrutura de acompanhamento e produção é a seguinte:

* [`EPICOS.md`](EPICOS.md): Painel geral dos 4 Épicos do projeto e status de cada entrega.
* [`tarefas/`](tarefas/): Diretório contendo os documentos individuais de planejamento e produção textual para cada tarefa (`EPIC1-T1.md` até `EPIC4-T12.md`).
* [`producao/docs/`](producao/docs/): Minutas consolidadas e documentos normativos finalizados (ex: [`minuta-elberth.docx`](producao/docs/minuta-elberth.docx)).
* [`documentos/referencias/`](documentos/referencias/): Biblioteca organizada de referência legal e benchmarking com catálogo em [`INDEX.md`](documentos/referencias/INDEX.md).

---

## 📋 Épicos do Projeto

1. **Épico 1: Regulamentação e Base Normativa** — Decreto regulamentador, cronograma do ciclo anual e portaria técnica.
2. **Épico 2: Arquitetura de Dados e Módulos** — Dicionário de dados dos módulos ambiental, georreferenciado, de gestão e tabela De-Para do CNUC.
3. **Épico 3: Fluxo Operacional e Validação** — Regras de upload, checklist de triagem, análise técnica e fase recursal.
4. **Épico 4: Transparência e Efetividade** — Requisitos do portal público e relatórios anuais e quadrienais de efetividade da gestão.

---

## 📁 Árvore do Repositório

```
.
├── EPICOS.md                      # Acompanhamento de Épicos e Status de Tarefas
├── README.md                      # Guia do ambiente de trabalho
├── tarefas/                       # Documentos das tarefas (.md)
│   ├── EPIC1-T1.md                # [CONCLUÍDO] Minuta do Decreto de Regulamentação
│   ├── EPIC1-T2.md                # Ciclo Anual de Gestão (Cronograma)
│   ├── EPIC1-T3.md                # Portaria de Diretrizes Técnicas
│   ├── EPIC2-T4.md                # Módulo de Caracterização Ambiental (Quadro I)
│   ├── EPIC2-T5.md                # Módulo Georreferenciado e Fundiário (Quadro II)
│   ├── EPIC2-T6.md                # Módulo de Gestão e Socioeconomia (Quadro III)
│   ├── EPIC2-T7.md                # Protocolo de Integração com o CNUC
│   ├── EPIC3-T8.md                # Fluxo de Envio e Protocolo Digital
│   ├── EPIC3-T9.md                # Checklist de Triagem e Admissibilidade
│   ├── EPIC3-T10.md               # Ciclo de Análise Técnica e Fase Recursal
│   ├── EPIC4-T11.md               # Portal de Transparência do SEINUC
│   └── EPIC4-T12.md               # Relatórios de Efetividade da Gestão
├── producao/
│   └── docs/
│       └── minuta-elberth.docx    # Minuta oficial entregue (T1)
└── documentos/
    └── referencias/               # Legislação comparada, resoluções e estudos (PDFs)
        └── INDEX.md               # Catálogo organizado das referências por estado/esfera
```
