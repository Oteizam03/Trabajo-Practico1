# MotionLab - Sistema de Análisis de Rendimiento Psicomotor

Este proyecto consiste en el desarrollo de un sistema de software modular en Python diseñado para procesar, validar y analizar series temporales provenientes de experimentos de comportamiento motor humano. El objetivo principal es evaluar cómo el contexto social (condiciones de competencia vs. cooperación) modula el rendimiento, la velocidad y la precisión de los participantes.

## Autores
* **Delfina Ferrero**
* **Milagros Oteiza**

---

## Descripción del Experimento y Funcionalidad
El sistema modela una tarea motora controlada donde cada participante debe realizar movimientos continuos durante un período fijo de tiempo con el objetivo de alcanzar una zona de interés en el espacio. 

Para evaluar el desempeño, el software realiza de forma automatizada:
1. **Registro Continuo:** Captura la posición espacial del movimiento (coordenadas `X` e `Y`), el tiempo transcurrido en segundos y la detección de eventos de acierto (`hit`).
2. **Estructuración de Datos:** Almacena y organiza las series temporales por participante y por condición experimental.
3. **Cálculo de Métricas Críticas:** Determina de forma masiva el total de hits globales y el tiempo exacto en el que ocurrió el primer acierto.

---

## Implementación de la Librería Pandas y Optimización del Sistema
Para optimizar el rendimiento y la escalabilidad del sistema, se migró el procesamiento nativo de Python hacia el paradigma vectorial de la librería **Pandas**. 

En lugar de abrir el archivo línea por línea y parsear los elementos manualmente, Pandas carga la totalidad de los datos directamente en un objeto `DataFrame`. Esto acelera drásticamente la velocidad de procesamiento, detecta automáticamente los tipos de datos en las columnas y elimina la necesidad de bucles iterativos (`for` o `while`), reemplazándolos por operaciones vectoriales altamente eficientes.

### Impacto en la Arquitectura del Código:
* `parsear_linea()`: **Se eliminó por completo**. Pandas procesa el archivo estructurado en bloque y no requiere evaluar cadenas de texto línea por línea.
* `cargar_datos()`: **Se modificó radicalmente**. Reemplaza los bloques `with open()` tradicionales por una sola instrucción estructurada (`pd.read_csv()`) que aplica validaciones masivas de rangos y nulidades en milisegundos empleando métodos como `.isna().any()`.
* `filtrar_por_participante()`: **Se optimizó**. Reemplaza la búsqueda secuencial manual por indexación lógica indexada (`df[df['id_participante'] == id]`).
* `metricas.py`: **Se vectorizó**. La contabilidad de hits y el cálculo del tiempo mínimo del primer acierto se delegan a las funciones nativas `.sum()` y `.min()` de Pandas sobre las columnas correspondientes.

---

## Instrucciones de Uso

### 1. Requisitos Previos
Asegúrese de tener instalado Python (versión 3.8 o superior) en su sistema. Para verificarlo, ejecute en su terminal:
```bash
python --version

## Estructura de archivos
su-repositorio/
│
├── datos/
│   └── MotionLab_mock_data.csv       <-- Archivo de datos a procesar
│
├── src/
│   ├── cargar_datos.py
│   ├── procesamiento_datos.py
│   └── metricas.py
│
├── graficos/                         <-- Se creará automáticamente
│
└── main.py                           <-- Script ejecutable principal


