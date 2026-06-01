#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 10:59:51 2026

@author: milagrosoteiza
"""
#app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from src.cargar_datos import cargar_datos
from src.metricas import calcular_hits_totales, calcular_tiempo_primer_hit
from src.procesamiento_datos import filtrar_por_participante

st.title("📊 MotionLab Dashboard")

archivo = st.file_uploader("Subí tu archivo CSV")

if archivo is not None:
    try:
        df = pd.read_csv(archivo, header=None)
        df.columns = ["id", "tiempo", "x", "y", "hit", "condicion"]

        # VALIDACIONES (reusás lógica)
        if df.isna().any().any():
            raise ValueError("El archivo tiene valores nulos")

        # KPIs
        hits = calcular_hits_totales(df)
        tiempo = calcular_tiempo_primer_hit(df)

        st.metric("Total Hits", hits)
        st.metric("Primer Hit (seg)", tiempo)
        
        # INPUT USUARIO
        id_participante = st.number_input("Ingresar ID participante", step=1)
        if id_participante:
            filtro = filtrar_por_participante(df, int(id_participante))

            if filtro is None:
                st.warning("Participante no encontrado")
            else:
                st.write(filtro.head())

            fig, ax = plt.subplots()
            filtro.groupby("condicion")["hit"].sum().plot(kind="bar", ax=ax)
            ax.set_title("Hits por condición")
            st.pyplot(fig)
            
    

        # INPUT USUARIO
        id_participante = st.number_input("Ingresar ID participante", step=1)

        if id_participante:
            filtro = filtrar_por_participante(df, int(id_participante))

            if filtro is None:
                st.warning("Participante no encontrado")
            else:
                st.write(filtro.head())

        # GRÁFICO
        fig, ax = plt.subplots()
        filtro.groupby("condicion")["hit"].sum().plot(kind="bar", ax=ax)

        ax.set_title("Hits por condición")
        st.pyplot(fig)

    except ValueError as e:
        st.error(f"Error: {e}")
    except Exception as e:
        st.error(f"Error inesperado: {e}")