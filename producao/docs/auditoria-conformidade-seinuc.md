# AUDITORIA TÉCNICA E JURÍDICA — SEINUC/PA

> **Documento de Auditoria Especializada** — Direito Ambiental, Geoprocessamento e Gestão Pública
> **Objeto:** Acervo documental do Sistema Estadual de Informações sobre Unidades de Conservação do Estado do Pará (SEINUC/PA)
> **Corpus auditado:** `producao/docs/` (5 produtos), `ROADMAP.md`, `EPICOS.md`, `tarefas/` e `documentos/referencias/`
> **Data da análise:** 07 de outubro de 2026
> **Base normativa verificada na íntegra:** Lei PA nº 10.306/2023 (texto consolidado do DOE nº 35.658), Lei Federal nº 9.985/2000, Decreto Federal nº 4.340/2002, Lei PA nº 7.638/2012 + Decreto PA nº 1.064/2020 (ICMS Verde) e Lei PA nº 8.972/2020 (processo administrativo estadual).

---

## VEREDITO EXECUTIVO

A documentação é **tecnicamente ambiciosa e bem estruturada**, mas **NÃO está pronta para publicação**. Ela contém **4 falhas críticas de legalidade** e **1 conflito de calendário insolúvel** com o ICMS Verde vigente. O produto nasce com risco real de **vício de competência**, **nulidade do rito recursal** e **inoperância do principal caso de uso declarado (subsidiar o ICMS Ecológico)**.

> **Risco-síntese:** um Decreto que atribui ao IDEFLOR-Bio competências que a Lei 10.306 reservou ao órgão central (SEMAS); que cria um rito de ICMS com prazos incompatíveis com o Decreto 1.064/2020; e que removeu do texto final o único artigo que dava base legal ao mascaramento de dados sensíveis — embora o Portal ainda o cite.

---

## METODOLOGIA

- Extração integral do texto da Lei 10.306/2023 (PDF) e leitura dos 5 produtos consolidados e dos 12 arquivos de tarefa.
- Conferência do texto original da minuta anterior (`minuta-elberth.docx`) para detectar regressões.
- Verificação externa dos diplomas não presentes no repositório (7.638/2012, 1.064/2020, 8.972/2020, 8.096/2015) em fontes oficiais (SEMAS, SEFA, LEGIS-PA, IOEPA).

---

# EIXO 1 — CONFORMIDADE LEGAL ESTRITA

## 1.1. Matriz de cobertura da Lei nº 10.306/2023

