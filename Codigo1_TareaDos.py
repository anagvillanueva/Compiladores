# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 00:28:25 2022

@author: PC
"""

def entero(cad):
    cad = str(cad)
    digitos = "0123456789"
    todosNum = True #Suponemos que todos lo son 
    for c in cad: 
        if not (c in digitos): #Preguntamos para cada caracter, si se encuentra en digitos 
            todosNum = False 
    return todosNum 

def flotante(cad):
    cad = str(cad)
    encuentra = cad.find(".") #Buscamos un punto en nuestra cadena
    if encuentra is -1: 
        return False
    else:
        return True
    
def exponencial(cad):
    cad = str.lower(cad) #Convertinos a minusculas
    encuentra = cad.find("e") #Buscamos una e en nuestra cadena
    if encuentra is -1: 
        return False
    else:
        return True
    
#Problema: detecta el punto, y la e, en cualquier parte de la cadena (no importa si es inicio o fin)
   
def numero(cad):
    if entero(cad):
        return("Es un numero entero")
    elif flotante(cad):
        return("Es un numero float")
    elif exponencial(cad):
        return("Es un numero exponencial")