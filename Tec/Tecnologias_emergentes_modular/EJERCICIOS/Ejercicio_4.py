import pandas as pd
import numpy as np

# Simular la creación de un DataFrame "grande"
num_filas = 1000000 # Un millón de filas
data = {
	'id_usuario': np.random.randint(1, 1000, num_filas),
	'producto': np.random.choice(['A', 'B', 'C', 'D'], num_filas),
	'precio': np.random.uniform(10, 100, num_filas),
	'fecha_compra': pd.to_datetime(np.random.choice(pd.date_range('2023-01-01', '2023-12-31'), num_filas)),
	'cantidad': np.random.randint(1, 5, num_filas)
}

df = pd.DataFrame(data)

print(f"Tamaño del DataFrame: {len(df)} filas")
print("Primeras 5 filas:")
print(df.head())

# Ejemplo de análisis básico: calcular el total gastado por usuario
df['total_gastado'] = df['precio'] * df['cantidad']
total_por_usuario = df.groupby('id_usuario')['total_gastado'].sum()

print("\nTotal gastado por los primeros 10 usuarios:")
print(total_por_usuario.head(10))

# Ejemplo de filtrado: encontrar compras del producto 'A' después de 2023-06-01
compras_a_despues_junio = df[(df['producto'] == 'A') & (df['fecha_compra'] > '2023-06-01')]
print(f"\nNúmero de compras del producto 'A' después de junio de 2023: {len(compras_a_despues_junio)}")