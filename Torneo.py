#Entrada inicial - datos del competidor(nombre, sexo, peso)

def datos_participante():
  a = input("¿Cuál es tu nombre? ")
  b = input("¿Cuál es tu sexo? (mujer/hombre) ").lower()
  c = float(input("¿Cuál es tu peso? "))
  return a,b,c

nombre, sexo, peso = datos_participante()
print(nombre, sexo, peso)


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

#Funciones para calcular cantidad de participantes

def cantidad_mujeres():
  num_mujeres = len(participantes_mujeres)
  return num_mujeres

def cantidad_hombres():
  num_hombres = len(participantes_hombres)
  return num_hombres

def cantidad_participantes():
  num_participantes = cantidad_mujeres() + cantidad_hombres()
  return num_participantes


#Funciones para calcular cantidad de personas en cada categoría

def cantidad_ligero_m():
  num_ligero_m = len(ligero_m)
  return num_ligero_m

def cantidad_ligero_h():
  num_ligero_h = len(ligero_h)
  return num_ligero_h

def cantidad_ligero_total():
  num_ligero_total = cantidad_ligero_m() + cantidad_ligero_h()
  return num_ligero_total

def cantidad_welter_m():
  num_welter_m = len(welter_m)
  return num_welter_m

def cantidad_welter_h():
  num_welter_h = len(welter_h)
  return num_welter_h

def cantidad_welter_total():
  num_welter_total = cantidad_welter_m() + cantidad_welter_h()
  return num_welter_total

def cantidad_pesado_m():
  num_pesado_m = len(pesado_m)
  return num_pesado_m

def cantidad_pesado_h():
  num_pesado_h = len(pesado_h)
  return num_pesado_h

def cantidad_pesado_total():
  num_pesado_total = cantidad_pesado_m() + cantidad_pesado_h()
  return num_pesado_total

#Funciones para calcular número de combates

def parejas(cantidad):
  return cantidad() // 2

def parejas_ligero_m():
  return parejas(cantidad_ligero_m)

def parejas_welter_m():
  return parejas(cantidad_welter_m)

def parejas_pesado_m():
  return parejas(cantidad_pesado_m)

def combates_mujeres():
  num_combate_m = parejas_ligero_m() + parejas_welter_m() + parejas_pesado_m()
  return num_combate_m

def parejas_ligero_h():
  return parejas(cantidad_ligero_h)

def parejas_welter_h():
  return parejas(cantidad_welter_h)

def parejas_pesado_h():
  return parejas(cantidad_pesado_h)

def combates_hombres():
  num_combate_h = parejas_ligero_h() + parejas_welter_h() + parejas_pesado_h()
  return num_combate_h

def combates_totales():
  num_combates_total = combates_mujeres() + combates_hombres()
  return num_combates_total

#Funciones para calcular el porcentaje de mujeres y hombres en la competencia

def porcentaje_mujeres():
  porcentaje_m = (cantidad_mujeres()*100)/cantidad_participantes()
  porcentaje_m = float(porcentaje_m)
  return porcentaje_m

def porcentaje_hombres():
  porcentaje_h = (cantidad_hombres()*100)/cantidad_participantes()
  porcentaje_h = float(porcentaje_h)
  return porcentaje_h

#Salida
#EF (num_participantes, num_ligero_total, num_welter_total, num_pesado_total, num_combates_total)

print("Mujeres total:", cantidad_mujeres())
print("Hombres total:", cantidad_hombres())
print("Total de participantes:", cantidad_participantes())

print("Participantes categoría ligero:", cantidad_ligero_total())
print("Participantes categoria welter:", cantidad_welter_total())
print("Participantes categoria pesado:", cantidad_pesado_total())

print("Combates mujeres:", combates_mujeres())
print("Combates hombres:", combates_hombres())
print("Combates totales:", combates_totales())

print("Porcentaje de mujeres:", porcentaje_mujeres())
print("Porcentaje de mujeres:", porcentaje_hombres())

