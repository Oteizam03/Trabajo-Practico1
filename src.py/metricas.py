#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:24:10 2026

@author: milagrosoteiza
"""

from cargar_datos_1 import parsear_linea, cargar_datos

def calcular_hits_totales(datos: list):
    """
    cuenta cantidad de veces en los que hay un hit

    Parameters
    ----------
    datos : list
        es lo que devuelve la fucnion cargar_datos. la lista de dicionarios con los registros

    Returns
    -------
    hits : int
        es la cantidad de hits que hubo en todo el archivo.

    """
    linea = parsear_linea()
    datos = cargar_datos(linea)
    hits = 0
    for diccionario in datos:
        if diccionario["hit"] == True:
            hits += 1
    return hits
    
def calcular_tiempo_primer_hit(datos: list):
    """
    esta funcion busca el primer hit entre los pacientes para devolver el tiempo de ese participante

    Parameters
    ----------
    datos : list
        es lo que devuelve la fucnion cargar_datos. la lista de dicionarios con los registros

    Returns
    -------
    la clave de valor["tiempo"]: es un int
        es el tiempo numerico que tardo el participante con el primer hit.

    """
    linea = parsear_linea()
    datos = cargar_datos(linea)
    for valor in datos:
        if valor["hit"] == True:
            return valor["tiempo"]      



