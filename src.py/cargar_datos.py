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
    #lista_separada = ""
    for linea in lineas:
        lista_separada = linea.split(",")
        for id_participante in lista_separada[0]:
            id_participante = int(id_participante)
        for tiempo in lista_separada[1]:
            tiempo = float(tiempo)
        for x in lista_separada[2]:
            x = float(x)
        for y in lista_separada[3]:
            y = float(y)
        for hit in lista_separada[4]:
            hit = bool(hit)
        for condicion in lista_separada[5]:
            condicion = str(condicion)
        registro = {}
    
            
            
            
        
       