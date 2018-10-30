class Nodo():#"""Se crea la clase nodo y se inicia el metodo constructor"""
    def __init__(self,dato): #Se inicializan los campos del objeto
        self.dato=dato
        self.next=None
        self.prev=None
    

    def peek():#Metodo peek se manda p a la raiz y recorre toda la lista para ir imprimiendo los datos de los nodos se detiene al encontrar que su enlace siguiente es none y se  imprime el ultimo valor por que ese no lo toma dentro del while
        global Raiz#lo mismo se hace para imprimir de derecha a izquierda pero aplicando el parametro prev y lee un dato para que inicie la siguiente parte del examen
        p=Raiz
        print("Imprime de izquierda a derecha")
        while(p.next!=None):
            print(p.dato)
            p=p.next
        print(p.dato)
        print("Imprime de derecha a izquierda")
        while(p!=Raiz):
            print(p.dato)
            p=p.prev
        print(p.dato)
        Readkey=(str(input("Presione cualquier tecla para continuar")))
        
    def crearlista():#se crea la lista y se inicializan las variable con un for imprime los valores del 1 al 9 y se guardan en los nodos
        global Raiz
        global p
        global q
        for i in range(1,10,1):   
            nodo=Nodo(i)          
            if (i==1):
                Raiz=Nodo(i)
                p=Raiz
                q=Raiz
            else:
                q=p
                p=nodo
                p.prev=q            
                q.next=p    
        
    
    def PushNodo():#se crean los 3 nodos con los tres valores a  ingresar y se realizan los enlaces correspondientes para no perder los datos
        global Raiz
        global p
        global q
        nodo=Nodo(10)
        p=nodo
        p.prev=q            
        q.next=p
        q=p
        nodo=Nodo(11)
        p=nodo
        p.prev=q            
        q.next=p
        q=p
        nodo=Nodo(13)
        p=nodo
        p.prev=q            
        q.next=p
        q=p
        
    def LeerRF(): #Se recorre la lista enlazada hasta llegar a la raiz para imprimirla, tambien recorre hasta el final para mostrar el ultimo dato 
        global Raiz
        global p
        global q
        while(p!=Raiz):
            p=p.prev
        print("Raiz: ",p.dato)
        while(p.next!=None):
            p=p.next
        print("Ultimo dato del lado derecho",p.dato)
    def Eliminar():#BUsca los valores igualando mandando los punteros al inicio y con un while va buscando el valor a eliminar, para decir que nodo se elimina se usa un contador y al final busca los valores para poder imprimirlos
        global Raiz
        global p
        global q
        c=1
        p=Raiz
        q=Raiz
        while(p.dato!=8):
            c=c+1
            p=p.next
            p.prev=q
            q.next=p
            q=p
        q.next=p.next
        p.next.prev=q
        del p
        print("Se ha eliminado el dato 8 del nodo ",c)
        p=Raiz
        q=Raiz
        p=p.next
        p.prev=None
        Raiz=p
        del q
        q=Raiz
        print("Se ha eliminado el dato 1 del nodo Raiz ")
        print("La nueva raiz es ", Raiz.dato)
    def buscar(item):#EL metodo devuelve la posicion y el valor a buscar si no lo encuentra muestra el dato que no encontro
        global Raiz
        encontrado = False
        global p
        global q
        c=1
        p=Raiz
        q=Raiz
        while(p.next != None):
            c=c+1
            if(p.dato==item):
                encontrado = True
                break
            p = p.next
        if encontrado:
            print("Dato "+ str(item) + " en el nodo " + str(c))
        else:
            print("El dato "  +str(item)+ " no se encuentra en la lista")

        #Se llaman los metodos para que se ejecuten    

Nodo.crearlista()
Nodo.peek()
Nodo.PushNodo()
Nodo.Eliminar()
Nodo.LeerRF()
Nodo.buscar(0) 
Nodo.buscar(7)
Nodo.buscar(8)
Nodo.buscar(1) 

