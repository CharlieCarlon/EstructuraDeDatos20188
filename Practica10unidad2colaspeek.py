#Metodo crear cola en ella declaramos la cola y le agregamos los valores de 0 lo cual significa valor nulo o que esta vacia
cola=[0,0,0,0,0]
dato = 0#iniciamos las variable que utilizaremos
index= 0  
c=1
import sys
def push(cola,c):#Creamos el metodo push el cual recibe los parametros de index c y cola   
    global index
    if (cola[4]!=0):#iniciamos revisando si la cola esta vacia o si esta llena si esta vacia le permite ingresar valores hasta que este llena y si se llena lo manda al menu
        print("La cola esta llena no puedes ingresar valores!!")
        menu()#busca inserta los datos en la cola y pregunta si gusta ingresar mas valores para volver a iniciar el ciclo
    elif (cola[0]==0)&(indice<len(cola)):
        print("La cola esta vacia puedes ingresar valores")
    dato=(int(input("Ingrese el dato a capturar en la cola:")))
    cola[index]=dato
    index=index+1
    r=input("\nDesea agregar otro dato?[S/N] ")
    if (r=='S'):
        push(cola,c)
    else:
        menu()
def pop():#Metodo pop revisa si la cola esta vacia para retornarla al menu si no elimina el primer valor ingresado de la cola y por medio de un for reimprime los valores
    global index#y ingresa el valor 0 en el indice que se quedo en el push para eliminar el valor y al finalizar disminuye el indice de uno en uno
    if (cola[0]==0):
        print("\nLo cola esta vacia no se puede eliminar nada")
        menu()
    else:  
        print("\nEliminando valor " + str(cola[0]))
        for i in range(0,len(cola)-1):
            cola[i] = cola[i+1]
        index=index-1#Se le pregunta el usuario si quiere eliminar otro elemento
        cola[index]=0
        r=input("\nDesea eliminar otro dato?[S/N] ")
        if (r=='S'):
             pop()
        else:
            menu()
            
def peek():#metodo peek menu para saber que dese hacer en caso de una opcion no vvalida regresa al menu
    opc=int(input("\nQue desea hacer\n1.-Ver a toda la cola?\n2.-Desea ver a algun valor de la cola?\n3.-Regresar :"))
    if(opc==1):
        print(cola)
        menu()
    else:
        if(opc==2):#en esta parte lee el valor a buscar y con un booleano revisa si se cumple la condicion que es encontrar el valor por medio de un while
            valor=int(input("\nIngrese el valor a buscar: "))
            found=False
            c=0
            while(c<=4):
                if(cola[c]==valor):
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
            
            
            
def menu():#Metodo menu es el menu del programa
    opc=int(input("\n\nCola Loca\n\n1.-Agregar Dato\n2.-Eliminar dato\n3.-Ver la cola o buscar un dato\n4.-Salir:"))
    if(opc==1):
        push(cola,c)
    elif(opc==2):
        pop()
    elif(opc==3):
        peek()
    elif(opc==4):
        sys.exit()
menu()
