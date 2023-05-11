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
    """
    Solicita al usuario que ingrese una clave que contenga solo letras del alfabeto inglés y devuelve la clave como una cadena.

    Returns:
        clave_real (str): La clave ingresada por el usuario como una cadena de letras del alfabeto inglés.
    """
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
    """
    Solicita al usuario el nombre del archivo de destino para una operación de encriptación o desencriptación.

    Args:
        opc (bool): Indicador de operación (True para desencriptar, False para encriptar).

    Returns:
       arc_d (str): Nombre del archivo de destino.
    """
    archivo_invalido = True
    archivo_no_sobreescripto = True
    while archivo_invalido or archivo_no_sobreescripto:
        # Solicita el nombre del archivo de destino.
        if archivo_invalido:
            arc_d = input(f"Ingrese nombre del archivo para la {'des' if opc else ''}encripción: ")
        # Verifica si se ingresó un nombre válido.
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
    """
    Desencripta o encripta un archivo de texto.

    Args:
        arc_o (str): Nombre del archivo de origen.
        clave (str): Clave para la encriptación/desencriptación.
        opc (bool): True para encriptar, False para desencriptar.

    Returns:
        l_final (list): Lista con las líneas encriptadas o desencriptadas.
    """
    l_final = [] # Lista para guardar las líneas encriptadas/desencriptadas.
    index = 0 # Índice para iterar sobre la clave.
    
    # Abre el archivo de origen y lee cada línea.
    with open(arc_o) as f:
        for linea in f:
            l_chars = []  # Lista para guardar los caracteres de cada línea.
            for letra in linea.rstrip().lower():
                # Si el carácter es una letra minúscula:
                if ord(letra) in range(97, 123):  
                    # Calcula el cambio de la letra según la clave y si se encripta o desencripta.
                    cambio_letra = chr(((ord(letra) - 97 + (1 if opc else -1) * (ord(clave[index]) - 97)) % 26) + 97)
                    l_chars.append(cambio_letra)
                    index = (index + 1) % len(clave)  # Actualiza el índice de la clave.
                else:
                    l_chars.append(letra) # Agrega el carácter tal cual si no es una letra minúscula.
            l_final.append("".join(l_chars) + "\n") # Agrega la línea encriptada/desencriptada a la lista final.

     # Si la lista está vacía, retorna una lista vacía.
    if len(l_final) == 0:
        return []
    
    l_final[-1] = l_final[-1][:-1] # Quita el último salto de línea agregado.
    return l_final

def escribir_lineas(arc_d, l_final):
    """
    Escribe una lista de cadenas en un archivo.

    Args:
        arc_d (str): Ruta del archivo a escribir.
        l_final (List[str]): Lista de cadenas a escribir en el archivo.

    Returns:
        None
    """
    # Abre el archivo en modo escritura y guarda el objeto de archivo en la variable 'f'.
    with open(arc_d, "w") as f:
        # Escribe las cadenas en el archivo.
        f.writelines(l_final)

def main():
    print("≡≡Desencriptador de Cifrado de Vigenère≡≡")
    arc_o = pedir_nombre_archivo("Ingrese nombre del archivo en texto plano: ")
    clave = pedir_clave()
    arc_d = pedir_nombre_archivo_destino(False)
    l_final = des_encripcion(arc_o, clave,True)

    #Si el archivo de origen está vacio, lo avisa y termina el codigo. 
    if len(l_final) == 0:
        print('El arcivo a encriptar está vacio, no se ha realizado nada.')
    else:
        escribir_lineas(arc_d, l_final)
        print('Archivo encriptado.')

if __name__ == "__main__":
    main()
