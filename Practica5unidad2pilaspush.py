pila=[0,0,0,0,0]#Creamos la pila y declaramos las variables del programa
import sys
index=0
def push(index):#metodo push recibe la variable inde, revisa que el indice sea menor a la longitud de la pila confirmado esto recibe el dato y reimprime el valor en el indice
    if (index<len(pila)):#actual despues de esto aumenta el indice si es mas grande no dejan capturar datos y despues pregunta si quieres ingresar mas datos o no
        dato=int(input("\nIngrese el dato "+ str(index+1)+":"))
        pila[index]=dato
        print(pila)        
        index=index+1
    else:
        print("La pila esta llena no se pueden agregar mas datos")
        menu()
    r=input("\nDesea agregar otro dato?[S/N] ")
    if (r=='S'):
        push(index)
    else:
        menu()   

def menu():#Menu donde se manda a llamar el metodo push y la opcion salida si metio un numero invalido vuelve a abrir el menu
    opc=int(input("\n\nPila Loca\n\n1.-Agregar Datos\n2.-Salir :"))
    if(opc==1):
            push(index)
      
    elif(opc==2):
            sys.exit()
    else:
        print("\nOpcion no valida, ingrese un valor valido")
        menu()
menu()
