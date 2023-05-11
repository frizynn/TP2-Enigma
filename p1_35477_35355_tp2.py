def pedir_nombre_archivo(pedido: str) -> str:
    """
    Solicita al usuario el nombre de un archivo existente.

    Args:
        pedido (str): Mensaje que se mostrará al usuario para pedir el nombre del archivo.

    Returns:
       arc_o (str): Nombre del archivo existente.

    Raises:
        FileNotFoundError: Si no se pudo abrir el archivo.

    """
    # Solicita el nombre del archivo al usuario.
    arc_o = input(pedido)

    # Bucle infinito para solicitar el nombre de un archivo existente.
    while True:
        try:
            # Intenta abrir el archivo. Si se puede abrir, sale del bucle.
            open(arc_o).close()
            break
        except FileNotFoundError:
            # Si no se puede abrir el archivo, muestra un mensaje de error y solicita nuevamente el nombre del archivo.
            print("...\nNo se pudo abrir el archivo")
            arc_o = input(pedido)

    # Retorna el nombre del archivo existente.
    return arc_o

def pedir_clave():
    """
    Solicita al usuario que ingrese una clave que contenga solo letras del alfabeto inglés sin mayúsculas y devuelve la clave como una cadena.

    Returns:
        clave_real (str): La clave ingresada por el usuario como una cadena de letras del alfabeto inglés.
    """
   
    # Variable para indicar si la clave es inválida.
    
    
    clave_invalida = True

    # Bucle que se repetirá mientras la clave sea inválida.
    while clave_invalida:
        clave_invalida = False
        # Solicita al usuario que ingrese la clave.
        clave = input("Ingrese la clave: ")

        # Si la clave está vacía, se le pide al usuario que la ingrese nuevamente.
        if len(clave) == 0:
            print("La clave está vacía")
            
            clave_invalida = True
        

        # Verifica que la clave contenga solo letras minúsculas del alfabeto inglés.
        for letra in clave:
            if not ord(letra) in range(97, 123):  
                print("La clave solo puede contener letras minusuclas del alfabeto inglés")
                clave_invalida = True
                break
        
        # Si la clave es válida, se establece clave_invalida en False para salir del bucle.
            
    
    # Retorna la clave validada.
    return clave



def pedir_nombre_archivo_destino(opc: bool) -> str:
    """
    Solicita al usuario el nombre del archivo de destino para una operación de encriptación o desencriptación.

    Args:
        opc (bool): Indicador de operación (True para desencriptar, False para encriptar).

    Returns:
       arc_d (str): Nombre del archivo de destino.
    """
    # Bandera que indica si el nombre de archivo es inválido.
    archivo_invalido = True  
    # Bandera que indica si se puede sobrescribir el archivo.
    archivo_no_sobreescripto = True  

     # Bucle mientras el archivo es inválido o no se puede sobrescribir.
    while archivo_invalido or archivo_no_sobreescripto: 
        # Si el archivo es inválido, solicita el nombre del archivo de destino.
        if archivo_invalido:  
            arc_d = input(f"Ingrese nombre del archivo para la {'des' if opc else ''}encripción: ")
             # Verifica si el nombre de archivo es inválido.
        if len(arc_d) == 0: 
            print("No ingresó un nombre válido")
        else:
            # Trata de abrir el archivo.
            try:
                with open(arc_d, 'x'):
                    archivo_no_sobreescripto = False
                    archivo_invalido = False

            except FileNotFoundError:  
                sobrescribir = input("El archivo ya existe, ¿desea sobrescribirlo? (Y/N) ").lower()
                if sobrescribir == 'y':
                    with open(arc_d, 'w'):
                        archivo_no_sobreescripto = False
                        archivo_invalido = False
                elif sobrescribir == 'n':
                    archivo_invalido = True
                else:
                    print('No ingresó una respuesta válida.')
    return arc_d  




def des_encripcion(arc_o, clave, opc):
    """
    Desencripta o encripta un archivo de texto.

    Args:
        arc_o (str): Nombre del archivo de origen.
        clave (str): Clave para la encriptación/desencriptación.
        opc (bool): True para encriptar, False para desencriptar.

    Returns:
        l_final (list): Lista con las líneas encriptadas o desencriptadas.
    """
    l_final = []  # Lista para guardar las líneas encriptadas/desencriptadas.
    index = 0  # Índice para iterar sobre la clave.

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
                    l_chars.append(letra)  # Agrega el carácter tal cual si no es una letra minúscula.
            l_final.append("".join(l_chars) + "\n")  # Agrega la línea encriptada/desencriptada a la lista final.

    # Si la lista está vacía, retorna una lista vacía.
    if len(l_final) == 0:
        return []
    
    # Quita el último salto de línea agregado.
    l_final[-1] = l_final[-1][:-1]  

    # Retorna la lista con las líneas encriptadas/desencriptadas.
    return l_final  

   
def escribir_lineas(arc_d: str, l_final: list[str]) -> None:
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
    # if len de texto es 0 terminar code y no hacer que se ejecute lo otro
    #Si el archivo de origen está vacio, lo avisa y termina el codigo. 
    if len(l_final) == 0:
        print('El arcivo a encriptar está vacio, no se ha realizado nada.')
    
    else:
        escribir_lineas(arc_d, l_final)
        print('Archivo encriptado.')
   

if __name__ == "__main__":
    main()
