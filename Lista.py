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
                unregistro=registro()
                for i in range (len(self.__indice)):
                    for j in range (len(self.__indice[i])):
                        self.__indice[i][j].appen(unregistro(Fila[0],Fila[1],Fila[2],Fila[3],Fila[4]))
    def opcion1(self):
        print ("Menor\n")
        D=min(self.__indice[0])
        H=min(self.__indice[1])


