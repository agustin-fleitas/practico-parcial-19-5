from funciones import verif_clave

while True :
        clave = input("ingrese su contraseña :")
        valida,mensaje = verif_clave(clave)
        print(mensaje)

        if valida == True:
            break
        
print("\n1 validar nivel de seguridad\n2 contar tipos de caracteres\n3 buscar caracter especifico\n4 mostrar contraseña invertida")
print("5 generar reporte estadistico\n6 verificar si es palidromo\n7 ordenar caracteres de la contraseña\n8 salir\n")
menu = int(input("seleccione el numero que corresponda :"))

if menu == 1:
    from funciones import val_seg
    nivel = val_seg(clave)
    print("Nivel de seguridad:", nivel)

if menu == 2 :
    from funciones import contador_caracteres
    clave = clave
    contador_caracteres(clave)

if menu == 3 :
    from funciones import buscar_caracter
    clave = clave
    caracter = input("Ingrese un caracter a buscar: ")

    buscar_caracter(clave, caracter)

if menu == 4 :
    from funciones import invertir_contrasena
    clave = clave
    invertir_contrasena(clave)

if menu == 5 :
    from funciones import reporte_estadistico 
    clave = clave
    reporte_estadistico(clave)

if menu == 6 :
    from funciones import es_palindromo
    clave = clave
    es_palindromo(clave)
     
if menu == 7 :
    from funciones import ordenar_contrasena
    clave = clave

    print("1. Ascendente")
    print("2. Descendente")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        ordenar_contrasena(clave, "asc")

    elif opcion == "2":
        ordenar_contrasena(clave, "desc")

    else:
        print("Opción inválida")

if menu == 8 :
    print("saliendo del sistema...")
        