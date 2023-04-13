def pedir_nombres():
    arc_o = input("Ingrese nombre del archivo en texto plano: ")
    clave = input("Ingrese la clave: ")
    arc_d = input("Ingrese nombre del archivo para la encripción:")
    return arc_o, clave, arc_d

def comprobar_archivo(arc_o):
    try:
        open(arc_o).close()
        return True
    except:
        print("No se pudo abrir el archivo")
        return False

def comprobar_clave(clave):
    if clave.isalpha():
        clave = clave.lower()
        return True, clave
    else:
        print("La clave solo puede contener letras del alfabeto inglés")
        return False, ""

def comprobar_archivo_destino(arc_o, arc_d):
    while arc_d == arc_o:
        overwrite = input("Ha ingresado el mismo archivo de origen que destino. Está seguro de que quiere sobreescribir los datos? (Y/N)").lower()
        if overwrite == "y":
            break
        else:
            arc_d = input("Ingrese nombre del archivo para la encripción:")
    return arc_d

def encripcion(arc_o, clave):
    l_final = [] 
    index = 0
    with open(arc_o) as f:
        for linea in f:
            l_chars = [] 
            for letra in linea.rstrip().lower():
                if letra.isalpha():
                    cambio_letra = chr(((ord(letra) - 97 + ord(clave[index]) - 97) % 26) + 97)
                    l_chars.append(cambio_letra)
                    index = (index + 1) % len(clave)
                else:
                    l_chars.append(letra)
            l_final.append("".join(l_chars) + "\n")
    l_final[-1] = l_final[-1][:-1]
    return l_final

def escribir_lineas(arc_d, l_final):
    with open(arc_d, "w") as f:
        f.writelines(l_final)

def main():
    print("≡≡Encriptador de Cifrado de Vigenère≡≡")
    arc_o, clave, arc_d = pedir_nombres()
    while not comprobar_archivo(arc_o):
        arc_o = input("Ingrese nombre del archivo en texto plano: ")
    while not comprobar_clave(clave)[0]:
        clave = input("Ingrese la clave: ")
    arc_d = comprobar_archivo_destino(arc_o, arc_d)
    l_final = encripcion(arc_o, comprobar_clave(clave)[1])
    escribir_lineas(arc_d, l_final)

if __name__ == "__main__":
    main()

