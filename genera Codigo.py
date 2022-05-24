class Pila:
    arreglo = []
    def meter(self, dato):
        self.arreglo.append(dato)
    def sacar(self):
        if (len(self.arreglo)==0):
            print("Pila vacia")
        else:
            return self.arreglo.pop()

def esOperador(v):
    return (v in "*/+-")

def esSeparador(caracter):
    return caracter in " \n\t"

def esSimboloEsp(caracter):
    return caracter in "+-*;,.:!=%&/()[]{}<><=>=:="

def obtenerPrioridadOperador(o):
    # Función que trabaja con convertirInfijaA**.
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

def tokeniza(cad):
    tokens = []
    dentro = False
    token = ""
    for c in cad:
        if dentro:  #esta dentro del token
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
        else: #esta fuera del token
            if esSimboloEsp(c):
                tokens.append(c)
            elif esSeparador(c):
                a=0
            else:
                dentro = True
                token = c
                  
    return tokens

prog = "a*b*c+d+e+f*g*a "
tokens = tokeniza(prog)
posfija = infija2Posfija(tokens)


ct = 1
pila1 = Pila()
intermedio = []
codigo = []
for e in posfija:    
    if esOperador(e):
        op2 = pila1.sacar()
        op1 = pila1.sacar()
        cad = "t"+str(ct)+"="+op1+e+op2+";"
        intermedio.append(cad)
        print("LDA "+op1+";")
        if e=="+":
            print("ADD "+op2+";")
        elif e=="*":
            print("MUL "+op2+";")
        pila1.meter("t"+str(ct))
        print("STA "+ "t"+str(ct)+";")
        ct = ct + 1
    else:
        pila1.meter(e)
    
