# EPIC2-T6: Estruturar Módulo de Gestão, Governança, Aspectos Antropológicos e UCs Legadas (Quadro III)

**Status:** Concluído  
**Produto Entregue:** [`producao/docs/especificacao-modulos-dados-seinuc.md#4-módulo-iii---gestão-governança-aspectos-antropológicos-e-ucs-legadas-quadro-iii`](../producao/docs/especificacao-modulos-dados-seinuc.md#4-módulo-iii---gestão-governança-aspectos-antropológicos-e-ucs-legadas-quadro-iii)  
**Responsável:** Analista Socioambiental / Gestão Pública  
**Base Legal:** Art. 67, §2º, IV, e Arts. 112, 113, 114 e 117 da Lei PA nº 10.306/2023 | Art. 4º, III do Decreto Regulamentador do SEINUC/PA

---

## 1. Resumo da Entrega

A especificação técnica do Módulo III (Gestão, Governança, Aspectos Antropológicos e UCs Legadas) foi consolidada no documento oficial de especificação em [`producao/docs/especificacao-modulos-dados-seinuc.md`](../producao/docs/especificacao-modulos-dados-seinuc.md).

### Elementos Especificados:
* **Dicionário de Atributos:** Controle de Conselhos Gestores e atas, Plano de Gestão (equivale ao plano de manejo federal), aspectos arqueológicos/antropológicos e sustentabilidade financeira.
* **Rastreamento de UCs Legadas:** `legada_status` e `legada_prazo_fim` para acompanhamento de Sítios Pesqueiros (Art. 112) e de UCs anteriores a 2023 (Art. 114, prazo legal até 2028).
* **Repasse Municipal (Art. 117):** `repasse_municipal_20pct` para rastreamento da destinação mínima de 20% do ICMS a UCs municipais.
* **Validação por Agentes de IA e Desenvolvedores:** Bloco de código em **JSON Schema draft-2020-12** com regra condicional `conselho_reunioes_qtd >= 2` quando `conselho_status = true`.