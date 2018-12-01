import random
arreglo=[]
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
for i in range(0,50):#este es el metodo for para crear los arreglos ramdom con 50 valores
    r=random.randint(1,100)
    arreglo.insert(i,r)
print("Arreglo original\n\n" + str(arreglo))#se imprime y el arreglo original, despues se llama al metodo merge con el arreglo y una vez terminada imprime el arreglo ordenado
merge(arreglo)
print("\n\nArreglo ordenado\n\n" + str(arreglo))