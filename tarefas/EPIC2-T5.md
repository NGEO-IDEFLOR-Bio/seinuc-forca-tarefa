# EPIC2-T5: Estruturar Módulo de Georreferenciamento e Fundiário (Quadro II)

**Status:** Concluído  
**Produto Entregue:** [`producao/docs/especificacao-modulos-dados-seinuc.md#3-módulo-ii---georreferenciamento-caracterização-fundiária-e-rppns-quadro-ii`](file:///H:/Meu%20Drive/IDEFLOR/SEINUC/producao/docs/especificacao-modulos-dados-seinuc.md#3-módulo-ii---georreferenciamento-caracterização-fundiária-e-rppns-quadro-ii)  
**Responsável:** Equipe de Geoprocessamento / Cadastro  
**Base Legal:** Art. 67, §2º, II e III da Lei PA nº 10.306/2023 | Art. 3º, II e IV da Minuta do Decreto SEINUC/PA  
**Padrão Cartográfico Oficial:** Base de Dados Vetoriais de UCs do IDEFLOR-Bio (Datum SIRGAS 2000 - EPSG:4674)

---

## 1. Resumo da Entrega

A especificação técnica do Módulo II (Georreferenciamento, Fundiário e RPPNs) foi consolidada no documento oficial de especificação em [`producao/docs/especificacao-modulos-dados-seinuc.md`](file:///H:/Meu%20Drive/IDEFLOR/SEINUC/producao/docs/especificacao-modulos-dados-seinuc.md).

### Elementos Especificados:
* **Tabela de Colunas do Shapefile DBF:** Atributos reais alinhados ao padrão oficial do IDEFLOR-Bio (`id`, `nome_`, `categoria`, `grupo`, `cat_territ`, `municipio_`, `data_de_cr`, `situacao_l`, `area_ha`, `area_decre`, `destinacao`, `orgao_gest`, `tipo_flore`, `obs`).
* **Datum e Topologia:** SIRGAS 2000 (EPSG:4674).
* **Submódulo RPPNs:** Inclusão de atributos para matrícula RGI cartorária e averbação de perpetuidade.
* **Validação por Agentes de IA e Desenvolvedores:** Bloco de código em **GeoJSON Schema draft-2020-12**.
