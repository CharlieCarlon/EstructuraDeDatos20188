"""Instancia variables"""
n=0
i=2
c=0
"""Metodo elevar amuenta el contador y se compara si el exponente es cero para dar el resultado,
se hace la comparacion para que se repita hasta que sea igual al exponente y la i la multiplica por 2
una vez que salga del if manda a imprimir el resultado"""
def elevar(n,i,c):
    c=c+1
    if (n==0):
        print("El Resultado es igual a 1")
    else:
        if (n>0):
            if (c!=n):
                i=i*2
                elevar(n,i,c)
            else:
                if(c==n):
                    print("El resultado es:",i)
"""Lee el valor para poder mandarlo al metodo elevar el cual se llama despues de leer la variable"""
n=int(input("A que valor desea elevear el 2? "))
elevar(n,i,c)