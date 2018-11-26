import sys
class Nodo(object):#"""Se crea la clase nodo y se inicia el metodo constructor"""
    def __init__(self,dato): #Se inicializan los campos del objeto
        self.dato=dato
        self.next=None
    
    def PushNodo(self,nodo):#Metodo push es el metodo el cual va a enlazar a los nodos unos con otros ademas muestra la lista que se esta creando
        global Raiz#declaramos las variables globales e igualamos a q con p para que q quede detras de ella siempre ya que en la siguiente linea se enlaza p.next al nodo creado
        global p#y despues p se iguala p a p.next, ahora entra la impresion de la lista p se iguala a raiz y se crea la variable lista que va aguardar los valores de los datos
        global q#para imprimirlos por medio de un while repite hasta que p sea none, si lo manejaba con .next nunca imprimia  el ultimo y lo tenia que imprimer fuera del while        
        q=p#de la manera actual es mas eficiente despues de guardar los valores se iguala p al p.next para el recorrido de la lista y al terminar se imprime toda la lista y
        p.next=nodo# con q.next que guardo a p en la posicion antes de estar en la raiz se refresa a la posicion que habia quedado guardada
        p=p.next
        q.next=p
        p=Raiz
        lista=" "
        print("\nLista actual")
        while(p!=None):
            lista=lista + "(" + str(p.dato)+ ") "            
            p=p.next
        print(lista)
        p=q.next
        
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
            p.next=None
            del p
            p=Raiz
            encontrado=True
            if(Raiz==None):#esta condicion es creada en caso de que la lista se haya borrado por completo y devuelva al menu
                print("La lista ah sido eliminada")
                menu()
            else:
                print("Se ha eliminado la raiz, la nueva Raiz es " + str(Raiz.dato))
            if(q.next==None):#esta condicion se creo en caso de que solo quedaran dos datos y se borre la raiz por que en el while recorre toda la lista para dejarla en la ultima posicion
                p=q            #pero en este caso no era necesario asi que solamente se mueve a q para dejar libre para poder ingresar mas datos                
                menu()
        elif(encontrado==False):#en caso de que ya haya borrado la raiz lo mande directo a acomodar los punteros para poder ingresar mas valores si no entra a buscar el
            while(p.dato!=dlt):#dato
                c=c+1
                q=p
                p.next=q.next
                p=p.next
                if(p==None):#si no se encuentra y ya paso por toda la lista cierra el ciclo y manda el msg e iguala a p con la q
                    print("El dato no se ha encontrado")
                    p=q
                    menu()
                    break
            if(p.next==None):#esta condicion es para saber si elimino el ultimo valor de la lista,ya que encontro el dato manda el msg y borra a p e iguala p con q
                q.next=None
                print("Se ha eliminado el dato " + str(p.dato)+ " del nodo "+ str(c))
                del p
                p=q
            else:#esta condicion es por si el dato estaba en alguna otra posicion, si no era el ultimo ni la raiz
                q.next=p.next
                p.next=None
                print("Se ha eliminado el dato " + str(p.dato)+ " del nodo "+ str(c))
                del p
                p=q.next
        while(p.next!=None):#este while acomoda los punteros para que haci queden bien para agregar mas valores
             q=p
             p.next=q.next
             p=p.next
        cont=Raiz#este ultimo es para imprimir la lista
        lista=" "
        print("\nLista actual")
        while(cont!=None):
            lista=lista + "(" + str(cont.dato)+ ") "            
            cont=cont.next
        print(lista)
        menu()
    
    
    def peek(self,nodos):#Metodo peek tiene un booleano el cual va a detectar cuando se encuentre el dato en el metodo se recibe el nodos, este va a servir para que en
        global Raiz#la variable search se guarde el dato que contenia y  por medio de esta buscar, en el while es un contador el cual contara el nodo en el que esta
        encontrado = False#despues de encontrarlo va a imprimir el dato y la posicion la variable p no afecta ya que no se declaro como global y el valor en el que quede
        search=nodos.dato#no afectara en otros metodos
        c=0
        p=Raiz
        while(p!= None):
            c=c+1
            if(p.dato==search):
                encontrado = True
                break
            if(p==None):
                break
            p = p.next
        if encontrado:
            print("Dato "+ str(search) + " en el nodo " + str(c))
        else:
            print("El dato "  +str(search)+ " no se encuentra en la lista")
        
Raiz=0
def menu():#en este metodo menu se realizan mas que en los otro metodos menu que habia, hecho ahora realiza una condicion en caso de que raiz sea 0 entonces se guardara ahi el primer
    global Raiz#valor de la lista y si no entonces ya hay una raiz declarada ahora guardara el valor en un nodo y llamara al metodo push que hara los enlaces correspondientes de la 
    global p#lista
    global q        
    opc=int(input("\n\nLista Loca\n\n1.-Agregar Datos\n2.-Borrar Datos\n3.-Buscar o ver\n4.-Salir :"))
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
    elif(opc==3):#en la opcion 3 es el peek pero como no podia llamar el metodo sin instanciarlo decidi dejar aqui las otras partes de el para que no afectara en el metodo
        opc=int(input("\nQue desea hacer\n1.-Ver a toda la lista?\n2.-Desea ver a algun valor de la lista?\n3.-Ver Raiz\n4.-Ver ultimo digito\n5.-Regresar :"))
        if(Raiz==0):# es un menu de las opciones que hay, en caso de que la raiz sea nula regresa al menu anterior, sino, imprime la lista con el metodo que ya se
            print("La lista no ah sido creada")#habia implementado en los otros dos metodos, en la opcion dos se hace los mismo que con el pop se guarda en un objeto
            menu()#el valor a buscar y se manda al metodo para poder ejecutarlo. En la opcion 3 se imprime la raiz y en la opcion 4 se recorre p para estar en el ultimo
        if(opc==1):#nodo y poder imprimirlo, y si no elige ninguna opcion lo regresa al menu inicial
            cont=Raiz
            lista=" "
            print("\nLista actual")
            while(cont!=None):
                lista=lista + "(" + str(cont.dato)+ ") "            
                cont=cont.next
            print(lista)
            menu()
        elif(opc==2):
            nodos=Nodo(int(input("Ingrese el dato a buscar: ")))
            nodos.peek(nodos)
        elif(opc==3):
            print("\n\nLa Raiz actual es: "+ str(Raiz.dato))
        elif(opc==4):
            while(p.next!=None):
                p=p.next
            print("\n\nUltimo dato de la lista es: "+str(p.dato))
        else:
            print("\nOpcion no valida, ingrese un valor valido")
        menu()
    elif(opc==4):
        sys.exit()

    else:
        print("\nOpcion no valida, ingrese un valor valido")
        menu()
        
menu()
       
