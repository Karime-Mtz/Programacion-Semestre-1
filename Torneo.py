"""
Proyecto Final
Karime Martínez A01709690

El programa recibe datos de los competidores (nombre, peso y sexo)
y de acuerdo a ellos asigna los combates. Al final aparecen
la cantidad de participantes de acuerdo al sexo y a su categoría.
También devuelve los combates generados aleatoriamente.
"""

# Biblioteca importada: random
# Utilizada en la función crear_matriz_combate() para mezclar los nombres
# Línea 177
import random


def datos_participante(diccionario, capacidad_max):
    """
    (funciones, while, if, operadores, listas, strings)
    Recibe: un diccionario y la capacidad máxima.
    Pregunta si se quieren agregar nuevos competidores.
    Pregunta los datos del competidor y actualiza el diccionario.
    Devuelve: el mismo diccionario ya sea actualizado con la nueva
    información o tal y cómo estaba.
    """
    print("Bienvenido a la Copa Jaguares de Taekwondo 2025")

    pregunta_agregar = "¿Deseas agregar un nuevo participante? (si/no) "
    agregar = input(pregunta_agregar).lower()
    i = 0

    while agregar == "si":
        if i < capacidad_max:
            nombre = input("¿Cuál es tu nombre? ")

            pregunta_sexo = "¿Cuál es tu sexo? (mujer/hombre) "
            sexo = input(pregunta_sexo).lower()
            while sexo not in ["mujer", "hombre"]:
                print("Respuesta no válida")
                sexo = input(pregunta_sexo).lower()

            peso = float(input("¿Cuál es tu peso? "))

            if peso < 65:
                categoria = "ligero"
            elif peso < 80:
                categoria = "welter"
            else:
                categoria = "pesado"

            diccionario[sexo][categoria].append(nombre)
            i += 1
            pregunta_otro = "¿Te gustaría agregar otro participante? (si/no) "
            agregar = input(pregunta_otro).lower()
            while agregar not in ["si", "no"]:
                print("Respuesta no válida")
                agregar = input(pregunta_otro).lower()
        else:
            agregar = "no"
            print("\nUna disculpa, has alcanzado la capacidad máxima.")

    return diccionario


def cantidad_mujeres(diccionario):
    """
    (funciones, listas, operadores)
    Recibe: un diccionario
    Cuenta la cantidad de elementos que hay en todas
    las categoría mujer
    Devuelve: la cantidad
    """
    acum = 0
    for categoria in diccionario["mujer"]:
        acum += len(diccionario["mujer"][categoria])
    return acum


def cantidad_hombres(diccionario):
    """
    (funciones, listas, operadores)
    Recibe: un diccionario
    Cuenta la cantidad de elementos que hay en todas
    las categoría hombre
    Devuelve: la cantidad
    """
    acum = 0
    for categoria in diccionario["hombre"]:
        acum += len(diccionario["hombre"][categoria])
    return acum


def cantidad_participantes(diccionario):
    """
    (funciones, listas, operadores)
    Recibe: un diccionario
    Llama a las dos funciones anteriores y suma
    la cantidad de mujeres y hombres
    Devuelve: la cantidad total
    """
    return cantidad_mujeres(diccionario) + cantidad_hombres(diccionario)


def cantidad_ligero_total(diccionario):
    """
    (funciones, listas, operadores)
    Recibe: un diccionario
    Cuenta la cantidad de elementos para la categoría ligero
    Devuelve: resultado de la suma de hombres y mujeres
    en esa categoría
    """
    mujeres = len(diccionario["mujer"]["ligero"])
    hombres = len(diccionario["hombre"]["ligero"])
    return mujeres + hombres


def cantidad_welter_total(diccionario):
    """
    (funciones, listas, operadores)
    Recibe: un diccionario
    Cuenta la cantidad de elementos para la categoría welter
    Devuelve: resultado de la suma de hombres y mujeres
    en esa categoría
    """
    mujeres = len(diccionario["mujer"]["welter"])
    hombres = len(diccionario["hombre"]["welter"])
    return mujeres + hombres


