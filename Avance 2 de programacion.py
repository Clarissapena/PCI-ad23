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



