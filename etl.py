import pandas as pd

# Leer el archivo de entrada
df = pd.read_csv('input.csv')

# Calcular IGV (18%) y total
df['IGV'] = df['valor'] * 0.18
df['total'] = df['valor'] + df['IGV']

# Clasificar productos según su valor original
def clasificar(valor):
    if valor < 200:
        return 'bajo'
    elif valor < 400:
        return 'medio'
    else:
        return 'alto'

df['clasificación'] = df['valor'].apply(clasificar)

# Guardar el resultado en output.csv
df.to_csv('output.csv', index=False)
print("✅ ETL completado con clasificación y cálculo de IGV.")