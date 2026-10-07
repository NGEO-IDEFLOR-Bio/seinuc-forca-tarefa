# ESPECIFICAÇÃO TÉCNICA E DICIONÁRIO DE DADOS DOS MÓDULOS DO SEINUC/PA

> **Documento Oficial de Especificação da Arquitetura de Informações do Sistema Estadual de Informações sobre Unidades de Conservação do Estado do Pará (SEINUC/PA)**
> **Base Legal:** Art. 67, § 2º da Lei Estadual nº 10.306/2023 | Capítulo II (Art. 3º) do Decreto Regulamentador | Padrão Cartográfico de UCs do IDEFLOR-Bio

---

## 1. Apresentação e Estrutura dos Módulos

O presente documento estabelece o Dicionário de Dados, a estrutura de atributos espaciais, as regras de validação e os esquemas de integração (JSON Schema) para os quatro eixos temáticos que compõem o banco de dados oficial do SEINUC/PA.

```
SEINUC/PA - ARQUITETURA DE MÓDULOS DE DADOS
├── MÓDULO I: Caracterização Ambiental e Biodiversidade (Quadro I)
├── MÓDULO II: Georreferenciamento, Caracterização Fundiária e RPPNs (Quadro II)
├── MÓDULO III: Gestão, Governança e Adequação Legada (Quadro III)
└── MÓDULO IV: Interoperabilidade e Integração (CNUC / ITERPA / SEMAS)
```

---

## 2. Módulo I - Caracterização Ambiental e Biodiversidade (Quadro I)

### 2.1. Dicionário de Dados da Tabela de Atributos Ambiental

| Campo | Nome Técnico (ID) | Tipo de Dado | Obrigatório | Regra de Validação / Vocabulário Controlado |
| :--- | :--- | :---: | :---: | :--- |
| **Identificador da UC** | `uc_id` | Número (Inteiro) | Sim | Chave primária vinculada ao cadastro da UC. |
| **Bioma Predominante** | `bioma_predominante` | Enum (Texto) | Sim | `Amazônia`, `Cerrado`, `Zona Costeira/Marinho`. |
| **Fitofisionomia** | `fitofisionomia` | Lista (Array Texto) | Sim | Vocabulário IBGE: `Floresta Ombrófila Densa`, `Floresta Ombrófila Aberta`, `Manguezal`, `Campinarana`, `Restinga`, `Savana/Cerrado`, `Várzea`. |
| **Bacia Hidrográfica** | `bacia_hidrografica` | Enum (Texto) | Sim | Divisão Hidrográfica Estadual: `Bacia do Amazonas`, `Bacia do Tocantins-Araguaia`, `Bacia do Atlântico Nordeste Ocidental`. |
| **Principais Rios** | `rios_principais` | Texto (Livre) | Não | Nomes dos rios, igarapés e lagos de relevância no interior da UC. |
| **Relevo Predominante** | `relevo_tipologia` | Enum (Texto) | Sim | `Planície Aluvial`, `Planalto Rebaixado da Amazônia`, `Depressão Peramázonica`, `Serras e Chapadas`. |
| **Espécies Ameaçadas (Fauna)** | `fauna_ameacada` | Lista Objetos | Não | Nome científico, nome popular, Categoria IUCN/MMA (`CR`, `EN`, `VU`). |
| **Espécies Ameaçadas (Flora)** | `flora_ameacada` | Lista Objetos | Não | Nome científico, nome popular, Categoria IUCN/MMA (`CR`, `EN`, `VU`). |
| **Espécies Exóticas Invasoras** | `especies_exoticas` | Lista Objetos | Sim | Nome científico, grau de infestação, existência de Plano de Controle (Sim/Não). |

### 2.2. Esquema JSON de Validação (Módulo I)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "ModuloCaracterizacaoAmbiental",
  "type": "object",
  "required": ["uc_id", "bioma_predominante", "fitofisionomia", "bacia_hidrografica", "relevo_tipologia", "especies_exoticas"],
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
    "bacia_hidrografica": { "type": "string" },
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

---

## 3. Módulo II - Georreferenciamento, Caracterização Fundiária e RPPNs (Quadro II)

### 3.1. Padrão Geospacial e Atributos da Tabela DBF (IDEFLOR-Bio)

