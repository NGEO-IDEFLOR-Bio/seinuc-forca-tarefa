# MINUTA DA PORTARIA TÉCNICA Nº ____/202X - IDEFLOR-Bio / SEMAS

> **Ementa:** Estabelece as diretrizes técnicas, os padrões de arquivos digitais, a regra de nomenclatura, as especificações cartográficas e o modelo de Declaração de Veracidade para o envio de dados e documentos ao Sistema Estadual de Informações sobre Unidades de Conservação do Estado do Pará (SEINUC/PA).

**O PRESIDENTE DO INSTITUTO DE DESENVOLVIMENTO FLORESTAL E DA BIODIVERSIDADE DO ESTADO DO PARÁ (IDEFLOR-Bio)** e o **SECRETÁRIO DE ESTADO DE MEIO AMBIENTE E SUSTENTABILIDADE (SEMAS/PA)**, no uso das atribuições que lhes são conferidas por lei, e tendo em vista o disposto na Lei Estadual nº 10.306, de 22 de dezembro de 2023, e no Decreto Regulamentador do SEINUC/PA,

**RESOLVEM:**

---

## CAPÍTULO I - DAS DISPOSIÇÕES PRELIMINARES

**Art. 1º** Esta Portaria estabelece os requisitos técnicos e os padrões formais de apresentação das informações e documentos a serem transmitidos pelos órgãos gestores municipais e executores ao Sistema Estadual de Informações sobre Unidades de Conservação do Estado do Pará (SEINUC/PA), para fins de cadastro, monitoramento e apuração do ICMS Ecológico.

---

## CAPÍTULO II - DOS FORMATOS E PADRÕES DE ARQUIVOS DIGITAIS

**Art. 2º** Os documentos textuais, relatórios de gestão, atos administrativos e comprovantes deverão ser transmitidos exclusivamente em meio digital, no formato **PDF pesquisável (com camada OCR de reconhecimento óptico de caracteres)**.

§ 1º Cada arquivo textual em PDF deverá conter obrigatoriamente:
* **I - Folha de Rosto:** identificando o Ente Federativo, o Nome da Unidade de Conservação, a Categoria, o Ano-Base de referência e o responsável técnico;
* **II - Sumário Paginado:** indicando a estrutura de tópicos e a paginação correspondente.

§ 2º O tamanho máximo por arquivo individual é de **50 MB (cinquenta megabytes)**. Arquivos que excederem este limite deverão ser fracionados em volumes correlacionados (ex: `VOL_01`, `VOL_02`).

**Art. 3º** As bases de dados geoespaciais e vetoriais referente aos limites e zoneamento da Unidade de Conservação deverão obedecer aos seguintes parâmetros cartográficos:
* **I - Datum Oficial:** **SIRGAS 2000 (EPSG:4674)** - Sistema de Coordenadas Geográficas;
* **II - Formatos Aceitos:** Pacote **Shapefile (.shp, .shx, .dbf, .prj, .cpg)** compactado em formato `.zip`, ou arquivo **KML/KMZ**;
* **III - Topologia:** As geometrias de polígono deverão apresentar fecho topológico perfeito, isentas de laços, vértices duplicados, sobreposições não justificadas ou lacunas (*gap/overlap zero*).

---

## CAPÍTULO III - DA PADRONIZAÇÃO DA NOMENCLATURA DE ARQUIVOS

**Art. 4º** É obrigatória a adoção do padrão estrito de nomenclatura para a transmissão de arquivos no SEINUC/PA, sob pena de recusa no procedimento de triagem automatizada.

§ 1º A nomenclatura dos arquivos deverá seguir a seguinte sintaxe:
`[CODIGO_IBGE_MUNICIPIO]_[SIGLA_UC]_[BLOCO]_[ANO_BASE].[extensao]`

§ 2º Exemplos de aplicação do padrão oficial:
* **Documentos de Gestão (Quadro III):** `1505502_APA_BOSQUE_Q3_2025.pdf`
* **Base Vetorial do Limite (Quadro II):** `1505502_APA_BOSQUE_VETOR_2025.zip`
* **Declaração de Veracidade:** `1505502_APA_BOSQUE_DECLARACAO_2025.pdf`

---

## CAPÍTULO IV - DA DECLARAÇÃO DE VERACIDADE E RESPONSABILIDADE TÉCNICA

**Art. 5º** Todo protocolo de envio no SEINUC/PA deverá vir acompanhado da **Declaração de Veracidade e Responsabilidade Técnica**, conforme modelo constante no Anexo I desta Portaria.

§ 1º A Declaração de Veracidade deverá ser assinada digitalmente (padrão ICP-Brasil ou Gov.br) pelo Prefeito Municipal, Secretário Municipal de Meio Ambiente ou Gestor responsável da Unidade de Conservação.

§ 2º A prestação de declaração falsa, adulterada ou a omissão de fatos relevantes sujeitará o declarante às sanções penais previstas no art. 299 do Código Penal e na Lei Federal nº 9.605/1998, além da perda do repasse do ICMS Ecológico.

---

## CAPÍTULO V - DISPOSIÇÕES FINAIS

**Art. 6º** Esta Portaria entra em vigor na data de sua publicação.

---

## ANEXO I - MODELO DE DECLARAÇÃO DE VERACIDADE E RESPONSABILIDADE TÉCNICA

```
DECLARAÇÃO DE VERACIDADE E RESPONSABILIDADE TÉCNICA

Eu, [NOME DO DECLARANTE], inscrito(a) no CPF sob o nº [CPF], ocupante do cargo de [CARGO/FUNÇÃO], representando o município/órgão gestor [NOME DO MUNICÍPIO OU ENTIDADE], DECLARO, sob as penas da lei, para fins de cadastramento e instrução do processo no Sistema Estadual de Informações sobre Unidades de Conservação do Estado do Pará (SEINUC/PA) relativo ao Ano-Base [ANO_BASE]:

1. Que todas as informações, relatórios, atas e dados vetoriais apresentados referentes à Unidade de Conservação [NOME DA UNIDADE DE CONSERVAÇÃO] são autênticos, fidedignos e expressam a exata verdade dos fatos ocorridos no Ano-Base.
2. Que os dados vetoriais encaminhados obedecem ao Datum SIRGAS 2000 e refletem a real delimitação territorial da Unidade de Conservação.
3. Estar ciente de que a inserção de informações falsas ou a adulteração de documentos sujeitará o subscritor às sanções administrativas, civis e penais previstas na Lei Federal nº 9.605/1998 e no Código Penal Brasileiro, além do indeferimento do pleito de Habilitação no ICMS Ecológico.

[CIDADE - PA], _____ de _______________ de 202X.

___________________________________________________
[NOME DO DECLARANTE]
[CARGO E INSTITUIÇÃO]
Assinatura Digital (Gov.br ou ICP-Brasil)
```
