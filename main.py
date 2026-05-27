# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 14:18:05 2026

@author: Delfina
"""

import os
import matplotlib.pyplot as plt
from src.cargar_datos import cargar_datos
from src.metricas import calcular_hits_totales, calcular_tiempo_primer_hit
from src.procesamiento_datos import filtrar_por_participante

ruta = "datos/MotionLab_mock_data.csv"

# Requisito de la consigna: Asegurar de manera automatizada la carpeta de gráficos
os.makedirs("graficos", exist_ok=True)

try:
    id_participante = int(input("Ingrese el ID del participante a buscar: "))
    
    # Carga y validaciones automáticas con Pandas
    df_datos = cargar_datos(ruta)
    
    if df_datos.empty:
        print("No hay datos en el archivo.")
        
    # Verificación de tiempo creciente de forma masiva (Pandas .diff())
    # Si hay alguna diferencia menor o igual a cero, el tiempo no es estrictamente creciente
    if (df_datos['tiempo'].diff().dropna() <= 0).any():
        print("Advertencia: El tiempo no es estrictamente creciente en algunos registros.")
        
    # Filtrado y métricas usando DataFrames
    filtro_participante = filtrar_por_participante(df_datos, id_participante)
    if filtro_participante is None:
        print("El participante no fue encontrado.")
        
    hits = calcular_hits_totales(df_datos)
    tiempo_primer = calcular_tiempo_primer_hit(df_datos)
    
    # --- PARTE NUEVA: Generación y exportación del gráfico ---
    print("\nGenerando gráfico estadístico...")
    plt.figure(figsize=(8, 5))
    
    # Agrupamos por condición y contamos cuántos hits hubo en cada una
    df_datos.groupby('condicion')['hit'].sum().plot(kind='bar', color=['tomato', 'skyblue'])
    
    plt.title("Cantidad Total de Hits por Condición Experimental")
    plt.xlabel("Condición")
    plt.ylabel("Cantidad de Hits")
    plt.xticks(rotation=0)
    plt.tight_layout()
    
    # Guardado obligatorio requerido por la consigna
    plt.savefig('graficos/distribucion_respuestas.png', dpi=300)
    plt.close()
    print("Gráfico exportado con éxito en 'graficos/distribucion_respuestas.png'")

except ValueError as error:
    print(f"Error de valor: {error}")
except FileNotFoundError as error:
    print(f"Error de archivo: {error}")
except Exception as error:
    print(f"Ocurrió un error inesperado: {error}")

else:
    print("\n--- RESULTADOS DEL PROCESAMIENTO ---")
    print(f"Total de hits globales: {hits}")
    print(f"Tiempo del primer hit global: {tiempo_primer} segundos")
    if filtro_participante is not None:
        print(f"\nPrimeros registros del participante {id_participante}:")
        print(filtro_participante.head()) # Muestra las primeras 5 filas para no saturar la consola
        






