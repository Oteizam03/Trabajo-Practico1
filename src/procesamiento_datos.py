#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:23:43 2026

@author: milagrosoteiza
"""


#from src.cargar_datos import parsear_linea, cargar_datos

import pandas as pd

def filtrar_por_participante(df: pd.DataFrame, id_participante: int) -> pd.DataFrame:
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
    
    # Filtramos el DataFrame por la columna id_participante
    df_filtrado = df[df['id_participante'] == id_participante]
    
    # Si el resultado está vacío, significa que el participante no existe
    if df_filtrado.empty:
        return None
        
    return df_filtrado

   

