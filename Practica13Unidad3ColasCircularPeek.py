cola=[0,0,0,0,0]#iniciamos las variable que utilizaremos
#index= 0 
pd=0
ud=0
import sys
def push():#Creamos el metodo push el cual recibe se declaran globales las variables pd y ud que seran los puinteros de la cola circular
    global pd
    global ud
    r=pd-ud#este es un operacion que nos dice la longitud entre los punteros si san uno estan lleno que es cuando los punteroes estan fuera del origen si es -4 es
    #cuando aun no se ah movido el puntero del primer digito que entro
    if (r==1)or(r==-4):#iniciamos revisando si la cola esta vacia o si esta llena si esta vacia le permite ingresar valores hasta que este llena y si se llena lo manda al menu
        print("La cola esta llena no puedes ingresar valores!!")
        menu()#si ambos indices dan 0 es por que la cola esta vacia asi que no se mueven los punteros pero si ingresan valores aqui
    elif (cola[ud]==0)&(cola[pd]==0):
        print("Cola Vacia Puedes ingresar valores")
    elif (ud<len(cola)-1):
        ud=ud+1#si el valor de ud es menor a la longitud del arregle se aumenta si no revisa que en el origen sea cero para poderse mover e imprimirse ahi el dato
    elif(cola[0]==0):
        ud=0
    dato=(int(input("Ingrese el dato a capturar en la cola:")))#una vez los punteros en su luger se capturan los datos en el array y se pregunta si desea continuar
    cola[ud]=dato# o termina de capturar datos
    print(cola)
    print(cola[ud])
    print(cola[pd])
    r=input("\nDesea agregar otro dato?[S/N] ")
    if (r=='S'):
        push()
    else:
        menu()
def pop():#Metodo pop revisa si la cola esta vacia para retornarla al menu si no elimina el primer valor ingresado de la cola y por medio de un for reimprime los valores
    global pd
    global ud
    if (cola[ud]==0)&(cola[pd]==0):
        print("\nLo cola esta vacia no se puede eliminar nada")
        menu()
    else:
        print("\nEliminando valor " + str(cola[pd]))
        cola[pd]=0
        if (pd<len(cola)-1) and (cola[pd+1]!=0):
            pd=pd+1
        elif(cola[0]!=0):
            pd=0
        else: 
            pop()
    print(cola)
    print(pd)
    print(ud)
    r=input("\nDesea eliminar otro dato?[S/N] ")
    if (r=='S'):
        pop()
    else:
        menu()

def peek():#metodo peek menu para saber que dese hacer en caso de una opcion no vvalida regresa al menu
    opc=int(input("\nQue desea hacer\n1.-Ver a toda la cola?\n2.-Desea ver a algun valor de la cola?\n3.-Mostrar el primer digito y el ultimo en entrar\n4.-Regresar :"))
    if(opc==1):
        print(cola)
        peek()
    else:
        if(opc==2):#en esta parte lee el valor a buscar y con un booleano revisa si se cumple la condicion que es encontrar el valor por medio de un while
            valor=int(input("\nIngrese el valor a buscar: "))
            found=False
            c=0
            while(c<=4):
                if(cola[c]==valor):
                    found=True#al encontrarse el valor sale e imprime el valor y el lugar, si no muestra el valor e imprime el msg de que no lo encontro y regresa al menu
                    break
                c=c+1
            if found:
                print("Dato "+ str(valor)+" esta en la posicion "+ str(c+1))
                peek()
            else:
                print("El Dato "+ str(valor)+" no se encuentra en la cola")
                peek()
        elif(opc==3):#imprime el primer y el ultimo digito en entrar a la cola circular
            print("Primer digito en entrar: "+ str(cola[pd]))
            print("Ultimo digito en entrar: " + str(cola[ud]))
            peek()
        elif(opc==4):
            menu()
        else:
            print("\nOpcion no valida, ingrese un valor valido")
            peek()
                    
    
def menu():#Metodo menu es el menu del programa
    opc=int(input("\n\nCola Loca\n\n1.-Agregar Dato\n2.-Eliminar dato\n3.-Ver la cola o buscar un dato\n4.-Salir:"))
    if(opc==1):
        push()
    elif(opc==2):
        pop()
    elif(opc==3):
        peek()
    elif(opc==4):
        sys.exit()
menu()
