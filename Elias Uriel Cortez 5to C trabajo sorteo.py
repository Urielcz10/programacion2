import random
#Lista vacia para los nombres de los estudiantes
nombres_estudiantes =[]
#Añadir los nombres de los estudiantes usando append ()
num_estudiantes =int(input("ingrese el numero de estudiantes:"))
for i in range(num_estudiantes):
    nombre =input("ingrese el nombre del estudiante {i+1}: ")
    nombres_estudiantes.append(nombre)
#Creo una lista vacia para el orden aleatorio
orden_aleatorio =[]
#Hago el orden aleatorio
for i in range(num_estudiantes):
    #Puse un indice aleatorio
    indice_aleatorio = random.randint(0,len(nombres_estudiantes) - 1)
    #Pongo el estudiante seleccionado a la lista orden_aleatorio
    orden_aleatorio.append(nombres_estudiantes[indice_aleatorio])
#Mostrar el orden en que deben pasar a exponer
print("El orden en que los estudiantes deben pasar a exponer es:")
for i in range(num_estudiantes):
    print(orden_aleatorio[i])
                               
                        