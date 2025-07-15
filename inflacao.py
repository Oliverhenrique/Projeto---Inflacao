import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# Configurações de ágina
st.set_page_config(page_title="Impacto real: Inflação no Bolso do brasileiro", layout="wide")

# --- Navegação na barra lateral ---
st.sidebar.title("Menu")
selecao = st.sidebar.radio(
    "**Explore as opções abaixo**:",
    ["**A inflação no seu bolso**", "**A inflação por região**", "**A inflação por grupo de consumo**", "**Sobre este projeto**"]
)

#--- Contato ---
st.sidebar.markdown("---")
st.sidebar.title("Redes sociais")
st.sidebar.markdown(
    """
     <a href="https://www.linkedin.com/in/lucas-henrique-usp/" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="50">

    </a><br>
    <a href="https://github.com/Oliverhenrique" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="50">
    </a>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("Developer by: **Lucas Henrique**")
# --- Função para classificar faixa de renda ---
def classificar_faixa_renda(renda):
    if renda < 2202.02:
        return "Renda muito baixa"
    elif renda < 3303.03:
        return "Renda baixa"
    elif renda < 5505.06:
        return "Renda média baixa"
    elif renda < 11010.11:
        return "Renda média"
    elif renda < 22020.22:
        return "Renda média-alta"
    else:
        return "Renda alta"

# --- Carregamento de dados com cache ---
@st.cache_data
def carregar_dados():
    df_ipca = pd.read_csv("dados_ipca.csv")
    return pd.read_csv("dados_ipca.csv")

df = carregar_dados()
# --- para a seção: A inflação por grupo de consumo ---

def carregar_dados3():
    df_consumo = pd.read_csv("dados_consumo.csv")
    return pd.read_csv("dados_consumo.csv")
dfconsumo = carregar_dados3()

# --- Seção: A inflação no seu bolso ---
if selecao == "**A inflação no seu bolso**":
    st.title("Impacto da inflação no orçamento domiciliar por grupo de consumo")
    st.markdown("Veja como a variação da inflação acumulada no ano (2025) impacta seu bolso, de acordo com a sua **região metropolitana** e **faixa de renda**")
    st.markdown("Entenda sobre a variação acumulada da inflação e os critérios de faixa de renda na seção 'Sobre este projeto'.")


    # Entrada da renda mensal
    renda_usuario = st.number_input("Informe a renda domiciliar mensal (em R$):", min_value=0.0, step=100.0)
    faixa_usuario = classificar_faixa_renda(renda_usuario)
    st.markdown(f"**Sua faixa de renda é:** {faixa_usuario}")

    # Seleção da região
    regiao_opcoes = sorted(df["regiao"].unique())
    regiao_selecionada = st.selectbox("Selecione sua região metropolitana:", regiao_opcoes)

    # Filtragem
    df_filtrado = df[
        (df["faixa_renda"] == faixa_usuario) &
        (df["regiao"] == regiao_selecionada)
    ]

    # Verificação
    if df_filtrado.empty:
        st.warning("Não há dados para essa combinação de faixa de renda e região.")
    else:
        # --- Plota o gráfico com as informações solicitadas ---
        fig = px.bar(
            data_frame=df_filtrado,
            x="grupo_consumo",
            y="inflacao_ponderada",
            color_discrete_sequence=px.colors.sequential.Magma,
            title='Impacto da inflação acumulada')
        fig.update_layout(
            showlegend=False,
            height=500)
        fig.update_xaxes(title_text='Grupo de consumo')
        fig.update_yaxes(title_text='Impacto inflacionário (%)')

        st.plotly_chart(fig, use_container_width=True)

# --- Seção: A inflação por região ---
elif selecao == "**A inflação por região**":
    st.title("Inflação acumulada por região metopolitana")
    # --- Criando seleção de gráficos ---
    st.markdown("Selecione a região **metropolitana** desejada abaixo  e veja como a **inflação acumulada ponderada** afetou o orçamento domiciliar das diferentes **faixas de renda**.")
    st.markdown("Saiba mais sobre os critérios de faixa de renda e pesos na seção **'Sobre este projeto'**")
    vt, bl, bh, ct, fl, pa, rc, sv, sp, rj = st.tabs(['Vitória', 'Belém', 'Belo Horizonte', 'Curitíba', 'Fortaleza',
     'Porto Alegre', 'Recife', 'Salvador', 'São Paulo', 'Rio de Janeiro'])
    # plotando o gráfico inflação por grupo de consumo x faixa de renda para região da Grande Vitória
    with vt:
        df_plotv = df[df['regiao'] == 'RM da Grande Vitória (ES)']

        fig = px.bar(
            df_plotv,
            x='faixa_renda',
            y='inflacao_ponderada',
            color='grupo_consumo',
            barmode='group',
            color_discrete_sequence=px.colors.sequential.Magma,
            title='Região metropolitana da Grande Vitória (ES)',
            labels={
                'faixa_renda': 'Faixa de renda',
                'inflacao_ponderada': 'Inflação ponderada (%)',
                'grupo_consumo': 'Grupo de consumo'
             })

        fig.update_layout(
            xaxis_tickangle=-45,
            legend_title='Grupo de consumo',
            title_x=0.5,
            height=500)

        st.plotly_chart(fig, use_container_width=True)


    # plotando o gráfico inflação por grupo de consumo x faixa de renda para região metropolitana de Belém (PA)
    with bl:
        df_plotb = df[df['regiao'] == 'RM de Belém (PA)']

        fig = px.bar(
            df_plotb,
            x='faixa_renda',
            y='inflacao_ponderada',
            color='grupo_consumo',
            barmode='group',
            color_discrete_sequence=px.colors.sequential.Magma,
            title='Região metropolitana de Belém (PA)',
            labels={
                'faixa_renda': 'Faixa de renda',
                'inflacao_ponderada': 'Inflação ponderada (%)',
                'grupo_consumo': 'Grupo de consumo'
             })

        fig.update_layout(
            xaxis_tickangle=-45,
            legend_title='Grupo de consumo',
            title_x=0.5,
            height=500)

        st.plotly_chart(fig, use_container_width=True)
    # plotando o gráfico inflação por grupo de consumo x faixa de renda para região metropolitana de Belo Horizonte
    with bh:
        df_ploth = df[df['regiao'] == 'RM de Belo Horizonte (MG)']

        fig = px.bar(
             df_ploth,
            x='faixa_renda',
            y='inflacao_ponderada',
            color='grupo_consumo',
            barmode='group',
            color_discrete_sequence=px.colors.sequential.Magma,
            title='Região metropolitana de Belo Horizonte (MG)',
            labels={
                'faixa_renda': 'Faixa de renda',
                'inflacao_ponderada': 'Inflação ponderada (%)',
                'grupo_consumo': 'Grupo de consumo'
             })

        fig.update_layout(
            xaxis_tickangle=-45,
            legend_title='Grupo de consumo',
            title_x=0.5,
            height=500)

        st.plotly_chart(fig, use_container_width=True)

    # plotando o gráfico inflação por grupo de consumo x faixa de renda para região metropolitana de Curitiba (PR)
    with ct:
        df_plotc = df[df['regiao'] == 'RM de Curitiba (PR)']

        fig = px.bar(
             df_plotc,
            x='faixa_renda',
            y='inflacao_ponderada',
            color='grupo_consumo',
            barmode='group',
            color_discrete_sequence=px.colors.sequential.Magma,
            title='Região metropolitana de Curitíba (PR)',
            labels={
                'faixa_renda': 'Faixa de renda',
                'inflacao_ponderada': 'Inflação ponderada (%)',
                'grupo_consumo': 'Grupo de consumo'
             })

        fig.update_layout(
            xaxis_tickangle=-45,
            legend_title='Grupo de consumo',
            title_x=0.5,
            height=500)

        st.plotly_chart(fig, use_container_width=True)

    # plotando o gráfico inflação por grupo de consumo x faixa de renda para região metropolitana de Fortaleza (CE)
    with fl:
        df_plotf = df[df['regiao'] == 'RM de Fortaleza (CE)']

        fig = px.bar(
             df_plotf,
            x='faixa_renda',
            y='inflacao_ponderada',
            color='grupo_consumo',
            barmode='group',
            color_discrete_sequence=px.colors.sequential.Magma,
            title='Região metropolitana de Fortaleza (CE)',
            labels={
                'faixa_renda': 'Faixa de renda',
                'inflacao_ponderada': 'Inflação ponderada (%)',
                'grupo_consumo': 'Grupo de consumo'
             })

        fig.update_layout(
            xaxis_tickangle=-45,
            legend_title='Grupo de consumo',
            title_x=0.5,
            height=500)

        st.plotly_chart(fig, use_container_width=True)

    # plotando o gráfico inflação por grupo de consumo x faixa de renda para região metropolitana de Porto Alegre
    with pa:
        df_plotp = df[df['regiao'] == 'RM de Porto Alegre (RS)']

        fig = px.bar(
             df_plotp,
            x='faixa_renda',
            y='inflacao_ponderada',
            color='grupo_consumo',
            barmode='group',
            color_discrete_sequence=px.colors.sequential.Magma,
            title='Região metropolitana de Porto Alegre (RS)',
            labels={
                'faixa_renda': 'Faixa de renda',
                'inflacao_ponderada': 'Inflação ponderada (%)',
                'grupo_consumo': 'Grupo de consumo'
             })

        fig.update_layout(
            xaxis_tickangle=-45,
            legend_title='Grupo de consumo',
            title_x=0.5,
            height=500)

        st.plotly_chart(fig, use_container_width=True)

    # plotando o gráfico inflação por grupo de consumo x faixa de renda para região metropolitana de Recife
    with rc:
        df_plotr = df[df['regiao'] == 'RM de Recife (PE)']

        fig = px.bar(
             df_plotr,
            x='faixa_renda',
            y='inflacao_ponderada',
            color='grupo_consumo',
            barmode='group',
            color_discrete_sequence=px.colors.sequential.Magma,
            title='Região metropolitana de Recife (PE)',
            labels={
                'faixa_renda': 'Faixa de renda',
                'inflacao_ponderada': 'Inflação ponderada (%)',
                'grupo_consumo': 'Grupo de consumo'
             })

        fig.update_layout(
            xaxis_tickangle=-45,
            legend_title='Grupo de consumo',
            title_x=0.5,
            height=500)

        st.plotly_chart(fig, use_container_width=True)

    # plotando o gráfico inflação por grupo de consumo x faixa de renda para região metropolitana de Salvador
    with sv:
        df_plots = df[df['regiao'] == 'RM de Salvador (BA)']

        fig = px.bar(
             df_plots,
            x='faixa_renda',
            y='inflacao_ponderada',
            color='grupo_consumo',
            barmode='group',
            color_discrete_sequence=px.colors.sequential.Magma,
            title='Região metropolitana de Salvador (BA)',
            labels={
                'faixa_renda': 'Faixa de renda',
                'inflacao_ponderada': 'Inflação ponderada (%)',
                'grupo_consumo': 'Grupo de consumo'
             })

        fig.update_layout(
            xaxis_tickangle=-45,
            legend_title='Grupo de consumo',
            title_x=0.5,
            height=500)

        st.plotly_chart(fig, use_container_width=True)

    # plotando o gráfico inflação por grupo de consumo x faixa de renda para região metropolitana de São Paulo
    with sp:
        df_plotsp = df[df['regiao'] == 'RM de São Paulo (SP)']

        fig = px.bar(
             df_plotsp,
            x='faixa_renda',
            y='inflacao_ponderada',
            color='grupo_consumo',
            barmode='group',
            color_discrete_sequence=px.colors.sequential.Magma,
            title='Região metropolitana de São paulo (SP)',
            labels={
                'faixa_renda': 'Faixa de renda',
                'inflacao_ponderada': 'Inflação ponderada (%)',
                'grupo_consumo': 'Grupo de consumo'
             })

        fig.update_layout(
            xaxis_tickangle=-45,
            legend_title='Grupo de consumo',
            title_x=0.5,
            height=500)

        st.plotly_chart(fig, use_container_width=True)

    # plotando o gráfico inflação por grupo de consumo x faixa de renda para região metropolitana do Rio de Janeiro
    with rj:
        df_plotrj = df[df['regiao'] == 'RM do Rio de Janeiro (RJ)']

        fig = px.bar(
            df_plotrj,
            x='faixa_renda',
            y='inflacao_ponderada',
            color='grupo_consumo',
            barmode='group',
            color_discrete_sequence=px.colors.sequential.Magma,
            title='Região metropolitana do Rio de Janeiro (RJ)',
            labels={
                'faixa_renda': 'Faixa de renda',
                'inflacao_ponderada': 'Inflação ponderada (%)',
                'grupo_consumo': 'Grupo de consumo'
             })

        fig.update_layout(
            xaxis_tickangle=-45,
            legend_title='Grupo de consumo',
            title_x=0.5,
            height=500)

        st.plotly_chart(fig, use_container_width=True)

    # --- Tabela de referência para faixas de renda ---
    # Dados da tabela
    faixas = [
        "1 - Renda muito baixa",
        "2 - Renda baixa",
        "3 - Renda média-baixa",
        "4 - Renda média",
        "5 - Renda média-alta",
        "6 - Renda alta"
    ]

    valores_2025 = [
        "Menor que R$ 2.202,02",
        "Entre R$ 2.202,02 e R$ 3.303,03",
        "Entre R$ 3.303,03 e R$ 5.505,06",
        "Entre R$ 5.505,06 e R$ 11.010,11",
        "Entre R$ 11.010,11 e R$ 22.020,22",
        "Maior que R$ 22.020,22"
    ]

    # Criar figura da tabela
    fig = go.Figure(data=[go.Table(
        header=dict(
            values=["<b>Faixa de renda</b>", "<b>Renda domiciliar (jan./2025)</b>"],
            fill_color="#f54275",
            font=dict(color='white', size=13),
            align="left"
        ),
        cells=dict(
            values=[faixas, valores_2025],
            fill_color='lavender',
            align="left",
            font=dict(size=12)
        )
    )])

    fig.update_layout(
        margin=dict(l=0, r=0, t=10, b=0),
        height=350
    )

    # Exibição
    st.subheader("Classificação de faixas de renda (jan./2025)")
    st.markdown('Fonte: IPEA')
    st.plotly_chart(fig, use_container_width=True)

    # --- Gráfico: O que mais pesa para cada faixa de renda? ---
    st.subheader("Qual grupo de consumo mais pesa no orçamendo domiciliar?")
    st.markdown("No gráfico abaixo, entenda qual grupo de consumo mais pesa, **em média**, no orçamento domiciliar para cada **faixa de renda**.")
    # Agrupando o df
    df_plot = df.groupby(['faixa_renda', 'grupo_consumo'], sort=False)['inflacao_ponderada'].mean().reset_index()
    # Plotando o gráfico
    fig = go.Figure()

    df_wide = df_plot.pivot(
        index='faixa_renda',
        columns='grupo_consumo',
        values='inflacao_ponderada'
    )  .reset_index()

    # Para cada grupo de consumo, adiciona uma barra empilhada
    for coluna in df_wide.columns[1:]:  # ignora a primeira coluna 'faixa_renda'
        fig.add_trace(go.Bar(
            x=df_wide['faixa_renda'],
            y=df_wide[coluna],
            name=coluna
    ))


    # Configurando o layout
    fig.update_layout(
        barmode='stack',
        title='Impacto médio por grupo de consumo e faixa de renda',
        xaxis_title='Faixa de renda',
        yaxis_title='Inflação ponderada (%)',
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)
    # --- Inserindo insights --
    st.subheader("Insights")
    st.markdown("""De acordo com os dados do ipca acumulado no ano de 2025, considerando o período de janeiro a junho:
     \n - Em 80% das regiões o maior impacto inflacionário veio do grupo de consumo **Alimentos e bebidas** seguido pelos grupos Habitação, Saúde e cuidados pessoais e Transportes.
     \n - **Fora da curva**: Os outros 20% são a região metropolitana de Belo Horizonte (MG) onde o orçamento domiciliar das famílias é mais corroido pela alta de preços no grupo de consumo **Habitação** enquanto Recife
     sofre com o grupo **Transportes**.
     \n **Disparidade no impacto inflacionário.** Os extremos da reta.
     \n - Enquanto o índice oficial pode parecer controlado, uma família de renda muito baixa pode sofrer com a inflação até 21,09% maior que a média nacional,
     como é o caso dessa faixa de renda para a região metropolitana de Belo Horizonte e Porto Alegre com 20,59%.
     \n - Ao mesmo tempo, as famílias de todas as faixas de renda na região metropolitana do Rio de Janeiro, abordadas nesta pesquisa, sofreram inflação 15% menor que a média.""")

# --- Seção: A inflação por grupo de consumo ---
elif selecao == "**A inflação por grupo de consumo**":
    # Título da seção
    st.title("Inflação acumulada por grupo de consumo e região ")
    # Subtítulo/descrição
    st.markdown("Entenda o comportamento da inflação a partir dos diferentes **grupos de consumo** pesquisados pelo IBGE para as diferentes **regiões metropolitanas**.")
    st.markdown("Selecione um grupo de consumo abaixo e veja o gráfico.")

    # Criando a seleção de Gráficos
    grupo1, grupo2, grupo3, grupo4, grupo5, grupo6, grupo7, grupo8, grupo9 = st.tabs(['Alimentação e bebidas', 'Habitação', 'Artigos de Residência', 'Vestuário', 'Transportes', 'Saúde e Cuidados pessoais', 'Despesas pessoais', 'Educação', 'Comunicação'])
    # Plotando o gráfico para o grupo 1
    with grupo1:
        grupo_1 = dfconsumo[dfconsumo['grupo_consumo'] == 'Alimentação e bebidas']
        grupo_1 = grupo_1.sort_values(by='valor_ipca', ascending=False)
        fig = px.bar(
            grupo_1,
            x='valor_ipca',
            y='regiao',
            orientation='h',
            color_discrete_sequence=px.colors.sequential.Magma,
            text='valor_ipca'
            )
        fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig.update_layout(
            title='Inflação acumulada para o grupo Alimentação e bebidas',
            xaxis_title='Inflação acumulada (%) de jan/2025 a maio/2025',
            yaxis_title='Região',
            yaxis={'categoryorder':'array', 'categoryarray': grupo_1['regiao']},
            showlegend=False)
        fig.update_xaxes(showgrid=True)

        st.plotly_chart(fig, use_container_width=True)

    # Plotando o gráfico para o grupo 2
    with grupo2:
        grupo_2 = dfconsumo[dfconsumo['grupo_consumo'] == 'Habitação']
        grupo_2 = grupo_2.sort_values(by='valor_ipca', ascending=False)
        fig = px.bar(
            grupo_2,
            x='valor_ipca',
            y='regiao',
            orientation='h',
            color_discrete_sequence=px.colors.sequential.Magma,
            text='valor_ipca'
            )
        fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig.update_layout(
            title='Inflação acumulada para o grupo Habitação',
            xaxis_title='Inflação acumulada (%)',
            yaxis_title='Região',
            yaxis={'categoryorder':'array', 'categoryarray': grupo_2['regiao']},
            showlegend=False)
        fig.update_xaxes(showgrid=True)

        st.plotly_chart(fig, use_container_width=True)

    # Plotando o gráfico para o grupo 3
    with grupo3:
        grupo_3 = dfconsumo[dfconsumo['grupo_consumo'] == 'Artigos de residência']
        grupo_3 = grupo_3.sort_values(by='valor_ipca', ascending=False)
        fig = px.bar(
            grupo_3,
            x='valor_ipca',
            y='regiao',
            orientation='h',
            color_discrete_sequence=px.colors.sequential.Magma,
            text='valor_ipca'
            )
        fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig.update_layout(
            title='Inflação acumulada para o grupo Artigos de residência',
            xaxis_title='Inflação acumulada (%)',
            yaxis_title='Região',
            yaxis={'categoryorder':'array', 'categoryarray': grupo_3['regiao']},
            showlegend=False)
        fig.update_xaxes(showgrid=True)

        st.plotly_chart(fig, use_container_width=True)

    # Plotando o gráfco para o grupo 4
    with grupo4:
        grupo_4 = dfconsumo[dfconsumo['grupo_consumo'] == 'Vestuário']
        grupo_4 = grupo_4.sort_values(by='valor_ipca', ascending=False)
        fig = px.bar(
            grupo_4,
            x='valor_ipca',
            y='regiao',
            orientation='h',
            color_discrete_sequence=px.colors.sequential.Magma,
            text='valor_ipca'
            )
        fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig.update_layout(
            title='Inflação acumulada para o grupo Vestuário',
            xaxis_title='Inflação acumulada (%)',
            yaxis_title='Região',
            yaxis={'categoryorder':'array', 'categoryarray': grupo_4['regiao']},
            showlegend=False)
        fig.update_xaxes(showgrid=True)

        st.plotly_chart(fig, use_container_width=True)

    # Plotando o gráfico para o grupo 5
    with grupo5:
        grupo_5 = dfconsumo[dfconsumo['grupo_consumo'] == 'Transportes']
        grupo_5 = grupo_5.sort_values(by='valor_ipca', ascending=False)
        fig = px.bar(
            grupo_5,
            x='valor_ipca',
            y='regiao',
            orientation='h',
            color_discrete_sequence=px.colors.sequential.Magma,
            text='valor_ipca'
            )
        fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig.update_layout(
            title='Inflação acumulada para o grupo Transportes',
            xaxis_title='Inflação acumulada (%)',
            yaxis_title='Região',
            yaxis={'categoryorder':'array', 'categoryarray': grupo_5['regiao']},
            showlegend=False)
        fig.update_xaxes(showgrid=True)

        st.plotly_chart(fig, use_container_width=True)

    # Plotando o gráfico para o grupo 6
    with grupo6:
        grupo_6 = dfconsumo[dfconsumo['grupo_consumo'] == 'Saúde e cuidados pessoais']
        grupo_6 = grupo_6.sort_values(by='valor_ipca', ascending=False)
        fig = px.bar(
            grupo_6,
            x='valor_ipca',
            y='regiao',
            orientation='h',
            color_discrete_sequence=px.colors.sequential.Magma,
            text='valor_ipca'
            )
        fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig.update_layout(
            title='Inflação acumulada para o grupo Saúde e cuidados pessoais',
            xaxis_title='Inflação acumulada (%)',
            yaxis_title='Região',
            yaxis={'categoryorder':'array', 'categoryarray': grupo_6['regiao']},
            showlegend=False)
        fig.update_xaxes(showgrid=True)

        st.plotly_chart(fig, use_container_width=True)

    # Plotando o gráfico para o grupo 7
    with grupo7:
        grupo_7 = dfconsumo[dfconsumo['grupo_consumo'] == 'Despesas pessoais']
        grupo_7 = grupo_7.sort_values(by='valor_ipca', ascending=False)
        fig = px.bar(
            grupo_7,
            x='valor_ipca',
            y='regiao',
            orientation='h',
            color_discrete_sequence=px.colors.sequential.Magma,
            text='valor_ipca'
            )
        fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig.update_layout(
            title='Inflação acumulada para o grupo Despesas pessoais',
            xaxis_title='Inflação acumulada (%)',
            yaxis_title='Região',
            yaxis={'categoryorder':'array', 'categoryarray': grupo_7['regiao']},
            showlegend=False)
        fig.update_xaxes(showgrid=True)

        st.plotly_chart(fig, use_container_width=True)

    # Plotando o gráfico para o grupo 8
    with grupo8:
        grupo_8 = dfconsumo[dfconsumo['grupo_consumo'] == 'Educação']
        grupo_8 = grupo_8.sort_values(by='valor_ipca', ascending=False)
        fig = px.bar(
            grupo_8,
            x='valor_ipca',
            y='regiao',
            orientation='h',
            color_discrete_sequence=px.colors.sequential.Magma,
            text='valor_ipca'
            )
        fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig.update_layout(
            title='Inflação acumulada para o grupo Educação',
            xaxis_title='Inflação acumulada (%)',
            yaxis_title='Região',
            yaxis={'categoryorder':'array', 'categoryarray': grupo_8['regiao']},
            showlegend=False)
        fig.update_xaxes(showgrid=True)

        st.plotly_chart(fig, use_container_width=True)

    # Plotando o gráfico para o grupo 9
    with grupo9:
        grupo_9 = dfconsumo[dfconsumo['grupo_consumo'] == 'Comunicação']
        grupo_9 = grupo_9.sort_values(by='valor_ipca', ascending=False)
        fig = px.bar(
            grupo_9,
            x='valor_ipca',
            y='regiao',
            orientation='h',
            color_discrete_sequence=px.colors.sequential.Magma,
            text='valor_ipca'
            )
        fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
        fig.update_layout(
            title='Inflação acumulada para o grupo Comunicação',
            xaxis_title='Inflação acumulada (%)',
            yaxis_title='Região',
            yaxis={'categoryorder':'array', 'categoryarray': grupo_9['regiao']},
            showlegend=False)
        fig.update_xaxes(showgrid=True)

        st.plotly_chart(fig, use_container_width=True)
    st.subheader("Insights")
    st.markdown("""
        No geral, houve deflação em 22% dos grupos de consumo para 30% das regiões no período análisado, impactando todas as faixas de renda, havendo:
        \n - Queda de preços para a região de Fortaleza no grupo Vestuário.
        \n - Queda de preços para as regiões de Recife e Salvador no grupo Artigos de residência
        \n **Casos especiais**
        \n - A inflação para o grupo de consumo **habitação** em Belo Horizonte é 65,54% maior que a média nacional, 45,95% para Porto Alegre e 34,46% para Belém.
        \n - Para Recife, no grupo **transportes**, a inflação é 120,64% maior que a média nacional.
        """)

# --- Seção : Sobre este projeto ---
elif selecao == "**Sobre este projeto**":
    st.title("Sobre este projeto")
    st.markdown("""
    Este projeto foi desenvolvido com o objetivo de avaliar o impacto da inflação acumulada no orçamento domiciliar das famílias residentes nas regiões metropolitanas disponíveis na pesquisa do IBGE sobre o IPCA de Janeiro a Junho de 2025 (período disponível  até o momento). Utilizou-se da classificação por faixa de renda para maior precisão dos resultados.
    Os dados são baseados no IPCA acumulado em 2025 do IBGE (Instituto Brasileiro de Geografia e Estatística), com vetores de peso estimados a partir de estudos do IPEA e da POF (Pesquisa de Orçamento Familiar de 2017/2018).
    Para avaliar o impacto da inflação acumulada nas diferentes regiões para cada faixa de renda por grupo de consumo foi necessário:""")
    st.markdown("""
    **1º Coletar os dados:**
    A coleta de dados foi realizada via biblioteca SidraPy.
    Para saber mais sobre este recurso, visite os links clicando nos botões abaixo:""")
    st.link_button("Página no Pypi.org", "https://pypi.org/project/sidrapy/")
    st.link_button("Git Hub do projeto e criador da biblioteca", "https://github.com/AlanTaranti/sidrapy")
    st.link_button("Documentação da biblioteca", "https://sidrapy.readthedocs.io/pt-br/latest/")
    st.markdown("**Indicador de inflação** : Índice de Preços ao Consumidor Amplo (IPCA), tabela 7060 - variável 69 (variação acumulada %)")
    st.markdown("""**2º Definir as faixas de renda:** As faixas de renda foram definidas conforme pesquisa do Instituto de Pesquisa Econômica Aplicada (Ipea) **Fonte:** Carta de conjuntura número 67 - nota de conjuntura 18 - 2º Trimetre de 2025 (Data da consulta: 21/06/2025 ás 19:43) Tabela 4: Faixas de renda mensal domiciliar : Dísponível em""")
    st.link_button("Critérios de Faixas de Renda", "https://www.ipea.gov.br/cartadeconjuntura/wp-content/uploads/2025/06/250616_cc_67_nota_18.pdf")
    st.markdown("""**3º Definir os vetores de pesos para cada faixa de renda e grupo de consumo**:
    **Fonte:**
    Tabela 3: Gastos com a aquisição de bens e serviços por faixa de renda: Carta de conjuntura número 47- 2º Trimestre de 2020 - Nota técnica - "Indicador ipea de inflação por faixa de renda:
    Atualização dos vetores de peso" (Data da consulta: 21/06/2025 ás 19:52)""")
    st.link_button("Vetores de peso", "https://portalantigo.ipea.gov.br/portal/images/stories/PDFs/conjuntura/200616_inflacao.pdf")

    st.markdown("""**Por quê vetores de peso são necessários?**:
    Os vetores de peso são necessários para calcular o quanto a inflação, por grupo de consumo,  impacta, especificamente, cada faixa de renda domiciliar uma vez que, conforme a POF (Pesquisa de Orçamento Familiar de 2017/2018 do IBGE),
    fazendo isso, estamos considerando a proporção de gastos das diferentes faixas de renda para os diferentes grupos de consumo na avaliação do impacto da inflação.
    Saiba mais sobre a POF no botão abaixo:""")
    st.link_button("POF", "https://www.ibge.gov.br/estatisticas/sociais/populacao/24786-pesquisa-de-orcamentos-familiares-2.html?edicao=37681&t=o-que-e>.")
    st.markdown('Confira o repositório completo deste projeto clicando no ícone do Git Hub do autor na barra lateral.')
