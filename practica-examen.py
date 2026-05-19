from funciones import verif_clave

while True :
        clave = input("ingrese su contraseña :")
        valida,mensaje = verif_clave(clave)
        print(mensaje)

        if valida == True:
            break
        
print("\n1 validar nivel de seguridad\n2 contar tipos de caracteres\n3 buscar caracter especifico\n4 mostrar contraseña invertida")
print("5 generar reporte estadistico\n6 verificar si es palidromo\n7 ordenar caracteres de la contraseña\n8 salir")
menu = int(input("seleccione el numero que corresponda :"))

if menu == 1:
    from funciones import val_seg
    clave = clave
    nivel = val_seg(clave)
    print("Nivel de seguridad:", nivel)

if menu == 2 :
     