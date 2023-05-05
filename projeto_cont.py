import pandas as pd

def get_tabela():
    tabela = pd.read_csv('tabela_dados.csv', low_memory=False)

    return tabela

def get_all_municipios(tabela: pd.DataFrame) -> list[str]:
    df_municipio = tabela['Instituição'].unique()
    list_municipio = list(df_municipio)
    list_municipio.sort()
    return list_municipio

def get_all_uf(tabela: pd.DataFrame) -> list[str]:
    df_estados = tabela['UF'].unique()
    list_estados = list(df_estados)
    list_estados.sort()
    return list_estados

def get_uf_municipios(tabela: pd.DataFrame, estado : str) -> list[str]:
    tabela_estado = tabela.loc[tabela['UF'] == estado]
    df_muni_uf = tabela_estado['Instituição'].unique()
    lista_munici_uf = list(df_muni_uf)
    lista_munici_uf.sort()
    return lista_munici_uf
    

def get_cidade(tabela: pd.DataFrame, cidade: str, contas_interesse, coluna_interesse) -> pd.DataFrame:
    df_cidade = tabela.loc[tabela['Instituição'] == cidade]
    df_cidade['Valor'] = pd.to_numeric(df_cidade['Valor'], errors='coerce').fillna(0)

    dicio = {}
    for coluna in coluna_interesse:
        dicio[coluna] = {}
        for conta in contas_interesse:
            dicio[coluna][conta] = df_cidade.loc[
                (df_cidade['Coluna'] == coluna) & 
                (df_cidade['Conta'] == conta)]['Valor'].sum()
            # value = dicio[coluna][conta]
            # if value.size >= 1:
            #     dicio[coluna][conta] = value.max()
    
    tabela_cidade = pd.DataFrame.from_dict(dicio)
    pd.set_option('float_format', '{:.2f}'.format)
    dicio.clear()
    return tabela_cidade

def get_uf(tabela: pd.DataFrame, estado: str, contas_interesse, coluna_interesse) -> pd.DataFrame:
    df_estado = tabela.loc[tabela['UF'] == estado]
    df_estado['Valor'] = pd.to_numeric(df_estado['Valor'], errors='coerce').fillna(0)

    dicio = {}
    for coluna in coluna_interesse:
        dicio[coluna] = {}
        for conta in contas_interesse:        
            array_soma_acumulativa = df_estado.loc[
                (df_estado['Coluna'] == coluna) &
                (df_estado['Conta'] == conta)]['Valor'].sum()

            dicio[coluna][conta] = array_soma_acumulativa
            
    tabela_uf = pd.DataFrame.from_dict(dicio)
    pd.set_option('float_format', '{:,.2f}'.format)
    dicio.clear()
    return tabela_uf

coluna_interesse = [
    'Despesas Empenhadas',
     'Despesas Liquidadas',
      'Despesas Pagas',
      'Inscrição de Restos a Pagar Não Processados',
    'Inscrição de Restos a Pagar Processados',
      ]

contas_interesse = [
    '06 - Segurança Pública', 
    '08 - Assistência Social', 
    '09 - Previdência Social', 
    '10 - Saúde', 
    '12 - Educação',
    '10.301 - Atenção Básica',
    '10.302 - Assistência Hospitalar e Ambulatorial', 
    '10.303 - Suporte Profilático e Terapêutico', 
    '10.304 - Vigilância Sanitária', 
    '10.305 - Vigilância Epidemiológica', 
    '10.306 - Alimentação e Nutrição',
    ]