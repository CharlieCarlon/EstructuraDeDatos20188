import sys
class Nodo(object):#"""Se crea la clase nodo y se inicia el metodo constructor"""
    def __init__(self,dato): #Se inicializan los campos del objeto
        self.dato=dato
        self.next=None
        self.prev=None

    def PushNodo(self,nodo):#Metodo push es el metodo el cual va a enlazar a los nodos unos con otros ademas muestra la lista que se esta creando
        global Raiz#declaramos las variables globales e igualamos a q con p para que q quede detras de ella siempre ya que en la siguiente linea se enlaza p.next al nodo creado
        global p#y despues p se iguala p a p.next, ahora entra la impresion de la lista p se iguala a raiz y se crea la variable lista que va aguardar los valores de los datos
        global q#para imprimirlos por medio de un while repite hasta que p sea none, si lo manejaba con .next nunca imprimia  el ultimo y lo tenia que imprimer fuera del while 
        q=p
        p.next=nodo
        p=p.next
        if(p.prev==None)and(q.prev==None):
            p.prev=Raiz
            q.prev=Raiz
        else:
            p.prev=q            
            q.prev=q
        q.next=p
        cont=Raiz#este ultimo es para imprimir la lista, como se va a quedar uno antes de guardarlo al salir lo vuelvo a guardar para que al imprimirlo muestre tambien
        lista=" "#la raiz que esta conectada a la p
        print("\nLista actual")
        while(cont!=None):
            lista=lista + "(" + str(cont.dato)+ ") "            
            cont=cont.next
        print(lista)
          
    def pop(self,nodob):#Clase pop recibe el objeto nodob que guarda el nodo a borrar, el dato del nodo se guarda en una variable con la cual vamos a comparar para 
        global Raiz#encontrar y borrar los datos elegidos por el usuario
        global p
        global q
        encontrado=False
        dlt=nodob.dato
        print("\nBuscando dato ", dlt, "para eliminar")
        c=1
        p=Raiz
        q=Raiz
        if(Raiz==0):#si la raiz es nula significa que la lista no ha sido creada y le manda un mensaje y lo manda al menu
            print("La lista no ah sido creada")
            menu()
        elif(Raiz.dato==dlt):#si el dato de la raiz es igual al delete significa que va a dejar a p en la raiz y movera a q una posicion adelante para eliminar a p y 
            q=p.next#mover la raiz a q y despues mover a la ultima posicion, al final imprime la nueva raiz
            Raiz=q
            p.next=None#Prev y next son igualados a none para que no tenga ninguna liga
            p.prev=None
            del p
            p=Raiz
            encontrado=True
            if(Raiz==None):#esta condicion es creada en caso de que la lista se haya borrado por completo y devuelva al menu
                print("La lista ah sido eliminada")
                menu()
            else:
                q.prev=Raiz#se mueve q.prev a la raiz y se pone aqui por que solo se puede mover si la raiz tiene dato si no no lo recibe por que prev no recibe nulls
                print("Se ha eliminado la raiz, la nueva Raiz es " + str(Raiz.dato))
            if(q.next==None):#esta condicion se creo en caso de que solo quedaran dos datos y se borre la raiz por que en el while recorre toda la lista para dejarla en la ultima posicion
                p=q            #pero en este caso no era necesario asi que solamente se mueve a q para dejar libre para poder ingresar mas datos                
                p.prev=q.prev                
                menu()
        elif(encontrado==False):#en caso de que ya haya borrado la raiz lo mande directo a acomodar los punteros para poder ingresar mas valores si no entra a buscar el
            while(p.dato!=dlt):#dato
                c=c+1
                q=p
                p.next=q.next
                p=p.next
                p.prev=q
                q.prev=q
                if(p==None):#si no se encuentra y ya paso por toda la lista cierra el ciclo y manda el msg e iguala a p con la q
                    print("El dato no se ha encontrado")
                    p=q
                    menu()
                    break
            if(p.next==None):#esta condicion es para saber si elimino el ultimo valor de la lista,ya que encontro el dato manda el msg y borra a p e iguala p con q
                q.next=None
                q.prev=None
                print("Se ha eliminado el dato " + str(p.dato)+ " del nodo "+ str(c))
                del p
                p=q
            else:#esta condicion es por si el dato estaba en alguna otra posicion, si no era el ultimo ni la raiz
                q.next=p.next
                q.prev=q
                p.next=None
                p.prev=None
                print("Se ha eliminado el dato " + str(p.dato)+ " del nodo "+ str(c))
                del p
                p=q.next
                p.prev=q
        
        while(p.next!=None):#este while acomoda los punteros para que haci queden bien para agregar mas valores
             q=p
             p.next=q.next
             p=p.next
             p.prev=q
             q.prev=q
        cont=Raiz#este ultimo es para imprimir la lista, como se va a quedar uno antes de guardarlo al salir lo vuelvo a guardar para que al imprimirlo muestre tambien
        lista=" "#la raiz que esta conectada a la p
        print("\nLista actual")
        while(cont!=None):
            lista=lista + "(" + str(cont.dato)+ ") "            
            cont=cont.next
        print(lista)
        menu()
        
Raiz=0
def menu():#en este metodo menu se realizan mas que en los otro metodos menu que habia, hecho ahora realiza una condicion en caso de que raiz sea 0 entonces se guardara ahi el primer
    global Raiz#valor de la lista y si no entonces ya hay una raiz declarada ahora guardara el valor en un nodo y llamara al metodo push que hara los enlaces correspondientes de la 
    global p#lista
    global q        
    opc=int(input("\n\nLista Loca\n\n1.-Agregar Datos\n2.-Borrar Datos\n3.-Salir :"))
    if(opc==1):    
        if (Raiz==0)or(Raiz==None):#si la raiz es 0 o ah sido eliminado entra para generar una nueva raiz
            Raiz=nodo=Nodo(int(input("Ingrese el dato a guardar: ")))
            print("La Raiz actual es: "+ str(Raiz.dato))
            p=Raiz
            q=Raiz
        else:
            nodo=Nodo(int(input("Ingrese el dato a guardar: ")))
            nodo.PushNodo(nodo)
        menu()
    elif(opc==2):#guarda en un nodo el dato a borrar y por medio del objeto manda a llamar el metodo pop el cual recibe al objeto
        nodob=Nodo(int(input("Ingrese el dato a eliminar: ")))
        nodob.pop(nodob)
    elif(opc==3):    
        sys.exit()

    else:
        print("\nOpcion no valida, ingrese un valor valido")
        menu()
        
menu()