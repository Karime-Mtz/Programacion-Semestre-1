Con el objetivo de usar operadores, cambié un poco el propósito de mi proyecto. Ahora en vez de formar parejas 
para los combates, este programa llevará un conteo de la cantidad de participantes dentro de la competencia, al igual que
la cantidad de personas que se encuentran en cada una de las categorías de peso (ligero, welter y pesado). De esta forma,
se podrá tener un mejor control y manejo de la información cuando haya competencias.

El algoritmo está dividido en partes y todavía no es completamente funcional.

#Entrada inicial - datos del competidor(nombre, sexo, peso)

nombre = input("¿Cuál es tu nombre? ")
sexo = input("¿Cuál es tu sexo? ")
peso = float(input("¿Cuál es tu peso? "))


#Creación de listas:
participantes_mujeres = []
participantes_hombres = []
ligero_m = []
ligero_h = []
welter_m = []
welter_h = []
pesado_m = []
pesado_h = []

capacidad_max = 50


#Agregar elementos a listas:
#Operadores: ==, >=, <=, and
  #todavía no funciona el if ni el loop

Mientras x sea menor que capacidad_max

si sexo == "mujer":
  agregar(nombre) a participantes_mujeres
else:
  agregar(nombre) a participantes_hombres

si sexo == "mujer": 
  si peso < 68:
    agregar(peso) a ligero_m
  sino peso >= 68 and peso < 80:
    agregar(peso) a welter_m
  sino peso >= 80:
    agregar(peso) a pesado_m

sino sexo == "hombre":
  si peso < 68:
    agregar(peso) a ligero_h
  sino peso >= 68 and peso < 80:
    agregar (peso) a welter_h
  sino peso >= 80:
    agregar(peso) a pesado_h

x = x+1

#Cantidad de elementos en las listas
#operador de suma
num_mujeres = len(participantes_mujeres)
num_hombres = len(participantes_hombres)
num_participantes = num_mujeres + num_hombres

num_ligero_m = len(ligero_m)
num_ligero_h = len(ligero_h)
num_ligero_total = num_ligero_m + num_ligero_h

num_welter_m = len(welter_m)
num_welter_h = len(welter_h)
num_welter_total = num_welter_m + num_welter_h

num_pesado_m = len(pesado_m)
num_pesado_h = len(pesado_h)
num_pesado_total = num_pesado_m + num_pesado_h

#Salida
EF (num_participantes, num_ligero_total, num_welter_total, nun_pesado_total)
