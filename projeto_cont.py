import pandas as pd

def get_tabela():
    tabela = pd.read_csv('tabela_dados.csv', low_memory=False)

    return tabela

"""def get_seguridade_social(tabela: pd.DataFrame, cidade: str):
    df_cidade = tabela.loc[tabela['Instituição'] == cidade]
    df_cidade['Valor'] = pd.to_numeric(df_cidade['Valor'], errors='coerce').fillna(0)
    print(df_cidade)

    df_valor_seguridade_social = df_cidade.loc[
        (df_cidade['Despesas Empenhadas']['08 - Assistência Social']) & 
        (df_cidade['Despesas Empenhadas']['09 - Previdência Social']) & 
        (df_cidade['Despesas Empenhadas']['10 - Saúde'])
        ]['Valor'].cumsum()
    
    

    df_assis = df_cidade.loc[df_cidade['Despesas Empenhadas']['08 - Assistência Social']]
    df_prev = df_cidade.loc[df_cidade['Despesas Empenhadas']['09 - Previdência Social']]
    df_saude = df_cidade.loc[df_cidade['Despesas Empenhadas']['10 - Saúde']]

    df_valor_seguridade_social = df_assis + df_prev + df_saude

    return df_valor_seguridade_social"""

def get_all_municipios(tabela: pd.DataFrame) -> list:
    df_municipio = tabela['Instituição'].unique()
    list_municipio = list(df_municipio)
    list_municipio.sort()
    return list_municipio

def get_all_uf(tabela: pd.DataFrame) -> list:
    df_estados = tabela['UF'].unique()
    list_estados = list(df_estados)
    list_estados.sort()
    return list_estados

def get_cidade(tabela: pd.DataFrame, cidade: str, contas_interesse, coluna_interesse) -> pd.DataFrame:
    df_cidade = tabela.loc[tabela['Instituição'] == cidade]
    df_cidade['Valor'] = pd.to_numeric(df_cidade['Valor'], errors='coerce').fillna(0)

    dicio = {}
    for coluna in coluna_interesse:
        dicio[coluna] = {}
        for conta in contas_interesse:
            dicio[coluna][conta] = df_cidade.loc[
                (df_cidade['Coluna'] == coluna) & 
                (df_cidade['Conta'] == conta)][['Valor']].values
            value = dicio[coluna][conta]
            if value.size >= 1:
                dicio[coluna][conta] = value.max()
    
    tabela_cidade = pd.DataFrame.from_dict(dicio)
    pd.set_option('float_format', '{:.2f}'.format)
    dicio.clear()
    return tabela_cidade

def get_uf(tabela: pd.DataFrame, estado: str, contas_interesse, coluna_interesse) -> pd.DataFrame:
    df_estado = tabela.loc[tabela['UF'] == estado]
    df_estado['Valor'] = pd.to_numeric(df_estado['Valor'], errors='coerce').fillna(0)
    pd.set_option('float_format', '{:,.2f}'.format)

    dicio = {}
    for coluna in coluna_interesse:
        dicio[coluna] = {}
        for conta in contas_interesse:        
            array_soma_acumulativa = df_estado.loc[
                (df_estado['Coluna'] == coluna) &
                (df_estado['Conta'] == conta)]['Valor'].cumsum()

            print(array_soma_acumulativa.values.max())
            dicio[coluna][conta] = array_soma_acumulativa.values.max()
            
    tabela_uf = pd.DataFrame.from_dict(dicio)
    pd.set_option('float_format', '{:,.2f}'.format)
    dicio.clear()
    return tabela_uf

coluna_interesse = ['Despesas Empenhadas', 'Despesas Liquidadas', 'Despesas Pagas']

contas_interesse = [
    '06 - Segurança Pública', 
    '08 - Assistência Social', 
    '09 - Previdência Social', 
    '10 - Saúde', 
    '10.301 - Atenção Básica',
    '10.302 - Assistência Hospitalar e Ambulatorial', 
    '10.303 - Suporte Profilático e Terapêutico', 
    '10.304 - Vigilância Sanitária', 
    '10.305 - Vigilância Epidemiológica', 
    '10.306 - Alimentação e Nutrição',
    '12 - Educação',
    ]


if __name__ == "__main__":
    tabela = get_tabela()
    #valor_seguridade = get_seguridade_social(tabela, 'Prefeitura Municipal de Recife - PE')
   #print(valor_seguridade)
    #print(tabela)
    #tabela_uf = get_uf(tabela, 'PE', contas_interesse, coluna_interesse)
    #tabela_uf2 = get_uf(tabela, 'PI', contas_interesse, coluna_interesse)
    #tabela_uf3 = get_uf(tabela, 'BA', contas_interesse, coluna_interesse)
    #tabela_cidade = get_cidade(tabela, 'Prefeitura Municipal de Recife - PE', contas_interesse, coluna_interesse)
    #tabela_cidade2 = get_cidade(tabela, 'Prefeitura Municipal de Jaboatão dos Guararapes - PE', contas_interesse, coluna_interesse)
    #tabela_todos_uf = get_all_uf(tabela)
    #print(tabela_uf, end='\n')
    #print(tabela_cidade)
    #print(tabela_todos_uf)
    #tabela_cidade.to_csv('valor_cidade.csv', index=False)