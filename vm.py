#Tenemos 2 listas, 2 contadores, 1 diccionario y nuestro archivo que se va a leer.
from numpy import char


inst = []
param = []
pc = 0
ac = 0
memDatos = {}
archivo = open("prueba.txt", "r")

# En la primera parte del codigo se encarga de separar las instrucciones y los parametros con split(espacios).
# Para despues colocar las instrucciones en la lista inst y los parametros en la lista param.
for renglon in archivo:
    datos = renglon.split() 
    if (len(datos)>0):
        inst.append(datos[0]) #['LDV', 'STA', 'LDV', 'STA', 'LDV', 'STA', 'LDV', 'STA', 'LDA', 'SUB', 'JZ', 'LDA', 'MUL', 'ADD', 'STA', 'INC', 'JMP', 'END']
        param.append(datos[1][:-1]) #['1', 'a', '5', 'b', '2', 'd', '0', 'c', 'c', 'b', '17', 'a', 'd', 'd', 'a', 'c', '8', '0']
archivo.close()

#En la segunda parte de nuestro codigo, depende de la isntruccion(LDA,LDV,STA,DIV,MUL,SUB,ADD,JZ,JMP),
#el acumulador hara ciertas operaciones, hasta que encuentre en la lista la instruccion END(FIN).
#por ejemplo si la instruccion es ADD el acumulador sera igual al valor del acumulador actual mas
#el valor que se encuentra con la llave(param[pc]) en el diccionario. 
#La operacion que realiza el acumulador la indica la instruccion, una vez realizada, se le aumenta 1 al contador(pc)
while (inst[pc]!="END"):
    #Imprime nuesto pc(direccion), acumulador,instruccion, parametro
    print ("PC: ", pc, "  AC: ",ac," inst: ", inst[pc], "  parametro: ", param[pc]) 
    if (inst[pc]=="LDV"): #Carga en el acumulador un valor.
        ac = int(param[pc]) 
        pc = pc + 1
    elif (inst[pc]=="STA"): #Acumulador->Memoria
        memDatos[param[pc]] = ac 
        pc = pc + 1              
    elif (inst[pc]=="LDA"): #Memoria-> Acumulador
        ac = memDatos[param[pc]] 
        pc = pc + 1
    elif (inst[pc]=="ADD"): #Suma
        ac = ac + memDatos[param[pc]]       
        pc = pc + 1
    elif (inst[pc]=="SUB"): #Resta
        ac = ac - memDatos[param[pc]]       
        pc = pc + 1
    elif (inst[pc]=="MUL"): #Multiplica
        ac = ac * memDatos[param[pc]]
        pc = pc + 1
    elif (inst[pc]=="DIV"): #Divide 
        ac = ac / memDatos[param[pc]]
        pc = pc + 1
    elif (inst[pc]=="JZ"): # Salto condicional, Salta si es cero. Funciona como etiqueta.
        if (ac==0):
            pc = int(param[pc])
        else:
            pc = pc + 1    
    elif (inst[pc]=="JMP"): #Salto incodicional
        pc = int(param[pc])
    elif (inst[pc]=="INC"): #Incrementa en 1
        valor = memDatos[param[pc]]        
        valor = valor + 1
        memDatos[param[pc]] = valor        
        pc = pc + 1      
#Interrupciones
    elif (inst[pc]=="IN1"):#Lee int
        memDatos[param[pc]] = int(input("Da un valor int: "))
        pc = pc + 1  
    elif (inst[pc]=="IN2"):#Lee float
        memDatos[param[pc]] = float(input("Da un valor float: "))
        pc = pc + 1  
    elif (inst[pc]=="IN3"):#Lee char
        memDatos[param[pc]] = (input("Da una letra: "))
        pc = pc + 1  
    elif (inst[pc]=="IN4"):#Lee string
        memDatos[param[pc]] = (input("Da una cadena: "))
        pc = pc + 1  
    elif (inst[pc]=="IN5"):#Imprime
        print(memDatos[param[pc]])
        pc = pc + 1 