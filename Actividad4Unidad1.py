"""Se inicializa las variables"""
i=0
fi=0
s=0
n=0
c=1 
import sys
"""Se crea el metodo suma el cual recibe al parametro i en esta metodo se aumenta en uno para poder desplegar 1 a 1 los valores hasta el 100
se hace una condicion para que mientras sea menor igual a 100 se imprima y se mande a llamar el metodo para aplicar recursividad"""
def suma(s):
    s=s+1    
        
    if (s<=100):
        print (s)
        suma(s)
    else:
        print("Se ha llegado al 100")
        menu()
"""Metodo factorial recibe el contenedor del factorial y el contador asi como el factorial a calcular, i se aumenta cada vez que entra el cual sera el contador y c es el contenedor"""
def factorial(c,fi,f):
    fi=fi+1
    c=fi*c
    """se compara para que no se pase del factorial y se imprime y se vuelve a llamar hasta completar el factorial, ya terminado impreme que se ha termiando el el calculo"""
    if (fi<=f):
       print(c)
       factorial(c,fi,f) 
    else:
        print("Fin del calculo del factorial")
    menu()

"""Creamos la libreria cache esta va a guardar las llamadas a la fuuncion mas 
renciente para que no gaste tanto en memoria volviendo a llamar a la funcion"""
fibonacci_cache = {}
def fibonacci(n):
    """Se revisa si el valor esta guardado en nuestra libreria, si no calculamos el termino de n, esto es para que no tenga que volver a hacer la recursividad y que quede guardado en la libreria
    para que no gaste tantos recursos la maquina"""
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n==1: #Lo que hacemso es calcular el valor, guardarlo en la libreria y luego retornarlo, si el valor es 1 se retorna 1 si es dos lo mismo, sino aplicamos la recursividad restandole 1 y 2 a la suma
        value=1
    elif n == 2:
        value = 1
    elif n>2:
        value = fibonacci(n-1) + fibonacci(n-2)
    fibonacci_cache[n]=value#Se guarda el valor en la libreria y lo retornamos
    return value
    """Se creo un metodo para la impresion para no usar ciclos se aumenta el valor de n que sera un contador se crea una condicion para que sea menor al valor que entrega el usuario
    despues se emprime el metodo fibonacci y se manda el valor de n el cual aumenta cada vez que entramos en el metodo y al terminar se imprime que se ha terminado"""
def impresion(i,n):
    
    n=n+1
    if n<=i:
        print(fibonacci(n))
        impresion(i,n)
    else:
        print("Fibonacci finalizado")
    menu()        
       


def menu():
    opc=int(input("\n\nMenu Unidad 1\n\n1.-Suma del 1 al 100\n2.-Fibonacci\n3.-Factorial\n4.-Salir :"))
    if(opc==1):
        print("Numeros del 1 al 100") 
        suma(s)
    else:
        if(opc==2):
            """Se guarda el limite del fibonacci y se manda a llamar el metodo impresion con los parametros i que es el limite y n el contador"""
            i=int(input("Hasta que numero desea evaluar Fibonacci "))
            impresion(i,n)

        else:
            if(opc==3):
                """primer llamada del metodo factorial se manda los valores de c, i y f que es el factorial"""
                f=int(input("Ingrese el valor del factorial a realizar "))
                factorial(c,fi,f) 
            else:
                if(opc==4):
                    sys.exit()
                else:
                    print("\nOpcion no valida, ingrese un valor valido")
                    menu()
"""Mandar a llamar el menu"""
menu()
