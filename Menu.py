from Lista import lista
class menu():
    __lis=lista()
    def init (self):
        self.__va=None
    def inicializar(self):
        self.__lis.agregar()
    def manejador(self,op):

        if op==1:
            self.opcion1()
        elif op==2:
            self.opcion2()
        elif op==3:
            self.opcion3()
        else:
            print("Error")
    def opcion1(self):
        self.__lis.opcion1()
    def opcion2(self):
        self.__lis.opcion2()
    def opcion3(self):
        dia=int (input ("¿Que dia busca?\n"))
        self.__lis.opcion3(dia)
