#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:24:10 2026

@author: milagrosoteiza
"""

from cargar_datos_1 import parsear_linea, cargar_datos

def calcular_hits_totales(datos: list):
    linea = parsear_linea()
    datos = cargar_datos(linea)
    hits = 0
    for diccionario in datos:
        if diccionario["hit"] == True:
            hits += 1
    return hits
    
def calcular_tiempo_primer_hit(datos: list):
    linea = parsear_linea()
    datos = cargar_datos(linea)
    for valor in datos:
        if valor["hit"] == True:
            return valor["tiempo"]      



