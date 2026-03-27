#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:23:43 2026

@author: milagrosoteiza
"""


from cargar_datos_1 import parsear_linea, cargar_datos

def filtrar_por_participante(datos: list, id_participante: int):
    linea = parsear_linea()
    datos = cargar_datos(linea)
    for dic in datos:
        if id_participante == dic["id_participante"]:
            return dic
        