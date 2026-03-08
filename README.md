# 🛡️ Network Sentinel: Detección Temprana de Ataques DDoS mediante Machine Learning

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-312/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)

**Network Sentinel** es un sistema de detección de anomalías basado en Machine Learning que actúa como un centinela para proteger servidores contra ataques de Denegación de Servicio (DDoS). A diferencia de los firewalls tradicionales que operan con reglas estáticas, este proyecto utiliza análisis de series temporales para **aprender el comportamiento normal del tráfico de red y alertar de forma inteligente cuando ocurre una desviación maliciosa**.

---

## 🎯 El Problema Real que Resuelve
Los cortafuegos convencionales luchan por diferenciar entre un pico de tráfico legítimo (como el de una promoción nocturna) y un ataque DDoS. Este sistema resuelve ese desafío mediante:

*   **Análisis de Comportamiento de Entidades (UEBA):** Aplica principios de User and Entity Behavior Analytics a la propia infraestructura de red.
*   **Estacionalidad Diaria:** Captura los patrones de tráfico que varían según la hora del día para construir una "línea base" robusta de lo que se considera normal.
*   **Detección Proactiva:** Predice el tráfico futuro esperado y dispara alertas únicamente cuando la desviación es tan grande que indica un ataque, no un simple ruido estadístico.

---

## 🛠️ Tecnologías y Arquitectura
*   **Lenguaje Principal:** Python 3.12
*   **Análisis y Manipulación de Datos:** `Pandas`, `NumPy`
*   **Machine Learning:** `Scikit-Learn` (Regresión Lineal para establecer la línea base)
*   **Visualización:** `Matplotlib` (para análisis exploratorio de datos)
*   **Arquitectura:** Diseñado para ser ligero y desplegable en entornos de **Edge Computing**, garantizando baja latencia y privacidad de los datos al procesar todo localmente.

---

## 📊 Metodología Técnica: El Ciclo de Vida del "Centinela"

El flujo de trabajo del proyecto simula un pipeline de machine learning aplicado a la ciberseguridad:

1.  **Ingeniería de Características Temporales:** Se implementan ventanas deslizantes (`lags` de 24 horas). Esta técnica permite al modelo "recordar" el comportamiento de las últimas 24 horas para predecir la siguiente, capturando así la estacionalidad diaria inherente al tráfico de red.

2.  **Entrenamiento y Establecimiento de la Línea Base:** Se entrena un modelo de **Regresión Lineal** con los datos de tráfico histórico (aproximadamente 30 días). El objetivo no es solo predecir, sino que el modelo **aprenda el patrón de comportamiento normal del servidor**.

3.  **Detección de Anomalías:** El modelo genera una predicción para el tráfico de la siguiente hora. El sistema compara este valor con el tráfico real observado.

4.  **Sistema de Alertas Inteligentes:** Se utiliza un umbral dinámico: **si el tráfico real supera en 3 veces el valor predicho, se dispara una alerta crítica**. Esto simula la acción de un sistema de Respuesta a Incidentes (IR).

5.  **Simulación de Ataque Realista:** Se incluye un script (`generar_datos.py`) que inyecta un ataque DDoS masivo en las últimas horas del conjunto de datos. Esto permite validar la eficacia del modelo en un entorno controlado pero realista.

---

## 🚀 Resultados e Impacto
*   **Detección Inteligente:** El sistema demostró la capacidad de diferenciar eficazmente entre picos de tráfico diarios y un ataque simulado, reduciendo drásticamente los falsos positivos.
*   **Privacidad por Diseño:** Al operar de forma local y no depender de servicios externos, se alinea perfectamente con arquitecturas de **Edge Computing** y políticas de soberanía de datos.
*   **Respuesta a Incidentes (IR) Acelerada:** La alerta temprana permite a los equipos de seguridad intervenir minutos u horas antes de que el servicio se vea comprometido.

---

## 📂 Estructura del Proyecto
```bash
.
├── deteccion_ddos.py          # Script principal: carga el modelo, predice y alerta.
├── generar_datos.py            # Generador de datos sintéticos con un ataque simulado.
├── network_traffic.csv         # Dataset generado con tráfico de red (normal + ataque).
└── README.md                   # Este archivo.
