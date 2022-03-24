inst = []
param = []
pc = 0
ac = 0
memDatos = {}
archivo = open("programa2.txt", "r")
for renglon in archivo:
    datos = renglon.split()
    if (len(datos)>0):
        inst.append(datos[0])
        param.append(datos[1][:-1])
archivo.close()

while (inst[pc]!="END"):
    print ("PC: ", pc, "  AC: ",ac," inst: ", inst[pc], "  parametro: ", param[pc]) 
    if (inst[pc]=="LDV"):
        ac = int(param[pc])
        pc = pc + 1
    elif (inst[pc]=="STA"):
        memDatos[param[pc]] = ac
        pc = pc + 1
    elif (inst[pc]=="LDA"):
        ac = memDatos[param[pc]]
        pc = pc + 1
    elif (inst[pc]=="ADD"):
        ac = ac + memDatos[param[pc]]       
        pc = pc + 1
    elif (inst[pc]=="SUB"):
        ac = ac - memDatos[param[pc]]       
        pc = pc + 1
    elif (inst[pc]=="MUL"):
        ac = ac * memDatos[param[pc]]
        pc = pc + 1
    elif (inst[pc]=="DIV"):
        ac = ac / memDatos[param[pc]]
        pc = pc + 1
    elif (inst[pc]=="JZ"):
        if (ac==0):
            pc = int(param[pc])
        else:
            pc = pc + 1    
    elif (inst[pc]=="JMP"):
        pc = int(param[pc])
    elif (inst[pc]=="INC"):
        valor = memDatos[param[pc]]        
        valor = valor + 1
        memDatos[param[pc]] = valor        
        pc = pc + 1  
