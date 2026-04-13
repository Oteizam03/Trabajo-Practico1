#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:22:53 2026

@author: milagrosoteiza
"""
#cargar_datos
with open ("datos.cvs" , "r") as archivo:
    for linea in archivo:
        print(linea)
 
    
def parsear_linea(lineas:str):

    """
    La siguiente funcion separa los datos, id, tiempo, x, y, hiy y condicion para cada participante para asi, almacenar los datos individuales de cada participante en un diccionario.

    Parameters
    ----------
    lineas : str
        es una linea de texto que contiene la informacion de un participante.

    Returns
    -------
    registro : Dict
        contiene los valores de un solo participante, como clave la categoria. Ya sea el id, el tiempo, etc y como clave el valor indicado para ese participante.

    """

    registro = {}
    for linea in lineas:
        lista_separada = linea.split(",")
        for valor in lista_separada:
            id_participante = int(lista_separada [0])
            registro["id_participante"] = id_participante
            tiempo = float(lista_separada[1])
            registro["tiempo"] = tiempo
            x = float(lista_separada[2])
            registro["x"] = x
            y = float(lista_separada[3])
            registro["y"] = y
            hit = bool(lista_separada[4])
            registro["hit"] = hit
            condicion = str(lista_separada[5])
            registro["condicion"] = condicion
            return registro
           
def cargar_datos (ruta:str):
    """
    su funcion es almacenar en una lista cada diccionario de la funcion parsear_datos. Para asi, tener los valores de todos los participantes ordenados en cada diccionario individual

    Parameters
    ----------
    ruta : str
        DESCRIPTION.

    Returns
    -------
    datos : list
        es una lista que contiene cada registro de la funcion a la que llama. quedaria cada registro de cada individuo.

    """
    
    with open ("datos.cvs" , "r") as archivo:
        datos = []
        for linea in archivo:
            print(linea)
            registro = parsear_linea(linea)
            datos.append(registro)
        return datos
    
    
