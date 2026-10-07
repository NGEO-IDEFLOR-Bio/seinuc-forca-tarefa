# EPIC2-T6: Estruturar Módulo de Gestão e Socioeconomia (Quadro III)

**Status:** Em Aberto  
**Responsável:** Analista Socioambiental / Gestão Pública  
**Base Legal:** Art. 67, §2º, IV, Art. 112 e Art. 114 da Lei PA nº 10.306/2023 | Art. 3º, III e IV da Minuta do Decreto SEINUC/PA

---

## 1. Escopo do Módulo de Gestão e Socioeconomia

Estruturação da especificação técnica, dicionário de dados de atributos, controle de conselhos, planos de manejo, receitas de uso público e rastreamento de readequação de categorias de UCs legadas.

---

## 2. Dicionário de Dados do Módulo de Gestão (Quadro III)

| Campo | Nome Técnico (ID) | Tipo de Dado | Obrigatório | Regra de Validação / Descrição |
| :--- | :--- | :---: | :---: | :--- |
| **Identificador da UC** | `uc_id` | Número (Inteiro) | Sim | Chave primária vinculada ao cadastro da UC. |
| **Possui Conselho Gestor** | `conselho_status` | Booleano (Sim/Não) | Sim | Indica a existência formal de Conselho Gestor. |
| **Tipo de Conselho** | `conselho_tipo` | Enum (Texto) | Não | `Consultivo`, `Deliberativo`. |
| **Ato de Criação do Conselho** | `conselho_ato_legal` | Texto (Livre) | Não | Número da Portaria/Decreto de criação do conselho. |
| **Reuniões no Ano-Base** | `conselho_reunioes_qtd` | Número (Inteiro) | Não | Quantitativo de reuniões ordinárias/extraordinárias realizadas. Exigido mínimo de 2 reuniões comprovadas por ata. |
| **Possui Plano de Manejo** | `plano_manejo_status` | Enum (Texto) | Sim | `Não Iniciado`, `Em Elaboração`, `Aprovado e Vigente`, `Em Revisão`. |
| **Ato de Aprovação do Plano** | `plano_manejo_ato` | Texto (Livre) | Não | Portaria/Decreto de aprovação do Plano de Manejo. |
| **Data de Aprovação** | `plano_manejo_data` | Data (DD/MM/AAAA) | Não | Data da publicação do ato de aprovação. |
| **Status de UC Legada** | `legada_status` | Enum (Texto) | Sim | `Conforme Lei 10.306/2023`, `Sítio Pesqueiro em Adequação (Art. 112)`, `UC Criada em Legislação Anterior em Reavaliação (Art. 114)`. |
| **Visitantes Anuais** | `visitantes_qtd` | Número (Inteiro) | Não | Estimativa ou contagem oficial de visitantes no ano-base. |
| **Receita de Uso Público** | `receita_arrecadada_brl` | Número (Decimal) | Não | Valor total arrecadado em R$ com bilheteria, serviços ou concessões. |
| **Comunidades Residentes** | `comunidades_tradicionais_qtd` | Número (Inteiro) | Não | Quantitativo de famílias de populações tradicionais residentes no interior ou Zona de Amortecimento. |

---

## 3. Esquema JSON de Validação (JSON Schema)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "ModuloGestaoESocioeconomia",
  "type": "object",
  "required": ["uc_id", "conselho_status", "plano_manejo_status", "legada_status"],
  "properties": {
    "uc_id": { "type": "integer" },
    "conselho_status": { "type": "boolean" },
    "conselho_tipo": { "type": "string", "enum": ["Consultivo", "Deliberativo"] },
    "conselho_ato_legal": { "type": "string" },
    "conselho_reunioes_qtd": { "type": "integer", "minimum": 0 },
    "plano_manejo_status": {
      "type": "string",
      "enum": ["Não Iniciado", "Em Elaboração", "Aprovado e Vigente", "Em Revisão"]
    },
    "plano_manejo_ato": { "type": "string" },
    "plano_manejo_data": { "type": "string" },
    "legada_status": {
      "type": "string",
      "enum": [
        "Conforme Lei 10.306/2023",
        "Sítio Pesqueiro em Adequação (Art. 112)",
        "UC Criada em Legislação Anterior em Reavaliação (Art. 114)"
      ]
    },
    "visitantes_qtd": { "type": "integer", "minimum": 0 },
    "receita_arrecadada_brl": { "type": "number", "minimum": 0 },
    "comunidades_tradicionais_qtd": { "type": "integer", "minimum": 0 }
  }
}
```
