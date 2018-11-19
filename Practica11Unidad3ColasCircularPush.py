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
    elif (ud<len(cola)):
        ud=ud+1#si el valor de ud es menor a la longitud del arregle se aumenta si no revisa que en el origen sea cero para poderse mover e imprimirse ahi el dato
    elif(cola[0]==0):
        ud=0
    dato=(int(input("Ingrese el dato a capturar en la cola:")))#una vez los punteros en su luger se capturan los datos en el array y se pregunta si desea continuar
    cola[ud]=dato# o termina de capturar datos
    r=input("\nDesea agregar otro dato?[S/N] ")
    if (r=='S'):
        push()
    else:
        menu()
    
def menu():#Metodo menu es el menu del programa   
    opc=int(input("\n\nCola Circular Loca\n\n1.-Agregar Dato\n2.-Salir:"))
    if(opc==1):
        push()
        menu()
    elif(opc==2):
        sys.exit()
menu() 