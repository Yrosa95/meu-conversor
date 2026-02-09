import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="Conversor de Produção", layout="wide")

st.title("🚀 Conversor de Produção - Um Clique")
st.write("Arraste o arquivo CSV original aqui para gerar sua 'colinha'.")

uploaded_file = st.file_uploader("Escolha o arquivo Supervisory", type="csv")

if uploaded_file is not None:
    # Lê o arquivo original usando ponto e vírgula como separador
    df = pd.read_csv(uploaded_file, sep=';', decimal=',')
    
    # Lista das colunas que você quer manter (Número seq. + MP 1 a 10)
    colunas_finais = ['Número sequencial do caminhão']
    for i in range(1, 11):
        colunas_finais.append(f'Descrição do Matéria-prima {i}')
        colunas_finais.append(f'Quantidade M.Prima {i}')
    
    # Filtra apenas as colunas que existem no arquivo
    df_result = df[[c for c in colunas_finais if c in df.columns]]
    
    st.success("Arquivo processado com sucesso!")
    st.dataframe(df_result) # Mostra uma prévia na tela

    # Botão para baixar em Excel
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df_result.to_excel(writer, index=False)
    
    st.download_button(
        label="📥 Baixar Planilha Pronta",
        data=output.getvalue(),
        file_name="colinha_pronta.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
