from Lista import lista
class menu():
    __lis=lista()
    def init (self):
        self.__va=None
    def manejador(self,op):
        self.__lis.agregar()
        if op==1:
            self.opcion1()
        elif op==2:
            self.opcion2()
        elif op==3:
            self.opcion3()
        elif op==5:
            self.opcion5()
    def opcion1(self):
        self.__lis.opcion1()
    def opcion2(self):
        print ("La temperatura promedio es:",self.__lis.opcion2())
    def opcion3(self):
        dia=int (input ("¿Que dia busca?\n"))
        self.__lis.opcion3(dia)
    def opcion5(self):
        print (self.__lis.mostrar())
