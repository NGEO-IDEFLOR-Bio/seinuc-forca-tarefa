# Template ABNT para Quarto

Template [Quarto](https://quarto.org) para criação de documentos acadêmicos seguindo as normas da ABNT (Associação Brasileira de Normas Técnicas).

Baseado na classe LaTeX [`abntex2`](https://www.abntex.net.br/) (família [`memoir`](https://www.ctan.org/pkg/memoir)).

## Requisitos

- **[Quarto](https://quarto.org)** 1.8.27 ou superior
- **[R](https://www.r-project.org/)** 4.5.2 ou superior
- **[LaTeX](https://www.latex-project.org/)** com engine [`lualatex`](https://www.luatex.org/)
  - Recomendado: [TinyTeX](https://yihui.org/tinytex/) (instalável via pacote R `tinytex`)
- **Fontes**: [Noto Sans](https://fonts.google.com/noto/specimen/Noto+Sans) e [Noto Sans Mono](https://fonts.google.com/noto/specimen/Noto+Sans+Mono)

## Estrutura de Arquivos

```
.
├── _quarto.yml          # Configuração principal do projeto
├── index.qmd            # Arquivo principal / Introdução
├── qmd/                 # Capítulos e seções pré-textuais/pós-textuais
│   ├── development.qmd  # Desenvolvimento
│   ├── conclusion.qmd   # Conclusão
│   ├── appendix-1.qmd   # Apêndices
│   └── annex-1.qmd      # Anexos
├── _extensions/         # Extensões Quarto (abnt, latex-environment)
├── tex/                 # Arquivos LaTeX customizados
├── references.bib       # Referências bibliográficas
└── R/                   # Scripts de pré/pós-processamento
```

## Como Usar

### 1. Renderizar o documento

No terminal, dentro do diretório do projeto:

```bash
quarto render
```

Ou via R:

```r
quarto::quarto_render()
```

### 2. Personalizar metadados

Edite `_quarto.yml` para configurar:

- Título, autor, data
- Orientador, coorientador
- Instituição, programa, área de concentração
- Tipo de trabalho (dissertação/tese)
- Idioma e formatação

Exemplo:

```yaml
book:
  title: "Seu Título Aqui"
  author: "Seu Nome"
  supervisor: "Prof. Dr. Nome do Orientador"
  university: "Nome da Universidade"
  program: "Programa de Pós-Graduação"
```

### 3. Adicionar conteúdo

- **Capítulos principais**: Edite `index.qmd` e arquivos em `qmd/`
- **Referências**: Adicione entradas em `references.bib`
- **Imagens**: Coloque na pasta `images/`

## Customização

Consulte a [documentação do Quarto](https://quarto.org/docs/reference/formats/pdf.html) para opções avançadas de PDF.

Configurações específicas do formato ABNT estão em `_extensions/abnt/_extension.yml`.

## Créditos

Template original desenvolvido por [Daniel Vartanian](https://github.com/danielvartan/abnt).

Baseado no projeto [`abntTeX`](https://www.abntex.net.br/).
