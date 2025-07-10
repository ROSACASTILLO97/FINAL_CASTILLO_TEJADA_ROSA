import pandas as pd

# Leer los datos
df = pd.read_csv('input.csv')

# Transformaciones:
# - Redondear los precios
# - Calcular IGV (18%)
# - Clasificar el precio (bajo, medio, alto)
df['valor_redondeado'] = df['valor'].round()
df['igv'] = df['valor'] * 0.18
df['total_con_igv'] = df['valor'] + df['igv']
df['clasificacion'] = pd.cut(df['valor'], bins=[0, 200, 400, float('inf')], labels=['bajo', 'medio', 'alto'])

# Guardar el resultado
df.to_csv('output.csv', index=False)
print("✅ ETL completado correctamente.")