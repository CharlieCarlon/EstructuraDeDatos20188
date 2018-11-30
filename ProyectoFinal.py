import random#declaro variables y agrego las librerias
import time
arreglo=[]
arregloRB=[]
arregloRQ=[]
arregloRS=[]
arregloRM=[]
arreglop=[]
c=1
j=0
change=False#estas condiciones booleanas son para el metodo shell
fin=True
salir=False
def captura():#metodo captura se ingresan las variables globales y se declaran las bariables promedio
    global b
    global q
    global m
    global s
    global tiempo
    global j
    promediob=0
    promedioq=0
    promedios=0
    promediom=0
    for i in range(j,30):#este for es el que correra todos los metodos las 30 veces requerrida para la tabulacion
        arreglo = []
        for k in range(0,50):
            r=random.randint(1,100)#este for va insertando numeros del 1 al 100 en el arreglo el limite son 50
            arreglo.insert(k,r)
        print("\n\nArreglo sin ordenar\n\n"+str(arreglo))
        
        b=arreglo[:]#una ves creado el arreglo desordenado se crea un arreglo que copiara el arreglo desordenado y empezara el contador del tiempo y manda a llamar el metodo que se va acontabilizar al terminar el metodo de ordenamiento
        print("\n\nMetodo de la Burbuja\n\n")#termina el conteo y guarda en un arreglo creado para cada metodo el tiempo que durara ordenando y despues imprime el arreglo ya ordenado por el metodo, esto lo realizan con todos los metodos
        tiempo=time.time()
        buble(c)
        tiempo=time.time()-tiempo
        arregloRB.append(tiempo)
        print(b)
        
        
        q=arreglo[:]
        print("\n\nMetodo Quicksort\n\n")
        tiempo=time.time()
        quicksort(q)
        tiempo=time.time()-tiempo
        arregloRQ.append(tiempo)
        print(q)
        
        m=arreglo[:]
        print("\n\nMetodo Merge\n\n")
        tiempo=time.time()
        merge(m)
        tiempo=time.time()-tiempo
        arregloRM.append(tiempo)
        print(m)
        
        s=arreglo[:]
        print("\n\nMetodo Shell\n\n")
        tiempo=time.time()
        shell(0,len(arreglo)//2)
        tiempo=time.time()-tiempo
        arregloRS.append(tiempo)
        change=False
        fin=True
        salir=False
        promediob=(promediob+arregloRB[i])#se guarda la posicion del arreglo i mas promedio arreglo que es igual a promedio arreglo esto se repite con cada uno de las variables promedio ya que es una para cada metodo
        promedioq=(promedioq+arregloRQ[i])
        promediom=(promediom+arregloRM[i])
        promedios=(promedios+arregloRS[i])
    arreglop.insert(0,promediob/30)#despues de terminar el for de los 30 guarda en un arreglo la suma de los promedios entre 30 para guardar en cada posicion el promedio de cada metodo diferente
    arreglop.insert(1,promedioq/30)
    arreglop.insert(2,promediob/30)
    arreglop.insert(0,promediob/30)
        
        

#Metodo de la burbuja
def buble(c):#metodo burbuja manda a recibe a cy l
    for i in range(0,len(b)-1):#se enlazan dos  y el primer for es el que va a ser el contador del otro for para que cuando se realizen cambios empieze de nuevo a ver si se cumplen las condiciones
        for i in range(0,len(b)-1):#este for es el que va a realizar los cambios y las condiciones son si arreglo indice i es mayor que arreglo indice c hacer el cambio
            if (b[i]>b[c]):#guarda el valor de arreglo indice c en una variable para realizar el cambio, arreglo indice c = arreglo indice i e indice i = a la 
                ii=b[c]#ii
                b[c]=b[i]
                b[i]=ii
            if(c==len(b)-1):#si c es = a lonngitud del arreglo, los valores se reinician c=1 y c=0 esto para que no rebase la longitud del mismo#en caso de que no pase
               c=1#simplemente los valores aumentan
               i=0
            else:
                c=c+1
                i=i+1
                
#Metodo QuickSort
def quicksort(arreglo):#metodo quicksort manda a llamar a el metodo recorrido
    recorrido(arreglo,0,len(arreglo)-1)#metodo recorrido recibe al arreglo y a los parametros de 0 y longitud del arreglo-1 que recibiran en el
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

#Metodo Shell
def shell(p,h):#el metodo recorrido recibe a p y a h, p es el puntero y h es la longitud del salto
    global s
    try:                    #Uso el try-except para evitar errores de Overflow
        global change
        global fin
        global salir
        salto=h#salto recibe a h y cambio sera igual a false
        while fin:                            #mientras cambio sea negativo while sera correra y dentro de el hay dos whiles
            while(s[p]<=s[salto]):      #si arreglo en el indice p es menor o igual a arreglo indice salto entrara esto es para hacer los recorrido de la lista
                p=p+1#al entrar aumentan el puntero y el salto en caso de que no haya habido ningun cambio y salto sea mayor a la longitud del arreglo y h sea mayor a 0
                salto=salto+1# se dividira el valor de h a la mitad y se llamara al metodo recorrido otra vez para que el valor de h cambio en  caso de que h sea igual a
                if(salto>len(s)-1)and(h//2>0)and not change:#1 y no hubo cambios durante el recorrido entonces ya estan ordenados todos los valores entonces imprime
                    h=h//2#el arreglo ordenado y cierra el programa si hubo un cambio entonces cambia la condicion a falsa para que entre el primer if y vuelve a llamar al
                    shell(0,h)#metodo sin cambiarle el valor a h
                elif(salto>len(s)-1)and(h==1)and not change and fin:
                    print(str(s))
                    fin=False
                elif(salto>len(s)-1)and change:
                    change=False
                    shell(0,h)
            if fin:
                while(s[p]>s[salto]):#en este while la condicion es la contraria y se realiza el metodo de reacomodo de los valores que hemos aplicado en los metodos
                    c=s[p]#de ordenamiento anteriores, y al acomodarlos aumenta al puntero y a el salto y la condicion de cambio se vuelve verdadera, este while tiene una condicion
                    s[p]=s[salto]#si salto es mayor que el arreglo y change es true el puntero regresa a 0 y salto vuelve a ser el valor de h
                    s[salto]=c
                    p=p+1
                    salto=salto+1
                    change=True
                    if(salto>len(s)-1)and change:
                        p=0
                        salto=h
    except:
        return -1            #Regreso un -1 indicando que ignore el error
                
                
#Metodo Merge                
def merge(arreglo):#metodo marge el el metodo padre el cual llamara a los otros del cual partiran los otros dos metodos, en este solo se recibe a el arreglo y se manda a
    division(arreglo,0,len(arreglo)-1)#a llamar al metodo division el cual recibira el arreglo, un valor en cero, y la longitud del arreglo, es el valor 0 es = al primer
def division(arreglo,pp,up):#puntero y la longitud al ultimo puntero dentro del metodo solo tenemos una condicion
    if pp<up:#si primer puentero es menor que ultimo puntero entonces declara a h como la suma de los dos punteros entre 2 esto para crear la primer division y al realizar
        h=(pp+up)//2#vuelve a llamarse al metodo division pero esta vez enviara al primer puntero y a h que es la division para asi crear las dovosiones de la primera parte
        division(arreglo,pp,h)#del arreglo y la segunda llamada de division es donde manda a la division +1 como parametro del primer puntero esto para crear las divisiones  
        division(arreglo,h+1,up)#en la segunda parte de la lista, una vez realizada las divisiones que se haya roto condicion del if podre entrar a la ultima llamada la cual 
        cambio(arreglo,pp,h,up)#es al metodo cambio en se van a combinar las divisiones de la primera y de la segunda parte del arreglo, por lo cual se envian los valores de
def cambio(arreglo,pp,h,up):#arreglo, primer puntero, h que es la division y ultimo puntero, esto mismo es lo que recibe el metodo cambio
    izq=arreglo[pp:h+1]#en este metodo se guardaran en la variable izq la parte del arreglo que va desde el primer puntero hasta la division +1 y en la varible derecha
    der=arreglo[h+1:up+1]#sera la division +1 hasta ultimo puintero mas 1 y se agregaran a esos arreglos creados dos valores como limte para que no se pase al momento de realizar
    izq.append(200)#las comparaciones
    der.append(200)
    cizq=cder=0#despues se crean los punteros para los dos mini arreglos los cual nos serviran para el intercambio de valores
    for i in range(pp,up+1):#entramos al for donde i ira desde el primer puntero hasya el ultimo +1 y al entrar tendremos la condicion de que, si arreglo izquierda en la
        if izq[cizq]<=der[cder]:#posicion contador izq es menor igual a arreglo derecha en la posicion contador der entonces se intercambian valores utilizando a i como puntero
            arreglo[i]=izq[cizq]#para guardar en el arreglo original en la posicion i el valor de arreglo izq en la posicion contador izq y aumenta al contador izq, si no se guarda
            cizq=cizq+1#el arreglo de la derecha en la posicion contador der en el arreglo en i y aumenta el contador der, esto se realiza hasta terminar con el for y asi se realiza
        else:# el intercambio de los datos
            arreglo[i]=der[cder]
            cder=cder+1
captura()#llamada del metodo e impresion de resultados
print("\n\nTiempos de la burbuja\n\n" +str(arregloRB)+"\n\n\nPromedio de tiempo burbuja " + str(arreglop[0]))
print("\n\nTiempos del Quicksort\n\n" +str(arregloRQ)+"\n\n\nPromedio de tiempo Quicksort " + str(arreglop[1]))
print("\n\nTiempos del Merge\n\n" +str(arregloRM)+"\n\n\nPromedio de tiempo Merge " + str(arreglop[2]))
print("\n\nTiempos del Shell\n\n" +str(arregloRS)+"\n\n\nPromedio de tiempo Shell " + str(arreglop[3]))
