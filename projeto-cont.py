import pandas as pd

"""def tratar_tabela(planilha: pd.DataFrame, coluna_interesse, contas_interesse) -> pd.DataFrame:
    del planilha['Cod_IBGE']
    del planilha['População']
    del planilha['Identificador da Conta']

    planilha_filtrada = planilha.loc[planilha['Coluna'].isin(coluna_interesse) & planilha['Conta'].isin(contas_interesse)]

    planilha_filtrada['Valor'] = pd.to_numeric(
        planilha_filtrada['Valor']
    ).fillna(0)

    return planilha_filtrada"""


def filtrar_tabela(tabela: pd.DataFrame, coluna_interesse, contas_interesse) -> pd.DataFrame:
    tabela_filtrada = tabela.loc[tabela['Coluna'].isin(coluna_interesse) & tabela['Conta'].isin(contas_interesse)]

    tabela_filtrada['Valor'] = pd.to_numeric(
        tabela_filtrada['Valor'], errors='coerce').fillna(0)

    return tabela_filtrada

coluna_interesse = ['Despesas Empenhadas', 'Despesas Liquidadas', 'Despesas Pagas']

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

if __name__ == "__main__":
    tabela = pd.read_excel('./Cópia de FINBRA_Municípios_Despesas por Função_2019.xlsx', skiprows=4)
    tabela.to_csv('tabela_dados.csv', index=False)
    #tabela_filtrada = tratar_tabela(tabela, coluna_interesse, contas_interesse)
    tabela_filtrada = filtrar_tabela(tabela, coluna_interesse, contas_interesse)
    #tabela_filtrada.to_csv('result.csv', index=False)
    print(tabela['Valor'][0])
    print(tabela_filtrada)