| Dispositivo | Exigência | Cobertura nos produtos | Status |
| :--- | :--- | :--- | :---: |
| Art. 67, *caput* | SEINUC = banco de UCs **estaduais** | Decreto estende a municipais e RPPN (Art. 1º, l.13) | ⚠️ Ampliação sem base expressa |
| Art. 67, §2º, I | paisagem, fauna, flora, ameaçadas, **recursos hídricos, clima, solos** | Módulo I cobre fauna/flora/hídricos/solo; **`clima` e `paisagem` ausentes** do dicionário (l.26-36) | ❌ Lacuna |
| Art. 67, §2º, II | georreferenciamento **inclusive zoneamento** | Módulo II ok; **sem camada própria de Zona de Amortecimento** | ⚠️ Parcial |
| Art. 67, §2º, III | situação fundiária | Módulo II/IV ok | ✔ |
| Art. 67, §2º, IV | sociais, econômicos, culturais, **antropológicos** e turísticos | Módulo III cobre socioeconômico; **antropológico/arqueológico ausente** | ❌ Lacuna |
| Art. 67, §3º | integração CNUC | Decreto Art. 10 (l.82) ok | ✔ |
| Art. 67, §4º | **Programas de pesquisa integrados** | **Nenhum campo/módulo** | ❌ Omissão |
| Art. 67, §5º | regulamento pelo Chefe do Executivo | Decreto cumpre | ✔ |
| Art. 67, §6º | LAI, proteção de dados, **patrimônio genético e conhecimento tradicional** | LGPD só no doc do Portal; **PG/CTA ausentes do Decreto** | ❌ Lacuna |
| **Art. 68, *caput*** | **o órgão central (SEMAS) organiza e mantém o SEINUC, com colaboração do IDEFLOR-Bio** | Decreto Art. 13 dá a organização ao **IDEFLOR-Bio** (l.94-97) | 🔴 **INVERSÃO DE COMPETÊNCIA** |
| Art. 68, §1º | inclui **aspectos arqueológicos** | Ausente | ❌ Lacuna |
| Art. 68, §3º | demais órgãos do SEUC fornecem dados | Não operacionalizado | ⚠️ |
| Art. 68, §4º | repasse trienal ao fundiário e licenciador | Decreto Art. 11 (l.84-86) ok | ✔ |
| **Art. 110** | ITERPA – levantamento de devolutas em 5 anos | Citado, mas **sem prazo/rastreio** (l.85) | ⚠️ Parcial |
| Art. 111 | mapas/cartas oficiais com UCs a partir do SEINUC | Portal + Decreto Art. 12 ok | ✔ |
| **Art. 113** | relatório **quadrienal** + **relatório anual (§1º)** | Decreto Art. 17 só traz o quadrienal (l.109); **anual inexiste** | ❌ Lacuna + inversão de competência |
| **Art. 114** | reavaliação de UCs legadas em **5 anos** (prazo encerra em 2028) | Mencionado como `legada_status`, **sem prazo/rastreio** (l.171) | ⚠️ |
| Art. 112 | Sítios Pesqueiros em 2 anos — **prazo já expirado em 22/12/2025** | Mencionado sem tratamento do prazo vencido | 🔴 Risco atual |
| **Art. 117** | 20% dos recursos a UCs municipais | **Não monitorado** em nenhum produto | ❌ Omissão |

## 1.2. Contradições em relação ao SNUC / Decreto 4.340/2002 / ICMS

1. **🔴 Competência invertida (Art. 68 *caput* vs. Decreto Arts. 13-14).** A Lei 10.306/2023 define o **órgão central = SEMAS** (Art. 9º, II) e executor = IDEFLOR-Bio (Art. 9º, III). O Art. 68 atribui a **organização e manutenção do SEINUC ao órgão central**, "com a colaboração do IDEFLOR-Bio". O Decreto transfere essa titularidade ao IDEFLOR-Bio e rebaixa a SEMAS a "apoio institucional". Decreto não pode deslocar competência reservada por lei → **vício de legalidade/excesso regulamentar**. O mesmo erro se repete no Art. 17 (relatório quadrienal deveria ser publicado pelo órgão central "por intermédio do órgão gestor").
2. **🔴 O SEINUC é anunciado como base do ICMS Ecológico, mas não é.** O Decreto Art. 2º, II (l.17) declara o SEINUC "base técnica e oficial" do ICMS. Na prática, o **ICMS Verde (Lei 7.638/2012 + Decreto 1.064/2020)** é calculado pela **SEMAS** com variáveis espaciais (CAR, ARL, APP, RVN, AA, UR, US, ACar) e abrange **"unidades de conservação E outras áreas protegidas"** (APP, Reserva Legal, Terras Indígenas, estradas/rios cênicos). O SEINUC cobre apenas UCs e RPPNs → **não é base suficiente**, e a competência de cálculo/pontuação não é do IDEFLOR-Bio.
3. **🔴 Sanção de perda de ICMS sem base.** Decreto Art. 15 (l.101) comina "perda dos repasses do ICMS Ecológico" por dado falso — matéria tributária reservada à Lei 7.638/2012 e seu regulamento, não podendo ser criada por decreto regulamentador de sistema de informações.
4. **Terminologia divergente do SNUC.** O produto mistura "Plano de Manejo" (federal) e "Plano de Gestão" (estadual, Lei 10.306, Art. 2º, XXII). O Decreto Art. 3º, III, "b" e o `plano_manejo_status` do Módulo III usam a nomenclatura federal — deve-se padronizar para **"Plano de Gestão"**.
5. **"Revisão quinquenal" do plano criada por decreto.** Art. 3º, III, "b" (l.37) impõe "controle automatizado de revisão quinquenal". A Lei 10.306 (Art. 54) fixa **elaboração em 5 anos**, não ciclo de revisão — a regra precisa de base legal explícita.
6. **Categorias de UC incompletas.** O vocabulário `categoria` (texto livre 254) não contempla as categorias estaduais reais (ex.: **Parque Estadual Ambiental, Reserva Estadual de Pesca, Floresta Estadual**), só siglas federais genéricas (`ESEC`, `APA`, `RESEX`...).

