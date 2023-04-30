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

# filtrar linhas com as colunas desejadas
col_des_empenhadas = ['Despesas Empenhadas']
col_des_liquidadas = ['Despesas Liquidadas']
col_des_pagas = ['Despesas Pagas']

#coluna 'DESPESAS EMPENHADAS'
empenhadas_filtro = table_excel_csv['Coluna'].isin(col_des_empenhadas)
empenhada_selecionada = table_excel_csv.loc[empenhadas_filtro]


# Filtra as linhas com base nos valores da coluna 'Conta'
filtro_epem = empenhada_selecionada['Conta'].isin(contas_interesse)
linhas_filtradas_empenhadas = empenhada_selecionada.loc[filtro_epem]

#coluna 'DESPESAS LIQUIDAS'
liquidadas_filtro = table_excel_csv['Coluna'].isin(col_des_liquidadas)
liquidada_selecionada = table_excel_csv.loc[liquidadas_filtro]


# Filtra as linhas com base nos valores da coluna 'Conta'
filtro_pagas = liquidada_selecionada['Conta'].isin(contas_interesse)
linhas_filtradas_liquidadas = liquidada_selecionada.loc[filtro_pagas]

#colunas DESPESAS PAGAS
pagas_filtro = table_excel_csv['Coluna'].isin(col_des_pagas)
paga_selecionada = table_excel_csv.loc[pagas_filtro]


# Filtra as linhas com base nos valores da coluna 'Conta'
filtro_pagas = liquidada_selecionada['Conta'].isin(contas_interesse)
linhas_filtradas_pagas = liquidada_selecionada.loc[filtro_pagas]


#uf = linhas_filtradas['UF']

#csv_result['UF'] = [uf]

#csv_result.to_csv('uf-result.csv', index=False)

linhas_filtradas_empenhadas.to_csv('teste_csv.csv', index=False)

