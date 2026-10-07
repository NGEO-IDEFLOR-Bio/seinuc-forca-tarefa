# EPIC2-T4: Estruturar Módulo de Caracterização Ambiental (Quadro I)

**Status:** Em Aberto  
**Responsável:** Analista Ambiental / Biólogo  
**Base Legal:** Art. 67, §2º, I da Lei PA nº 10.306/2023 | Art. 3º, I da Minuta do Decreto SEINUC/PA  
**Fonte de Referência Real:** Dados de Inventário Biótico do IDEFLOR-Bio

---

## 1. Escopo do Módulo de Caracterização Ambiental

Estruturação da especificação técnica, dicionário de dados de atributos, vocabulários controlados e esquemas JSON para cadastramento das informações bióticas e abióticas das Unidades de Conservação do Estado do Pará.

---

## 2. Dicionário de Dados do Módulo Ambiental (Quadro I)

| Campo | Nome Técnico (ID) | Tipo de Dado | Obrigatório | Regra de Validação / Vocabulário Controlado |
| :--- | :--- | :---: | :---: | :--- |
| **Identificador da UC** | `uc_id` | Número (Inteiro) | Sim | Chave primária vinculada ao cadastro da UC. |
| **Bioma Predominante** | `bioma_predominante` | Enum (Texto) | Sim | `Amazônia`, `Cerrado`, `Zona Costeira/Marinho`. |
| **Fitofisionomia** | `fitofisionomia` | Lista (Array Texto) | Sim | Vocabulário IBGE: `Floresta Ombrófila Densa`, `Floresta Ombrófila Aberta`, `Manguezal`, `Campinarana`, `Restinga`, `Savana/Cerrado`, `Várzea`. |
| **Bacia Hidrográfica** | `bacia_hidrográfica` | Enum (Texto) | Sim | Divisão Hidrográfica Estadual: `Bacia do Amazonas`, `Bacia do Tocantins-Araguaia`, `Bacia do Atlântico Nordeste Ocidental`. |
| **Principais Rios** | `rios_principais` | Texto (Livre) | Não | Nomes dos rios, igarapés e lagos de relevância no interior da UC. |
| **Relevo Predominante** | `relevo_tipologia` | Enum (Texto) | Sim | `Planície Aluvial`, `Planalto Rebaixado da Amazônia`, `Depressão Peramázonica`, `Serras e Chapadas`. |
| **Espécies Ameaçadas (Fauna)** | `fauna_ameacada` | Lista Objetos | Não | Nome científico, nome popular, Categoria IUCN/MMA (`CR`, `EN`, `VU`). |
| **Espécies Ameaçadas (Flora)** | `flora_ameacada` | Lista Objetos | Não | Nome científico, nome popular, Categoria IUCN/MMA (`CR`, `EN`, `VU`). |
| **Espécies Exóticas Invasoras** | `especies_exoticas` | Lista Objetos | Sim | Nome científico, grau de infestação, existência de Plano de Controle (Sim/Não). |

---

## 3. Esquema JSON de Validação (JSON Schema)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "ModuloCaracterizacaoAmbiental",
  "type": "object",
  "required": ["uc_id", "bioma_predominante", "fitofisionomia", "bacia_hidrográfica", "relevo_tipologia", "especies_exoticas"],
  "properties": {
    "uc_id": { "type": "integer" },
    "bioma_predominante": {
      "type": "string",
      "enum": ["Amazônia", "Cerrado", "Zona Costeira/Marinho"]
    },
    "fitofisionomia": {
      "type": "array",
      "items": { "type": "string" },
      "minItems": 1
    },
    "bacia_hidrográfica": { "type": "string" },
    "rios_principais": { "type": "string" },
    "relevo_tipologia": { "type": "string" },
    "fauna_ameacada": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["nome_cientifico", "categoria_ameaca"],
        "properties": {
          "nome_cientifico": { "type": "string" },
          "nome_popular": { "type": "string" },
          "categoria_ameaca": { "type": "string", "enum": ["CR", "EN", "VU"] }
        }
      }
    },
    "flora_ameacada": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["nome_cientifico", "categoria_ameaca"],
        "properties": {
          "nome_cientifico": { "type": "string" },
          "nome_popular": { "type": "string" },
          "categoria_ameaca": { "type": "string", "enum": ["CR", "EN", "VU"] }
        }
      }
    },
    "especies_exoticas": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["nome_cientifico", "possui_plano_controle"],
        "properties": {
          "nome_cientifico": { "type": "string" },
          "possui_plano_controle": { "type": "boolean" }
        }
      }
    }
  }
}
```
