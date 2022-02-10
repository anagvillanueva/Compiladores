# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:59:38 2022

@author: PC
"""
# estados: A, B, C, Z
estado ="Z"

cad = "main(){ /*inicio*/ \n int a; /*se declara a*/"
#cad = "a=b/c;"
cad2 =""

for c in cad:
    if (estado=="Z"):
        if (c=="/"):
            estado = "A"
        else:
            cad2 = cad2 + c
    elif (estado=="A"):
        if (c=="*"):
            estado="B"
        else:
            estado = "Z"
            cad2=cad2+"/"+c
    elif (estado=="B"):
        if (c=="*"):
            estado = "C"
    elif(estado=="C"):
        if (c=="/"):
            estado="Z"
        else:
            estado="B"

print(cad)
print()
print(cad2)