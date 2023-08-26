Avance de proyecto
Easily Life 

Ha medida que vamos creciendo en la parte formativa la educación de ha vuelto cada vez más diversa y dinámica, la educación va más allá de las aulas. Las actividades extracurriculares desempeñan un papel fundamental en el desarrollo integral de los estudiantes, brindándoles oportunidades para explorar sus pasiones, fortalecer habilidades y forjar relaciones significativas. Reconociendo la importancia de estas experiencias enriquecedoras el TEC creo “LiFE”. Que significa Liderazgo y Formación Estudiantil, el cual va de la mano del nuevo Modelo Educativo TEC21, que tiene a la vivencia estudiantil memorable como uno de sus 4 pilares.

En el panorama educativo actual, existe una creciente demanda por actividades extracurriculares de este tipo. Sin embargo, encontrar las opciones adecuadas puede ser complicado y confuso para los estudiantes. Aquí es donde entra en juego "Easily LiFE" un proyecto el cual tiene como objetivo simplificar y optimizar este proceso de búsqueda, brindando a los usuarios la capacidad de encontrar las actividades extracurriculares que mejor se alinean con sus intereses y disponibilidad. 

Como estudiante de primer ingreso, puedo dar una retroalimentación de como fue mi proceso para encontrar estas actividades extracurriculares. Para empezar la información se encontraba en un formato de Excel muy extenso, por lo que pasar por cada una de ellas se volvía tedioso. Además, los horarios de estas actividades no estaban especificados de la mejor manera al igual que el área de interés de cada una de ellas. Lo que para un alumno de primer ingreso lo volvía un proceso dificultoso.

Los objetivos de "Easily LiFE" son los siguientes:
1.	Proporcionar a los estudiantes un acceso fácil y conveniente a una amplia gama de actividades extracurriculares.
2.	Facilitar la exploración y búsqueda personalizada en función de los intereses y preferencias de cada usuario.
3.	Dar a conocer cada una de las actividades que hay en este programa educativo.

Algoritmo: 
Ingresar cada una de las actividades extracurriculares y distinguirlas según su área de conocimiento, horario y eje. 

Segundo avance
Avance 2
Incorporando a tu proyecto libre operaciones con operadores
Para poder involucrar estas operaciones dentro del proyecto se llevará a cabo una encuesta, por la cual los alumnos podrán tener una mejor idea de cuál es el área en la que deberían de participar. 
Para esto se necesitara la operación de suma.

Algoritmo:

#Este es un ejemplo de como se usarían los operadores para hacer la encuesta

print("Qué es lo que más te gusta?")
print("a) Jugar")
print("b) Leer")
print("c) Alguna idea")

respuesta = input("Inserta tu respuesta: ")

acumulador = 0

if respuesta == "a":
    acumulador = acumulador + 10
elif respuesta == "b":
    acumulador = acumulador + 20
elif respuesta == "c":
    acumulador = acumulador + 30

print("Qué es lo que más te gusta comer?")
print("a) pizza")
print("b) hamburguesa")
print("c) tacos")

respuesta = input("Inserta tu respuesta: ")


if respuesta == "a":
    acumulador = acumulador + 10
elif respuesta == "b":
    acumulador = acumulador + 20
elif respuesta == "c":
    acumulador = acumulador + 30

if acumulador == 20:
    print(" Tu personalidad es extrovertida")
elif acumulador >= 20:
    print("Tu personalidad es introvertida")
    
