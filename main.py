from Menu import menu
if __name__ =="__main__":
    unmenu=menu()
    unmenu.inicializar()
    op=int (input ("1_Mostrar para cada variable el día y hora de menor y mayor valor.\n2_Indicar la temperatura promedio mensual por cada hora.\n3_Dado un número de día listar los valores de las tres variables para cada hora del día dado.\n4_Salir\n"))
    while op!=4 and op<6 and op>0:
        unmenu.manejador(op)
        op=int(input ("1_Mostrar para cada variable el día y hora de menor y mayor valor.\n2_Indicar la temperatura promedio mensual por cada hora.\n3_Dado un número de día listar los valores de las tres variables para cada hora del día dado.\n4_Salir\n"))
    print ("Adios")
