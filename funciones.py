

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

    print(f"Cantidad de letras: {cantidad_letras}")
    print(f"Cantidad de números: {cantidad_numeros}")
    print(f"Cantidad de símbolos: {cantidad_simbolos}")
    print(f"Cantidad de espacios: {cantidad_espacios}")




def buscar_caracter(contra, caracter):

    cantidad = 0

    print("Posiciones donde aparece:")

    for i in range(len(contra)):

        if contra[i] == caracter:
            cantidad += 1
            print(i)

    print(f"Cantidad de veces que aparece: {cantidad}")



def invertir_contrasena(contra):

    invertida = ""

    for i in range(len(contra) - 1, -1, -1):
        invertida += contra[i]

    print(f"Contraseña invertida: {invertida}")




def reporte_estadistico(contra):

    letras = 0
    numeros = 0
    simbolos = 0
    repetidos = 0

    longitud = len(contra)

    for i in range(longitud):

        codigo = ord(contra[i])

        # Letras
        if (codigo >= 65 and codigo <= 90) or (codigo >= 97 and codigo <= 122):
            letras += 1

        # Números
        elif codigo >= 48 and codigo <= 57:
            numeros += 1

        # Símbolos
        else:
            simbolos += 1

    # Buscar repetidos consecutivos
    i = 0

    while i < longitud - 1:

        contador = 1

        while i < longitud - 1 and contra[i] == contra[i + 1]:
            contador += 1
            i += 1

        if contador > 1:
            repetidos += 1
            print(f"El caracter {contra[i]} se repite {contador} veces consecutivas")

        i += 1

    porcentaje_letras = (letras * 100) / longitud
    porcentaje_numeros = (numeros * 100) / longitud
    porcentaje_simbolos = (simbolos * 100) / longitud

    print(f"Longitud total: {longitud}")
    print(f"Porcentaje de letras: {porcentaje_letras}%")
    print(f"Porcentaje de números: {porcentaje_numeros}%")
    print(f"Porcentaje de símbolos: {porcentaje_simbolos}%")
    print(f"Cantidad de grupos repetidos: {repetidos}")




def es_palindromo(contra):

    invertida = ""

    # Invertir manualmente
    for i in range(len(contra) - 1, -1, -1):
        invertida += contra[i]

    # Comparar
    if contra == invertida:
        print("La contraseña es palíndroma")
    else:
        print("La contraseña NO es palíndroma")




def ordenar_contrasena(contra, orden):

    lista = []

    # Pasar string a lista manualmente
    for caracter in contra:
        lista += caracter

    # Ordenamiento manual (Burbuja)
    for i in range(len(lista)):

        for j in range(len(lista) - 1):

            if orden == "asc":

                # Ascendente
                if ord(lista[j]) > ord(lista[j + 1]):

                    aux = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = aux

            elif orden == "desc":

                # Descendente
                if ord(lista[j]) < ord(lista[j + 1]):

                    aux = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = aux

    # Convertir lista a string
    resultado = ""

    for caracter in lista:
        resultado += caracter

    print(f"Contraseña ordenada: {resultado}")




