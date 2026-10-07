# EPIC2-T7: Definir Protocolo de Integração com CNUC, ITERPA e SEMAS Licenciamento

**Status:** Em Aberto  
**Responsável:** Equipe de Dados / TI  
**Base Legal:** Art. 67, §3º e Art. 68, §4º da Lei PA nº 10.306/2023 | Art. 6º da Minuta do Decreto SEINUC/PA

---

## 1. Escopo da Interoperabilidade e Notificação Interinstitucional

Garantir o alinhamento total das informações estaduais e municipais do Pará com o Cadastro Nacional de Unidades de Conservação (CNUC/MMA) e a transmissão periódica obrigatória aos órgãos fundiário e licenciador estaduais.

---

## 2. Subtarefas de Execução

### Subtarefa 1: Identificador Único (Chave Primária)
* Definição do ID oficial da UC utilizando como chave primária o código originário do CNUC (`COD_CNUC`), impedindo a criação de registros duplicados e sincronizando históricos.

### Subtarefa 2: Tabela De-Para (Mapeamento de Atributos CNUC)
Estruturação da correspondência entre os campos do SEINUC e do CNUC:

| Campo SEINUC (Pará) | Campo CNUC (MMA) | Regra de Conversão / Tipo |
| :--- | :--- | :--- |
| `nome_uc` | `nomeUC` | Texto |
| `categoria_manejo` | `idCategoria` | Mapeamento por Código de Categoria SNUC |
| `esfera_adm` | `esfera` | 1 = Federal, 2 = Estadual, 3 = Municipal |
| `area_oficial_ha` | `areaTotal` | Numérico Flutuante (Decimal) |
| `vetor_limite_zip` | `geometria` | SIRGAS 2000 (WGS84) Reprojeção automática |
| `plano_manejo_status` | `possuiPlanoManejo` | Booleano (Sim/Não) + Data de Publicação |
| `conselho_status` | `possuiConselho` | Booleano (Sim/Não) + Tipo de Conselho |

### Subtarefa 3: Protocolo Trienal Obrigatório com ITERPA e SEMAS (Art. 68, §4º)
* **Rotina Trienal de Repasse de Dados:** Implementação de rotina de exportação automatizada para repassar a base cadastral e vetorial do SEINUC a cada **3 (três) anos** para:
  1. **Instituto de Terras do Pará (ITERPA):** Para atualização da malha fundiária e arrecadação de terras devolutas (Art. 110).
  2. **SEMAS (Diretoria de Licenciamento Ambiental):** Para subsidiar análises de impacto e restrições socioambientais no licenciamento do Estado.

### Subtarefa 4: Endpoint de Exportação API / Web Service
* Desenvolvimento da especificação técnica de API REST (JSON/GeoJSON) para exportação de dados aos órgãos parceiros e ao Ministério do Meio Ambiente.
