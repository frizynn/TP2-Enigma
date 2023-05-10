def pedir_nombre_archivo(pedido:str):
    arc_o = input(pedido)
    while True:
        try:
            open(arc_o).close()
            break
        except:
            print("...\nNo se pudo abrir el archivo")
            arc_o = input(pedido)
    return arc_o

def pedir_clave():
    clave_invalida = True
    while clave_invalida:
        clave = input("Ingrese la clave: ")
        clave_invalida = False
        if len(clave) == 0:
            print("La clave está vacía")
            clave_invalida = True
        for letra in clave:
            if not ord(letra) in range(97, 123):  
                print("...\nLa clave solo puede contener letras del alfabeto inglés")
                clave_invalida = True
    return clave


def pedir_nombre_archivo_destino(opc):
    archivo_invalido = True
    archivo_no_sobreescripto = True
    while archivo_invalido or archivo_no_sobreescripto:
        if archivo_invalido:
            arc_d = input(f"Ingrese nombre del archivo para la {'des' if opc else ''}encripción: ")
        if len(arc_d) == 0:
            print("No ingresó un nombre válido")
        else:
            try:
                open(arc_d).close()
                des = input("El archivo existe, desea sobreescribirlo? (Y/N)\n").lower()
                if des == 'y':
                    archivo_no_sobreescripto = False
                    archivo_invalido = False
                elif des != 'n':
                    print('No se ha ingresado una respuesta válida.')
                    archivo_invalido = False
            except:
                archivo_invalido = False
                archivo_no_sobreescripto = False                
    return arc_d


def des_encripcion(arc_o, clave,opc):
    l_final = [] 
    index = 0
    
    with open(arc_o) as f:
        for linea in f:
            l_chars = [] 
            for letra in linea.rstrip().lower():
                if ord(letra) in range(97, 123):  
                    cambio_letra = chr(((ord(letra) - 97 + (1 if opc else -1) * (ord(clave[index]) - 97)) % 26) + 97)
                    l_chars.append(cambio_letra)
                    index = (index + 1) % len(clave)
                else:
                    l_chars.append(letra)
            l_final.append("".join(l_chars) + "\n")
    if len(l_final) == 0:
        return []
    l_final[-1] = l_final[-1][:-1]
    return l_final

def escribir_lineas(arc_d, l_final):
    with open(arc_d, "w") as f:
        f.writelines(l_final)

def main():
    print("≡≡Desencriptador de Cifrado de Vigenère≡≡")
    arc_o = pedir_nombre_archivo("Ingrese nombre del archivo en texto plano: ")
    clave = pedir_clave()
    arc_d = pedir_nombre_archivo_destino(False)
    l_final = des_encripcion(arc_o, clave,True)
    if len(l_final) == 0:
        print("El archivo está vacío")
    else:
        escribir_lineas(arc_d, l_final)

if __name__ == "__main__":
    main()
