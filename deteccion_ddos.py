import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 1. Cargar los datos
df = pd.read_csv('network_traffic.csv', parse_dates=['datetime'], index_col='datetime')

# 2. Ingeniería de características (Lógica de "lags" que usaste en los taxis)
def make_features(data, max_lag):
    df_f = data.copy()
    df_f['hour'] = df_f.index.hour
    for lag in range(1, max_lag + 1):
        df_f[f'lag_{lag}'] = df_f['packets_per_second'].shift(lag)
    return df_f.dropna()

# Usamos 24 horas de historia para predecir la siguiente
df_featured = make_features(df, 24)

# 3. División de datos (Entrenamos con lo normal, probamos con el ataque)
# Dejamos las últimas 24 horas para la prueba (donde está el DDoS)
train = df_featured.iloc[:-24]
test = df_featured.iloc[-24:]

X_train = train.drop(['packets_per_second'], axis=1)
y_train = train['packets_per_second']
X_test = test.drop(['packets_per_second'], axis=1)
y_test = test['packets_per_second']

# 4. Entrenar el modelo "Centinela"
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Predicción y Detección de Anomalías
predictions = model.predict(X_test)
rmse = mean_squared_error(y_test, predictions)**0.5

print(f"Análisis completado. RECM: {rmse:.2f}")

# Si el valor real es mucho mayor a la predicción, hay alerta
test['prediccion'] = predictions
test['alerta'] = test['packets_per_second'] > (test['prediccion'] * 3)

if test['alerta'].any():
    print("¡ALERTA CRÍTICA: Posible ataque DDoS detectado en las últimas horas!")
else:
    print("Tráfico dentro de los parámetros normales.")