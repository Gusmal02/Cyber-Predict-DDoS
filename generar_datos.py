import pandas as pd
import numpy as np

# 1. Crear rango de fechas
dates = pd.date_range(start='2026-01-01', periods=24*30, freq='h')
n = len(dates)

# 2. Generar el tráfico base como una lista de números (para que sea 100% editable)
hour_effect = np.sin(2 * np.pi * dates.hour / 24)
# Usamos .tolist() para salir de cualquier estructura protegida de Pandas/Numpy
traffic = (500 + 200 * hour_effect + np.random.normal(0, 30, n)).tolist()

# 3. Inyectar el Ataque DDoS (multiplicar las últimas 12 horas)
# Al ser una lista, la mutación es directa y sencilla
for i in range(1, 13):
    traffic[-i] = traffic[-i] * 10

# 4. Crear el DataFrame y guardar
df = pd.DataFrame({'datetime': dates, 'packets_per_second': traffic})
df.to_csv('network_traffic.csv', index=False)

print("¡Logrado! El archivo network_traffic.csv se ha generado correctamente.")