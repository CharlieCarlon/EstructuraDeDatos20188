import random#importacion de libreria random y creacion de variable y del arrelgo
arreglo=[]
c=1

def buble(c):#metodo burbuja manda a recibe a cy l
    for i in range(0,len(arreglo)-1):#se enlazan dos  y el primer for es el que va a ser el contador del otro for para que cuando se realizen cambios empieze de nuevo a ver si se cumplen las condiciones
        for i in range(0,len(arreglo)-1):#este for es el que va a realizar los cambios y las condiciones son si arreglo indice i es mayor que arreglo indice c hacer el cambio
            if (arreglo[i]>arreglo[c]):#guarda el valor de arreglo indice c en una variable para realizar el cambio, arreglo indice c = arreglo indice i e indice i = a la 
                ii=arreglo[c]#ii
                arreglo[c]=arreglo[i]
                arreglo[i]=ii
            if(c==len(arreglo)-1):#si c es = a lonngitud del arreglo, los valores se reinician c=1 y c=0 esto para que no rebase la longitud del mismo#en caso de que no pase
               c=1#simplemente los valores aumentan
               i=0
            else:
                c=c+1
                i=i+1
    print("\n\nArreglo acomodado\n\n" + str(arreglo))
for i in range(0,50): #este for va insertando numeros del 1 al 100 en el arreglo el limite son 50
    r=random.randint(1,100)
    arreglo.insert(i,r)#al terminar de insertar se imprime el arreglo creado y se manda a llamar el metodo burbuja el cual recibe los parametros de c, l
print("Arreglo original\n\n " + str(arreglo))
buble(c)