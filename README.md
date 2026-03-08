# Network Sentinel: Detección de Anomalías DDoS con ML

Este proyecto implementa un sistema de **Análisis de Comportamiento de Red (UBA)** para la detección temprana de ataques de Denegación de Servicio (DDoS). Utiliza modelos de regresión lineal y análisis de series temporales para establecer una línea base de tráfico normal y disparar alertas ante desviaciones críticas.

## 🛡️ Objetivo del Proyecto
Desarrollar una herramienta defensiva capaz de diferenciar entre los picos naturales de tráfico (estacionalidad diaria) y ataques maliciosos, permitiendo una respuesta a incidentes (IR) más rápida.

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.12
* **Análisis de Datos:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (LinearRegression)
* **Visualización:** Matplotlib
* **Entorno:** VS Code / Local Home Lab

## 📊 Metodología Técnica
1. **Ingeniería de Características:** Implementación de *lags* (24 horas) para capturar la estacionalidad del tráfico de red.
2. **Entrenamiento:** El modelo aprende los patrones de consumo habituales del servidor.
3. **Detección:** Uso de la métrica **RECM (Root Mean Squared Error)** para cuantificar la anomalía.
4. **Alerta:** Disparo de notificación crítica cuando el tráfico real supera en 3x la predicción del modelo.

## 🚀 Resultados
* **Precisión:** Capacidad de identificar picos de tráfico malicioso con una desviación clara del comportamiento histórico.
* **Privacidad:** Procesamiento local alineado con arquitecturas de **Edge Computing**.