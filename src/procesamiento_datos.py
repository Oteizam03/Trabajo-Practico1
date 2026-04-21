#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:23:43 2026

@author: milagrosoteiza
"""


from src.cargar_datos import parsear_linea, cargar_datos

def filtrar_por_participante(datos: list, id_participante: int):
    '''
    se encarga de seleccionar los datos correspondientes de un alumno y devolverlos en un diccionario

    Parameters
    ----------
    datos : list
        es una lista que contiene cada registro de la funcion a la que llama. quedaria cada registro de cada individuo..
    id_participante : int
        identiicador del participante.

    Returns
    -------
    dic : dicc
        diccionario que contiene los datos correspondientes a un alumno.

    '''
    
    for dic in datos:
        if dic["id_participante"] == id_participante:
            return dic

    return None

   

