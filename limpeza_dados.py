import pandas as pd

df = pd.read_csv('clientes.csv')

pd.set_option('display.width', None)
print(df.head())

# Remover dados
df.drop('pais', axis=1, inplace=True)  # Coluna(1)
df.drop(2, axis=0, inplace=True)  # Linha (0)

# Normalizar campos de texto
df['nome'] = df['nome'].str.title()
df['endereco'] = df['endereco'].str.lower()
df['estado'] = df['estado'].str.strip().str.upper()

# Converter tipo de dados
df['idade'] = df['idade'].astype(int)

print('Normalizar Textos',df.head())

# Tratar valores nulos (ausentes)
df_fillna = df.fillna(0)  # Substituir valores nulos por zero
df_dropna = df.dropna()  # Remover registros com valores nulos
df_dropna4 = df.dropna(thresh=4)  # Manter resgistro com no minimo 4 valores não nulos
df = df.dropna(subset=['cpf'])  # Remover Registro com cpf nulo

print('Valores nulos:\n', df.isnull().sum())
print('Qtd de registros nulos com fillna:', df_fillna.isnull().sum().sum())
print('Qtd de registros nulos com dropna:', df_dropna.isnull().sum().sum())
print('Qtd de registros nulos com fillna:', df_dropna4.isnull().sum().sum())
print('Qtd de registros nulos com fillna:', df.isnull().sum().sum())

df.fillna({'estado': 'Desconhecido'}, inplace=True)
df['endereco'] = df['endereco'].fillna('Endereço não informado')
df['idade_corrigida'] = df['idade'].fillna(df['idade'].mean())

# Tratar formato de dados
df['data_corrigida'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

# Tratar dados duplicados
print('Qtd registros atuais:', df.shape[0])
df.drop_duplicates()
df.drop_duplicates(subset='cpf', inplace=True)
print('QTD registros removendo duplicatas:', len(df))

print('Dados Limpos:\n', df)

# Salvar dataframe
df['data'] = df['data_corrigida']
df['idade'] = df['idade_corrigida']

df_salvar = df[['nome', 'cpf', 'idade', 'data', 'endereco','estado']]
df_salvar.to_csv('clientes_limpeza.csv', index=False)

print('Novo DataFrame: \n', pd.read_csv('clientes_limpeza.csv'))