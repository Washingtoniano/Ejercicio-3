from Registro import registro
import csv
class lista():
    __indice=[[],[]]
    def __init__(self):
        self.__indice=[[],[]]
    def agregar (self):
        archivo=open("Registro.csv","r")
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for Fila in reader:
            if bandera==True:
                bandera=False
            else:
                dia=(Fila[0],Fila[1])
                unregistro=registro(Fila[2],Fila[3],Fila[4])
                for i in range (len(self.__indice)):
                    self.__indice[i].append (dia)
                    for j in range (len(self.__indice[i])):
                        self.__indice[i][j].append (unregistro)
            archivo.close()
    def opcion1(self):
        print ("Menor\n")
        mid=min(self.__indice[0][0])
        mih=min(self.__indice[0][1])
        for i in range (len(self.__indice)):
            for j in range (len (self.__indice[i])):
             if self.__indice[i][j]==mih and self.__indice[i][j]==mid:
               print (self.__indice[i][j])
        print ("Mayor\n")
    def opcion2(self):
        temp=0
        co=0
        for i in range (len(self.__indice)):
            co=co+1
            for j in range (len(self.__indice[i])):
                temp=self.__indice[i][j].tem()+temp
        return (int(temp/co))
    def opcion3 (self,d):
        for re in self.__indice[d]:
            print (re)




