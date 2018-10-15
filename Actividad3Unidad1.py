'''Declarando variable '''
c=1 
i=0
"""Metodo factorial recibe el contenedor del factorial y el contador asi como el factorial a calcular, i se aumenta cada vez que entra el cual sera el contador y c es el contenedor"""
def factorial(c,i,f):
    i=i+1
    c=i*c
    """se compara para que no se pase del factorial y se imprime y se vuelve a llamar hasta completar el factorial, ya terminado impreme que se ha termiando el el calculo"""
    if (i<=f):
       print(c)
       factorial(c,i,f) 
    else:
        print("Fin del calculo del factorial")
"""primer llamada del metodo factorial se manda los valores de c, i y f que es el factorial"""
f=int(input("Ingrese el valor del factorial a realizar "))
factorial(c,i,f)         
         