---

# EIXO 2 — RITOS PROCESSUAIS E SEGURANÇA JURÍDICA

## 2.1. Conflito de calendário com o ICMS Verde (CRÍTICO)

**O rito do Decreto é temporalmente inoperante.** Comparação:

| Etapa | ICMS Verde vigente (Lei 7.638 + Decreto 1.064/2020) | Minuta SEINUC |
| :--- | :--- | :--- |
| Índice/resultado **provisório** | Publicado no DOE até **31 de maio** | **15 de julho** (Decreto Art. 7º, III, l.68) |
| Recurso/impugnação | **30 dias** | **15 dias** |
| **Definitivo** | **60 dias** após o provisório (~31/07) | **30 de setembro** (Art. 9º, l.76) |

**Consequência:** se o SEINUC alimentasse o ICMS Verde, o resultado só sairia **após o fechamento do índice**. O Decreto, portanto, cria um **segundo rito sobreposto** ao da SEMAS, com prazos incompatíveis. É a falha operacional mais grave e a maior fonte de contencioso com municípios.

## 2.2. Contraditório e ampla defesa — problemas concretos

- **🔴 Contagem de prazo ilegal.** O Decreto fixa recurso em **"15 dias corridos"** (Art. 8º, l.70). A **Lei Estadual nº 8.972/2020 (LEPA)** — que **não é citada em nenhum produto** — determina, no art. 83, contagem em **dias úteis** e, no art. 139, aplicação subsidiária. O TJPA já aplica a LEPA (dias úteis) inclusive a procedimentos especiais. Um recurso contado em dias corridos tende a ser **anulado**.
- **🔴 Prazo divergente do próprio ICMS Verde** (15 vs. 30 dias), gerando dupla janela recursal para o mesmo município.
- **Preclusão documental desproporcional.** Art. 8º, §2º veda "documentos novos". Combinado com a triagem, cria assimetria: o Decreto não define **o que é vício sanável**, não prevê **intimação específica do déficit** antes da rejeição e não garante produção de prova contra a nota. Isso colide com a ampla defesa (CF art. 5º, LV; LEPA).
- **Efeito do recurso não definido.** O Decreto não diz se o recurso tem efeito **suspensivo**. Sem isso, o resultado definitivo pode ser publicado antes do julgamento → nulidade.
- **Decisão imotivada.** Não se exige que o extrato provisório publique **motivação/nota por quesito**; sem isso, o município não sabe o que contestar (vedação à "decisão surpresa").
- **Julgador e recorrido são o mesmo.** A CT-SEINUC emite a nota **e** julga o recurso (Art. 6º e Art. 8º). Falta câmara de revisão distinta, ou participação decisória da SEMAS.

## 2.3. Comissão Técnica (CT-SEINUC) — lacuna estrutural

O Art. 6º apenas "institui" a Comissão "no âmbito do IDEFLOR-Bio". **Faltam**: composição, número de membros, representação do órgão central e dos municípios, mandato, quórum, impedimentos/suspeição, suplentes, forma de deliberação e desempate. Uma comissão sem regras de composição é **nula por falta de motivação da autoridade** e vulnerável a questionamento de imparcialidade.

## 2.4. Admissibilidade, preclusão e prazos operacionais

