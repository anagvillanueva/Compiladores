# Realice un compilador de una versión recortada de lenguaje “C”, el cual cuente con las siguientes 
# características:

class Variable: 
    nombre = ""
    tipo = ""
    valor= ""
    direccion= 0
    def __init__(self, n, t, v,d):
        self.nombre = n
        self.tipo = t
        self.valor = v
        self.direccion = d

# Al programa primero se le deben quitar los comentarios para que quede de la siguiente forma
def quitaComentarios(cad):
    estado ="Z"
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
    return cad2

#Separa en tokens
def esSeparador(caracter): 
    return caracter in " \n\t"

def esSimboloEsp(caracter):
    return caracter in "+-*;,.:!=%&/()[]{}<><=>=:="

def tokeniza(cad):
    tokens = []
    dentro = False
    token = ""
    for c in cad:
        if dentro: #esta dentro del token
            if esSeparador(c): 
                tokens.append(token)
                token = ""
                dentro = False
            elif esSimboloEsp(c):
                tokens.append(token)
                tokens.append(c)
                token = ""
                dentro = False
            else:
                token = token + c
        else: 
            if esSimboloEsp(c):
                tokens.append(c)
            elif esSeparador(c):
                a=0
            else:
                dentro = True
                token = c
    if token != '':
       tokens.append(token)
    return tokens

#Debe crear una tabla de variables donde vaya almacenando cada variable de la siguiente manera:
def estaEnTabla(nombreVar): 
    esta = False
    for v in tablaVar:
        if(v.nombre == nombreVar):
            esta = True
    return esta

def agregaVar(ren,c):
    tipos=["int","float","string","char"] #Tipos de datos
    datos = ren.split()
    nombreVar = datos[2][:-1]
    tipoVar = datos[1]
    vr=True
    if tipoVar in tipos:
        if estaEnTabla(nombreVar):
            print(f"Variable redeclarada! {nombreVar}")
            vr=False
        else:
            tablaVar.append(Variable(nombreVar, tipoVar, "0.0",c))
    else:
        print("Tipo de dato enexistente:", tipoVar)
        vr=False
    return vr

#Muestra nuestra tabla 
def muestraVar():
    print("nombre \t tipo \t valor \t direccion")
    for v in tablaVar:
        print(v.nombre,"\t",v.tipo,"\t",v.valor,"\t",v.direccion)
    pass

#Todos los “read”,“print”,“println” serán reemplazados por interrupciones.
def cambiaPR(cat):
    cad=tokeniza(cat)
    cad2 =""
    ct=0
    for c in cad:
        if (c=="read"):
            for n in cad:
                if estaEnTabla(n):
                    for v in tablaVar:
                        if (v.nombre == n):
                            if v.tipo == "float":
                                c="IN2"
                            elif v.tipo == "int":
                                c="IN1"
                            elif v.tipo == "string":
                                c="IN4"
                            elif v.tipo == "char":
                                c="IN3"
        elif (c=="print"):
            if ("," in cad):
                for a in cad:
                    ct+=1
                    if (cad[ct-1]==","):
                        if estaEnTabla(cad[ct]):
                            for v in tablaVar:
                                if (v.nombre == cad[ct]):
                                    if v.tipo == "float":
                                        c="IN6"
                                    elif v.tipo == "int":
                                        c="IN5"
                                    elif v.tipo == "string":
                                        c="IN8"
                                    elif v.tipo == "char":
                                        c="IN7"           
            else:
                c="IN9"

        elif (c=="println"):
            if ("," in cad):
                for a in cad:
                    ct+=1
                    if (cad[ct-1]==","):
                        if estaEnTabla(cad[ct]):
                            for v in tablaVar:
                                if (v.nombre == cad[ct]):
                                    if v.tipo == "float":
                                        c="IN6s"
                                    elif v.tipo == "int":
                                        c="IN5s"
                                    elif v.tipo == "string":
                                        c="IN8s"
                                    elif v.tipo == "char":
                                        c="IN7s"           
            else:
                c="IN9s"

        cad2 = cad2 + " " + c   
    return cad2

#Quita los () en print, println y read.
def ordenaEnsamblador(tok):
    l=["IN2","IN1","IN3","IN4"]
    p=["IN5","IN6","IN7","IN8", "IN5s","IN6s","IN7s","IN8s"]
    cad1=""
    a=""
    for c in tok:
        if tok[0]!="var":
            if (tok[0]=="IN9") or (tok[0]=="IN9s"):
                if (c==";"):
                    cad1= cad1 + c
                else:
                    cad1 = cad1 + " " + c
            elif (tok[0] in p):
                if (a==","):
                    for v in tablaVar:
                        if (v.nombre==c):
                            d=v.direccion
                            c=str(d)
                    cad1 = cad1 + " " + c
                elif (c==";"):
                    cad1= cad1 + c
                else:
                    cad1 = cad1 + " " + c
            for v in tablaVar:
                    if (v.nombre==c):
                        d=v.direccion
                        c=str(d)
            if (tok[0] in l):
                if (c!=")") and (c!="("):
                    if (c==";"):
                        cad1= cad1 + c
                    else:
                        cad1 = cad1 + " " + c 
            a=c
    return cad1[1:]
        


