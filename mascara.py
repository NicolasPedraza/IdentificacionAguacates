# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 18:51:52 2020

@author: nnico
"""
import cv2 as cv
import numpy as np
import glob
from random import sample


# Aplica la mascara de bordes segun color
def mascara(img):
    blurred_frame = cv.GaussianBlur(img, (5, 5), 0)
    hsv = cv.cvtColor(blurred_frame, cv.COLOR_BGR2HSV)
    lower_blue = np.array([38, 86, 0])
    upper_blue = np.array([121, 255, 255])
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    return mask

img = cv.imread('1_reducido.jpg')
mask = mascara(img)

cv.imshow('imagen original',img)
cv.imshow('imagen reducida',mask)

cv.waitKey(0)
cv.destroyAllWindows()