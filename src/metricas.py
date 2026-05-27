#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:24:10 2026

@author: milagrosoteiza
"""

import pandas as pd

def calcular_hits_totales(df: pd.DataFrame) -> int:
    """
    Cuenta la cantidad total de hits en el DataFrame utilizando suma directa.
    """
    return int(df['hit'].sum())
    
def calcular_tiempo_primer_hit(df: pd.DataFrame) -> float:
    """
    Filtra los registros donde hubo un hit y encuentra el menor tiempo registrado.
    """
    # Filtramos donde hit sea True
    df_hits = df[df['hit'] == True]
    
    if df_hits.empty:
        return None # Por si no hubo ningún hit en todo el archivo
        
    # Obtenemos el tiempo mínimo de ese grupo filtrado
    return float(df_hits['tiempo'].min())


        
        



