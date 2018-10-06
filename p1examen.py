'''Declarando variable '''
n=0 
i=0
"""Metodo sumar recibe el contenedor de la suma y el contador """
def suma(n,i):
    i=i+1
    n=i+n
    """se compara para que no se pase del nueve y se repita hasta completar la suma"""
    if (i<9):
       suma(n,i) 
    else:
        print("El resultado de la sumatoria es:",n)
"""primer llamada del metodo sumar se manda los valores de n e i"""
suma(n,i)         
         
