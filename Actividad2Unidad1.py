"""Iciciamos variables"""
n=0
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
        """Se guarda el limite del fibonacci y se manda a llamar el metodo impresion con los parametros i que es el limite y n el contador"""
i=int(input("Hasta que numero desea evaluar Fibonacci "))
impresion(i,n)
