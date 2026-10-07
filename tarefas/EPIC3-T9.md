# EPIC3-T9: Criar o Checklist de Validação (Triagem)

**Status:** Em Aberto  
**Responsável:** Coordenação SEINUC / Análise Técnica  
**Base Legal:** Art. 4º, I e III da Minuta do Decreto SEINUC/PA

---

## 1. Escopo da Triagem e Aceite Preliminar

Definição dos critérios de adimplência formal que determinam se o processo enviado pela UC está apto a prosseguir para a fase de análise de conteúdo ou se deve ser rejeitado compulsoriamente na entrada.

---

## 2. Subtarefas de Execução

### Subtarefa 1: Checklist de Admissibilidade (Fase 1 - Formal)

| Item | Critério de Verificação | Tipo | Ação em Caso de Descumprimento |
| :--- | :--- | :---: | :--- |
| **01** | Envio dentro do prazo regulamentar (Até 31/Jan) | Eliminatório | Indeferimento Sumário |
| **02** | Ofício de Encaminhamento assinado por autoridade competente | Eliminatório | Rejeição de Protocolo |
| **03** | Declaração de Veracidade assinada e com ciência legal | Eliminatório | Rejeição de Protocolo |
| **04** | Legibilidade e OCR nos arquivos PDF | Eliminatório | Solicitação de Reenvio em 5 dias |
| **05** | Formato e Datum correto dos arquivos vetoriais (SIRGAS 2000) | Eliminatório | Rejeição do Bloco Vetorial |

### Subtarefa 2: Formulário Eletrônico de Triagem
* Desenvolvimento da **Ficha de Aceite Preliminar** no SEINUC, permitindo ao técnico validar individualmente cada item com *status*: `Conforme`, `Não Conforme` ou `Não Aplicável`.

### Subtarefa 3: Notificação Automática de Rejeição
* Disparo automatizado de e-mail ao gestor da UC com o extrato fundamentado em caso de recusa formal por vício sanável ou insanável.
