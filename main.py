# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 14:18:05 2026

@author: Delfina
"""

ruta = "datos/MotionLab_mock_data.csv"

from src.cargar_datos import cargar_datos
from src.metricas import calcular_hits_totales, calcular_tiempo_primer_hit
from src.procesamiento_datos import filtrar_por_participante


try:
    id_participante = int(input("Ingrese un numero: "))
        
    datos = cargar_datos(ruta)
    if len(datos) == 0:
        print("No hay datos")

    for i in range(1, len(datos)):
        if datos[i]["tiempo"] < datos[i-1]["tiempo"]:
            print("Error: el tiempo no ess creciente")
          
    filtro = filtrar_por_participante(datos, id_participante)
    if filtro is None:
        print("el participante no fue encontrado")

    hits = calcular_hits_totales(datos)
    tiempo_primer = calcular_tiempo_primer_hit(datos)
    
except ValueError as error:
    print(error)

else:
    print(datos)
    print(filtro)
    print(hits)
    print(tiempo_primer)

