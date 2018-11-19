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
    elif (cola[0]==0):
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
def menu():#Metodo menu es el menu del programa
    opc=int(input("\n\nCola Loca\n\n1.-Agregar Dato\n2.-Eliminar dato\n3.-Salir:"))
    if(opc==1):
        push(cola,c)
    elif(opc==2):
        pop()
    elif(opc==3):
        sys.exit()
menu()
