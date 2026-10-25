Disciplina: Auditoria 1 — Universidade de Brasília (UnB)    

Preparadora: Ana Clara Tavares Freire    

Matrícula: 241021687    

Companhia examinada: TOTVS S.A. (TOTS3)    

Data-base das demonstrações: 31/12/2025    

Natureza: trabalho acadêmico com documentos públicos, procedimentos planejados e simulações didáticas.  

Não constitui auditoria independente da TOTVS. 

1. Objetivo 

Organizar os papéis de trabalho relativos às NBC TAs previstas no roteiro acadêmico, demonstrar a origem das evidências, apresentar análises das demonstrações individuais e consolidadas da TOTVS S.A. de 2025 e possibilitar a reprodução da base sintética e dos testes computacionais. Nenhuma comunicação, confirmação, entrevista ou inspeção foi efetuada em nome da universidade perante a companhia ou terceiros. 

As análises devem ser interpretadas conforme o status informado em cada PT: 

    Executado com documentos públicos: consulta, comparação e cálculo com fontes efetivamente acessadas. 

    Simulado para fins didáticos: procedimentos sobre dados artificiais, sem vínculo com registros reais da TOTVS. 

    Planejado e não executado: procedimento que exige documentos internos, indagações, circularizações ou testes não realizados. 

2. Organização do repositório 

A pasta pública informada é Códigos. Como a listagem atual do GitHub não pôde ser conferida, a organização abaixo é proposta de padronização, não descrição verificada das pastas existentes. Se os arquivos estiverem em diretórios diferentes, ajuste os caminhos nos links. 

AUD1_P2/ 
├── README.md                         ← este documento  
├── Matriz_de_Cobertura_das_Normas_TOTVS_2025.docx 
├──Códigos/ 
│   ├── gerar_e_testar.py 
│   ├── auditar_base.py 
│   └── testar_excecoes_pt530.py 
├──Papéis_de_Trabalho/                
│   ├── PT_EC_Estrutura_Conceitual_TOTVS_2025.pdf 
│   ├── PT_200_Objetivos_Gerais_TOTVS_2025.pdf 
│   ├── PT_210_Termos_Trabalho_TOTVS_2025.pdf 
│   ├── PT_220_Gestao_Qualidade_TOTVS_2025.pdf 
│   ├── PT_240_Fraude_TOTVS_2025.pdf 
│   ├── PT_250_Leis_Regulamentos_TOTVS_2025.pdf 
│   ├── PT_260_Comunicacao_Governanca_TOTVS_2025.pdf 
│   ├── PT-230-01_...docx 
│   ├── PT-300-01_...docx 
│   ├── PT-320_...                     ← materialidade 
│   ├── PT-530_...                     ← amostragem 
│   └── demais_PT_...                  ← conforme matriz de cobertura 
├── Planilhas/                        ←  
│   ├── Conciliação_Intangível_TOTVS_2025.xlsx 
│   ├── PT-520_Planilha_...xlsx 
│   ├── PT-540_Planilha_...xlsx 
│   ├── PT-570_Planilha_...xlsx 
│   └── PT-600_Planilha_...xlsx 
├── /   Fontes_Documentais.pdf 
│    
│    
└── Bases_simuladas                 ←  
    └── LINKS_Bases_Simuladas.txt 

A matriz de cobertura é o índice para localizar qual papel documenta cada NBC TA; a presença efetiva e a versão final dos arquivos precisam ser conferidas antes da entrega.  

3. Fontes documentais e delimitação 

O documento Fontes_Documentais.pdf reúne as fontes declaradas pela preparadora e deve acompanhar o dossiê. São utilizadas, conforme aplicabilidade em cada PT: 

    DFPs e notas explicativas de 2024 e 2025, incluindo demonstrações consolidadas, individuais, relatórios dos auditores e saldos comparativos, obtidos da CVM/B3. 

    Formulário de Referência 2025 da TOTVS (versão 13), especialmente informações sobre atividades, riscos, governança, estrutura societária e transações com partes relacionadas. 

    Materiais da área de Relações com Investidores, inclusive os Fatos Relevantes de 06/01/2026 (6ª emissão de debêntures) e 02/02/2026 (Dimensa), utilizados no PT-560. 

    Política de Gestão de Riscos, Controles Internos e Compliance, publicada em 2026, exclusivamente como contexto posterior: a publicação não comprova a vigência ou execução dos mesmos controles em 2025. 

    Relatório do agente fiduciário da 5ª emissão de debêntures (2025), aplicável à análise contratual e de continuidade operacional. 

    Normas NBC TA, além de CPCs pertinentes ao objeto; a bibliografia de Gramling, Rittenberg e Johnstone constitui apoio teórico, não prova automática dos percentuais acadêmicos adotados. 

