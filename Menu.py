from Lista import lista
class menu():
    __lis=lista()
    def init (self):
        self.__va=None
    def manejador(self,op):
        if op==1:
            self.opcion1()
        elif op==2:
            self.opcion2()
        elif op==3:
            self.opcion3()
        else:
            print ("Error")
    def opcion1(self):
        self.__lis.opcion1()
   # def opcion2(self):
   # def opcion3(self):
