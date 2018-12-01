#recibe la libreria random
import random
arreglo=[]#se crea el arreglo y se declaran los booleanos comofalsos
change=False
fin=True
salir=False
def recorrido(p,h):#el metodo recorrido recibe a p y a h, p es el puntero y h es la longitud del salto
    try:                    #Uso el try-except para evitar errores de Overflow
        global change
        global fin
        global salir
        salto=h#salto recibe a h y cambio sera igual a false
        while fin:                            #mientras cambio sea negativo while sera correra y dentro de el hay dos whiles
            while(arreglo[p]<=arreglo[salto]):      #si arreglo en el indice p es menor o igual a arreglo indice salto entrara esto es para hacer los recorrido de la lista
                p=p+1#al entrar aumentan el puntero y el salto en caso de que no haya habido ningun cambio y salto sea mayor a la longitud del arreglo y h sea mayor a 0
                salto=salto+1# se dividira el valor de h a la mitad y se llamara al metodo recorrido otra vez para que el valor de h cambio en  caso de que h sea igual a
                if(salto>len(arreglo)-1)and(h//2>0)and not change:#1 y no hubo cambios durante el recorrido entonces ya estan ordenados todos los valores entonces imprime
                    h=h//2#el arreglo ordenado y cierra el programa si hubo un cambio entonces cambia la condicion a falsa para que entre el primer if y vuelve a llamar al
                    recorrido(0,h)#metodo sin cambiarle el valor a h
                elif(salto>len(arreglo)-1)and(h==1)and not change and fin:                  
                    print("\n\nArreglo ordenado\n\n" + str(arreglo))
                    fin=False
                elif(salto>len(arreglo)-1)and change:
                    change=False
                    recorrido(0,h)
            if fin:
                while(arreglo[p]>arreglo[salto]):#en este while la condicion es la contraria y se realiza el metodo de reacomodo de los valores que hemos aplicado en los metodos
                    c=arreglo[p]#de ordenamiento anteriores, y al acomodarlos aumenta al puntero y a el salto y la condicion de cambio se vuelve verdadera, este while tiene una condicion
                    arreglo[p]=arreglo[salto]#si salto es mayor que el arreglo y change es true el puntero regresa a 0 y salto vuelve a ser el valor de h
                    arreglo[salto]=c
                    p=p+1
                    salto=salto+1
                    change=True
                    if(salto>len(arreglo)-1)and change:
                        p=0
                        salto=h
    except:
        return-1            #Regreso un -1 indicando que ignore el error
        
            
for i in range(0,50):#este for va insertando numeros del 1 al 100 en el arreglo el limite son 50
    r=random.randint(1,100)
    arreglo.insert(i,r)
print("Arreglo original\n\n" + str(arreglo))#al terminar de insertar se imprime el arreglo creado y se manda a llamar el metodo recorrido el cual recibe los parametros de 0, la longitud del arreglo a la mitad
recorrido(0,len(arreglo)//2)
print("\n\nArreglo ordenado\n\n" + str(arreglo))

