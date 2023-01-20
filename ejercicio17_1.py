#17.1 Realizar operaciones de unión, intersección y diferencia  de conjuntos con tres conjuntos

#creamos tres conjuntos
conjunto_A= set({1,3,5,7,9,'Belgica'})
conjunto_B= set({2,4,6,8,10,'Alexa'})
conjunto_C= set({1,2,3,4,5,6,7,8,9,10})

# operacion union

resultado_Union = conjunto_A.union(conjunto_B,conjunto_C)
print(resultado_Union)
