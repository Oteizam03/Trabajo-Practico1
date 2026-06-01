ahora? # MotionLab - Sistema de Analisis de Rendimiento Psicomotor

Este proyecto consiste en el desarrollo de un sistema de software modular en Python diseñado para procesar, validar y analizar series temporales provenientes de experimentos de comportamiento motor humano. El objetivo principal es evaluar c√≥mo el contexto social (condiciones de competencia vs. cooperacion) modula el rendimiento, la velocidad y la precision de los participantes.

## Autores
Delfina Ferrero
Milagros Oteiza

---

## Descripci√≥n del Experimento y Funcionalidad
El sistema modela una tarea motora controlada donde cada participante debe realizar movimientos continuos durante un periodo fijo de tiempo con el objetivo de alcanzar una zona de interes en el espacio. 

Para evaluar el desempeño, el software realiza de forma automatizada:

1. Registro Continuo: Captura la posici√≥n espacial del movimiento (coordenadas `X` e `Y`), el tiempo transcurrido en segundos y la detecci√≥n de eventos de acierto (`hit`).
2. Estructuraci√≥n de Datos: Almacena y organiza las series temporales por participante y por condicion experimental.
3. Calculo de Metricas Criticas: Determina de forma masiva el total de hits globales y el tiempo exacto en el que ocurrio el primer acierto.

---

## Implementaci√≥n de la Libreria Pandas y Optimizacion del Sistema

Para optimizar el rendimiento y la escalabilidad del sistema, se migro el procesamiento nativo de Python hacia el paradigma vectorial de la libreria **Pandas**. 

En lugar de abrir el archivo linea por linea y parsear los elementos manualmente, Pandas carga la totalidad de los datos directamente en un objeto `DataFrame`. Esto acelera drasticamente la velocidad de procesamiento, detecta automaticamente los tipos de datos en las columnas y elimina la necesidad de bucles iterativos (`for` o `while`), reemplazandolos por operaciones vectoriales altamente eficientes.

### Impacto en la Arquitectura del Codigo:

* `parsear_linea()`: Se elimino por completo. Pandas procesa el archivo estructurado en bloque y no requiere evaluar cadenas de texto linea por linea.
* `cargar_datos()`: Se modifico radicalmente Reemplaza los bloques `with open()` tradicionales por una sola instrucci√≥n (`pd.read_csv()`) que aplica validaciones masivas en milisegundos usando metodos como `.isna().any()`.
* `filtrar_por_participante()`: Se optimizo. Reemplaza la busqueda manual por indexacion logica (`df[df['id_participante'] == id]`).
* `metricas.py`: Se vectorizo. El conteo de hits y el calculo del tiempo del primer acierto se realizan con `.sum()` y `.min()`.

---

## Instrucciones de Uso

### 1. Requisitos Previos

Asegurese de tener instalado Python (version 3.8 o superior) en su sistema. Para verificarlo, ejecute en su terminal:


python --version
## Estructura de archivos
su-repositorio/
‚îÇ
‚îú‚îÄ‚îÄ datos/
‚îÇ   ‚îî‚îÄ‚îÄ MotionLab_mock_data.csv    <-- Archivo de datos a procesar
‚îÇ
‚îú‚îÄ‚îÄ src/
‚îÇ   ‚îú‚îÄ‚îÄ cargar_datos.py
‚îÇ   ‚îú‚îÄ‚îÄ procesamiento_datos.py
‚îÇ   ‚îî‚îÄ‚îÄ metricas.py
‚îÇ
‚îú‚îÄ‚îÄ graficos/   <--  Se crea autom√°ticamente
‚îÇ
‚îú‚îÄ‚îÄ main.py  <-- Script ejecutable principal
‚îú‚îÄ‚îÄ app.py
‚îú‚îÄ‚îÄ prompts_dashboard.txt
‚îî‚îÄ‚îÄ README.md

#no sabemos porque cuando se guarda se ponen esos caracteres raros
Trabajo-Practico1/
│
├── app.py
├── main.py
├── README.md
├── prompts_dashboard.txt
│
├── datos/
│ └── MotionLab_mock_data.csv
│
├── graficos/
│
├── src/
│ ├── cargar_datos.py
│ ├── procesamiento_datos.py
│ ├── metricas.py
│ └── validacion_datos.py

---

## Ejecución del Programa (Consola)

Para ejecutar el análisis desde consola:
python main.py

###Interfaz Web (Streamlit)

Para ejecutar el dashboard interactivo:
streamlit run app.py

La aplicación permite:

Subir un archivo CSV
Validar los datos automáticamente
Visualizar métricas clave
Filtrar por participante
Ver gráficos de rendimiento

###Manejo de Errores

El sistema implementa manejo de errores mediante bloques try/except, contemplando:

Archivos inexistentes
Datos inválidos o fuera de rango
Valores nulos
Errores inesperados

###Requisitos

Instalar dependencias necesarias:
pip install pandas matplotlib streamlit

###Uso de Inteligencia Artificial

Se utilizó inteligencia artificial como asistente para:

Generación inicial de código
Corrección de errores
Diseño del dashboard con Streamlit
Documentación del proyecto

El proceso fue documentado en el archivo:
prompts_dashboard.txt

###Consideraciones Finales

El sistema fue diseñado siguiendo una arquitectura modular, separando responsabilidades en distintos archivos para facilitar su mantenimiento, reutilización y escalabilidad.

Además, se incorporó una interfaz web interactiva mediante Streamlit, permitiendo una exploración más intuitiva y visual de los datos.



