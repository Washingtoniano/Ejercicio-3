import Registro
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
        self.mostrarD()
        print ("Mayor\n")
        self.mostrarM()

    def opcion2(self):
        for i in range (len(self.__indice)):
            temp=0.0
            co=0
            for j in range (len(self.__indice[i])):
                if type(self.__indice[i][j])==Registro.registro:
                    co=co+1
                    temp=self.__indice[i][j].tem()+temp
            if co!=0:
                va=float(temp/co)
                print ("En el mes {} la temperatura promedio fue de {}°c".format(i,va))

    def opcion3 (self,d):
        for i in range (len(self.__indice[d])):
            print ("Dia:{}-Hora:{}".format(d,i+1))
            print (type(self.__indice[d][i]))
            print (self.__indice[d][i])
            #else:
              #  print ("Error")
    def mostrarD(self):
        minT=999999999999999
        minh=999999999999999
        minp=999999999999999
        for i in range(len(self.__indice)):
            for j in range(len(self.__indice[i])):
                if (type(self.__indice[i][j])==Registro.registro):
                    if (self.__indice[i][j].tem()<minT):
                            minT=self.__indice[i][j].tem()
                    if (self.__indice[i][j].hu()<minh):
                            minh=self.__indice[i][j].hu()
                    if (self.__indice[i][j].pre()<minp):
                            minp=self.__indice[i][j].pre()
        for j in range (len (self.__indice)):
            for a in range (len(self.__indice[j])):
                if (type(self.__indice[j][a])==Registro.registro):
                    if (self.__indice[j][a].tem()==minT):
                        print ("Dia de menor temperatura:{}\nHora de menor temperatura:{}\n".format(j,a+1))
                    if (self.__indice[j][a].hu()==minh):
                        print ("Dia de menor humedad:{}\nHora de menor humedad:{}\n".format(j,a+1))
                    if (self.__indice[j][a].pre()==minp):
                        print ("Dia de menor presion:{}\nHora de menor presion:{}\n".format(j,a+1))
    def mostrarM(self):
        maxT=0
        maxh=0
        maxp=0
        for i in range(len(self.__indice)):
            for j in range (len( self.__indice[i])):
                if (type(self.__indice[i][j])==Registro.registro):
                    if (self.__indice[i][j].tem()>maxT):
                        maxT=self.__indice[i][j].tem()
                    if (self.__indice[i][j].hu()>maxh):
                        maxh=self.__indice[i][j].hu()
                    if (self.__indice[i][j].pre()>maxp):
                        maxp=self.__indice[i][j].pre()
        for j in range (len (self.__indice)):
            for a in range (len(self.__indice[j])):
                if (type(self.__indice[j][a])==Registro.registro):
                    if (self.__indice[j][a].tem()==maxT):
                        print ("Dia de mayor temperatura:{}\nHora de mayor temperatura:{}\n".format(j,a+1))
                    elif (self.__indice[j][a].hu()==maxh):
                          print ("Dia de mayor humedad:{}\nHora de mayor humedad:{}\n".format(j,a+1))
                    elif (self.__indice[j][a].pre()==maxp):
                          print ("Dia de mayor presion:{}\nHora de mayor presion:{}\n".format(j,a+1))








