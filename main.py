# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 14:18:05 2026

@author: Delfina
"""

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

