from Registro import registro
import csv
class lista():
    __indice=[]
    def __init__(self):
        self.__indice=[]
    def agregar (self):
        archivo=open("Registro.csv","r")
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        dia=31
        hora=24
        for i in range(dia):
                self.__indice.append([0]*hora)
        for Fila in reader:
            if bandera==True:
                bandera=False
            else:
                dia=int (Fila[0])
                hora=int(Fila[1])
                unregistro=registro(Fila[2],Fila[3],Fila[4])
                self.__indice[dia][hora-1]=(unregistro)
        archivo.close()
    def opcion1(self):
        print ("Menor\n")
        self.__indice.mostrarD()
    def opcion2(self):
        temp=0
        co=0
        for i in range (len(self.__indice)):
            co=co+1
            for j in range (len(self.__indice[i])):
                temp=self.__indice[i][j].tem()+temp
                return (int(temp/co))

    def opcion3 (self,d):
        for i in range (len(self.__indice)):
            if (self.__indice[i][0]==d):
                for j in range (len (self.__indice[i])):
                    print (self.__indice[i][j])
            else:
                print ("Error")
    def mostrar(self):
        return (self.__indice())
