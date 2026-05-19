

def verif_clave(contrasena):

    # no puede estar vacía
    if not contrasena:
        return False, "La contraseña no puede estar vacía."

    # no puede comenzar con espacios
    if contrasena[0] == " ":
        return False, "La contraseña no puede comenzar con espacios."

    # debe tener al menos 8 caracteres
    if len(contrasena) < 8:
        return False, "La contraseña debe tener al menos 8 caracteres."

    # debe contener al menos una letra
    tiene_letra = False
    i = 0

    while i < len(contrasena):

        caracter = contrasena[i]

        if (caracter >= 'a' and caracter <= 'z') or (caracter >= 'A' and caracter <= 'Z'):
            tiene_letra = True
            break

        i = i + 1

    if tiene_letra == False:
        return False, "La contraseña debe contener al menos una letra."

    return True, "Contraseña válida."




def val_seg(contrasena):

    tiene_letras = False
    tiene_numeros = False
    tiene_simbolos = False

    simbolos = '!\"#$%&\'()*+,-./'

    i = 0

    while i < len(contrasena):

        caracter = contrasena[i]

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
    if len(contrasena) >= 12 and tiene_letras and tiene_numeros and tiene_simbolos:
        return "Fuerte"

    # CONTRASEÑA MEDIA
    elif tiene_letras and tiene_numeros:
        return "Media"

    # CONTRASEÑA DÉBIL
    elif len(contrasena) >= 8 and len(contrasena) <= 9 and tiene_letras and not tiene_numeros and not tiene_simbolos:
        return "Débil"

    






