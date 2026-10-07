# ESPECIFICAÇÃO TÉCNICA E DICIONÁRIO DE DADOS DOS MÓDULOS DO SEINUC/PA

> **Documento Oficial de Especificação da Arquitetura de Informações do Sistema Estadual de Informações sobre Unidades de Conservação do Estado do Pará (SEINUC/PA)**
> **Base Legal:** Art. 67, § 2º e Art. 68, § 1º da Lei Estadual nº 10.306/2023 | Decreto Regulamentador do SEINUC/PA | Padrão Cartográfico Oficial do IDEFLOR-Bio

---

## 1. Apresentação e Estrutura dos Módulos

O presente documento estabelece o Dicionário de Dados, a estrutura de atributos espaciais, as regras de validação e os esquemas de integração (JSON Schema) para os quatro eixos temáticos que compõem o banco de dados oficial do SEINUC/PA.

```
SEINUC/PA - ARQUITETURA CANÔNICA DE MÓDULOS DE DADOS
├── MÓDULO I: Caracterização Ambiental, Biodiversidade e Clima (Quadro I)
├── MÓDULO II: Geotecnologias, Delimitação e Zonas de Amortecimento (Quadro II)
├── MÓDULO III: Gestão, Governança, Aspectos Antropológicos e UCs Legadas (Quadro III)
└── MÓDULO IV: Caracterização Fundiária, Dominial e RPPNs (Quadro IV)
```

---

## 2. Módulo I - Caracterização Ambiental, Biodiversidade e Clima (Quadro I)

### 2.1. Dicionário de Dados da Tabela de Atributos Ambiental

| Campo | Nome Técnico (ID) | Tipo de Dado | Obrigatório | Regra de Validação / Vocabulário Controlado |
| :--- | :--- | :---: | :---: | :--- |
| **Identificador da UC** | `uc_id` | Número (Inteiro) | Sim | Chave primária vinculada ao cadastro da UC. |
| **Código CNUC** | `cod_cnuc` | Texto (20) | Sim | Código oficial da UC no Cadastro Nacional de UCs (MMA). |
| **Bioma Predominante** | `bioma_predominante` | Enum (Texto) | Sim | `Amazônia`, `Cerrado`, `Zona Costeira/Marinho`. |
| **Fitofisionomia** | `fitofisionomia` | Lista (Array Texto) | Sim | Vocabulário IBGE: `Floresta Ombrófila Densa`, `Floresta Ombrófila Aberta`, `Manguezal`, `Campinarana`, `Restinga`, `Savana/Cerrado`, `Várzea`. |
| **Paisagem Predominante** | `paisagem_tipologia` | Texto | Sim | Descrição da fisionomia de paisagem natural e ecossistemas. |
| **Bacia Hidrográfica** | `bacia_hidrografica` | Enum (Texto) | Sim | Divisão Hidrográfica Estadual: `Bacia do Amazonas`, `Bacia do Tocantins-Araguaia`, `Bacia do Atlântico Nordeste Ocidental`. |
| **Principais Rios** | `rios_principais` | Texto (Livre) | Não | Nomes dos rios, igarapés e lagos de relevância no interior da UC. |
| **Relevo Predominante** | `relevo_tipologia` | Enum (Texto) | Sim | `Planície Aluvial`, `Planalto Rebaixado da Amazônia`, `Depressão Peramázonica`, `Serras e Chapadas`. |
| **Dados Climáticos** | `clima_caracterizacao` | Texto (Livre) | Sim | Classificação de Köppen, precipitação pluviométrica média e temperatura. |
| **Espécies Ameaçadas (Fauna)** | `fauna_ameacada` | Lista Objetos | Não | Nome científico, nome popular, Categoria IUCN/MMA (`CR`, `EN`, `VU`). |
| **Espécies Ameaçadas (Flora)** | `flora_ameacada` | Lista Objetos | Não | Nome científico, nome popular, Categoria IUCN/MMA (`CR`, `EN`, `VU`). |
| **Espécies Exóticas Invasoras** | `especies_exoticas` | Lista Objetos | Sim | Nome científico, grau de infestação, existência de Plano de Controle (Sim/Não). |
| **Programas de Pesquisa** | `programas_pesquisa` | Lista Objetos | Não | Projetos de pesquisa científica registrados na UC (Art. 67, § 4º da Lei). |

