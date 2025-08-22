Contexto

De acuerdo al reglamento de Taekwondo de competencia de la CONADE (Comisión Nacional de Cultura Físical y el Deporte) 
la asignación de combates no se hace de forma aleatoria, sino que se considera el sexo, la cinta y peso del competidor o competidora. 
El proceso que se debe llevar a cabo empieza por agrupar en una categoría a las hombres y en otra a las mujeres y posteriormente se 
forman las parejas de acuerdo a su peso.

Este procedimiento se debe llevar a cabo en todo tipo de torneo de Taekwondo antes de empezar cualquier contienda, 
por lo que es importante contar con los datos de cada participante para todos los competidores reciban una asignación de 
combate justa y que no ponga en riesgo su integridad física.

Creo que es interesante porque yo hice taekwondo durante 10 años entonces es un tema que conozco. Me gustaría ver este 
proceso que viví tantas veces ser automatizado.


categoria_mujer = [ ]
categoria_hombre = [ ]
capacidad = 10


Mientras capacidad < 10
  E0 (nombre, sexo, peso)
  Si sexo == "mujer"
    agregar (nombre, peso) a categoria_mujer
  Else agregar (nombre, peso) a categoria_hombre

capacidad = capacidad + 1

Ordenar categoria_mujer(de menor a mayor)
Ordenar categoria_hombre(de menor a mayor)

m = (longitud de categoria_mujer)
h = (longitud de categoria_hombre)

i = 0
j = 0

Salida Final:

mientras i <= m
print( categoria_mujer[i], categoria_mujer[i+1])
i = i + 2

mientras j <= m
print( categoria_mujer[j], categoria_mujer[j+1])
j = j + 2
