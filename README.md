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


#Este es el avance del 22-09-23
def obtener_respuesta(pregunta):
    respuesta = input(pregunta + " Escribe la letra de tu respuesta: ")
    while respuesta not in ("a", "b", "c"):
        print("Respuesta no válida. Por favor, elige 'a', 'b' o 'c'.")
        respuesta = input(pregunta + " Escribe la letra de tu respuesta: ")
    return respuesta

def contar_respuestas(respuestas):
    a = respuestas.count("a")
    b = respuestas.count("b")
    c = respuestas.count("c")
    return a, b, c

respuestas = []

print("¿Qué tipo de actividades prefieres durante tu tiempo libre?")
print("a) Leer o escribir.")
print("b) Escuchar música o podcasts.")
print("c) Practicar deportes o actividades físicas.")

respuesta1 = obtener_respuesta("")

respuestas.append(respuesta1)

print("¿Cómo te describirías en términos de sociabilidad?")
print("a) Introvertido.")
print("b) Ambivertido.")
print("c) Extrovertido.")

respuesta2 = obtener_respuesta("")

respuestas.append(respuesta2)

a, b, c = contar_respuestas(respuestas)

if a > b and a > c:
    print("Arte podría ser una buena opción para ti.")
elif b > a and b > c:
    print("Música podría ser una buena opción para ti.")
elif c > b and c > a:
    print("Baile podría ser una buena opción para ti.")

print("!Muchas gracias por responder la encuesta!")



#Aquí comienza el horario 

horario = input("¿Quieres buscar un horario para tus clases? (Escribe SI / NO) ").lower()

if horario == "si":
    print("Vamos a realizar tu horario")

    if a>b and a>c:
        print("Las clases para ARTE disponible son:")
        print("a. Teatro.")
        print("b. Diseño.")
        print("c. Dibujo")
        selec_arte = (input("Selecciona la letra del curso en el que estás interesado: ")).lower()

        if selec_arte == "a":
            print("Los horarios disponible para TEATRO son:")
            print("a. 9:oo - 10:00 a.m.")
            print("b. 11:oo - 12:00 a.m.")
            print("c. 2:oo - 3:00 p.m.")
        elif selec_arte == "b":
            print("Los horarios disponible para DISEÑO son:")
            print("a. 9:oo - 10:00 a.m.")
            print("b. 11:oo - 12:00 a.m.")
            print("c. 2:oo - 3:00 p.m.")
        elif selec_arte == "c":
            print("Los horarios disponible para DIBUJO son:")
            print("a. 9:oo - 10:00 a.m.")
            print("b. 11:oo - 12:00 a.m.")
            print("c. 2:oo - 3:00 p.m.")

    elif b>a and b>c:
        print("Las clases para MÚSICA disponible son:")
        print("a. Guitarra.")
        print("b. Piano.")
        print("c. Canto")
        selec_music = (input("Selecciona la letra del curso en el que estás interesado: ")).lower()

        if selec_music == "a":
            print("Los horarios disponible para GUITARRA son:")
            print("a. 9:oo - 10:00 a.m.")
            print("b. 11:oo - 12:00 a.m.")
            print("c. 2:oo - 3:00 p.m.")
        elif selec_music == "b":
            print("Los horarios disponible para PIANO son:")
            print("a. 9:oo - 10:00 a.m.")
            print("b. 11:oo - 12:00 a.m.")
            print("c. 2:oo - 3:00 p.m.")
        elif selec_music == "c":
            print("Los horarios disponible para CANTO son:")
            print("a. 9:oo - 10:00 a.m.")
            print("b. 11:oo - 12:00 a.m.")
            print("c. 2:oo - 3:00 p.m.")

    elif c>b and c>a:
        print("Las clases para DEPORTE disponible son:")
        print("a. Fútbol.")
        print("b. Natación.")
        print("c. Basket.")
        selec_deport = (input("Selecciona la letra del curso en el que estás interesado: ")).lower()

        if selec_deport == "a":
            print("Los horarios disponible para GUITARRA son:")
            print("a. 9:oo - 10:00 a.m.")
            print("b. 11:oo - 12:00 a.m.")
            print("c. 2:oo - 3:00 p.m.")
        elif selec_deport == "b":
            print("Los horarios disponible para PIANO son:")
            print("a. 9:oo - 10:00 a.m.")
            print("b. 11:oo - 12:00 a.m.")
            print("c. 2:oo - 3:00 p.m.")
        elif selec_deport == "c":
            print("Los horarios disponible para CANTO son:")
            print("a. 9:oo - 10:00 a.m.")
            print("b. 11:oo - 12:00 a.m.")
            print("c. 2:oo - 3:00 p.m.")


else:
    print("Gracias por participar")

else:
    print("Gracias por participar")



