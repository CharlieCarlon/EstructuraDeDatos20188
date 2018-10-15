"""Se inicializa las variables"""
i=0
"""Se crea el metodo suma el cual recibe al parametro i en esta metodo se aumenta en uno para poder desplegar 1 a 1 los valores hasta el 100
se hace una condicion para que mientras sea menor igual a 100 se imprima y se mande a llamar el metodo para aplicar recursividad"""
def suma(i):
    i=i+1    
        
    if (i<=100):
        print (i)
        suma(i)
    else:
        print("Se ha llegado al 100")
"""Se imprime el tituto y mandamos a llamar el metodo sume enviandole el parametro i"""
print("Numeros del 1 al 100")        
suma(i)