- **Rejeição sumária sem contingência.** Intempestividade (Checklist item 01) é eliminatória sem previsão para **indisponibilidade do portal/SFTP**, caso fortuito ou força maior — risco de judicialização trivial (basta o sistema cair em 31/01).
- **Falta integração com o protocolo oficial do Estado.** O manual inventa `ANO-MUNICIPIO-SEINUC-Nº` (l.45) sem vinculação ao processo administrativo eletrônico estadual (autuação/numeração única). Isso compromete rastreabilidade e o próprio contraditório.
- **Requisitos técnicos não previstos.** `SIGLA_UC` não possui tabela oficial; UCs interestaduais/multimunicipais não têm regra de código IBGE (l.39); não há tratamento para RPPN sobreposta a mais de um município.
- **Inconsistência 50 MB × 200 MB.** A Portaria limita **50 MB por arquivo** (Art. 2º, §2º, l.25), mas o manual afirma pacotes de até **200 MB** no Portal (l.40). Escopos diferentes, mas sem explicação — gera glosa indevida.

---

# EIXO 3 — RIGOR TÉCNICO E GEOPROCESSAMENTO

## 3.1. O que está correto

- **SIRGAS 2000 (EPSG:4674)** é o datum oficial correto para o Pará. ✔
- Uso de **WMS 1.3.0 / WFS 2.0.0 / WCS 2.0.1** e **Perfil MGB/INDE** é adequado em conceito. ✔
- Estrutura modular (Ambiental / Geo-Fundiário / Gestão / Integração) é coerente com o Art. 67, §2º. ✔

## 3.2. Falhas técnicas

1. **🔴 O "Esquema GeoJSON" não é GeoJSON.** O bloco do Módulo II (`especificacao-modulos-dados-seinuc.md`, l.131-153) é um `type: object` **sem `geometry`**, sem `Feature`/`FeatureCollection`, sem CRS e sem validação de coordenadas. Não valida nada de geoespacial.
2. **🔴 Incompatibilidade conceitual GeoJSON × SIRGAS 2000.** A **RFC 7946** exige WGS84/CRS84 em GeoJSON. Servir "vetores brutos em GeoJSON" sob SIRGAS 2000 (como propõe o Portal, l.63) é tecnicamente contraditório (SIRGAS2000 e WGS84 são praticamente coincidentes, mas formalmente distintos, e a RFC ignora datum alternativo). Para SIRGAS 2000, o correto é **GeoPackage/Shapefile/GML**.
3. **Numeração de módulos divergente.** O **Decreto (Art. 3º, l.26-43)** define: II = Geotecnologias, III = Gestão, **IV = Fundiário/Dominial/RPPN**. A **especificação (l.15-17)** define: II = Geo/Fundiário, III = Gestão/Socio, **IV = Interoperabilidade**. O manual (l.18-33) segue o Decreto. **Há duas taxonomias inconciliáveis no mesmo projeto.**
4. **Vocabulários não aplicados no schema.** As tabelas trazem enums (`relevo_tipologia`, `bacia_hidrografica`, `fitofisionomia`), mas o JSON Schema os declara como `"type":"string"` sem `enum` (l.52-59) — a validação **não controla vocabulário**.
5. **Regra de negócio não validada.** `conselho_reunioes_qtd`: a tabela diz "**mínimo de 2 reuniões comprovadas**" (l.167), mas o schema só impõe `"minimum": 0` (l.189). O requisito legal/ICMS não é exigível.
6. **`COD_CNUC` prometido e ausente.** O Módulo IV cita a chave `COD_CNUC` (l.216), mas **nenhum schema/tabela DBF** a contém — quebra a integração com o CNUC (Art. 67, §3º).
7. **Campos inconsistentes entre tabela e schema.** `tipo_flore`, `obs`, `cat_territ`, `grau_infestacao` aparecem no dicionário e **somem** do schema; `data_de_cr` e `situacao_l` (ato legal) são **opcionais** no schema, quando deveriam ser obrigatórios para validar a UC.
8. **Zona de Amortecimento sem camada.** O Art. 54, §1º da Lei manda o plano abranger a ZA; o Decreto Art. 3º, II, "a" fala em georreferenciar a ZA, mas **não há geometria/layer nem atributo** para isso.
9. **Tipos DBF sem precisão.** `area_ha`/`area_decre` descritos como "Número 24" sem casas decimais (DBF exige N,24,2); datas como texto (`data_de_cr` DD/MM/AAAA) sem `format: date`.
10. **Metadata INDE incompleta.** Faltam **CSW**, **UUID do conjunto**, versão do perfil MGB, e periodicidade de atualização — sem isso não há catalogação válida na INDE.
11. **Obrigação sem base legal.** Decreto Art. 3º, II, "c" exige limites verticais (subsolo/espaço aéreo) "quando exigido pela categoria" — não há tal exigência na Lei 10.306/2023 nem no SNUC.
12. **Sem SLA, versionamento, trilha de auditoria, backup/DR** e sem definição de **controlador/operador de dados**.

