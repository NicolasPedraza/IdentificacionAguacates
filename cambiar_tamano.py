# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 18:50:50 2020

@author: nnico
"""

import cv2 as cv

# Cambia al tamaño de la imagen
def cambio_tamano_porcentaje(image,scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    
    img = cv.resize(image, dim, interpolation = cv.INTER_AREA)
    return img