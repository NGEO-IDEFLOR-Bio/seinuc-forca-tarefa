# EPIC2-T5: Estruturar Módulo de Georreferenciamento e Fundiário (Quadro II)

**Status:** Em Aberto  
**Responsável:** Equipe de Geoprocessamento / Cadastro  
**Base Legal:** Art. 67, §2º, II e III da Lei PA nº 10.306/2023 | Art. 3º, II e IV da Minuta do Decreto SEINUC/PA  
**Padrão Cartográfico Oficial:** Base de Dados Vetoriais de UCs do IDEFLOR-Bio (Datum SIRGAS 2000 - EPSG:4674)

---

## 1. Escopo do Módulo Georreferenciado e Fundiário

Definição da arquitetura de dados espaciais, dicionário de atributos vetoriais, limites verticais e situação dominial, perfeitamente alinhados à estrutura de shapefiles oficiais do IDEFLOR-Bio.

---

## 2. Dicionário de Atributos da Tabela de Vetores (Shapefile DBF)

Estrutura de colunas alinhada ao padrão oficial de geoprocessamento do IDEFLOR-Bio:

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

---

## 3. Parâmetros de Geoprocessamento e RPPNs

### Parâmetros Cartográficos Obrigatórios
* **Sistema de Referência de Coordenadas (Datum):** **SIRGAS 2000 (EPSG:4674)** - Coordenadas Geográficas.
* **Formatos Aceitos:** Pacote Shapefile compressos em `.zip` (`.shp`, `.shx`, `.dbf`, `.prj`, `.cpg`) ou arquivo `.kml`/`.kmz`.
* **Topologia:** Polígonos fechados sem autopreenchimento, laços, vértices duplicados ou sobreposições não justificadas (*Topology gap/overlap zero*).

### Submódulo Fundiário e RPPNs
* **Dominialidade:**
  * Publica Estadual (IDEFLOR-Bio / ITERPA).
  * Pública Municipal / Federal.
  * Privada em Regularização.
  * **RPPN (Reserva Particular):** Exigência de anexar o número do Registro Geral do Imóvel (RGI) e certidão da averbação da perpetuidade à margem da matrícula em cartório.

---

## 4. Esquema JSON de Validação Espacial (GeoJSON Schema)

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
