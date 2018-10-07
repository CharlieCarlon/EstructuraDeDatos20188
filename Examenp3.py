"""Declaramos Variables e importamos la libreria sys"""
pilamig=[]
opc=0
import sys
"""Metodo push captura el rango de la pila y por medio de un for captura los datos en la pila
una vez termiando retorna al menu"""
def push():
    nummig = int(input("\nIngrese el numero de migraciones a capturar: "))
    for i in range(0 , nummig):
        migracion=int(input("\nIngrese la migracion "+ str(i+1)+":"))
        pilamig.append(migracion)
        i=i+1   
    menu()
    """Metodo peek compara si la pila esta vacia y ese es el caso lo retorna al menu
    si no por medio un for va imprimiendo los datos de mas nuevo al mas viejo comparando la longitud de la pila
    hasta cero para imprimirlo de manera correcta"""
def peek():
    if (len(pilamig)<=0):
        print("La pila esta vacia")
        menu()
    else:
        for i in range(len(pilamig),0,-1):
            print(pilamig[i-1])
        menu()
"""metodo menu dode se hace una condicion anidada para poder llamar al metodo que tiene cada opcion"""
def menu():
    opc=int(input("\n\nMigraciones Romero\n\n1.-Agregar Migraciones\n2.-Ver las migraciones\n3.-Salir :"))
    if(opc==1):
        
        push()
        menu()
      
    else:
        if(opc==2):
            peek()
        else:
            if(opc==3):
                 sys.exit()
            else:
                print("\nOpcion no valida, ingrese un valor valido")
                menu()
    
"""Mandar a llamar el menu"""
menu()