#Declaro una matriz de 5 por 5 llena de ceros
matriz = [[0 for _ in range(5)] for _ in range(5)]
#Lleno la matriz con numeros enteros sucesivos
num = 1
for i in range(5):
    for j in range(5):
        matriz[i][j] = num
        num += 1
#Muestro la matriz terminada
print("matriz terminada:")
for fila in matriz:
    print(fila)
#Calculo la suma y la multiplicacion de todos los numeros de la matriz
suma_total = 0
multiplicacion_total = 1
for i in range(5):
    for j in range(5):
        suma_total += matriz[i][j]
        multiplicacion_total *= matriz[i][j]
#Ahora muestro la suma y la multiplicacion
print("suma de todos los elementos:", suma_total)
print("multiplicacion de todos los elementos:", multiplicacion_total)
