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
    
    with open ("datos.cvs" , "r") as archivo:
        datos = []
        for linea in archivo:
            print(linea)
            registro = parsear_linea(linea)
            datos.append(registro)
    
    
"""

def parsear_linea(lineas:str):
    
    registro = {}
    for linea in lineas:
        lista_separada = linea.split(",")
        for id_participante in lista_separada[0]:
            id_participante = int(id_participante)
            registro["id_participante"] = id_participante
        for tiempo in lista_separada[1]:
            tiempo = float(tiempo)
            registro["tiempo"] = tiempo
        for x in lista_separada[2]:
            x = float(x)
            registro["x"] = x
        for y in lista_separada[3]:
            y = float(y)
            registro["y"] = y
        for hit in lista_separada[4]:
            hit = bool(hit)
            registro["hit"] = hit
        for condicion in lista_separada[5]:
            condicion = str(condicion)
            registro["condicion"] = condicion
    return registro
    """