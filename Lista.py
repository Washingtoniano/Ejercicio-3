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
                co=co+1
                temp=self.__indice[i][j].tem()+temp
            va=float(temp/co)
            print ("En el mes {} la temperatura fue de {}°c".format(i,va))

    def opcion3 (self,d):
        for i in range (len(self.__indice[d])):
            print (self.__indice[d][i])
            #else:
              #  print ("Error")
    def mostrarD(self):
        minT=999999999999999
        minh=999999999999999
        minp=999999999999999
        for i in range(len(self.__indice)):
            for j in range(len(self.__indice[i])):
                if (self.__indice[i][j].tem()<minT):
                    minT=self.__indice[i][j].tem()
                elif (self.__indice[i][j].hu()<minh):
                    minh=self.__indice[i][j].hu()
                elif (self.__indice[i][j].pre()<minp):
                    minp=self.__indice[i][j].pre()
        for j in range (len (self.__indice)):
            for a in range (len(self.__indice[j])):
                if (self.__indice[j][a].tem()==minT):
                    print ("Dia de menor temperatura{}\nHora de menor temperatura\n{}".format(j,a+1))
                elif (self.__indice[j][a].hu()==minh):
                    print ("Dia de menor humedad{}\nHora de menor humedad\n{}".format(j,a+1))
                elif (self.__indice[j][a].pre()==minp):
                    print ("Dia de menor presion{}\nHora de menor presion\n{}".format(j,a+1))
    def mostrarM(self):
        minT=0
        minh=0
        minp=0
        for i in range(len(self.__indice)):
            for registro in self.__indice[i]:
                tem=(registro.tem())
                hu=(registro.hu())
                pre=(registro.pre())
                if (tem>minT and hu>minh and pre>minp):
                    minh=hu
                    minp=pre
                    minT=tem
        for j in range (len (self.__indice)):
            for a in range (len(self.__indice[j])):
                if (self.__indice[j][a].tem()==minT):
                    print ("Dia de mayor temperatura{}\nHora de mayor temperatura\n{}".format(j,a+1))
                elif (self.__indice[j][a].hu()==minh):
                      print ("Dia de mayor humedad{}\nHora de mayor humedad\n{}".format(j,a+1))
                elif (self.__indice[j][a].pre()==minp):
                      print ("Dia de mayor presion{}\nHora de mayor presion\n{}".format(j,a+1))