### 2.2. Esquema JSON de Validação (Módulo I)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "ModuloCaracterizacaoAmbiental",
  "type": "object",
  "required": ["uc_id", "cod_cnuc", "bioma_predominante", "fitofisionomia", "bacia_hidrografica", "relevo_tipologia", "clima_caracterizacao", "especies_exoticas"],
  "properties": {
    "uc_id": { "type": "integer" },
    "cod_cnuc": { "type": "string" },
    "bioma_predominante": {
      "type": "string",
      "enum": ["Amazônia", "Cerrado", "Zona Costeira/Marinho"]
    },
    "fitofisionomia": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": ["Floresta Ombrófila Densa", "Floresta Ombrófila Aberta", "Manguezal", "Campinarana", "Restinga", "Savana/Cerrado", "Várzea"]
      },
      "minItems": 1
    },
    "paisagem_tipologia": { "type": "string" },
    "bacia_hidrografica": {
      "type": "string",
      "enum": ["Bacia do Amazonas", "Bacia do Tocantins-Araguaia", "Bacia do Atlântico Nordeste Ocidental"]
    },
    "rios_principais": { "type": "string" },
    "relevo_tipologia": {
      "type": "string",
      "enum": ["Planície Aluvial", "Planalto Rebaixado da Amazônia", "Depressão Peramázonica", "Serras e Chapadas"]
    },
    "clima_caracterizacao": { "type": "string" },
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
    },
    "programas_pesquisa": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["titulo_pesquisa", "institucao"],
        "properties": {
          "titulo_pesquisa": { "type": "string" },
          "institucao": { "type": "string" }
        }
      }
    }
  }
}
```

---

## 3. Módulo II - Geotecnologias, Delimitação e Zonas de Amortecimento (Quadro II)

### 3.1. Padrão Geospacial e Atributos DBF (Padrão Oficial IDEFLOR-Bio)

* **Sistema de Referência de Coordenadas (Datum):** **SIRGAS 2000 (EPSG:4674)** - Coordenadas Geográficas.
* **Nota de Interoperabilidade GeoJSON:** O formato nativo de intercâmbio vetorial em SIRGAS 2000 é GeoPackage ou GML. O envio via GeoJSON (RFC 7946) será aceito mediante reprojeção/equivalência transparente pelo servidor do SEINUC.

| Nome da Coluna (Shapefile DBF) | Tipo | Tamanho | Precisão | Descrição do Atributo | Exemplo Real |
| :--- | :---: | :---: | :---: | :--- | :--- |
| `id` | N | 10 | 0 | Identificador numérico da feição | `1`, `2` |
| `cod_cnuc` | C | 20 | 0 | Código CNUC oficial (MMA) | `PA00001` |
| `nome_` | C | 254 | 0 | Nome oficial da UC | `Estação Ecológica do Grão-Pará (ESEC)` |
| `categoria` | C | 254 | 0 | Categoria estadual/federal | `ESEC`, `PARQUE ESTADUAL`, `APA`, `RESEX`, `RPPN`, `FLOTA` |
| `grupo` | C | 50 | 0 | Grupo de Manejo SNUC | `Proteção Integral` ou `Uso Sustentável` |
| `cat_territ` | C | 254 | 0 | Descrição estendida territorial | `Unidade de conservação de proteção integral` |
| `municipio_` | C | 254 | 0 | Município(s) de abrangência | `Alenquer/MonteAlegre/Obidos/Oriximiná` |
| `data_de_cr` | C | 10 | 0 | Data do ato de criação (DD/MM/AAAA) | `04/12/2006` |
| `situacao_l` | C | 254 | 0 | Diploma legal de criação | `Decreto nº 2.609` |
| `area_ha` | N | 24 | 2 | Área calculada pelo GIS (Hectares) | `4245819.11` |
| `area_decre` | N | 24 | 2 | Área decretada oficial (Hectares) | `4245819.11` |
| `destinacao` | C | 254 | 0 | Situação da destinação pública | `Floresta Destinada` |
| `orgao_gest` | C | 254 | 0 | Órgão Gestor responsável | `IDEFLOR-Bio`, `Sema Municipal` |
| `tipo_flore` | C | 254 | 0 | Tipologia florestal | `TIPO A` |
| `za_delim` | C | 3 | 0 | Possui Zona de Amortecimento | `SIM` ou `NAO` |
| `obs` | C | 254 | 0 | Observações cartográficas | `Zona de Amortecimento delimitada` |

---

## 4. Módulo III - Gestão, Governança, Aspectos Antropológicos e UCs Legadas (Quadro III)

### 4.1. Dicionário de Dados da Tabela de Gestão

| Campo | Nome Técnico (ID) | Tipo de Dado | Obrigatório | Regra de Validação / Descrição |
| :--- | :--- | :---: | :---: | :--- |
| **Identificador da UC** | `uc_id` | Número (Inteiro) | Sim | Chave primária vinculada ao cadastro da UC. |
| **Possui Conselho Gestor** | `conselho_status` | Booleano (Sim/Não) | Sim | Indica a existência formal de Conselho Gestor. |
| **Tipo de Conselho** | `conselho_tipo` | Enum (Texto) | Não | `Consultivo`, `Deliberativo`. |
| **Ato de Criação do Conselho** | `conselho_ato_legal` | Texto (Livre) | Não | Número da Portaria/Decreto de criação do conselho. |
| **Reuniões no Ano-Base** | `conselho_reunioes_qtd` | Número (Inteiro) | Não | Mínimo de 2 reuniões ordinárias/extraordinárias comprovadas por ata. |
| **Possui Plano de Gestão** | `plano_gestao_status` | Enum (Texto) | Sim | `Não Iniciado`, `Em Elaboração`, `Aprovado e Vigente`, `Em Revisão`. |
| **Ato de Aprovação do Plano** | `plano_gestao_ato` | Texto (Livre) | Não | Portaria/Decreto de aprovação do Plano de Gestão / Manejo. |
| **Data de Aprovação** | `plano_gestao_data` | Data (AAAA-MM-DD) | Não | Data da publicação do ato de aprovação. |
| **Status de UC Legada** | `legada_status` | Enum (Texto) | Sim | `Conforme Lei 10.306/2023`, `Sítio Pesqueiro em Adequação (Art. 112)`, `UC Criada em Legislação Anterior em Reavaliação (Art. 114)`. |
| **Aspectos Arqueológicos/Antropológicos**| `antropologico_caracterizacao` | Texto (Livre) | Não | Descrição de sítios arqueológicos, patrimônio cultural e terras comunitárias (Art. 68, §1º). |
| **Visitantes Anuais** | `visitantes_qtd` | Número (Inteiro) | Não | Estimativa ou contagem oficial de visitantes no ano-base. |
| **Receita de Uso Público** | `receita_arrecadada_brl` | Número (Decimal) | Não | Valor total arrecadado em R$ com bilheteria, serviços ou concessões. |

---

## 5. Módulo IV - Caracterização Fundiária, Dominial e RPPNs (Quadro IV)

### 5.1. Dicionário de Dados Fundiário
* **Dominialidade:** Pública Estadual, Pública Federal/Municipal, Privada em Regularização.
* **RPPN (Reserva Particular):** Envio da certidão do Registro Geral do Imóvel (RGI) e averbação da perpetuidade à margem da matrícula em cartório.

---

## 6. Módulo V - Interoperabilidade e Integração Interinstitucional

### 6.1. Protocolo de Integração com o CNUC/MMA (Art. 10 do Decreto)
Exportação dos dados cadastrais e vetoriais em conformidade com o Dicionário do Cadastro Nacional de Unidades de Conservação (CNUC), utilizando o código único `cod_cnuc`.

### 6.2. Repasse Trienal ao ITERPA e SEMAS Licenciamento (Art. 11 do Decreto e Art. 68, §4º da Lei)
Exportação trienal automatizada para instrução da arrecadação de terras devolutas (ITERPA - Art. 110) e restrições socioambientais no Licenciamento Ambiental (SEMAS).
