# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 18:50:50 2020

@author: nnico
"""

import cv2 as cv
import numpy as np
import glob
from random import sample

# Cambia al tamaño de la imagen
def cambio_tamano_porcentaje(image,scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    
    img = cv.resize(image, dim, interpolation = cv.INTER_AREA)
    return img

scale_percent = 10 # Porcentaje de cambio de tamaño de la imagen

img = cv.imread('1.jpg')
reducido = cambio_tamano_porcentaje(img,scale_percent)
    
cv.imshow('imagen original',img)
cv.imshow('imagen reducida',reducido)

cv.waitKey(0)
cv.destroyAllWindows()