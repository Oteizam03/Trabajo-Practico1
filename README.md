# Trabajo-Practico1
Este es un trabajo realizado por Milagros Oteiza y Delfina Ferrero. Lo que realiza este trabajo es leer y estructurar datos de una tarea motora, representa correctamente eventos en el tiempo, y calcula metricas basicas de desempeño.
El participante debe realizar movimientos continuos durante un periodo fijo de tiempo y alcanzar una zona objetiva en el espacio. Debe repetir esto la mayor cantidad de veces posibles. Y el sistema debe registrar continuamente la posicion del movimiento, el tiempo transcurrido desde el inicio, y si ocurrio un evento relevante (hit). 

Libreria Pandas:
Para optimizar el rendimiento del istema proponemos utilizar la libreria Pandas. En lugar de abrir el archivo linea por linea y parsear los elementos manualmente, Pandas permite cargar todos los datos directamente en la memoria de un DataFrame. Ademas, Pandas permite leer y procesar textos con muchisima mas velocidad, detectando columnas y datos automaticamente. 
Las funciones creadas se modificarian o directamente se eliminarian:
parsear_linea() se elimina ya que no es necesario el parseo linea por linea. Pandas procesa el archivo entero, no necesita ir linea por linea. 
cargar_datos() se reemplaza ya que con Pandas se realiza automaticamente. 
Las otras funciones tambien se modificarian, haciendo el codigo mas sencillo y directo. 
De esta forma se eliminan los bucles manuales, y se reemplazan por operaciones vectoriales. Son mucho mas eficientes. 