def cantidad_pesado_total(diccionario):
    """
    (funciones, listas, operadores)
    Recibe: un diccionario
    Cuenta la cantidad de elementos para la categoría pesado
    Devuelve: resultado de la suma de hombres y mujeres
    en esa categoría
    """
    mujeres = len(diccionario["mujer"]["pesado"])
    hombres = len(diccionario["hombre"]["pesado"])
    return mujeres + hombres


def porcentaje_mujeres(diccionario):
    """
    (funciones, operadores)
    Recibe: un diccionario
    Calcula el porcentaje de mujeres respecto a la
    cantidad total de participantes
    Devuelve: resultado de la operación
    """
    porcentaje_m = (cantidad_mujeres(diccionario) * 100)
    porcentaje_m /= cantidad_participantes(diccionario)
    return "%.2f" % porcentaje_m


def porcentaje_hombres(diccionario):
    """
    (funciones, operadores)
    Recibe: un diccionario
    Calcula el porcentaje de hombres respecto a la
    cantidad total de participantes
    Devuelve: resultado de la operación
    """
    porcentaje_h = (cantidad_hombres(diccionario) * 100)
    porcentaje_h /= cantidad_participantes(diccionario)
    return "%.2f" % porcentaje_h


def crear_matriz_combate(lista_participantes):
    """
    (funciones, while, matrices, operadores, if)
    Recibe: una lista de participantes
    Mezcla aleatoriamente la lista y agrega cada dos
    participantes a una lista anidada.
    Devuelve: una lista anidada con los combates aleatorios.
    """
    random.shuffle(lista_participantes)
    matriz = []
    i = 0

    while i < len(lista_participantes) - 1:
        fila = [lista_participantes[i], lista_participantes[i + 1]]
        matriz.append(fila)
        i += 2

    if len(lista_participantes) % 2 != 0:
        matriz.append([lista_participantes[-1], "descansa"])

    return matriz


def main():
    """
    (diccionarios, funciones, matrices)
    Crea un diccionario, manda llamar las funciones
    datos_participante() y crear_matriz_combate() e
    imprime las estadísticas generales.
    """
    participantes = {
        "mujer": {"ligero": [], "welter": [], "pesado": []},
        "hombre": {"ligero": [], "welter": [], "pesado": []},
    }

    capacidad_max = 50
    participantes = datos_participante(participantes, capacidad_max)

    # ---- Creación de matrices ----
    matriz_ligero_m = crear_matriz_combate(participantes["mujer"]["ligero"])
    matriz_ligero_h = crear_matriz_combate(participantes["hombre"]["ligero"])
    matriz_welter_m = crear_matriz_combate(participantes["mujer"]["welter"])
    matriz_welter_h = crear_matriz_combate(participantes["hombre"]["welter"])
    matriz_pesado_m = crear_matriz_combate(participantes["mujer"]["pesado"])
    matriz_pesado_h = crear_matriz_combate(participantes["hombre"]["pesado"])

    # ---- Salidas ----
    print("\nDatos Generales")
    print(
        "\nHombres total:", cantidad_hombres(participantes),
        "(", porcentaje_hombres(participantes), "%)"
    )
    print(
        "Mujeres total:", cantidad_mujeres(participantes),
        "(", porcentaje_mujeres(participantes), "%)"
    )
    print("Total de participantes:", cantidad_participantes(participantes))

    print("\nParticipantes categoría ligero:",
          cantidad_ligero_total(participantes))
    print("Participantes categoría welter:",
          cantidad_welter_total(participantes))
    print("Participantes categoría pesado:",
          cantidad_pesado_total(participantes))

    print("\nMatrices de combates:")
    print("\nCombates ligeros mujeres:", matriz_ligero_m)
    print("Combates ligeros hombres:", matriz_ligero_h)
    print("Combates welter mujeres:", matriz_welter_m)
    print("Combates welter hombres:", matriz_welter_h)
    print("Combates pesado mujeres:", matriz_pesado_m)
    print("Combates pesado hombres:", matriz_pesado_h)


main()

