<p align="center">
  <img src="img/capa.png" alt="Capa do projeto" width="800">
</p>
<h1 align="left">Sobre este projeto</h1>

###

<p align="left">Este projeto analisa como a inflação acumulada em 2025 impactou o orçamento das famílias de diferentes faixas de renda em regiões metropolitanas do Brasil considerando os grupos de consumo definidos na pesquisa do IPCA (índice de Preço ao Consumidor Amplo) realizada pelo IBGE (Instituto Brasileiro de Geografia e Estatística).<br><br>Período analisado: Janeiro - Junho 2025<br>Unidades de análise: Região metropolitana x Faixa de renda x Grupo de consumo<br><br>🚀 Acesse a aplicação: Você pode interagir com a análise completa na aplicação em Streamlit:</p>

###

<h2 align="left">🎯 Objetivo</h2>

###

<p align="left">Avaliar o impacto da inflação acumulada no orçamento domiciliar para famílias de diferentes faixas de renda em diferentes regiões metropolitanas do Brasil.</p>

###

<h2 align="left">📋 Sobre este repositório.</h2>

###

<p align="left">Arquivos:<br><br>Analise inflação: Arquivo .ipynb Notebook contendo a análise do impacto inflacionário.<br>inflacao: Arquivo .py código da aplicação streamlit.<br>dados_consumo: Arquivo csv com os dados brutos da inflação.<br>dados_ipca: Arquivo csv com os dados tratados e inflação ponderada.<br>IPCA - CAPA: Arquivo contendo a capa deste README.<br>requeriments: arquivo txt com as dependências deste projeto.<br>README.md: Arquivo deste guia.</p>

###

<h2 align="left">🧠 Alguns Insights do projeto</h2>

###

<p align="left">- O índice oficial da inflação pode mascarar algumas realidades locais pois algumas famílias de baixa renda podem sofrer com uma inflação até 21% maior que a média nacional.<br>- As regiões metropolitanas de Belo Horizonte, Porto Alegre, Belém e Vitória (ES) concentram os maiores índices de inflação ponderada para faixas de menor renda.<br>- Para 80% das regiões a maior pressão inflacionária veio do grupo de consumo Alimentos e bebidas.</p>

###

<h2 align="left">💻 Tecnologias utilizadas.</h2>

###

<div align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge" height="40" alt="python logo"  />
  <img width="12" />
  <img src="https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=black&style=for-the-badge" height="40" alt="jupyter logo"  />
  <img width="12" />
  <img src="https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white&style=for-the-badge" height="40" alt="pandas logo"  />
  <img width="12" />
  <img src="https://img.shields.io/badge/Plotly-3C4C63?logo=plotly&logoColor=white&style=flat-square" height="40" />
  <img width="12" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white&style=flat-square" height="40" />
  <img width="12" />
  <img src="https://img.shields.io/badge/Seaborn-546D78?logo=seaborn&logoColor=white&style=flat-square" height="40" />
  <img width="12" />
  <img src="https://img.shields.io/badge/SidraPy-C9D1D9?style=flat-square" height="40" />
</div>

###

<p align="left">Linguagem/ Biblioteca     |  Versão<br>- Python ---------------|   3.9.13<br>- Streamlit -------------|   1.46.0<br>- Pandas ---------------|   1.4.4<br>- Plotly -----------------|   5.9.0<br>- Seaborn --------------|    0.12.2<br>- SidraPy ---------------|   0.1.4</p>

###

<h2 align="left">Fontes de dados</h2>

###

### 🔎 Metodologia: Etapas para avaliar o impacto da inflação acumulada

Para avaliar o impacto da inflação acumulada nas diferentes regiões, faixas de renda e grupos de consumo, as seguintes etapas foram realizadas:

---

#### 📥 1. Coleta dos dados

A coleta foi feita via biblioteca **SidraPy**, que permite acessar diretamente dados do IBGE via API.

- 📦 [Página no PyPI (sidrapy)](https://pypi.org/project/sidrapy/)
- 🧠 [GitHub do projeto](https://github.com/AlanTaranti/sidrapy)
- 📚 [Documentação oficial da biblioteca](https://sidrapy.readthedocs.io/pt-br/latest/)

**Indicador utilizado**: IPCA – Índice de Preços ao Consumidor Amplo  
Tabela 7060 – Variável 69 (variação acumulada %)

---

#### 💰 2. Definição das faixas de renda

As faixas foram definidas com base no estudo do **Instituto de Pesquisa Econômica Aplicada (Ipea)**.

- 📄 [Carta de Conjuntura nº 67 – 2º Trim./2025](https://www.ipea.gov.br/cartadeconjuntura/)

> Tabela 4: Faixas de renda mensal domiciliar (Consulta: 21/06/2025 às 19:43)

---

#### ⚖️ 3. Definição dos vetores de peso

Os vetores de peso foram obtidos na **Nota Técnica do Ipea**, que atualiza a metodologia de ponderação do impacto da inflação por faixa de renda.

- 📑 [Carta de Conjuntura nº 47 – 2º Trim./2020 (Nota Técnica)](https://repositorio.ipea.gov.br/)

> Tabela 3: Gastos com a aquisição de bens e serviços por faixa de renda  
(Consulta: 21/06/2025 às 19:52)

---

#### ❓ Por que usar vetores de peso?

Os vetores de peso são essenciais para refletir **como cada faixa de renda consome diferentes grupos de bens de consumo**.

Baseiam-se na **POF 2017/2018 (Pesquisa de Orçamento Familiar)**, do IBGE.

- 📊 [Saiba mais sobre a POF no site do IBGE](https://www.ibge.gov.br/estatisticas/sociais/populacao/24786-pesquisa-de-orcamentos-familiares-2.html?edicao=37681&t=o-que-e)

Com isso, o impacto da inflação **passa a considerar a estrutura real de consumo de cada faixa de renda**, tornando a análise mais fiel à realidade.

---


###
