#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:23:43 2026

@author: milagrosoteiza
"""


#from src.cargar_datos import parsear_linea, cargar_datos

import pandas as pd

def filtrar_por_participante(df: pd.DataFrame, id_participante: int) -> pd.DataFrame:
    """
    Selecciona y devuelve todas las filas correspondientes a un participante.

    Parameters
    ----------
    df : pd.DataFrame
        El DataFrame general cargado con todos los datos.
    id_participante : int
        Identificador numérico del participante a buscar.

    Returns
    -------
    df_filtrado : pd.DataFrame o None
        Un DataFrame filtrado con los registros del participante, o None si no existe.
    """
    
    # Filtramos el DataFrame por la columna id_participante
    df_filtrado = df[df['id_participante'] == id_participante]
    
    # Si el resultado está vacío, significa que el participante no existe
    if df_filtrado.empty:
        return None
        
    return df_filtrado

   

