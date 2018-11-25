pila=[0,0,0,0,0]#Creamos la pila y declaramos las variables del programa
import sys
index=0
def push():#metodo push recibe la variable inde, revisa que el indice sea menor a la longitud de la pila confirmado esto recibe el dato y reimprime el valor en el indice
    global index    
    if (index<len(pila))&(pila[index]==0):#actual despues de esto aumenta el indice si es mas grande no dejan capturar datos y despues pregunta si quieres ingresar mas datos o no
        dato=int(input("\nIngrese el dato "+ str(index+1)+":"))
        pila[index]=dato
        if(index==len(pila)-1):
            print(pila)
            print("La pila esta llena no se pueden agregar mas datos")
            menu()
        else:
            index=index+1#esta condicion se crea por que al entrar aumenta y al momento de querer  borrar un dato quedaba fuera de rango entonces se aumenta la pila no es igual
    else:#al la longitu de la cola menos uno, si es igual manda el msg de que la pila esta llena e imprime la pila
        print(pila)
        print("La pila esta llena no se pueden agregar mas datos")
        menu()
    r=input("\nDesea agregar otro dato?[S/N] ")
    if (r=='S'):
        push()
    else:
        menu()   
def pop():#En el metodo pop si la pila en la posicion 0 es 0 la pila esta vacia y regresa al menu, si no puede reimprimir los datos para que se vuelvan 0 e imprima la pila
    global index#si la pila en el indice 0 es igual a 0 no aumenta y sale del pop, si no, aumenta y pregunta si quiere volver a borrar otro numero para volver entrar al push
    if(pila[0]==0):
        print("La pila esta vacia no se puede borrar nada")
        menu()
    else:
        print("\nEliminando valor " + str(pila[index]))
        pila[index]=0
        print(pila)
        if(pila[0]!=0):
            index=index-1
        else:            
            print("La pila esta vacia no se puede borrar nada")
            menu()
    r=input("\nDesea borrar otro dato?[S/N] ")
    if (r=='S'):
        pop()
    else:
        menu()

def peek():#metodo peek menu para saber que dese hacer en caso de una opcion no vvalida regresa al menu
    opc=int(input("\nQue desea hacer\n1.-Ver a toda la pila?\n2.-Desea ver a algun valor de la pila?\n3.-Regresar :"))
    if(opc==1):
        print(pila)
        menu()
    else:
        if(opc==2):#en esta parte lee el valor a buscar y con un booleano revisa si se cumple la condicion que es encontrar el valor por medio de un while
            valor=int(input("\nIngrese el valor a buscar: "))
            found=False
            c=0
            while(c<len(pila)):
                if(pila[c]==valor):
                    found=True#al encontrarse el valor sale e imprime el valor y el lugar, si no muestra el valor e imprime el msg de que no lo entonctro y regresa al menu
                    break
                c=c+1
            if found:
                print("Dato "+ str(valor)+" esta en la posicion "+ str(c+1))
                menu()
            else:
                print("El Dato "+ str(valor)+" no se encuentra en la cola")
                menu()
        elif(opc==3):
            menu()
        else:
            print("\nOpcion no valida, ingrese un valor valido")
            peek()       


def menu():#Menu donde se manda a llamar el metodo push y la opcion salida si metio un numero invalido vuelve a abrir el menu
    opc=int(input("\n\nPila Loca\n\n1.-Agregar Datos\n2.-Borrar Dato\n3.-Ver pila o algun valor de la pila\n4.-Salir : "))
    if(opc==1):
            push()
      
    elif(opc==2):
            pop()
    elif(opc==3):
        peek()
    elif(opc==4):
        sys.exit()
        print("\nOpcion no valida, ingrese un valor valido")
        menu()
menu()


