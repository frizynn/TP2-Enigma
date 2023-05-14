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

    # Flag para salir del bucle si el archivo ingresado existe.
    archivo_invalido = True

    while archivo_invalido is True:

        # Solicita el nombre del archivo al usuario.
        arc_o = input(pedido)
        try:
            # Intenta abrir el archivo. Si se puede abrir, sale del bucle.
            open(arc_o).close()
            archivo_invalido = False
        except FileNotFoundError:
            # Si no se puede abrir el archivo, muestra un mensaje de error y solicita nuevamente el nombre del archivo.
            print("...\nNo se pudo abrir el archivo")

    # Retorna el nombre del archivo existente.
    return arc_o

def pedir_clave() -> str:
    """
    Solicita al usuario que ingrese una clave que contenga solo letras del alfabeto inglés en miúscula, y devuelve la clave como una cadena.

    Returns:
        clave_real (str): La clave ingresada por el usuario como una cadena de letras del alfabeto inglés.
    """
   
    # Flag para indicar si la clave es inválida.
    
    clave_invalida = True

    # Bucle que se repetirá mientras la clave sea inválida.
    while clave_invalida:

        # Si la clave es válida, se establece clave_invalida en False para salir del bucle.
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
    # Flag que indica si el nombre de archivo es inválido.
    archivo_invalido = True 

    # Flag que indica si se puede sobrescribir el archivo.
    archivo_no_sobreescripto = True  

    # Mientras el archivo es inválido o no se puede sobrescribir, se repite el bucle.
    while archivo_invalido or archivo_no_sobreescripto:

        # Si el archivo es inválido, solicita el nombre del archivo de destino.
        if archivo_invalido:  
            arc_d = input(f"Ingrese nombre del archivo para la {'des' if opc else ''}encripción: ")
        
        # Verifica si el nombre ingresado está vacío.
        if len(arc_d) == 0: 
            print("No ingresó un nombre válido")
        else:
            # Trata de abrir el archivo.
            try:
                with open(arc_d, 'x'):
                    archivo_no_sobreescripto = False
                    archivo_invalido = False
            
            except FileExistsError:
                # Si el archivo ya existe, pregunta al usuario si desea sobreescribirlo.
                sobrescribir = input("El archivo ya existe, ¿desea sobrescribirlo? (Y/N) ").lower()

                # Si desea hacerlo, sale del bucle.
                if sobrescribir == 'y':
                    archivo_no_sobreescripto = False
                    archivo_invalido = False

                # Sino, vuelve a pedir el nombre del archivo
                elif sobrescribir == 'n':
                    archivo_invalido = True

                # Si ingresa una respuesta inválida, entra de nuevo al bucle, pero sin pedir el archivo.
                else:
                    print('No ingresó una respuesta válida. Intente de vuelta. ')
                    archivo_invalido = False

    return arc_d 




def des_encripcion(arc_o:str, clave:str, opc:bool) -> list:
    """
    Desencripta o encripta un archivo de texto. Sólo lo hace con letras del alfabeto inglés en minúsculas (case insensitive).

    Args:
        arc_o (str): Nombre del archivo de origen.
        clave (str): Clave para la encriptación/desencriptación.
        opc (bool): Indicador de operación (True para desencriptar, False para encriptar).

    Returns:
        l_final (list): Lista con las líneas encriptadas o desencriptadas, con todas las letras del alfabeto inglés en minúsculas. 
    """

    # Lista para guardar las líneas encriptadas/desencriptadas.
    l_final = []

    # Índice para iterar sobre la clave.
    index = 0 

    # Abre el archivo de origen y lee cada línea.
    with open(arc_o) as f:
        for linea in f:

            # Lista para guardar los caracteres de cada línea.
            l_chars = [] 

            #Itera sobre cada linea del archivo, sacandole el \n del final, y convirtiendo todas sus letras en minúscula.
            for letra in linea.rstrip().lower():

                # Checkea si el carácter actual de la línea es una letra minúscula del alfabeto inglés.
                if ord(letra) in range(97, 123):

                    # Calcula el cambio de la letra según la clave y si se encripta o desencripta.
                    cambio_letra = chr(((ord(letra) - 97 + (1 if opc else -1) * (ord(clave[index]) - 97)) % 26) + 97)

                    # Lo agrega a la lista de caracteres con la encriptación o desencripción necesaria.
                    l_chars.append(cambio_letra)

                    # Actualiza el índice de la clave.
                    index = (index + 1) % len(clave)  
                
                # Si el caracter no es una letra del 
                else:

                    # Agrega el carácter tal cual si no es una letra minúscula.
                    l_chars.append(letra)

            # Agrega la línea encriptada/desencriptada a la lista final.
            l_final.append("".join(l_chars) + "\n")  

    # Si la lista que contiene a las líneas encriptadas o desencriptadas está vacía, retorna una lista vacía.
    if len(l_final) == 0:
        return []
    
    # Quita el último salto de línea agregado.
    l_final[-1] = l_final[-1][:-1]  

    # Retorna la lista con las líneas encriptadas/desencriptadas.
    return l_final  

   
def escribir_lineas(arc_d: str, l_final: list[str]):
    """
    Escribe una lista de cadenas en un archivo. No posee returns.

    Args:
        arc_d (str): Ruta del archivo a escribir.
        l_final (list[str]): Lista de cadenas a escribir en el archivo.
    """
    # Abre el archivo en modo escritura y guarda el objeto de archivo en la variable 'f'.
    with open(arc_d, "w") as f:

        # Escribe las cadenas en el archivo.
        f.writelines(l_final)


def main():
    """  

    Función principal. Realiza la ejecución del programa de encripción de un archivo (utilizando el Cifrado de Vigenère)
    Lo encriptan mediante una clave ingresada por el usuario.
    Lo guarda en un archivo también elegido por el usuario (preexistente o creado en el momento).
    
    """
    print("≡≡Desencriptador de Cifrado de Vigenère≡≡")

    # Se pide al usuario el nombre del archivo encriptado, la clave y el nombre del archivo destino
    arc_o = pedir_nombre_archivo("Ingrese nombre del archivo en texto plano: ")
    clave = pedir_clave()
    arc_d = pedir_nombre_archivo_destino(False)

    # Se realiza la encripción del archivo y se almacena el resultado en una lista
    l_final = des_encripcion(arc_o, clave,True)
    
    #Si la lista está vacía, lo avisa y termina el codigo. 
    if len(l_final) == 0:
        print('El arcivo a encriptar está vacio, no se ha realizado nada.')
    
    # Si la lista tiene elementos, se escribe en el archivo destino y se imprime un mensaje de éxito.
    else:
        escribir_lineas(arc_d, l_final)
        print('Archivo encriptado.')
        print(f"\n---------------------------------\n\nLa encriptación se guardó en el archivo '{arc_d}'\n\n---------------------------------\n")
   
# Si este es el archivo principal, ejecuta la función principal.
if __name__ == "__main__":
    main()