# Las asignaciones que involucren expresiones tales como: CODIGO INTERMEDIO
def esId(cad):
    return (cad[0] in "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

def obtenerPrioridadOperador(o): # Función que trabaja con convertirInfijaA**.
    return {'(':1, ')':2, '+': 3, '-': 3, '*': 4, '/':4, '^':5}.get(o)

def obtenerListaInfija(cadena_infija):
    if(type(cadena_infija) == list):
        return obtenerListaInfija("".join(cadena_infija))
    '''Devuelve una cadena en notación infija dividida por sus elementos.'''
    infija = []
    cad = ''
    for i in cadena_infija:
       if i in['+', '-', '*', '/', '(', ')', '^', '=']:
           if cad != '':
               infija.append(cad)
               cad = ''
           infija.append(i)
       elif i == chr(32): # Si es un espacio.
           cad = cad
       else:
           cad += i
    if cad != '':
       infija.append(cad)
    return infija

def infija2Posfija(expresion_infija):
    '''Convierte una expresión infija a una posfija, devolviendo una lista.'''
    infija = obtenerListaInfija(expresion_infija)
    pila = []
    salida = []
    for e in infija:
        if e == '(':
            pila.append(e)
        elif e == ')':
            while pila[len(pila) - 1 ] != '(':
                salida.append(pila.pop())
            pila.pop()
        elif e in ['+', '-', '*', '/', '^']:
            while (len(pila) != 0) and (obtenerPrioridadOperador(e)) <= obtenerPrioridadOperador(pila[len(pila) - 1]):
                salida.append(pila.pop())
            pila.append(e)
        else:
            salida.append(e)
    while len(pila) != 0:
        salida.append(pila.pop())
    return salida

#Marca error cuando falta un “;” 
def puntoComa(archivo):
    z=True
    d=0
    l=[]
    for ren in archivo:
        datos = quitaComentarios(ren)#1
        da=tokeniza(datos)
        d+=1
        if (da[-1]!=";") and (da[-1]!="{") and (da[-1]!="}") and (da[0]!="for") :
            z=False
            l.append(d)
    return z,l

#Esta expresión debe evaluarse con una pila para generar el código intermedio.
class Pila:
    arreglo = []
    def meter(self,dato):
        self.arreglo.append(dato)
    def sacar(self):
        if len(self.arreglo)==0:
            print("Pila vacia")
        else:
            return self.arreglo.pop()

def esOperador(v):
    return (v in "*/+-")

def codI(posfija):
    ct=1
    codigoIntermedio=[]
    pila1=Pila()
    for e in posfija:
        if esOperador(e):
            op2=pila1.sacar()
            op1=pila1.sacar()
            cad="t"+str(ct)+"="+op1+e+op2+";"
            codigoIntermedio.append(cad)
            pila1.meter(cad[0:2]) 
            ct+=1
        else:
            pila1.meter(e)
    return codigoIntermedio

#genera el CODIGO ENSAMBLADOR
def codE(posfija,segundap):#Cuando es exprecion.
    ct = 1
    pila1 = Pila()
    codigo=[]
    if (len(posfija)!=0):
        for e in posfija:    
            if esOperador(e):
                op2 = pila1.sacar() 
                op1 = pila1.sacar() 
                codigo.append("LDA "+op1+";")#CARGA
                if e=="+":
                    codigo.append("ADD "+op2+";")#SUMA
                elif e=="-":
                    codigo.append("SUB "+op2+";")#RESTA
                elif e=="*":
                    codigo.append("MUL "+op2+";")#MULTIPLICA
                elif e=="/":
                    codigo.append("DIV "+op2+";")#DIVIDE
                pila1.meter("t"+str(ct))
                
                if e is posfija[-1]:
                    codigo.append("STA "+segundap[-1][:1] +";")#TOMA
                else:
                    codigo.append("STA "+ "t"+str(ct)+";")#TOMA
                    ct = ct + 1
            else:
                pila1.meter(e)
    else:
        if (esId(segundap[2])):
            if (segundap[1]=="<"):#parte del for i<m
                codigo.append("LDA "+segundap[0]+";")#CARGA NUMERO
                codigo.append("SUB "+segundap[2]+";")#resta
            elif (segundap[1]==">"):
                codigo.append("LDA "+segundap[0]+";")#CARGA NUMERO
                codigo.append("ADD "+segundap[2]+";")#suma
            else:
                codigo.append("LDA "+segundap[2]+";")#CARGA VARIABLE
                codigo.append("STA "+segundap[0]+";")#GUARDA 
        else:
            if (segundap[1]=="<"):#parte del for i<10
                codigo.append("LDA "+segundap[0]+";")#CARGA NUMERO
                codigo.append("SUB "+segundap[2]+";")#resta
            elif (segundap[1]==">"):
                codigo.append("LDA "+segundap[0]+";")#CARGA NUMERO
                codigo.append("ADD "+segundap[2]+";")#suma
            else:
                codigo.append("LDV "+segundap[2]+";")#CARGA NUMERO
                codigo.append("STA "+segundap[0]+";")#GUARDA 

    return codigo

#Asigna el tipo de variable, en la parte del codigo intermedio. - t1 float 0.0 205 
def tipo(lista,c):#['t1=y2-y1;', 't2=x2-x1;', 't3=t1/t2;']
    for l in lista:
        li=tokeniza(l)
        for v in tablaVar:
            if (v.nombre == li[2]):
                a=v.tipo
            elif (v.nombre == li[4]):
                b=v.tipo
        ult=lista[-1]
        ul=tokeniza(ult)
        ex=0.0
        #enteros
        if (a=="int") and (li[3]=="*") and (b=="int") : # int * int = int multi
            if (li[0]==ul[2]) or (li[0]==ul[4]):
                tablaVar.append(Variable(li[0], "int", ex,c))
                c+=1

        elif (a=="int") and (b=="int") and (li[3]=="+"): # int + int = int suma
            if (li[0]==ul[2]) or (li[0]==ul[4]):
                tablaVar.append(Variable(li[0], "int", ex,c))
                c+=1
                
        elif (a=="int") and (b=="int") and (li[3]=="-"): # int - int = int menos
            if (li[0]==ul[2]) or (li[0]==ul[4]):
                tablaVar.append(Variable(li[0], "int", ex,c))
                c+=1      
                
        elif (a=="int") and (b=="int") and (li[3]=="/"): # int / int = float division
            if (li[0]==ul[2]) or (li[0]==ul[4]):
                tablaVar.append(Variable(li[0], "float", ex,c))
                c+=1
         
        #flotantes
        elif (a=="float") and (b=="float") and (li[3]=="*"): # float * float = float multi 
            if (li[0]==ul[2]) or (li[0]==ul[4]):
                tablaVar.append(Variable(li[0], "float", ex,c))
                c+=1

        elif (a=="float") and (b=="float") and (li[3]=="+"): # float + float = float suma
            if (li[0]==ul[2]) or (li[0]==ul[4]):
                tablaVar.append(Variable(li[0], "float", ex,c))
                c+=1
                
        elif (a=="float") and (b=="float") and (li[3]=="-"): # float - float = float resta
            if (li[0]==ul[2]) or (li[0]==ul[4]):
                tablaVar.append(Variable(li[0], "float", ex,c))
                c+=1
                
        elif (a=="float") and (b=="float") and (li[3]=="/"): # float / float = float 
            if (li[0]==ul[2]) or (li[0]==ul[4]):
                tablaVar.append(Variable(li[0], "float", ex,c))
                c+=1
                
          #int y float 
        elif (a=="int") and (b=="float") and (li[3]=="+"):# int + float = float suma 
            if (li[0]==ul[2]) or (li[0]==ul[4]):
                tablaVar.append(Variable(li[0], "float", ex,c))
                c+=1    
                
        elif (a=="float") and (b=="int") and (li[3]=="-"):# float + int = float suma 
            if (li[0]==ul[2]) or (li[0]==ul[4]):
                tablaVar.append(Variable(li[0], "float", ex,c))
                c+=1          
        else:
            if (li[0]==ul[2]) or (li[0]==ul[4]):
                tablaVar.append(Variable(li[0], "", ex,c))
                c+=1
    return c

def isfor(tok):
    b="var"+" int "+tok[2]+";"
    a=tok[2]+tok[3]+tok[4]+tok[5]#i=0;
    e=tok[6]+tok[7]+tok[8]+tok[9]#i<b;
    return b,a,e

    
#PRUEBA
tablaVar = []
segundaparte=[]#codigointermedio
terceraparte=[]#codigoensamblador
archivo = open("ansu.txt", "r")
instrucciones=["sin","cos","tan"]
indicacion=["IN2","IN1","IN3","IN4","IN9","IN5","IN6","IN7","IN8"]
contador=200
#Se ocupa dentro del for
j="" 
ansu=0
ans=0
#Marca error cuando falta un “;”
coma=puntoComa(archivo)

if (coma[0]==True):
    archivo = open("for.txt", "r")
    for ren in archivo:
        datos = quitaComentarios(ren)#1
        if (datos != "end;"):
            datos1 = cambiaPR(datos)#3
            tok = tokeniza(datos1)
            dt=ordenaEnsamblador(tok)
            if dt!="":
                terceraparte.append(dt)
            if (tok[0] == "var"):#2
                vr=agregaVar(datos,contador)
                contador+=1
                if vr==False:
                    break
            #for
            elif  (tok[0] == "for") or (tok[0] == "{") or \
                (tok[0] == "}") or (j[0]=="{"):#6
                if (tok[0] == "for"):
                    fr=isfor(tok)
                    agregaVar(fr[0],contador)
                    contador+=1
                    seguns = tokeniza(fr[1])
                    ters=tokeniza(fr[2])
                    if len(seguns)==4 and len(ters)==4 :
                        codigoEns= codE([],seguns)
                        for c in codigoEns:
                          terceraparte.append(c)
                        codigoEns= codE([],ters)
                        for c in codigoEns:
                          terceraparte.append(c)
                elif (tok[0] == "{"):
                    for i in terceraparte:
                        ansu+=1
                        ans+=1
                    terceraparte.append("JZ "+"0"+";")
                    ansu+=1
                elif (tok[0] == "}"):#termina instruccion dentro del for
                    terceraparte.append("JMP "+str(ans-1)+";")
                    ansu+=1
                    terceraparte.append("END "+"0"+";")
                    ansu+=1
                elif (tok[1]=="="):#4 
                        d= ren.split("=") #5
                        expresion=d[1][:-2]
                        posfija = infija2Posfija(expresion)
                        codigoInter= codI(posfija)
                        for c in codigoInter:
                            if (c==codigoInter[-1]):
                                j=c.split("=")
                                a=d[0].strip()+"="+j[1]#cambio t3 por m
                                segundaparte.append(a)
                            else:
                                segundaparte.append(c)
                        codigoEnsam= codE(posfija,segundaparte)
                        for c in codigoEnsam:
                            terceraparte.append(c)
                            ansu+=1
                        contador=tipo(codigoInter,contador)
                        terceraparte.append("INC "+fr[0][-2]+";")
                        ansu+=1

            elif (tok[1]=="=") and (j[0]!="{"):#4 
                if len(tok)==4:
                    codigoEn= codE([],tok)
                    for c in codigoEn:
                        terceraparte.append(c)
                else:
                    d= ren.split("=") #5
                    expresion=d[1][:-2]
                    posfija = infija2Posfija(expresion)
                    codigoInter= codI(posfija)
                    for c in codigoInter:
                        if (c==codigoInter[-1]):
                            j=c.split("=")
                            a=d[0].strip()+"="+j[1]#cambio t3 por m
                            segundaparte.append(a)
                        else:
                            segundaparte.append(c)
                    codigoEnsam= codE(posfija,segundaparte)
                    for c in codigoEnsam:
                        terceraparte.append(c)
                    contador=tipo(codigoInter,contador)
            elif  (tok[0] in instrucciones):#7 sin,cos,tan
                terceraparte.append(datos1)

            j=tok

else:
    print(f"Error falta ; en la linea {coma[1]}")
archivo.close()


codigoEnsamblador=open("codigoEnsamblador.txt","w") 
print("\tCODIGO INTERMEDIO")
for c in segundaparte:
    print(c) 
# print("\n\tCODIGO ENSAMBLADOR")
for f in terceraparte:
    k=f.split()
    if esId(k[1]):
        for v in tablaVar:
            if (v.nombre==k[1][:-1]):
                g=str(v.direccion)
                codigoEnsamblador.write(k[0]+" "+g+";"+"\n")
    elif (k[0] in instrucciones):
         for v in tablaVar:
            if (v.nombre==k[2]):
                g=str(v.direccion)
                codigoEnsamblador.write(k[0].upper()+" "+g+k[4]+"\n")    
    elif (k[0] in indicacion):
        codigoEnsamblador.write(f+"\n")
    elif (k[0][-1]=="s"):
        pln='\/n'
        codigoEnsamblador.write(k[0][:-1]+f[4:]+"\n")
        codigoEnsamblador.write('IN9 ( "'+pln[0]+pln[2]+'" );'+"\n")
    elif (k[0] in "JZ"):
        codigoEnsamblador.write(k[0]+" "+str(ansu)+k[1][-1]+"\n") 
    else:
        codigoEnsamblador.write(k[0]+" "+k[1]+"\n")
codigoEnsamblador.close()
print("\n\tTABLA DE VARIABLES")
muestraVar()