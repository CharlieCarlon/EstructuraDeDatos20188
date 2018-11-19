#Metodo crear cola en ella declaramos la cola y le agregamos los valores de 0 lo cual significa valor nulo o que esta vacia
cola=[0,0,0,0,0]
dato = 0#iniciamos las variable que utilizaremos
index= 0  
c=1
import sys
def push(index,cola,c):#Creamos el metodo push el cual recibe los parametros de index c y cola
    if (cola[4]!=0):#iniciamos revisando si la cola esta vacia o si esta llena si esta vacia le permite ingresar valores hasta que este llena y si se llena lo manda al menu
        print("La cola esta llena no puedes ingresar valores!!")
        menu()#busca inserta los datos en la cola y pregunta si gusta ingresar mas valores para volver a iniciar el ciclo
    elif (cola[0]==0):
        print("La cola esta vacia puedes ingresar valores")
    dato=(int(input("Ingrese el dato a capturar en la cola:")))
    cola.insert(index,dato)
    index=index+1
    r=input("\nDesea agregar otro dato?[S/N] ")
    if (r=='S'):
        push(index,cola,c)
    else:
        menu()
    
def menu():#Metodo menu es el menu del programa
    opc=int(input("\n\nCola Loca\n\n1.-Agregar Dato\n2.-Salir:"))
    if(opc==1):
        push(index,cola,c)
        menu()
    elif(opc==2):
        sys.exit()
menu()