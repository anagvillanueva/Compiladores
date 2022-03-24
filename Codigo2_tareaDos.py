def entero(cad):
    cad = str(cad)
    digitos = "0123456789"
    todosNum = True #Suponemos que todos lo son 
    for c in cad: 
        if not (c in digitos): #Preguntamos para cada caracter, si se encuentra en digitos
            todosNum = False 
    return todosNum 

def flotante(cad):
    cad = str.lower(cad)
    encuentraF = cad.find(".") #Buscamos un punto 
    encuentraE = cad.find("e") #Buscamos una E 
    if (encuentraF == -1) or (encuentraE >= 0):
        return False
    else:
        return True
    
def exponencial(cad): #E ante y al final, . menor a e y - despues de e o en la posicion 0.
    cad = str.lower(cad) # Convertir en minuscula, en caso de que entre E 
    encuentraE = cad.find("e") #Buscamos una E 
    encuentraF = cad.find(".") #Buscamos un punto 
    encuentraM = cad.find("-") #Buscamos - para negativos
    if (encuentraE == -1) or (encuentraE==0) or (encuentraE==len(cad)-1)\
    or (encuentraF > encuentraE) or ((encuentraM != encuentraE+1) and (encuentraM != -1) and (encuentraM !=0)): 
        return False
    else:
        return True
    
    
   #Juntamos las funciones 
def numero(cad):
    if flotante(cad):
        return("Numero: Float")
    if entero(cad):
        return("Numero: Entero")
    elif flotante(cad):
        return("Float")
    elif exponencial(cad):
        return("Numero: Exponencial")
    else:
        return("Error")}
    
    