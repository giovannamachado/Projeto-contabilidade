import pandas as pd
"""
# URL pública do arquivo
url = 'https://docs.google.com/spreadsheets/d/1Ieu4xMlig3BsLpMUNhiipxXxcjHZQNNa/edit#gid=1541167812'

# Carrega a tabela a partir da URL
table_excel_csv = pd.read_csv('./FINBRA_Municípios_Despesas por Função_2019.xlsx - finbra.csv', skiprows=4, low_memory=False)

# filtrar linhas com as colunas desejadas
colunas_contas = ['Despesas Empenhadas', 'Despesas Liquidadas', 'Despesas Pagas']

colunas_filtro = table_excel_csv['Coluna'].isin(colunas_contas)
colunas_selecionadas = table_excel_csv.loc[colunas_filtro]


# Valores da coluna 'Conta' a serem selecionados
contas_interesse = [
    '06 - Segurança Pública', 
    '08 - Assistência Social', 
    '09 - Previdência Social', 
    '10 - Saúde', 
    '12 - Educação',
    '10.301  - Atenção Básica',
    '10.302 - Assistência Hospitalar e Ambulatorial', 
    '10.303 - Suporte Profilático e Terapêutico', 
    '10.304 - Vigilância Sanitária', 
    '10.305 - Vigilância Epidemiológica', 
    '10.306 - Alimentação e Nutrição'
    ]


# Filtra as linhas com base nos valores da coluna 'Conta'
filtro = colunas_selecionadas['Conta'].isin(contas_interesse)
linhas_filtradas = colunas_selecionadas.loc[filtro]

# Agrupa por Estado e Cidade e realiza a soma das colunas 'Valor'
somas = linhas_filtradas.groupby(['UF', 'Instituição'])['Valor'].sum().reset_index()

# Salva os resultados em outro arquivo CSV
somas.to_csv('resultados.csv', index=False)"""

# Carrega a tabela a partir da URL
table_excel_csv = pd.read_csv('./FINBRA_Municípios_Despesas por Função_2019.xlsx - finbra.csv', skiprows=4, low_memory=False)

csv_result = pd.DataFrame(columns=['UF', 'Instituição', 'Despesas Empenhadas', 'Despesas Liquidadas', 'Despesas Pagas'])


# Valores da coluna 'Conta' a serem selecionados
contas_interesse = [
    '06 - Segurança Pública', 
    '08 - Assistência Social', 
    '09 - Previdência Social', 
    '10 - Saúde', 
    '12 - Educação',
    '10.301  - Atenção Básica',
    '10.302 - Assistência Hospitalar e Ambulatorial', 
    '10.303 - Suporte Profilático e Terapêutico', 
    '10.304 - Vigilância Sanitária', 
    '10.305 - Vigilância Epidemiológica', 
    '10.306 - Alimentação e Nutrição'
    ]


def get_data_csv(tipo_conta: str):
    """retorna os dados da tabela csv da coluna e conta definidas"""
    df_despesa = table_excel_csv.loc[table_excel_csv['Coluna'] == tipo_conta]
    df_contas = df_despesa.loc[df_despesa['Conta'].isin(contas_interesse)]

    return df_contas

df_empenhadas = get_data_csv('Despesas Empenhadas')
df_liquidadas = get_data_csv('Despesas Liquidadas')
df_pagas = get_data_csv('Despesas Pagas')

df_empenhadas.to_csv('empenhadas.csv', index=False)
df_liquidadas.to_csv('liquidadas.csv', index=False)
df_pagas.to_csv('pagas.csv', index=False)

#uf = linhas_filtradas_empenhadas['UF']

#csv_result['UF'] = uf.reset_index()

#csv_result.to_csv('uf-result.csv', index=False)

"""for row in linhas_filtradas_empenhadas.itertuples():
    csv_result.at[row.Index, 'UF'] = row.UF
    csv_result.at[row.Index, 'Instituição'] = row.Instituição

    csv_result.at[row.Index, 'Despesas Empenhadas'] = linhas_filtradas_empenhadas.groupby(['UF', 'Instituição'])['Valor'].sum().reset_index()




csv_result.to_csv('resultados.csv', index=False)"""