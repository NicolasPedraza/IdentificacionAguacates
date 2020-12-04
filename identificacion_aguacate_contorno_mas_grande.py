# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 19:07:32 2020

@author: nnico
"""

def identificacion_aguacate_contorno_mas_grande(nombre):
    import cv2 as cv
    img = cv.imread(nombre)
    imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    
    4
    # Encontrando por area mas grande
    cnt_area_grande = -1
    max_area = -1
    for i in range(len(contours)):
        area = cv.contourArea(contours[i])
        if area>max_area:
            cnt = contours[i] #Guarda el contorno mas grande
            max_area = area   #Guarda el area mas grande
            cnt_area_grande = i #Guarda el numero del contorno mas grande
            
    # Encontrando por perimetro mas grande
    cnt_perimetro_grande = -1
    max_perimeter = -1
    for i in range(len(contours)):
        perimeter = cv.arcLength(contours[i],True)
        if perimeter>max_perimeter:
            cnt = contours[i]
            max_perimeter = perimeter
            cnt_perimetro_grande = i
            
    # Si el contorno elegido es diferente para perimetro y area, se tiene como prioridad
    # el area debido a que el numero establecido es mas cercano
    if cnt_area_grande != cnt_perimetro_grande:
        cnt_perimetro_grande = cnt_area_grande
    
    cv.drawContours(img, contours, cnt_area_grande, (255,0,0), 3)
    #cv.drawContours(img, contours, cnt_perimetro_grande, (255,0,0), 3)
    
    print('Area Maxima Contorno:' + str(max_area))
    print('Perimetro Maxima Contorno:' + str(max_perimeter))
    
    cv.imshow('contornos',img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    
identificacion_aguacate_contorno_mas_grande('1_mask.jpg')