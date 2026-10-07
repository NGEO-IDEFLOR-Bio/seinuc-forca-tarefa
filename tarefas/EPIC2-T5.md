# EPIC2-T5: Estruturar Módulo de Georreferenciamento e Fundiário (Quadro II)

**Status:** Em Aberto  
**Responsável:** Equipe de Geoprocessamento / Cadastro  
**Base Legal:** Art. 67, §2º, II e III da Lei PA nº 10.306/2023 | Art. 3º, II e IV da Minuta do Decreto SEINUC/PA | Decreto Federal nº 4.340/2002

---

## 1. Escopo do Módulo Georreferenciado e Fundiário

Definição da arquitetura de dados espaciais e fundiários para armazenar polígonos, zoneamento, limites verticais, situação jurídico-dominial e cadastro de Reservas Particulares do Patrimônio Natural (RPPNs).

---

## 2. Subtarefas de Execução

### Subtarefa 1: Padrão Geospacial e Vetorial
* **Mapeamento de Perímetro:** Geometria oficial da UC em Polígono 2D.
* **Zoneamento Ambiental:** Polígonos das zonas de uso (Ex: Zona de Preservação, Zona de Uso Intensivo, Zona de Amortecimento).
* **Atributos da Tabela de Vetores:**
  * `NOME_UC`, `CATEGORIA`, `ESFERA`, `ATODECRIACAO`, `AREA_HA_OFICIAL`, `AREA_HA_CALCULADA`.

### Subtarefa 2: Módulo Fundiário, Dominial e RPPNs
* **Tipologia Dominial:**
  * Terra Pública Estadual.
  * Terra Pública Federal / Municipal.
  * Propriedade Privada Regularizada / Pendente de Desapropriação.
  * Território Tradicional (Quilombola / Terra Indígena / Assentamento).
  * **Reserva Particular do Patrimônio Natural (RPPN):** Cadastro do imóvel privado de origem, número da matrícula em cartório (RGI) e averbação do Termo de Compromisso de perpetuidade.
* **Percentual de Regularização Fundiária:** Campo numérico de 0% a 100%.

### Subtarefa 3: Delimitação dos Limites Verticais
* Registro das cotas de altitude (subsolo e espaço aéreo) quando aplicável para categorias específicas (ex: Monumento Natural, Cavernas).

### Subtarefa 4: Protocolo de Validação Geográfica
Regras de validação automatizada: conferência se o polígono da UC municipal/estadual está contido nos limites do Estado do Pará e se há sobreposições não autorizadas com outras UCs de mesma esfera.
