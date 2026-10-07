# EPIC1-T3: Criar a Portaria de Diretrizes Técnicas

**Status:** 🟡 **EM ABERTO**  
**Responsável:** Equipe Técnica / Geoprocessamento  
**Base Legal:** Art. 4º, II e III e Art. 12 da Minuta do Decreto SEINUC/PA | Benchmark Portaria IEPHA nº 34/2024

---

## 📄 Escopo da Portaria Técnica

A Portaria de Diretrizes Técnicas fixará os requisitos formais para formatação, validação e transmissão dos documentos exigidos pelo SEINUC/PA, garantindo padronização digital e integridade cartográfica.

---

## 🎯 Subtarefas de Execução

### Subtarefa 1: Formato e Padrão de Arquivos Digitais
* **Documentos Textuais e Comprovantes:**
  * Formato obrigatório: **PDF searchable (com camada OCR de texto)**.
  * Organização obrigatória: **Folha de Rosto** identificando o Ente/UC, seguido de **Sumário Paginado**.
  * Tamanho máximo por arquivo: 50 MB (para arquivos maiores, fracionar em volumes codificados: `VOL_01`, `VOL_02`).
* **Dados Geoespaciais (Vetores):**
  * Formatos aceitos: **Shapefile (.shp, .dbf, .shx, .prj compressos em .zip)** ou **KML/KMZ**.
  * Sistema de Referência de Coordenadas (Datum): **SIRGAS 2000 (EPSG:4674)**.
  * Obrigatoriedade de fecho topológico: Polígonos sem sobreposição de vértices ou lacunas (*gap/overlap* zero).

### Subtarefa 2: Regras de Nomenclatura e Indexação
Padronização rígida do nome dos arquivos para garantir recepção e processamento por algoritmos de triagem:
* `[CODIGO_MUNICIPIO]_[SIGLA_UC]_[QUADRO]_[ANO_BASE].[ext]`
* *Exemplo:* `PARAGOMINAS_APA_BOSQUE_Q1_2025.pdf` | `PARAGOMINAS_APA_BOSQUE_VETOR_2025.zip`

### Subtarefa 3: Declaração de Veracidade das Informações
Criação do modelo oficial de **Declaração de Veracidade e Responsabilidade Técnica** (Anexo I da Portaria):
* Assinatura obrigatória do Prefeito Municipal, Secretário de Meio Ambiente ou Gestor da UC.
* Inclusão do termo expresso de ciência das sanções administrativas e penais da Lei nº 9.605/1998 para prestação de informações falsas.

### Subtarefa 4: Elaboração da Minuta da Portaria
Redação dos artigos normativos estabelecendo os critérios de recusa imediata na fase de triagem (ilegibilidade, ausência de assinatura, sistema de projeção inconsistente).
