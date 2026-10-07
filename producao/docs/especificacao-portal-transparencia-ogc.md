# ESPECIFICAÇÃO DO PORTAL DE TRANSPARÊNCIA E SERVIÇOS DE MAPAS OGC (SEINUC/PA)

> **Documento Oficial de Especificação Técnica e Regulamentação da Transparência Ativa e Geoserviços**
> **Base Legal:** Art. 67, § 1º e Art. 111 da Lei Estadual nº 10.306/2023 | Art. 7º e Art. 12 do Decreto Regulamentador do SEINUC/PA | Lei Federal nº 12.527/2011 (LAI) | Padrões OGC (Open Geospatial Consortium)

---

## 1. Apresentação e Objetivos

Este documento especifica os requisitos funcionais, a arquitetura de transparência ativa, as diretrizes de dados abertos e a infraestrutura de geoserviços nos padrões da *Open Geospatial Consortium (OGC)* do **Sistema Estadual de Informações sobre Unidades de Conservação do Estado do Pará (SEINUC/PA)**.

O objetivo precípuo consiste em garantir o controle social, a publicidade irrestrita das ações de conservação do patrimônio natural paraense e a obrigatoriedade de alimentação da **Cartografia Oficial do Estado do Pará** (Art. 111 da Lei nº 10.306/2023).

---

## 2. Arquitetura do Portal Público de Transparência Ativa

O Portal Público do SEINUC/PA será estruturado em três módulos integrados de livre acesso ao cidadão, pesquisadores e órgãos de controle, isentos de necessidade de cadastro prévio:

```
PORTAL PÚBLICO SEINUC/PA (TRANSPARÊNCIA ATIVA)
├── MÓDULO A: Visualizador WebGIS Interativo de UCs e Zoneamento
├── MÓDULO B: Repositório e Consulta Documental de Unidades de Conservação
└── MÓDULO C: Painel Transparente do ICMS Ecológico por Município
```

### 2.1. Módulo A - Visualizador WebGIS Interativo
* **Funcionalidade:** Interface cartográfica de alto desempenho para navegação espacial sobre as Unidades de Conservação estaduais, municipais e RPPNs.
* **Camadas de Informação Disponíveis:**
  * Polígonos de Perímetros Oficiais de UCs (Proteção Integral e Uso Sustentável).
  * Zoneamento Ambiental Interno e Zonas de Amortecimento.
  * Mosaicos de Áreas Protegidas e terras comunitárias limítrofes.
  * Camada de Hidrografia e Bacias Hidrográficas.
* **Ferramentas do Usuário:** Consulta por atributos, medição de áreas/distâncias, alternância de mapas de fundo (satélite/topográfico) e exportação de mapas em PDF.

### 2.2. Módulo B - Repositório e Consulta Documental
* **Funcionalidade:** Mecanismo de busca textual e download público de documentos oficiais vinculados às UCs.
* **Acervo Disponível:**
  * Atos Legais de Criação (Leis e Decretos).
  * Planos de Manejo / Planos de Gestão em formato PDF pesquisável.
  * Portarias de instituição e Atas de Reuniões dos Conselhos Gestores.
  * Fichas de Caracterização Ambiental e Resumos Executivos.

### 2.3. Módulo C - Painel Transparente do ICMS Ecológico
* **Funcionalidade:** Painel de prestação de contas dos repasses ambientais aos municípios paraense.
* **Dados Publicizados:**
  * Relação de municípios habilitados e indeferidos por exercício.
  * Extratos de Pontuação Provisória e Definitiva.
  * Fichas de Avaliação Técnica emitidas pela Comissão Técnica (CT-SEINUC).
  * Relatórios de Julgamento de Recursos Administrativos.

---

## 3. Geoserviços OGC e Integração com a Cartografia Oficial do Estado (Art. 111)

Em estrito cumprimento ao **Art. 111 da Lei Estadual nº 10.306/2023** e ao **Art. 12 do Decreto Regulamentador**, as bases de dados geográficos do SEINUC/PA serão disponibilizadas em tempo real via geoserviços padronizados pela *Open Geospatial Consortium (OGC)* para consumo obrigatório pelos geoportais oficiais do Estado do Pará (SIEPA, ITERPA, SEMAS e SEFA).

### 3.1. Especificação dos Geoserviços OGC

| Serviço OGC | Versão Padrão | Endpoint de Acesso | Finalidade e Aplicação na Cartografia Oficial |
| :--- | :---: | :--- | :--- |
| **WMS (Web Map Service)** | 1.3.0 | `https://seinuc.ideflor.pa.gov.br/geoserver/wms` | Renderização de mapas dinâmicos e camadas visuais das UCs na confecção das cartas e mapas oficiais do Governo do Estado do Pará. |
| **WFS (Web Feature Service)** | 2.0.0 | `https://seinuc.ideflor.pa.gov.br/geoserver/wfs` | Download e consumo de vetores brutos em formatos abertos (`GeoJSON`, `Shapefile zip`, `KML`) por órgãos ambientais, pesquisadores e sistemas parceiros. |
| **WCS (Web Coverage Service)** | 2.0.1 | `https://seinuc.ideflor.pa.gov.br/geoserver/wcs` | Transmissão de dados raster e modelos digitais de elevação de UCs quando aplicável. |

### 3.2. Padrão de Metadados Geográficos (Perfil MGB / INDE)
Todos os conjuntos de dados geográficos do SEINUC/PA serão catalogados segundo o **Perfil de Metadados Geográficos do Brasil (MGB)** da Infraestrutura Nacional de Dados Espaciais (INDE), contendo:
* Linhagem e histórico do dado vetorial.
* Sistema de Referência: SIRGAS 2000 (EPSG:4674).
* Responsável técnico pelo mapeamento e data de atualização.

---

## 4. Diretrizes de Sigilo, Proteção da Biodiversidade e LGPD (Art. 7º do Decreto)

A transparência pública no SEINUC/PA observará as ressalvas legais de proteção ao patrimônio biológico e à privacidade, nos termos do Art. 7º do Decreto Regulamentador e da Lei Geral de Proteção de Dados (Lei Federal nº 13.709/2018):

### 4.1. Resguardo da Biodiversidade (Proteção contra Biopirataria)
* **Regra de Mascaramento Espacial:** As coordenadas geográficas exatas de pontos de nidificação, avistamento ou ocorrência de espécies da fauna e flora criticamente ameaçadas de extinção (CR) suscetíveis à caça, ilícito ou biopirataria serão mascaradas no visualizador público.
* **Visualização Generalizada:** Para o público geral, o dado de ocorrência sensível será exibido por polígono de quadrícula regional (ex: 10 x 10 km), mantendo a precisão exata restrita ao corpo técnico autorizado do IDEFLOR-Bio e SEMAS.

### 4.2. Conformidade com a LGPD
* Os dados pessoais de conselheiros civis ou gestores (CPF, telefone pessoal, endereço residencial) serão tarjados e anonimizados nos documentos públicos colocados para download, preservando-se a identificação institucional e o nome completo.