---

# EIXO 4 — SEGURANÇA DA INFORMAÇÃO, LAI E LGPD

## 4.1. Mascaramento de espécies ameaçadas — base legal evaporou

- **🔴 Referência normativa inexistente.** O Portal e a tarefa EPIC4-T11 citam **"Art. 7º do Decreto"** como base do mascaramento (l.4 e l.74-80). No **texto final**, o Art. 7º é o **procedimento de avaliação/triagem** — não trata de sigilo. A base citada **não existe**.
- **A causa:** a minuta anterior (`minuta-elberth.docx`) tinha, no **Art. 7º**, "amplo e livre acesso... ressalvadas as informações cujo sigilo seja imprescindível à segurança da biodiversidade". **O texto final suprimiu esse artigo** (não há capítulo de transparência/sigilo), mas os produtos derivados continuaram a citá-lo. **É uma regressão grave e um erro de rastreabilidade.**
- **Tensão com a própria lei.** O Art. 59, I determina que a relação de espécies ameaçadas seja de "**amplo e livre acesso**", e o §único manda enviá-la ao órgão central para o SEINUC. O mascaramento é defensável (biopirataria/prevenção), mas **precisa de base expressa** e de regra que reconcilie "amplo acesso à lista" com "proteção da localização exata".
- **Cobertura insuficiente.** Mascara-se apenas **CR**; EN/VU ficam expostos. E, sobretudo, a regra vale só para o "**visualizador público**" — **o WFS/WMS também são públicos** e podem vazar a coordenada exata via `GetFeature`/`GetFeatureInfo`. **Não há separação "servidor público limpo × servidor técnico sujo"**, nem restrição de `GetFeatureInfo`.

## 4.2. LGPD — tratamento superficial e incompleto

- A única menção está no doc do Portal (l.82-83): tarjar CPF/telefone/endereço, **preservando o nome completo**. Faltam:
  - **base legal** do tratamento (art. 7º/11 LGPD) e finalidade;
  - definição de **controlador, operador e encarregado (DPO)**;
  - **direitos do titular**, retenção, eliminação e **RIPD/DPIA**;
  - regras para dados sensíveis e para **crianças/adolescentes** (uso público);
  - **segurança da informação** (controle de acesso, cifra, logs, ISO 27001/27002);
  - **LGPD no próprio Decreto** (a Lei 10.306, Art. 67, §6º exige expressamente observância da proteção de dados).
- **Patrimônio genético e conhecimento tradicional associado** (Art. 67, §6º) **não são tratados**: não há referência à **Lei nº 13.123/2015**, ao **SisGen**, nem regra de anonimização de coordenadas de populações tradicionais (dados sensíveis e de risco à biopirataria).

## 4.3. Integridade documental

- O **SHA-256** (manual l.48) garante **integridade**, mas **não autoria/não repúdio**. Não há **assinatura digital do pacote** nem **carimbo de tempo (RFC 3161/ICP-Brasil)**; a assinatura existe só na Declaração. Recomenda-se assinar o pacote/hash.

---

