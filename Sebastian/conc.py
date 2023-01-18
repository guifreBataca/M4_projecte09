#la suma de 2 variables
a = 5
b = 7
print(a + b)
#la suma de dos varibles dentro de un texto string
print(f"cuanto es 5 + 7: {a + b}")
#array
areas = ['cuina', 7.88, 'menjador', 13.0, 'terrassa', 20.34, 'lavabo', 6.55, 'habitació1', 7.98, 'habitació2', 12, 'rebedor', 4.23]
#imprimir el segundo elemento
print(areas[1])
#imprimir el último elemento
print(areas[-1])
#imprimir el área de la terrasa
print(areas[5])
#imprimir del primer elemento al tercer elemnto
for elementos in areas[:3]:
    print(elementos)
#imprimir del tercer elemento al último
print(areas[2:])
#imprimir el área de las 2 habitaciones
print(areas[9] + areas[11])
#Modificar el dato el lavabo y imprimir la nueva lista
areas[7] = 9
print(areas)
#Agrega el “pati interior” y 2.78 a las últimas posiciones
areas.append('pati interior')
areas.append(2.78)
print(areas)






