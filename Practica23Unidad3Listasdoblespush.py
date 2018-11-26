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
            q.next=p
        q.next=p
        cont=Raiz#este ultimo es para imprimir la lista, como se va a quedar uno antes de guardarlo al salir lo vuelvo a guardar para que al imprimirlo muestre tambien
        lista=" "#la raiz que esta conectada a la p
        print("\nLista actual")
        while(cont!=None):
            lista=lista + "(" + str(cont.dato)+ ") "            
            cont=cont.next
        print(lista)
          
Raiz=0
def menu():#en este metodo menu se realizan mas que en los otro metodos menu que habia, hecho ahora realiza una condicion en caso de que raiz sea 0 entonces se guardara ahi el primer
    global Raiz#valor de la lista y si no entonces ya hay una raiz declarada ahora guardara el valor en un nodo y llamara al metodo push que hara los enlaces correspondientes de la 
    global p#lista
    global q        
    opc=int(input("\n\nLista Loca\n\n1.-Agregar Datos\n2.-Salir :"))
    if(opc==1):    
        if (Raiz==0):
            Raiz=nodo=Nodo(int(input("Ingrese el dato a guardar: ")))
            print("La Raiz actual es: "+ str(Raiz.dato))
            p=Raiz
            q=Raiz
        else:
            nodo=Nodo(int(input("Ingrese el dato a guardar: ")))
            nodo.PushNodo(nodo)
        menu()
    elif(opc==2):
        sys.exit()
    else:
        print("\nOpcion no valida, ingrese un valor valido")
        menu()
        
menu()
