#17.1 Realizar operaciones de unión, intersección y diferencia  de conjuntos con tres conjuntos
'''en este programa haremos las operaciones con datos definidos
y tambien con datos introducidos por teclado'''
#creamos tres conjuntos
conjuntoA= set({1,3,5,'Belgica'})
conjuntoB= set({1,2,4,6,'Alexa'})
conjuntoC= set({1,2,3,4,5,6})
# operacion union
resultadoUnion = conjuntoA.union(conjuntoB,conjuntoC)
print("la union de los conjuntos es => ",resultadoUnion)
#operacion interseccion
resultadoInterseccion= conjuntoA.intersection(conjuntoB,conjuntoC)
print("La interseccion de los conjuntos es => ", resultadoInterseccion)
# operacion diferencia
resultadoDiferencia= conjuntoA.difference(conjuntoB,conjuntoC)
print("La diferencia entre los conjuntos es=> ",resultadoDiferencia)

#Mediante la entrada de datos por teclado
conjunto_A = set() #creamos un conjunto vacio para almacenar las entradas de datos
while True:    #ciclo para que el usuario introduzca la cantidad de datos que quiera
    valores_conjuntoA = input("Ingrese un valor para el conjunto_A o (ingrese 'exit' para salir) => ")
    if valores_conjuntoA == 'exit':   # para quee termine de introducir datos en ese conjunto
        break
    conjunto_A.add(valores_conjuntoA)  # agregamos los valores introducidos al conjunto vacio
print('Elementos del conjunto_A',conjunto_A)    #imprimir para visualizar los datos introducidos

# el conjunto_B y conjunto_C llevan los mismos pasos que el conjunto A
conjunto_B = set()
while True:
    valores_conjuntoB = input("Ingrese un valor para el conjunto_B o (ingrese 'exit' para salir) => ")
    if valores_conjuntoB == 'exit':
        break
    conjunto_B.add(valores_conjuntoB)
print('Elementos del conjunto_B',conjunto_B)#imprimir para visualizar los datos introducidos

conjunto_C = set()
while True:
    valores_conjuntoC = input("Ingrese un valor para el conjunto _C o (ingrese 'exit' para salir)=> ")
    if valores_conjuntoC == 'exit':
        break
    conjunto_C.add(valores_conjuntoC)
print('Elementos del conjunto_C',conjunto_C)#imprimir para visualizar los datos introducidos

#operacion union de conjunto mediante la entrada de datos por el usuario
resultado_Union = conjunto_A.union(conjunto_B,conjunto_C)
print('La union de el conjunto_A, conjunto_B y el conjunto_C es : ',resultado_Union)
#operacion interseeccion de conjunto mediante la entrada de datos por el usuario
resultado_Interseccion = conjunto_A.intersection(conjunto_B,conjunto_C)
print('La interseccion de los conjuntos es => ',resultado_Interseccion)
#operacion diferencia de conjunto mediante la entrada de datos por el usuario
resultado_Diferencia=conjunto_A.difference(conjunto_B,conjunto_C)
print('La diferencia entre los conjuntos es => ',resultado_Diferencia)
