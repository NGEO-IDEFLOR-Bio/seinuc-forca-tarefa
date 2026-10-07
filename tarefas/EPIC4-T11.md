# EPIC4-T11: Projetar o Portal de Transparência do SEINUC e Serviços de Mapas

**Status:** 🟡 **EM ABERTO**  
**Responsável:** Equipe de TI / Geoprocessamento  
**Base Legal:** Art. 67, §1º e Art. 111 da Lei PA nº 10.306/2023 | Art. 7º da Minuta do Decreto SEINUC/PA | Lei de Acesso à Informação (Lei nº 12.527/2011)

---

## 🌐 Escopo do Portal de Transparência e Cartografia Oficial

Garantir o controle social, o livre acesso público e a integração dos dados geográficos do SEINUC com a cartografia e mapas oficiais do Estado do Pará.

---

## 🎯 Subtarefas de Execução

### Subtarefa 1: Módulos de Consulta Pública
* **Mapa Interativo de UCs:** Visualizador geográfico (WebGIS) contendo polígonos, limites, zoneamento e infraestruturas das UCs estaduais e municipais.
* **Fichas Informativas por UC:** Download dos Planos de Manejo, Atos de Criação, dados do Conselho Gestor e contatos oficiais da gestão.
* **Painel do ICMS Ecológico:** Consulta aos extratos anuais de habilitação e pontuação das UCs municipais.

### Subtarefa 2: Serviços OGC para Cartografia Oficial do Estado (Art. 111)
* **Integração Obrigatória (Art. 111):** Disponibilização de geoserviços nos padrões da *Open Geospatial Consortium (OGC)*:
  * **WMS (Web Map Service):** Para visualização das camadas de UCs nas cartas oficiais e geopartais do Estado.
  * **WFS (Web Feature Service):** Para download de vetores brutos (.shp, .geojson, .kml) por órgãos estaduais, pesquisadores e cidadãos.
* Sincronização direta com o Sistema Estadual de Informações Ambientais (SIEPA).

### Subtarefa 3: Exceções e Proteção de Dados Sensíveis
* Implementação de regra de resguardo e sigilo para localização exata de espécimes da fauna/flora criticamente ameaçadas de extinção (evitando biopirataria ou caça predatória), em conformidade com o Art. 7º do Decreto Regulamentador.