# EIXO 5 — PONTOS CEGOS, GARGALOS E MELHORIAS

## 5.1. Riscos não previstos (por severidade)

| # | Risco | Severidade |
| :-- | :--- | :---: |
| 1 | **Colisão de calendário** SEINUC × ICMS Verde (provisório 15/07 vs 31/05) | 🔴 Crítico |
| 2 | **Inversão de competência** SEMAS ↔ IDEFLOR-Bio (Art. 68 *caput*) | 🔴 Crítico |
| 3 | **Recurso em "dias corridos"** contra a LEPA (dias úteis) | 🔴 Crítico |
| 4 | **Sem base legal** para mascaramento/LGPD no Decreto final | 🔴 Crítico |
| 5 | Perda de ICMS por decreto (matéria tributária) | 🟠 Alto |
| 6 | CT-SEINUC sem composição/mandato/impedimentos | 🟠 Alto |
| 7 | Exposição de coordenadas sensíveis via WFS/GetFeatureInfo | 🟠 Alto |
| 8 | Prazo do Art. 112 **já expirado** (22/12/2025) sem tratamento | 🟠 Alto |
| 9 | Sem contingência para queda do portal em 31/01 | 🟠 Alto |
| 10 | Sem relatório anual (Art. 113, §1º) e sem rastreio de Art. 114 | 🟠 Alto |
| 11 | Numeração de módulos divergente entre Decreto e especificação | 🟡 Médio |
| 12 | `COD_CNUC`/`clima`/`arqueológico`/pesquisa ausentes | 🟡 Médio |
| 13 | GeoJSON inválido / incompatível com SIRGAS | 🟡 Médio |
| 14 | Sem efeito suspensivo do recurso / sem decisão motivada | 🟡 Médio |
| 15 | 20% de destinação municipal (Art. 117) não monitorado | 🟡 Médio |
| 16 | Inconsistência 50 MB × 200 MB | 🟢 Baixo |

## 5.2. Recomendações concretas

### Bloco A — Correções jurídicas obrigatórias (antes de publicar)

1. Reescrever Arts. 13-14 e 17 para refletir o Art. 68 *caput*: **SEMAS (órgão central)** organiza e mantém o SEINUC; **IDEFLOR-Bio** opera/executa. CT-SEINUC colegiada com **presidência/coordenação da SEMAS** e assento dos municípios.
2. **Remover a perda de ICMS** do Decreto (Art. 15) e limitar a sanção a **falsidade (CP 299 + L. 9.605)** e responsabilização administrativa pela **LEPA (Lei 8.972/2020)**.
3. **Alinhar o rito recursal à LEPA**: prazo em **dias úteis**, previsão de **intimação motivada**, **efeito suspensivo**, produção de prova e **câmara de revisão distinta** da que pontuou.
4. Inserir **artigo de transparência/sigilo** que dê base expressa ao **mascaramento** e à **LGPD** (ver Bloco C), corrigindo as citações erradas do Portal.
5. Acrescentar dispositivos para os **Art. 59, 67 §4º, 68 §1º/§3º, 113 §1º** (clima, arqueológico, pesquisa, relatório anual, fluxo da lista de ameaçadas).

### Bloco B — Reconciliação com o ICMS Ecológico

6. Substituir a pretensão de "base oficial do ICMS" por **integração formal ao ICMS Verde da SEMAS**: o SEINUC fornece o **subconjunto de UCs/RPPN** como *input* do índice, **respeitando o calendário do Decreto 1.064/2020** (provisório 31/05; impugnação 30 dias; definitivo em 60 dias), ou o Decreto será letra morta.
7. Definir explicitamente que **não substitui** as demais variáveis do ICMS Verde (CAR, APP, ARL, RVN, AA, UR, US, ACar) e as demais áreas protegidas (TI, APP, RL, cênicos).
8. Criar monitoramento dos **20% de destinação municipal (Art. 117)** no Painel do Portal.

### Bloco C — Segurança, LAI e LGPD

