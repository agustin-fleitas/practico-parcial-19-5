

def verif_clave(contra):

    # no puede estar vacía
    if not contra:
        return False, "La contraseña no puede estar vacía."

    # no puede comenzar con espacios
    if contra[0] == " ":
        return False, "La contraseña no puede comenzar con espacios."

    # debe tener al menos 8 caracteres
    if len(contra) < 8:
        return False, "La contraseña debe tener al menos 8 caracteres."

    # debe contener al menos una letra
    tiene_letra = False
    i = 0

    while i < len(contra):

        caracter = contra[i]

        if (caracter >= 'a' and caracter <= 'z') or (caracter >= 'A' and caracter <= 'Z'):
            tiene_letra = True
            break

        i = i + 1

    if tiene_letra == False:
        return False, "La contraseña debe contener al menos una letra."

    return True, "Contraseña válida."




def val_seg(contra):

    tiene_letras = False
    tiene_numeros = False
    tiene_simbolos = False

    simbolos = """!"#$%&'()*+,-./"""

    i = 0

    while i < len(contra):

        caracter = contra[i]

        # verificar letras
        if (caracter >= 'a' and caracter <= 'z') or (caracter >= 'A' and caracter <= 'Z'):
            tiene_letras = True

        # verificar números
        elif caracter >= '0' and caracter <= '9':
            tiene_numeros = True

        # verificar símbolos
        else:

            j = 0

            while j < len(simbolos):

                if caracter == simbolos[j]:
                    tiene_simbolos = True

                j = j + 1

        i = i + 1

    # CONTRASEÑA FUERTE
    if len(contra) >= 12 and tiene_letras and tiene_numeros and tiene_simbolos:
        return "Fuerte"

    # CONTRASEÑA MEDIA
    elif tiene_letras and tiene_numeros:
        return "Media"

    # CONTRASEÑA DÉBIL
    elif len(contra) >= 8 and len(contra) <= 9 and tiene_letras and not tiene_numeros and not tiene_simbolos:
        return "Débil"

    


def contador_caracteres(contra):

    cantidad_letras = 0
    cantidad_numeros = 0
    cantidad_simbolos = 0
    cantidad_espacios = 0

    for caracter in contra:

        #devuelve el codigo ascii de un caracter 
        codigo = ord(caracter)

        # Letras
        if (codigo >= 65 and codigo <= 90) or (codigo >= 97 and codigo <= 122):
            cantidad_letras += 1

        # Números
        elif codigo >= 48 and codigo <= 57:
            cantidad_numeros += 1

        # Espacios
        elif codigo == 32:
            cantidad_espacios += 1

        # Símbolos
        else:
            cantidad_simbolos += 1

    print("Cantidad de letras:", cantidad_letras)
    print("Cantidad de números:", cantidad_numeros)
    print("Cantidad de símbolos:", cantidad_simbolos)
    print("Cantidad de espacios:", cantidad_espacios)




def buscar_caracter(contra, caracter):

    cantidad = 0

    print("Posiciones donde aparece:")

    for i in range(len(contra)):

        if contra[i] == caracter:
            cantidad += 1
            print(i)

    print("Cantidad de veces que aparece:", cantidad)







