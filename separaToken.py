def esSeparador(c):
    separadores = "\n\t "
    return c in separadores

def esSimboloEsp(c):
    especiales = "¡#$%&/*+-=:;[]{}(),"
    return c in especiales

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

def tokeniza(cad):
    tokens=[]
    dentro = False
    token = ""
    for c in cad:
        if dentro:#esta dentro del token
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
                # print(c)
            elif esSeparador(c):
                a=0
            else:
                dentro = True
                token = c
    return tokens

cad = "main(){\nint var1, var2; /* declara variables*/\n"\
    "var1=38;\nvar2=6;\nvar1 = var1+ var2;\n}\n"
print("Programa Original")
print(cad)
cad=quitaComentarios(cad)
print("Programa sin comentarios")
print(cad)
tokens = tokeniza(cad)
print(tokens)