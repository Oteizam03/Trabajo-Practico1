#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:22:53 2026

@author: milagrosoteiza
"""
#cargar_datos

import pandas as pd
import os

def cargar_datos(ruta: str) -> pd.DataFrame:
    """
    Carga el archivo CSV directamente en un DataFrame de Pandas y
    realiza todas las validaciones vectorizadas de forma masiva.

    Parameters
    ----------
    ruta : str
        La ruta física del archivo CSV con los datos a cargar.

    Returns
    -------
    df : pd.DataFrame
        Un DataFrame de Pandas con todos los registros validados.
    """
    # 1. Validar si el archivo existe físicamente
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"No se encontró el archivo en la ruta: {ruta}")
        
    # 2. Carga inmediata del CSV
    df = pd.read_csv(ruta)
    
    # 3. Validación de campos vacíos o nulos (NaN)
    if df.isna().any().any():
        raise ValueError("Error crítico: El archivo contiene campos vacíos o valores nulos (NaN).")
        
    # 4. Validar rangos lógicos (sin bucles)
    if (df['tiempo'] < 0).any():
        raise ValueError("Error crítico: Hay tiempos con valores negativos.")
        
    if (df['x'] < 0).any() or (df['x'] > 100).any():
        raise ValueError("Error crítico: Coordenadas X fuera del rango [0, 100].")
        
    if (df['y'] < 0).any() or (df['y'] > 100).any():
        raise ValueError("Error crítico: Coordenadas Y fuera del rango [0, 100].")
        
    # 5. Validar que la columna 'condicion' contenga solo valores válidos
    valores_validos = ["competencia", "cooperacion"]
    if not df['condicion'].isin(valores_validos).all():
        raise ValueError("Error crítico: El archivo contiene condiciones experimentales inválidas.")
        
    return df

    

    
    