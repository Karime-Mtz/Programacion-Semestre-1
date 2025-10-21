"""
Proyecto Final
Karime Martínez A01709690

El programa recibe datos de los competidores (nombre, peso y sexo)
y de acuerdo a ellos asigna los combates. A final aparecen
la cantidad de participantes de acuerdo al sexo y a su categoría.
También devuelve 

"""
"""
Creación de un diccionario donde se pondrán los nombres de
los competidores:
"""

import random


def datos_participante(diccionario, capacidad_max):
    """
    Recibe: un diccionario
    Pregunta los datos del competidor y actualiza el diccionario
    Devuelve: el mismo diccionario actualizado con la nueva información
    """
    print("Bienvenido a la Copa Jaguares de Taekwondo 2025")
    agregar = input("¿Deseas agregar un nuevo participante? (si/no) ").lower()
    i=0

    while agregar == "si":
        if capacidad_max > i:
            nombre = input("¿Cuál es tu nombre? ")
            sexo = input("¿Cuál es tu sexo? (mujer/hombre) ").lower()
            
            while sexo not in ["mujer", "hombre"]:
                print("Respuesta no válida")
                sexo = input("¿Cuál es tu sexo? (mujer/hombre) ").lower() 
                
            peso = float(input("¿Cuál es tu peso? (sólo el número) "))

            if peso < 65:
                categoria = "ligero"
            elif peso < 80:
                categoria = "welter"
            else:
                categoria = "pesado"
            diccionario[sexo][categoria].append(nombre)
            i = i + 1
            agregar = input("¿Te gustaría agregar otro participante? (si/no) ").lower()
        else:
            agregar = 'no'
            print('\nUna disculpa has alcanzado la capacidad máxima')
    return diccionario
         

def cantidad_mujeres(diccionario):
    
    acum = 0
    for a in diccionario["mujer"]:
        acum = acum + len(diccionario["mujer"][a])
    return acum


def cantidad_hombres(diccionario):
    acum = 0
    for a in diccionario["hombre"]:
        acum = acum + len(diccionario["hombre"][a])
    return acum


def cantidad_participantes(diccionario):
    return cantidad_mujeres(diccionario) \
           + cantidad_hombres(diccionario)


def cantidad_ligero_total(diccionario):
    mujeres = len(diccionario["mujer"]["ligero"])
    hombres = len(diccionario["hombre"]["ligero"])
    return mujeres + hombres


def cantidad_welter_total(diccionario):
    mujeres = len(diccionario["mujer"]["welter"])
    hombres = len(diccionario["hombre"]["welter"])
    return mujeres + hombres


def cantidad_pesado_total(diccionario):
    mujeres = len(diccionario["mujer"]["pesado"])
    hombres = len(diccionario["hombre"]["pesado"])
    return mujeres + hombres


def porcentaje_mujeres(diccionario):
    porcentaje_m = (cantidad_mujeres(diccionario)*100)
    porcentaje_m = porcentaje_m/cantidad_participantes(diccionario)
    return "%.2f" % porcentaje_m


def porcentaje_hombres(diccionario):
    porcentaje_h = (cantidad_hombres(diccionario)*100)
    porcentaje_h = porcentaje_h/cantidad_participantes(diccionario)
    return "%.2f" % porcentaje_h


def crear_matriz_combate(lista_participantes):
    random.shuffle(lista_participantes)
    matriz = []
    i = 0
    while i < len(lista_participantes) - 1:
        fila = [lista_participantes[i], lista_participantes[i + 1]]
        matriz.append(fila)
        i = i + 2
        
    if len(lista_participantes) % 2 != 0:
        matriz.append([lista_participantes[-1], "descansa"])
    return matriz


""" ------ Función Principal ------ """

def main():
    participantes = {
        "mujer": {"ligero": [], "welter": [], "pesado": []},
        "hombre": {"ligero": [], "welter": [], "pesado": []}
        }
    capacidad_max = 5
    participantes = datos_participante(participantes, capacidad_max)

    """ ---- Creación de Matrices ----- """
    
    matriz_ligero_m = crear_matriz_combate(participantes["mujer"]["ligero"])
    matriz_ligero_h = crear_matriz_combate(participantes["hombre"]["ligero"])
    matriz_welter_m = crear_matriz_combate(participantes["mujer"]["welter"])
    matriz_welter_h = crear_matriz_combate(participantes["hombre"]["welter"])
    matriz_pesado_m = crear_matriz_combate(participantes["mujer"]["pesado"])
    matriz_pesado_h = crear_matriz_combate(participantes["hombre"]["pesado"])

    """ ----- Salidas ----- """
    print("\nDatos Generales")
    print("\nHombres total:", cantidad_hombres(participantes),
          "(", porcentaje_hombres(participantes), "%)")
    print("Mujeres total:", cantidad_mujeres(participantes), "(", porcentaje_mujeres(participantes), "%)")
    print("Total de participantes:", cantidad_participantes(participantes))

    print("\nParticipantes categoría ligero:", cantidad_ligero_total(participantes))
    print("Participantes categoría welter:", cantidad_welter_total(participantes))
    print("Participantes categoría pesado:", cantidad_pesado_total(participantes))

    print("\nMatrices de combates:")
    print("\nCombates ligeros mujeres:", matriz_ligero_m)
    print("Combates ligeros hombres:", matriz_ligero_h)
    print("Combates welter mujeres:", matriz_welter_m)
    print("Combates welter hombres:", matriz_welter_h)
    print("Combates pesado mujeres:", matriz_pesado_m)
    print("Combates pesado hombres:", matriz_pesado_h)


""" ----- Ejecutar el Programa ----- """
main()

