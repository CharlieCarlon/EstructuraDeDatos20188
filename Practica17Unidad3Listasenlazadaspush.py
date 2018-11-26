import sys
class Nodo:#"""Se crea la clase nodo y se inicia el metodo constructor"""
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
            