* **Sistema de Referência de Coordenadas (Datum):** **SIRGAS 2000 (EPSG:4674)** - Coordenadas Geográficas.
* **Tabela de Atributos do Shapefile (Alinhada à Base Oficial do IDEFLOR-Bio):**

| Nome da Coluna (Shapefile DBF) | Tipo | Tamanho | Descrição do Atributo | Exemplo de Preenchimento Real |
| :--- | :---: | :---: | :--- | :--- |
| `id` | Número | 10 | Identificador numérico da feição espacial | `1`, `2`, `3` |
| `nome_` | Texto | 254 | Nome oficial da Unidade de Conservação | `Estação Ecológica do Grão-Pará (ESEC)` |
| `categoria` | Texto | 254 | Sigla ou nome da categoria SNUC/SEUC | `ESEC`, `PARQUE ESTADUAL`, `APA`, `RESEX`, `RPPN` |
| `grupo` | Texto | 50 | Grupo de Manejo SNUC | `Proteção Integral` ou `Uso Sustentável` |
| `cat_territ` | Texto | 254 | Descrição estendida da categoria territorial | `Unidade de conservação de proteção integral` |
| `municipio_` | Texto | 254 | Município(s) de abrangência territorial | `Alenquer/MonteAlegre/Obidos/Oriximiná` |
| `data_de_cr` | Texto | 254 | Data oficial do ato de criação (DD/MM/AAAA) | `04/12/2006` |
| `situacao_l` | Texto | 254 | Diploma legal de criação (Decreto/Lei) | `Decreto nº 2.609` |
| `area_ha` | Número | 24 | Área calculada pelo sistema GIS (Hectares) | `4245819.11` |
| `area_decre` | Número | 24 | Área declarada no ato de criação (Hectares) | `4245819.11` |
| `destinacao` | Texto | 254 | Situação da destinação pública | `Floresta Destinada`, `Área Arrecadada` |
| `orgao_gest` | Texto | 254 | Órgão Gestor responsável | `IDEFLOR-Bio`, `Sema Municipal` |
| `tipo_flore` | Texto | 254 | Tipologia florestal predominante | `TIPO A`, `TIPO B` |
| `obs` | Texto | 254 | Observações cartográficas ou ressalvas | `Zona de Amortecimento em delimitação` |

### 3.2. Submódulo Fundiário e RPPNs
* **Dominialidade:** Pública Estadual, Pública Federal/Municipal, Privada em Regularização.
* **Reserva Particular do Patrimônio Natural (RPPN):** Obrigatoriedade do envio do número do Registro Geral do Imóvel (RGI) e certidão da averbação da perpetuidade à margem da matrícula em cartório.

### 3.3. Esquema GeoJSON de Validação (Módulo II)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "ModuloGeorreferenciamentoEFundiario",
  "type": "object",
  "required": ["id", "nome_", "categoria", "grupo", "municipio_", "area_decre", "orgao_gest"],
  "properties": {
    "id": { "type": "integer" },
    "nome_": { "type": "string" },
    "categoria": { "type": "string" },
    "grupo": { "type": "string", "enum": ["Proteção Integral", "Uso Sustentável"] },
    "cat_territ": { "type": "string" },
    "municipio_": { "type": "string" },
    "data_de_cr": { "type": "string" },
    "situacao_l": { "type": "string" },
    "area_ha": { "type": "number" },
    "area_decre": { "type": "number" },
    "destinacao": { "type": "string" },
    "orgao_gest": { "type": "string" },
    "rppn_rgi_matricula": { "type": "string" }
  }
}
```

---

## 4. Módulo III - Gestão, Governança e Socioeconomia (Quadro III)

### 4.1. Dicionário de Dados da Tabela de Gestão

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

### 4.2. Esquema JSON de Validação (Módulo III)

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

---

## 5. Módulo IV - Interoperabilidade e Integração Interinstitucional

### 5.1. Protocolo de Integração com o CNUC/MMA (Art. 10 do Decreto)
Exportação dos dados cadastrais e vetoriais em conformidade com o Dicionário do Cadastro Nacional de Unidades de Conservação (CNUC), utilizando o código único `COD_CNUC`.

### 5.2. Repasse Trienal ao ITERPA e SEMAS Licenciamento (Art. 11 do Decreto e Art. 68, §4º da Lei)
Exportação trienal automatizada para instrução da arrecadação de terras devolutas (ITERPA - Art. 110) e restrições socioambientais no Licenciamento Ambiental (SEMAS).
