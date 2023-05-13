from p1_35477_35355_tp2 import pedir_clave, pedir_nombre_archivo, pedir_nombre_archivo_destino, des_encripcion, escribir_lineas

def main():
    """
    Función principal del programa que realiza la desencripción (utilizando el Cifrado de Vigenère) de un archivo encriptado utilizando la clave 
    ingresada por el usuario y lo guarda en un nuevo archivo.
    """

    # Se pide al usuario el nombre del archivo encriptado, la clave y el nombre del archivo destino
    print("≡≡Desencriptador de Cifrado de Vigenère≡≡")
    arc_o = pedir_nombre_archivo("Ingrese nombre del archivo encriptado: ")
    clave = pedir_clave()
    arc_d = pedir_nombre_archivo_destino(True)

    # Se realiza la desencripción del archivo y se almacena el resultado en una lista
    l_final = des_encripcion(arc_o, clave,False)

    # Si la lista está vacía, se imprime un mensaje informando que el archivo encriptado estaba vacío
    if len(l_final) == 0:
        print("El archivo encriptado está vacío, no se ha realizado nada.")
    
    # Si la lista tiene elementos, se escribe en el archivo destino y se imprime un mensaje de éxito
    else:
        escribir_lineas(arc_d, l_final)
        print(f"\n---------------------------------\n\nLa desencripción se guardó en el archivo '{arc_d}'\n")

if __name__ == "__main__":
    main()