Links de referência informados na relação de fontes: 

    CVM — consulta de documentos 

    B3 — relatórios TOTVS 

    TOTVS RI — Central de Downloads 

    CFC — publicação das NBC TA 

A conta selecionada para a simulação foi o ativo intangível consolidado, com saldo publicado de R$ 3.904.253 mil, desdobrado em R$ 737.114 mil de intangíveis sem goodwill e R$ 3.167.139 mil de goodwill. Os 500.000 componentes gerados em Python correspondem somente às seis classes de intangíveis sem goodwill. O goodwill é mantido em controle separado por UGC; não integra a população de 500.000 linhas. 

4. Requisitos para reprodução 

    Python 3.10 ou superior. 

    Bibliotecas Python: numpy e pandas (demais módulos usados são da biblioteca padrão). 

    Memória e espaço livre suficientes para processar um CSV de 500.000 linhas e uma cópia integral adulterada. 

    Codificação dos CSVs: UTF-8, separador ponto e vírgula (;). 

    Colunas terminadas em _centavos: números inteiros em centavos de real; converter para reais dividindo por 100 e para R$ mil dividindo por 100.000. 

Instalação: 

python -m pip install numpy pandas 

4.1. Gerar a população original 

Coloque gerar_e_testar.py em uma pasta gravável e execute: 

python gerar_e_testar.py 

O programa utiliza semente 20251021 e produz, na pasta do próprio script: 

    intangiveis_sinteticos_500000.csv — 500.000 registros inteiramente sintéticos; 

    intangiveis_sinteticos_500000.zip — versão compactada; 

    goodwill_por_ugc.csv — controles de goodwill divulgados por UGC; 

    excecoes_injetadas.csv — gabarito com 100 cenários de erro; não altera a base original; 

    resultado_validacao.json — parâmetros, saldos e conciliação. 

Os custos e as amortizações são alocados artificialmente para coincidir com os saldos públicos. Portanto, diferença zero na conciliação demonstra a consistência matemática da simulação, não evidência independente de transações reais. 

4.2. Validar a base original 

Mantenha auditar_base.py, intangiveis_sinteticos_500000.csv, resultado_validacao.json e excecoes_injetadas.csv na mesma pasta e execute: 

python auditar_base.py 

O programa verifica a quantidade de registros, exclusividade dos IDs, relação saldo = custo − amortização, limites da amortização, vida útil positiva e totais de controle por classe. Também valida a quantidade de cenários no gabarito, que permanecem separados da base original. O resultado é salvo em resultado_testes.json. 

4.3. Reproduzir os testes de exceções — PT-530 

Na pasta do script testar_excecoes_pt530.py, disponibilize intangiveis_sinteticos_500000.csv e excecoes_injetadas.csv (o script também pesquisa alguns caminhos alternativos previstos para o Colab). Execute: 

python testar_excecoes_pt530.py 

O programa preserva a base original, cria uma cópia adulterada com 100 erros e executa cinco regras: 

Regra 
	

Verificação 

T01 
	

Saldo líquido diferente de custo menos amortização acumulada 

T02 
	

Vida útil igual ou inferior a zero 

T03 
	

Amortização acumulada superior ao custo 

T04 
	

Data de disponibilização inválida 

T05 
	

Data de disponibilização posterior a 31/12/2025 

Arquivos de saída: base_adulterada_500000.csv, registro_alteracoes.csv, resultado_teste_censo.csv, resultado_amostra_300.csv e metricas.json. O CSV do censo documenta os registros sinalizados ou presentes no gabarito, enquanto as métricas consolidam o exame dos 500.000 registros; não é uma exportação de todas as 500.000 linhas testadas. 

A amostra é aleatória estratificada proporcional por classe, com random_state=2025, e contém 300 registros. O tamanho é didático e não foi dimensionado estatisticamente para assegurar precisão e risco amostral aceitáveis. 

4.4. Reproduzir no Google Colab 

Notebook informado pela preparadora: Abrir Google Colab. 

    Abra o notebook e, se necessário, faça uma cópia no seu Drive. 

    Instale numpy e pandas. 

    Faça upload dos scripts e das entradas para /content, mantendo os arquivos exigidos no mesmo diretório (ou ajuste os caminhos explicitamente no notebook). 

    Execute geração → validação → testes de exceções, nessa ordem. 

    Confira os JSONs e CSVs produzidos, comparando-os às métricas esperadas abaixo. 

