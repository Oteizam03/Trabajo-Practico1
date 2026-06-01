ahora? # MotionLab - Sistema de Analisis de Rendimiento Psicomotor

Este proyecto consiste en el desarrollo de un sistema de software modular en Python dise�ado para procesar, validar y analizar series temporales provenientes de experimentos de comportamiento motor humano. El objetivo principal es evaluar cómo el contexto social (condiciones de competencia vs. cooperacion) modula el rendimiento, la velocidad y la precision de los participantes.

## Autores
Delfina Ferrero
Milagros Oteiza

---

## Descripción del Experimento y Funcionalidad
El sistema modela una tarea motora controlada donde cada participante debe realizar movimientos continuos durante un periodo fijo de tiempo con el objetivo de alcanzar una zona de interes en el espacio. 

Para evaluar el desempe�o, el software realiza de forma automatizada:

1. Registro Continuo: Captura la posición espacial del movimiento (coordenadas `X` e `Y`), el tiempo transcurrido en segundos y la detección de eventos de acierto (`hit`).
2. Estructuración de Datos: Almacena y organiza las series temporales por participante y por condicion experimental.
3. Calculo de Metricas Criticas: Determina de forma masiva el total de hits globales y el tiempo exacto en el que ocurrio el primer acierto.

---

## Implementación de la Libreria Pandas y Optimizacion del Sistema

Para optimizar el rendimiento y la escalabilidad del sistema, se migro el procesamiento nativo de Python hacia el paradigma vectorial de la libreria **Pandas**. 

En lugar de abrir el archivo linea por linea y parsear los elementos manualmente, Pandas carga la totalidad de los datos directamente en un objeto `DataFrame`. Esto acelera drasticamente la velocidad de procesamiento, detecta automaticamente los tipos de datos en las columnas y elimina la necesidad de bucles iterativos (`for` o `while`), reemplazandolos por operaciones vectoriales altamente eficientes.

### Impacto en la Arquitectura del Codigo:

* `parsear_linea()`: Se elimino por completo. Pandas procesa el archivo estructurado en bloque y no requiere evaluar cadenas de texto linea por linea.
* `cargar_datos()`: Se modifico radicalmente Reemplaza los bloques `with open()` tradicionales por una sola instrucción (`pd.read_csv()`) que aplica validaciones masivas en milisegundos usando metodos como `.isna().any()`.
* `filtrar_por_participante()`: Se optimizo. Reemplaza la busqueda manual por indexacion logica (`df[df['id_participante'] == id]`).
* `metricas.py`: Se vectorizo. El conteo de hits y el calculo del tiempo del primer acierto se realizan con `.sum()` y `.min()`.

---

## Instrucciones de Uso

### 1. Requisitos Previos

Asegurese de tener instalado Python (version 3.8 o superior) en su sistema. Para verificarlo, ejecute en su terminal:


python --version
## Estructura de archivos
su-repositorio/
│
├── datos/
│   └── MotionLab_mock_data.csv    <-- Archivo de datos a procesar
│
├── src/
│   ├── cargar_datos.py
│   ├── procesamiento_datos.py
│   └── metricas.py
│
├── graficos/   <--  Se crea automáticamente
│
├── main.py  <-- Script ejecutable principal
├── app.py
├── prompts_dashboard.txt
└── README.md
#no sabemos porque cuando se guarda se ponen esos caracteres raros

---

## Ejecuci�n del Programa (Consola)

Para ejecutar el an�lisis desde consola:
python main.py

###Interfaz Web (Streamlit)

Para ejecutar el dashboard interactivo:
streamlit run app.py

La aplicaci�n permite:

Subir un archivo CSV
Validar los datos autom�ticamente
Visualizar m�tricas clave
Filtrar por participante
Ver gr�ficos de rendimiento

###Manejo de Errores

El sistema implementa manejo de errores mediante bloques try/except, contemplando:

Archivos inexistentes
Datos inv�lidos o fuera de rango
Valores nulos
Errores inesperados

###Requisitos

Instalar dependencias necesarias:
pip install pandas matplotlib streamlit

###Uso de Inteligencia Artificial

Se utiliz� inteligencia artificial como asistente para:

Generaci�n inicial de c�digo
Correcci�n de errores
Dise�o del dashboard con Streamlit
Documentaci�n del proyecto

El proceso fue documentado en el archivo:
prompts_dashboard.txt

###Consideraciones Finales

El sistema fue dise�ado siguiendo una arquitectura modular, separando responsabilidades en distintos archivos para facilitar su mantenimiento, reutilizaci�n y escalabilidad.

Adem�s, se incorpor� una interfaz web interactiva mediante Streamlit, permitiendo una exploraci�n m�s intuitiva y visual de los datos.



