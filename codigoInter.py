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


posfija=["a","b","*","c","d","*","+"]

ct=1
pila1=Pila()
p=[]
for e in posfija:
    if esOperador(e):
        op2=pila1.sacar()
        op1=pila1.sacar()
        cad="t"+str(ct)+"="+op1+e+op2+";"
        p.append(cad)
        pila1.meter(cad[0:2]) # pila1.meter("t"+str(ct))
        ct+=1
    else:
        pila1.meter(e)
print(p)