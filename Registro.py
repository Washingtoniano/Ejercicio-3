import csv
class registro():
    __dia=0
    __hora=0.0
    __temperatura=0
    __humedad:0
    __presion:0
    def __init__(self,dia,hora,temperatura,humedad,presion):
        self.__dia=dia
        self.__hora=hora
        self.__temperatura=temperatura
        self.__humedad=humedad
        self.__presion=presion
    def agregar(self):
        archivo=open("Registro.csv",'r')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for Fila in reader:
            if bandera==False:
                bandera=True
            else:
                self.__indice.append(Fila[0],Fila[1],Fila[2],Fila[3],Fila[4])



