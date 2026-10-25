Matrícula: 241021687

# PT 530 — Testes de exceções sintéticas — TOTVS 2025

**Finalidade exclusivamente acadêmica. Nenhuma exceção constitui achado sobre os registros reais da TOTVS.**

## Execução no Google Colab
1. Envie os três arquivos `intangiveis_sinteticos_500000.csv`, `excecoes_injetadas.csv` e `testar_excecoes_pt530.py` para `/content`.
2. Execute `!pip -q install pandas numpy`.
3. Execute `!python /content/testar_excecoes_pt530.py`.
4. Os arquivos de resultados serão produzidos em `/content`.

Também é possível colocar os dois arquivos CSV na mesma pasta do script e executar `python testar_excecoes_pt530.py`.

## Entradas
- CSV dos 500 mil registros sintéticos, geração original — intocado.
- `excecoes_injetadas.csv` — gabarito original com exatamente 100 alterações.

## Alterações
- 56 registros: valor de amortização acumulada substituído por valor superior ao custo.
- 44 registros: vida útil alterada para zero.
- Cópia integral adulterada: `base_adulterada_500000.csv`.
- Cadastro das alterações: `registro_alteracoes.csv`.

## Saídas
- `resultado_teste_censo.csv` — apenas os registros sinalizados ou listados no gabarito, com flags de testes e classificações.
- `resultado_amostra_300.csv` — seleção estratificada proporcional reproduzível (random_state=2025) e resultados de cada teste.
- `metricas.json` — sumário de resultados do censo e da amostra.

## Resultados obtidos em 24/10/2026
- Censo: 500.000 analisados; 100 adulterados; 100 detectados; 0 falsos positivos; 0 falsos negativos.
- Amostra: 300 analisados; 0 adulterados selecionados; 0 detectados. Não inferir ausência de erros no universo.
- 56 diferenças aritméticas, coincidentes com 56 casos de amortização acumulada superior ao custo. Os testes se sobrepõem: **não somar contagens de flags como se fossem erros adicionais**.
- Efeito sintético introduzido no campo de amortização: **R$ 98.508,58**, sem inferência para a TOTVS nem projeção amostral.

## Limitações
Os erros foram inseridos artificialmente de modo a serem detectáveis por regras explícitas. Isso demonstra o funcionamento dos testes, não sua capacidade de identificar erros desconhecidos. A amostra de 300 não foi dimensionada por um modelo formal de risco amostral, devendo ser identificada como preliminar. A alteração intencional do campo de amortização quebra a conciliação original; o gabarito e o ajuste estão documentados. A coluna `indicador_erro` é marcação didática, **não usada pelas regras para detectar exceções**.
