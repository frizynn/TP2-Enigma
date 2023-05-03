def pedir_nombre_archivo():
    arc_o = input("Ingrese nombre del archivo en texto plano: ")
    while True:
        try:
            open(arc_o).close()
            break
        except:
            print("...\nNo se pudo abrir el archivo")
            arc_o = input("Ingrese nombre del archivo en texto plano: ")
    return arc_o

def pedir_clave():
    while True:
        clave = input("Ingrese la clave: ")
        if clave.isalpha():
            clave = clave.lower()
            break
        else:
            print("...\nLa clave solo puede contener letras del alfabeto inglés")
    return clave

def pedir_nombre_archivo_destino(arc_o):
    while True:
        arc_d = input("Ingrese nombre del archivo para la encripción:")
        if arc_d != arc_o or input("Ha ingresado el mismo archivo de origen que destino. Está seguro de que quiere sobreescribir los datos? (Y/N)").lower() == "y":
            break
    return arc_d

def encripcion(arc_o, clave):
    l_final = [] 
    index = 0

    with open(arc_o) as f:
        for linea in f:
            l_chars = [] 
            for letra in linea.rstrip().lower():
                if letra.isalpha():
               #if ord(letra) in range(97, 123):               HAY QUE VER SI ESTO ANDA
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
    arc_o = pedir_nombre_archivo()
    clave = pedir_clave()
    arc_d = pedir_nombre_archivo_destino(arc_o)
    l_final = encripcion(arc_o, clave)
    escribir_lineas(arc_d, l_final)

if __name__ == "__main__":
    main()
