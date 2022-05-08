
import csv
class registro():

    __temperatura=int
    __humedad=int
    __presion=int
    def __init__(self,temperatura=0,humedad=0,presion=0):
        self.__temperatura=temperatura
        self.__humedad=humedad
        self.__presion=presion

    def mostrarD(self):
        return (self.__temperatura,self.__presion,self.__humedad)
    def tem(self):
        p=int(self.__temperatura)
        return (p)
    def pre(self):
        return self.__presion
    def hu(self):
        return self.__humedad
    def __str__(self):
        return ("Temperatura:{}°C-Presion:{}Pa-Humedad:{}%".format(self.__temperatura,self.__presion,self.__humedad))




