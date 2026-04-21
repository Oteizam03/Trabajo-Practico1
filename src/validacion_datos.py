#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:23:25 2026

@author: milagrosoteiza
"""

def validar_registro(registro: dict):
    try:
        int(registro["id_participante"])
        float(registro["tiempo"])
        float(registro["x"])
        float(registro["y"])
        
        if registro["tiempo"] < 0:
            return False
        
        if registro["x"] < 0 or registro["x"] > 100:
            return False
    
        if registro["y"] < 0 or registro["y"] > 100:
            return False

        if registro["hit"] != True and registro["hit"] != False:
            return False


        return True

    except:
        return False
    
    
