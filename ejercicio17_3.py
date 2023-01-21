#17.3 Calcular la diferencia simétrica entre 2 conjuntos
''' a diferencia simétrica entre dos conjuntos A y B es un conjunto con los
 elementos que están en A o en B pero no en ambos'''

 #crendo el conjunto A
conjunto_A = set() #cconjunto vacio para despues almacenar en ella los datos obtenidos por teclado
while True:    #ciclo para que el usuario introduzca la cantidad de datos que desee
    valores_conjuntoA = input("Ingrese un valor para el conjunto_A o (ingrese 'exit' para termianar de introducir )=> ")
    if valores_conjuntoA == 'exit':   # para quee termine de introducir datos en ese conjunto
        break
    conjunto_A.add(valores_conjuntoA)  # agregamos los valores introducidos al conjunto vacio
print('Elementos del conjunto_A: ',conjunto_A)    #imprimir para visualizar los datos introducidos
#creando el conjunto B
conjunto_B = set()      #cconjunto vacio para despues almacenar en ella los datos obtenidos por teclado
while True:             #ciclo para que el usuario introduzca la cantidad de datos que desee
    valores_conjuntoB = input("Ingrese un valor para el conjunto_B o (ingrese 'exit' para terminar de introducir)=> ")
    if valores_conjuntoB == 'exit':               # para quee termine de introducir datos en ese conjunto
        break
    conjunto_B.add(valores_conjuntoB)             # agregamos los valores introducidos al conjunto vacio
print('Elementos del conjunto_B: ',conjunto_B)    #imprimir para visualizar los datos introducidos

# LA diferencia simetrica entre dos conjuntos
diferenciaSimetrica=conjunto_A.symmetric_difference(conjunto_B)
print("La diferencia simetrica  entre el conjunto_A y el conjunto_B es => ", diferenciaSimetrica)