9. **Regra de mascaramento em três níveis** (exato/servidor técnico restrito; quadrícula 10×10 km/público; metadados), aplicada **na WMS, WFS, WCS e GetFeatureInfo**, com *throttling* e log de acesso.
10. Incorporar **Lei 13.123/2015 + SisGen** (patrimônio genético e CTA) e proteção reforçada de **terras indígenas/comunidades tradicionais**.
11. Definir **controlador, operador, DPO, base legal, retenção, RIPD e segurança** (ISO 27001/27002), com plano de resposta a incidentes.
12. **Assinatura digital do pacote + carimbo de tempo**, além do SHA-256.

### Bloco D — Excelência técnica/geográfica

13. Publicar o dicionário **canônico** com **tabela oficial de categorias estaduais**, `COD_CNUC`, `esfera`, `clima`, `paisagem`, `arqueológico`, camada de **Zona de Amortecimento** e **programas de pesquisa**.
14. Usar **JSON Schema + validador geoespacial real** (GeoPackage/GML para SIRGAS 2000; GeoJSON só se documentada a equivalência/conversão) e impor enums, `format: date`, precisão DBF e topologia (`gap/overlap=0`).
15. Implementar **CSW/INDE**, UUID de conjunto, versão MGB e periodicidade; padronizar nomenclatura de módulos entre Decreto, especificação e manual.

### Bloco E — Governança operacional

16. **Contingência de prazo** (prorrogação automática por indisponibilidade comprovada do sistema) e **integração ao protocolo eletrônico estadual**.
17. Publicar **SLA de análise**, cronograma anual estável e **regra transitória** para o Art. 112 (prazo vencido) e Art. 114.
18. **Consulta pública** prévia das minutas com municípios e **parecer da PGE/PA** antes da assinatura.

---

## CONCLUSÃO

A engenharia documental é de bom nível, mas o pacote confunde **produto técnico** com **segurança jurídica**. Os quatro pontos decisivos — **competência (SEMAS × IDEFLOR-Bio), calendário (ICMS Verde), contagem de prazos (LEPA) e base legal do sigilo/LGPD** — não são ajustes de redação; são **condições de validade**. Sem corrigi-los, o Decreto tende a: (i) ser questionado por **excesso regulamentar**; (ii) **não influenciar o ICMS Verde** que diz subsidiar; (iii) **nulidade do rito recursal**; e (iv) **vazamento de dados sensíveis** ou **insegurança jurídica** na transparência.

**Recomendação final:** não publicar o Decreto no estado atual. Revisar os Blocos A e B com a PGE e a SEMAS e reapresentar como **regulamento conjunto (SEMAS + IDEFLOR-Bio)**, com anexos técnicos versionados e calendário sincronizado ao Decreto 1.064/2020.

---

## ANEXO — Referências de rastreabilidade

- Produtos auditados: `minuta-decreto-seinuc.md`, `especificacao-modulos-dados-seinuc.md`, `minuta-portaria-diretrizes-tecnicas.md`, `manual-fluxo-envio-e-triagem.md`, `especificacao-portal-transparencia-ogc.md`.
- Planejamento: `ROADMAP.md`, `EPICOS.md`, `tarefas/EPIC1..EPIC4`.
- Minuta anterior comparada: `producao/docs/minuta-elberth.docx`.
- Fontes normativas externas conferidas: Lei PA 7.638/2012 e Decreto PA 1.064/2020 (SEMAS/ICMS Verde); Lei PA 8.972/2020 (LEPA); Lei PA 8.096/2015 (estrutura administrativa); Decreto PA 775/2013.

> **Observação de método:** os PDFs não são legíveis diretamente pelo modelo auditor; o texto da Lei nº 10.306/2023 foi extraído integralmente e as normas ausentes no repositório (7.638/2012, 1.064/2020, 8.972/2020) foram conferidas em fontes oficiais. Recomenda-se juntar ao repositório os PDFs do Decreto 1.064/2020 e da Lei 8.972/2020, hoje referenciados sem estar disponíveis em `documentos/referencias/`.
