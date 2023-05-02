import pandas as pd

def get_cidade(tabela: pd.DataFrame, cidade: str, contas_interesse, coluna_interesse) -> pd.DataFrame:
    df_cidade = tabela.loc[tabela['Instituição'] == cidade]
    print(df_cidade)
    df_cidade['Valor'] = pd.to_numeric(df_cidade['Valor'])

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
    return tabela_cidade

def get_uf(tabela: pd.DataFrame, estado: str, contas_interesse, coluna_interesse) -> pd.DataFrame:
    df_estado = tabela.loc[tabela['UF'] == estado]
    df_estado['Valor'] = pd.to_numeric(df_estado['Valor'])

    dicio = {}
    for coluna in coluna_interesse:
        dicio[coluna] = {}
        for conta in contas_interesse:
            dicio[coluna][conta] = df_estado.loc[
                (df_estado['Coluna'] == coluna) & 
                (df_estado['Conta'] == conta)]['Valor'].sum(axis=0)
            
    tabela_uf = pd.DataFrame.from_dict(dicio)
    return tabela_uf

coluna_interesse = ['Despesas Empenhadas', 'Despesas Liquidadas', 'Despesas Pagas']

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
    '10.306 - Alimentação e Nutrição'
    ]

if __name__ == "__main__":
    tabela = pd.read_csv('tabela_dados.csv', low_memory=False)
    tabela_uf = get_uf(tabela, 'PE', contas_interesse, coluna_interesse)
    tabela_cidade = get_cidade(tabela, 'Prefeitura Municipal de Recife - PE', contas_interesse, coluna_interesse)
    print(tabela_uf, end='\n')
    print(tabela_cidade)
    tabela_cidade.to_csv('valor_cidade.csv', index=False)