5. Controles esperados da simulação 

Controle 
	

Resultado documentado 

População original 
	

500.000 componentes 

Identificadores únicos 
	

500.000 

Custo sintético sem goodwill 
	

R$ 2.196.074 mil 

Amortização acumulada sintética 
	

R$ 1.458.960 mil 

Saldo líquido sem goodwill 
	

R$ 737.114 mil 

Goodwill em controle separado 
	

R$ 3.167.139 mil 

Intangível total de referência 
	

R$ 3.904.253 mil 

Registros adulterados na cópia 
	

100 

Amortização superior ao custo 
	

56 

Vida útil zerada 
	

44 

Registros detectados nos testes integrais 
	

100 

Registros selecionados na amostra 
	

300 

Exceções identificadas na amostra 
	

0 

Variação monetária artificial na amortização 
	

R$ 98.508,58 

Interpretação: os 56 casos de amortização superior ao custo também geram a sinalização T01 de diferença aritmética; não são 56 erros extras. Os 44 casos de vida útil zero não foram monetizados. O valor de R$ 98.508,58 não é distorção real da TOTVS nem projeção amostral. A amostra sem exceções não prova a inexistência de erros na população. 

6. Bases volumosas e links externos 

Base 
	

Acesso 

Original — intangiveis_sinteticos_500000.csv ou ZIP 
	

https://drive.google.com/drive/folders/1c8tt322cuceXiV2l58j_-zn0OAQaGS9O?usp=drive_link 

Adulterada — base_adulterada_500000.csv 
	

https://drive.google.com/drive/folders/1c8tt322cuceXiV2l58j_-zn0OAQaGS9O?usp=drive_link 

7. Índice dos papéis de trabalho e anexos 

Norma / assunto 
	

Papel de trabalho 

Estrutura Conceitual 
	

PT-EC — Estrutura Conceitual 

NBC TA 200 
	

PT-200 — Objetivos gerais 

NBC TA 210 
	

PT-210 — Termos do trabalho 

NBC TA 220 
	

PT-220 — Gestão da qualidade 

NBC TA 230 
	

PT-230 — Documentação 

NBC TA 240 
	

PT-240 — Fraude 

NBC TA 250 
	

PT-250 — Leis e regulamentos 

NBC TA 260 
	

PT-260 — Governança 

NBC TA 265 
	

PT-265 — Deficiências de controle 

NBC TA 300 
	

PT-300 — Planejamento 

NBC TA 315 
	

PT-315 — Identificação e avaliação de riscos 

NBC TA 320 
	

PT-320 — Materialidade 

NBC TA 330 
	

PT-330 — Respostas aos riscos 

NBC TA 402 
	

PT-402 — Organizações prestadoras de serviços 

NBC TA 450 
	

PT-450 — Avaliação de distorções 

NBC TA 500 
	

PT-500 — Evidência 

NBC TA 501 
	

PT-501 — Itens específicos 

NBC TA 505 
	

PT-505 — Confirmações externas 

NBC TA 510 
	

PT-510 — Saldos iniciais 

NBC TA 520 
	

PT-520 — Procedimentos analíticos 

NBC TA 530 
	

PT-530 — Amostragem 

NBC TA 540 
	

PT-540 — Estimativas contábeis 

NBC TA 550 
	

PT-550 — Partes relacionadas 

NBC TA 560 
	

PT-560 — Eventos subsequentes 

NBC TA 570 
	

PT-570 — Continuidade operacional 

NBC TA 580 
	

PT-580 — Representações formais 

NBC TA 600 
	

PT-600 — Auditoria de grupos 

Anexos analíticos reproduzíveis: conciliação de intangíveis (PT-500); bases e códigos (PT-530); planilhas de procedimentos analíticos (PT-520), sensibilidade do goodwill (PT-540), continuidade operacional (PT-570) e auditoria de grupos (PT-600). Planilhas e cenários hipotéticos não representam informações internas obtidas da TOTVS. 

8. Limitações, confidencialidade e conferência final 

Este trabalho baseia-se em fontes públicas e em simulações. Não houve acesso ao razão analítico real dos intangíveis, contratos individuais, modelos internos de impairment, balancetes de componentes, confirmações de terceiros ou papéis de auditores externos. Não houve circularização real nem assinatura/revisão de terceiros simulada. As conclusões dos PTs devem refletir essas restrições. 

 
