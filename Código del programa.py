#Este es el avance del 13-10-23
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

    clases = ["a) ARTE", "b) MÚSICA", "c) DEPORTE"]
    horarios = [
        ["a) Teatro", "b) Diseño", "c) Dibujo"],
        ["a) Guitarra", "b) Piano", "c) Canto"],
        ["a) Fútbol", "b) Natación", "c) Basket"]
    ]

    horarios_disponibles = [
        ["9:00 - 10:00 a.m.", "11:00 - 12:00 a.m.", "2:00 - 3:00 p.m."],
        ["9:00 - 10:00 a.m.", "11:00 - 12:00 a.m.", "2:00 - 3:00 p.m."],
        ["9:00 - 10:00 a.m.", "11:00 - 12:00 a.m.", "2:00 - 3:00 p.m."]
    ]

    for i, categoria in enumerate(clases):
        print(f"Clases de {categoria} disponibles.")
    
    seleccion_categoria = input("Selecciona la letra de la categoría en la que estás interesado: ").lower()
    indice_categoria = ord(seleccion_categoria) - ord("a")

    if 0 <= indice_categoria < len(clases):
        categoria_seleccionada = clases[indice_categoria]

        print(f"Las clases para {categoria_seleccionada} disponibles son:")
        for i, clase in enumerate(horarios[indice_categoria]):
            print(f"{clase}")

        seleccion_clase = input("Selecciona la letra del curso en el que estás interesado: ").lower()
        indice_clase = ord(seleccion_clase) - ord("a")

        if 0 <= indice_clase < len(horarios[indice_categoria]):
            clase_seleccionada = horarios[indice_categoria][indice_clase]

            print(f"Los horarios disponibles para {clase_seleccionada} son:")
            for i, horario in enumerate(horarios_disponibles[indice_categoria]):
                print(f"{horario}")
        else:
            print("Selección de curso no válida.")
    else:
        print("Selección de categoría no válida.")

else:
    print("Gracias por participar")



