import pandas as pd

#def get_uf(tabela: pd.DataFrame) -> pd.DataFrame:


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
    tabela = pd.read_csv('tabela_dados.csv', skiprows=4, low_memory=False)