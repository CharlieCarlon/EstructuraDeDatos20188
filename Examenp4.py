"""Instaciando variables"""
colaclientes=[]
l=5
indice=0
opc=0
cliente=''
import sys
"""Metodo push compara que sea menor a la longitud para poder ingresar valores
se lee el cliente y se agrega, se aumenta el valor del indice y pregunta si quiere otro mas para volver a llamar el metodo
cuando se pase ya no se podra imprimir mas"""
def push(indice,l):
    if (indice<l):
        cliente=input("\nIngrese el nombre del cliente que va entrar a la lista:")
        colaclientes.append(cliente)
        indice=indice+1
        r=input("\nDesea agregar otro cliente?[S/N] ")
        if (r=='S'):
            push(indice,l)
        else:
            menu()
    else:
        print("\nLa fila esta llena regrese cuando algun cliente salga")
        menu()

    """Metodo peek menu donde selecciona imprimir toda la cola o por indice el indice lo lee y le resta uno ya que se toma desde 0"""
def peek(opc,indice):

    opc=int(input("\nQue desea hacer\n1.-Ver a todos los integrantes de la fila?\n2.-Desea ver a algun integrante de la fila segun su posicion\n3.-Regresar :"))
    if(opc==1):
        print(colaclientes)
        menu()
    else:
        if(opc==2):
            indice=int(input("\nIngrese la posicion que desea ver[1 al 5]: "))
            if (indice<=5 and indice>=1):
                indice=indice-1
                print(colaclientes[indice])
                peek(opc,indice)
                
            else:
                print("\nOpcion no valida, ingrese un valor valido")
                peek(opc,indice)
                
        else:
            if(opc==3):
                menu()
            else:
                print("\nOpcion no valida, ingrese un valor valido")
                peek(opc,indice)
    """Metodo pop se compara si la longitud es cero para saber si la cola esta vacia si no esta vacia elemina el primer elemento y reimprime la cola para que se recorran el penultimo elemento y sea el siguiente a borrar"""
def pop():
    if (len(colaclientes)<=0):
        print("\nLo fila esta vacia pueden entrar clientes")
        menu()
    else:
        print("\nAtendiendo cliente "+colaclientes[0])
        for i in range(0,len(colaclientes)-1):
            colaclientes[i] = colaclientes[i+1]
        del colaclientes[-1]
    """Metodo menu se compara la opcion para mandar a llamar el metodo correspondiente"""
def menu():
    opc=int(input("\n\nTienda Caralmi\n\n1.-Atender cliente\n2.-Dejar entrar un nuevo cliente\n3.-Clientes en la fila\n4.-Salir :"))
    if(opc==1):
        pop()
        menu()
    else:
        if(opc==2):
            push(indice,l)
        else:
            if(opc==3):
                peek(opc,indice)
            else:
                if(opc==4):
                    sys.exit()
                else:
                    print("\nOpcion no valida, ingrese un valor valido")
                    menu()
"""Mandar a llamar el menu"""
menu()
