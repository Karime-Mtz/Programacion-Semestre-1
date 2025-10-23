###Contexto

De acuerdo al reglamento de Taekwondo de competencia de la CONADE (Comisión Nacional de Cultura Físical y el Deporte) 
la asignación de combates no se hace de forma aleatoria, sino que se considera el sexo, la cinta y peso del competidor o competidora. 
El proceso que se debe llevar a cabo empieza por agrupar en una categoría a las hombres y en otra a las mujeres y posteriormente se 
forman las parejas de acuerdo a su peso.

Este procedimiento se debe llevar a cabo en todo tipo de torneo de Taekwondo antes de empezar cualquier contienda, 
por lo que es importante contar con los datos de cada participante para que todos los competidores reciban una asignación de 
combate justa y que su integridad física no sea puesta en riesgo.

Creo que es interesante porque yo hice taekwondo durante 10 años, por lo que es un tema que conozco. Además, me gustaría ver este proceso que vivido tantas veces de forma automatizada.

###Algoritmo:
E0 información sobre el competidor (nombre, sexo, peso)

Crear un diccionario:
 mujer: ligero, welter, pesado
 hombre: ligero, welter, pesado

Definir capacidad de competidores
Capacidad = 10

Mientras x sea menor que capacidad
  Preguntas si se quiere agregar un participante
  Si peso < 65
   asignar categoría: ligero
  Si peso < 80
   asignar categoría: welter
  else
   asignar categoría: pesado
   
  Agregar (nombre) a diccionario en la categoría correcto
x = x +1


m = longitud de lista categoria_mujer
h = longitud de lista categoria_hombre

Mientras i sea menor o igual que m
resultados_mujer = categoria_mujer[i], categoria_mujer[i+1]
i = i+2

Mientras j sea menor o igual que h
resultados_hombre = categoria_hombre[j], categoria_hombre[j+1]
j = j+2

EF (resultados_mujer, resultados_hombre)

###Instrucciones
Descargar el archivo y correr en terminal con:
  python Torneo.py
o abrir en Thonny y dar botón de play
Llenar los datos que se preguntan.
Gracias por su visita
