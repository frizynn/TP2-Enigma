from p1_35477_35355_tp2 import pedir_clave, pedir_nombre_archivo, pedir_nombre_archivo_destino, des_encripcion, escribir_lineas

def main():
    """

    Función principal que realiza la ejecución del programa de desencripción de un archivo (encriptado anteriormente con el Cifrado de Vigenère).
    Lo desencripta mediante la clave con la que fue encriptado (que debe ser ingresada por el usuario).
    Guarda el texto desencriptado en un archivo elegido por el usuario (preexistente o creado en el momento).

    """
    print("≡≡Desencriptador de Cifrado de Vigenère≡≡")

    # Se pide al usuario el nombre del archivo encriptado, la clave y el nombre del archivo destino
    arc_o = pedir_nombre_archivo("Ingrese nombre del archivo encriptado: ")
    clave = pedir_clave()
    arc_d = pedir_nombre_archivo_destino(True)

    # Se realiza la desencripción del archivo y se almacena el resultado en una lista
    l_final = des_encripcion(arc_o, clave,False)

    # Si la lista está vacía, se imprime un mensaje informando que el archivo encriptado estaba vacío
    if len(l_final) == 0:
        print("El archivo encriptado está vacío, no se ha realizado nada.")
    
    # Si la lista tiene elementos, se escribe en el archivo destino y se imprime un mensaje de éxito.
    else:
        escribir_lineas(arc_d, l_final)
        print(f"\n---------------------------------\n\nLa desencripción se guardó en el archivo '{arc_d}'\n\n---------------------------------\n")

# Si este es el archivo principal, ejecuta la función principal.
if __name__ == "__main__":
    main()
