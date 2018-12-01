def busqueda():#metodo busqueda menu
    rep=True
    while rep:      #mientras rep sea verdadero entrara una y otra vez a buscar el dato del usuario
                valor=int(input("\nIngrese el valor a buscar: "))           #ingresa el valor a buscar entra a un while que no parara hasta que que llegue al limite del 
                found=False                                                 #del arreglo
                c=0
                while(c<=len(arreglo)-1):
                    if(arreglo[c]==valor):
                        found=True#al encontrarse el valor sale e imprime el valor y el lugar, si no muestra el valor e imprime el msg de que no lo encontro y regresa al menu
                        break
                    c=c+1
                if found:
                    print("Dato "+ str(valor)+" esta en la posicion "+ str(c+1))
                else:
                    print("El Dato "+ str(valor)+" no se encuentra en la cola")
                opc=input("Desea buscar otro valor?[S/N] ") #aqui se revalida la condicion del while inicial si la respuesta es S continua, si no el booleano cambia afalse y
                if opc=='S':        #sale del ciclo al salir imprime el msg de adios
                    rep=True
                else:
                    rep=False
    print("\n\nADIOS!!")
import random
arreglo=[]
def quicksort(arreglo):#metodo quicksort manda a llamar a el metodo recorrido
    recorrido(arreglo,0,len(arreglo)-1)#metodo recorrido recibe al arreglo y a los parametros de 0 y longitud del arreglo-1 que recibiran en el
    print("\n\nArreglo ordenado\n\n"+str(arreglo))
def recorrido(arreglo,p,u):#metodo como p de primer indice y u del ultimo indice
    if p<u:#si el primer indice es menor al segun llamara al metodo orden el cual genera el punto de particion del arreglo y ademas ordena
        pp=Orden(arreglo,p,u)#los valores, despues de haber guardado el splitpoint, volvera a llamar el arreglo recorrido pero esta vez el ultimo
        recorrido(arreglo,p,pp-1)#digito sera menor al punto de particion, para que empieze a acomodar del lado de los pequenines a los mas pequinos
        recorrido(arreglo,pp+1,u)#del puntero una vez acomo dados manda a el indice primero como 1 mas al punto de particion para esta vez acomodar a
def Orden(arreglo,p,u):#los mayores
    piv=arreglo[p]#en el metodo orden el metodo recibe el arreglo, primer indice y el ultimo, el pivote sera igual al primer digito del arreglo
    izq=p+1 #y se crearan dos punteros izq y derecha, derecha sera igual al primer digito +1 y le derecho sera igual que el ultimo, tambien
    der=u#declararemos un valor booleano que nos dara el break del while que se ejecutara para recorrer el arreglo y crear los puntos de particion
    punto=False#dentro del while mientra sea negativo el punto seguira dando vueltas y dentro del while tenemos otros dos los cuales seran
    while not punto:#los que ayuden a hacer los recorridos del arreglo
        while izq<=der and arreglo[izq]<= piv:#mientras que el puntero de la izquierda sea menor al puntero de la derecha y elvalor del arreglo
            izq=izq+1#en la posicion de el puntero de la izquierda es menor al valor del pivote se repite y aumenta el puntero de la izquierda
        while arreglo[der]>=piv and der>=izq:#si el valor del arreglo en la posicion del puntero derecha es mayo o igual al piv y puntero derecha
            der=der-1#es mayor igual al puntero izquierda derecha disminuye 1 osea es el recorrido original
        if der<izq:#en caso de que el puntedo derecha es menor al de la izquierda  se creal el punto y deja de ejecutarse el while
            punto=True
        else:#si no empieza a hacer el recorrido de los valores, el recorrido empieza una vez que salen de los 2 whiles que estan dentro de
            valor=arreglo[izq]#este ciclo, valor es una variable que guardara el valor del arreglo en el indice izquierda y luego el valor
            arreglo[izq]= arreglo[der]#del indice izquierda se cambiara con el valor del indice derecha y alfinal el valor del indice derecha
            arreglo[der]=valor#sera igual al valor previo del indice izq el cual se guardo en la variable valor
    valor=arreglo[p]#cuando cierra el while se hace otro recorrido ya que se encontro el punto de particion y valor es igual al valor del primer
    arreglo[p]=arreglo[der]#dato del arreglo,arreglo indice primero intercambia valores con el del indice derecho y el arreglo en el indice derecha
    arreglo[der]=valor#toma el valor del valor previo del arreglo en el primer indice
    return der#al final returna el puntero derecha
    
for i in range(0,50):
    r=random.randint(1,100)#este for va insertando numeros del 1 al 100 en el arreglo el limite son 50
    arreglo.insert(i,r)
print("Arreglo original\n\n" + str(arreglo))#al terminar de insertar se imprime el arreglo creado y se manda a llamar el metodo quicksort el cual recibe al arreglo 
quicksort(arreglo)
busqueda()