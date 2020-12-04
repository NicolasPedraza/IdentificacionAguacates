# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 18:52:27 2020

@author: nnico
"""

import cv2 as cv


# Identifica el contorno segun area y perimetro
def identificacion_aguacate_contornos(img,mask):
    imgray = mask
    #imgray = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    
    
    # Encontrando por area 
    cnt_area_grande = -1
    #max_area = -1
    for i in range(len(contours)):
        area = cv.contourArea(contours[i])
        if area>10000 and area <40000: # Area del aguacate
            #cnt_area = contours[i] #Guarda el contorno que corresponde al rango
            #max_area = area   #Guarda el area que corresponde al rango
            cnt_area_grande = i #Guarda el numero del contorno del aguacate
            
            
    # Encontrando por perimetro 
    cnt_perimetro_grande = -1
    #max_perimeter = -1
    for i in range(len(contours)):
        perimeter = cv.arcLength(contours[i],True)
        if perimeter>500 and perimeter <1800: #Perimetro aguacate
            #cnt_perimeter = contours[i] #Guarda el contorno que corresponde al rango
            #max_perimeter = perimeter #Guarda el perimetro que corresponde al rango
            cnt_perimetro_grande = i #Guarda el numero del contorno del aguacate
    
    
    # Si el contorno elegido es diferente para perimetro y area, se tiene como prioridad
    # el area debido a que el numero establecido es mas cercano
    if cnt_area_grande != cnt_perimetro_grande:
        cnt_perimetro_grande = cnt_area_grande
    
    # Se dibuja el contorno identificado
    cv.drawContours(img, contours, cnt_area_grande, (255,0,0), 3)
    #cv.drawContours(img, contours, cnt_perimetro_grande, (255,0,0), 3)
    
    
    cv.imshow('contorno_aguacate',img)
    cv.waitKey(0)
    cv.destroyAllWindows()