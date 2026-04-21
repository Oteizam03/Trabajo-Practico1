

from src.cargar_datos import cargar_datos
from src.validacion_datos import validar_registro
from src.metricas import calcular_hits_totales, calcular_tiempo_primer_hit
from src.procesamiento_datos import filtrar_por_participante


def main():
    """
    maneja la carga, validación, procesamiento y análisis de datos.
    """
    ruta = "/Users/milagrosoteiza/Documents/GitHub/Trabajo-Practico1/datos/MotionLab_mock_data.csv"

    try:
        datos = cargar_datos(ruta)

        datos_validos = []
        for registro in datos:
            if validar_registro(registro):
                datos_validos.append(registro)

        if len(datos_validos) == 0:
            raise ValueError("No hay datos válidos para analizar")

        id_participante = int(input("Ingrese un número de cuatro dígitos: "))

        hits = calcular_hits_totales(datos_validos)
        tiempo_primer = calcular_tiempo_primer_hit(datos_validos)
        filtro = filtrar_por_participante(datos_validos, id_participante)

        print("Cantidad total de hits:", hits)
        print("Tiempo del primer hit:", tiempo_primer)
        print("Registros del participante:", filtro)

    except FileNotFoundError as e:
        print("Error de archivo:", e)
    except ValueError as e:
        print("Error de validación o entrada:", e)
    except Exception as e:
        print("Ocurrió un error inesperado:", e)


ruta = "datos/MotionLab_mock_data.csv"

from src.cargar_datos import parsear_linea, cargar_datos
from src.metricas import calcular_hits_totales, calcular_tiempo_primer_hit
from src.procesamiento_datos import filtrar_por_participante

with open (ruta, "r") as archivo:
    for linea in archivo:
        print(linea)
        
id_participante = input("Ingrese un numero de cuatro digitos: ")
        
parseo = parsear_linea(linea)
datos = cargar_datos(ruta)
hits = calcular_hits_totales(datos)
tiempo_primer = calcular_tiempo_primer_hit(datos)
filtro = filtrar_por_participante(datos, id_participante)

print(parseo)
print(datos)
print(hits)
print(tiempo_primer)
print(filtro)

