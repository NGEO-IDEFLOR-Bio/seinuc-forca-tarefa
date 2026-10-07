# EPIC4-T11: Projetar o Portal de Transparência do SEINUC e Serviços de Mapas (OGC)

**Status:** Concluído  
**Produto Entregue:** [`producao/docs/especificacao-portal-transparencia-ogc.md`](../producao/docs/especificacao-portal-transparencia-ogc.md)  
**Responsável:** Equipe de TI / Geoprocessamento  
**Base Legal:** Art. 67, §6º e Art. 111 da Lei PA nº 10.306/2023 | Arts. 13 e 14 do Decreto Regulamentador do SEINUC/PA | Lei Federal nº 12.527/2011 (LAI) | Lei Federal nº 13.709/2018 (LGPD) | Lei Federal nº 13.123/2015 (SisGen)

---

## 1. Resumo da Entrega

A especificação técnica do Portal de Transparência Ativa e dos Serviços de Mapas OGC foi totalmente desenvolvida e consolidada no documento oficial de entrega em [`producao/docs/especificacao-portal-transparencia-ogc.md`](../producao/docs/especificacao-portal-transparencia-ogc.md).

### Elementos Especificados:
* **Módulos do Portal Público:** Visualizador WebGIS Interativo, Repositório Documental e Painel Transparente do ICMS Ecológico por Município (com rastreamento do repasse de 20% - Art. 117).
* **Geoserviços OGC (Art. 111 da Lei):** Serviços **WMS 1.3.0**, **WFS 2.0.0**, **WCS 2.0.1** e **CSW 2.0.2** para a Cartografia Oficial do Estado (SIEPA, ITERPA, SEMAS e SEFA), disponibilizados por ciclo anual com atualização contínua intra-ciclo.
* **Metadados:** Perfil MGB/INDE com UUID do conjunto e periodicidade de atualização.
* **Proteção de Dados e Biodiversidade:** Mascaramento de coordenadas exatas de ocorrência de espécies criticamente ameaçadas (CR) **em todos os geoserviços** (WebGIS, WMS, WFS, WCS, GetFeatureInfo e GetFeature), LGPD (SEMAS Controladora / IDEFLOR Operador) e Lei nº 13.123/2015 (SisGen).