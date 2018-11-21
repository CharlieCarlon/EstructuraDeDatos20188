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
    elif (cola[ud]==0) &(cola[pd]==0):
        print("Cola Vacia Puedes ingresar valores")
    elif (ud<len(cola)-1):
        ud=ud+1#si el valor de ud es menor a la longitud del arregle se aumenta si no revisa que en el origen sea cero para poderse mover e imprimirse ahi el dato
    elif(cola[0]==0):
        ud=0
    dato=(int(input("Ingrese el dato a capturar en la cola:")))#una vez los punteros en su luger se capturan los datos en el array y se pregunta si desea continuar
    cola[ud]=dato# o termina de capturar datos
    print(cola)
    r=input("\nDesea agregar otro dato?[S/N] ")
    if (r=='S'):
        push()
    else:
        menu()
def pop():#Metodo pop revisa si la cola esta vacia con la misma condicion que manejamos  en el metodo push si esta vacio retorna al menu
    global pd
    global ud
    if (cola[ud]==0)&(cola[pd]==0):
        print("\nLo cola esta vacia no se puede eliminar nada")
        menu()
    else:#si no esta vacio cambia el valor a 0 en el arreglo e imprime la cola para que veas como esta quedando y comienza una nueva condicion
        print("\nEliminando valor " + str(cola[pd]))#si  pd es mayo a la longitud de la cola -1(4) y el siguiente valor de pd es direferente se pueda mover para
        cola[pd]=0# que no tenga problemas al momento de revisar la condicion si no al momento de moverse se adelantaria sin tener un numero entonces la condicion
        print(cola)#del push para saber si esta llena o no fallaria
        if (pd<len(cola)-1) and(cola[pd+1]!=0):
            pd=pd+1
        elif(cola[0]!=0):# en caso de que se pase de la longitud significa que esta en el ultimo lugar y si sigue deberia regresar al primer lugar (indice 0)
            pd=0#entoces se revisa para que no pase el mismo error y no se mueva sin tener un digito al cual moverse si diferente de 0 es por que se agrego un valor
        else: # y se puede mover en caso contrario vuele a llamar al metodo pop para que despliegue el msg que la cola esta vacia 
            pop()
    r=input("\nDesea eliminar otro dato?[S/N] ")#se realiza la misma pregunta para saber si quiere segui borrando datos
    if (r=='S'):
        pop()
    else:
        menu()
    
def menu():#Metodo menu es el menu del programa
    opc=int(input("\n\nCola Loca\n\n1.-Agregar Dato\n2.-Eliminar dato\n3.-Salir:"))
    if(opc==1):
        push()
    elif(opc==2):
        pop()
    elif(opc==3):
        sys.exit()
menu() 