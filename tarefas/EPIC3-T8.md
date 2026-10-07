# EPIC3-T8: Desenhar o Fluxo de Envio de Documentos (Upload)

**Status:** Em Aberto  
**Responsável:** Equipe de TI / Processos  
**Base Legal:** Art. 4º, II da Minuta do Decreto SEINUC/PA | Benchmark IEPHA/MG

---

## 1. Escopo da Esteira Digital de Envio de Documentos

Desenho da infraestrutura e regras de transmissão para envio dos dados das UCs pelos gestores municipais e executores estaduais ao sistema SEINUC.

---

## 2. Subtarefas de Execução

### Subtarefa 1: Arquitetura de Recepção Digital
* **Portal Web SEINUC (Upload Direto):** Interface web para preenchimento dos formulários dos Quadros I, II e III e envio de arquivos até 50 MB.
* **Repositório Seguro FTP / SFTP:** Servidor seguro para o recebimento de arquivos pesados (ex: relatórios volumosos, acervos fotográficos e bases vetoriais brutas).

### Subtarefa 2: Regras de Nomenclatura e Organização de Pastas
Estruturação de diretórios obrigatória para recepção dos pacotes de dados:

```
[PACOTE_ENVIO]/
├── 01_OFICIO_E_DECLARACAO/
│   ├── OFICIO_ENCAMINHAMENTO.pdf
│   └── DECLARACAO_VERACIDADE.pdf
├── 02_DOCUMENTOS_GESTAO/
│   ├── ATO_CRIACAO.pdf
│   ├── ATAS_CONSELHO_2025.pdf
│   └── PLANO_DE_MANEJO.pdf
├── 03_DADOS_VETORIAIS/
│   └── LIMITES_E_ZONEAMENTO_SIRGAS2000.zip
└── 04_INVENTARIOS_AMBIENTAIS/
    └── RELATORIO_FAUNA_FLORA.pdf
```

### Subtarefa 3: Recibo Eletrônico de Protocolo
* Emissão automática de **Recibo de Envio com Hash de Validação (SHA-256)**, comprovando a data, hora exata e a relação de arquivos transmitidos pelo gestor.
