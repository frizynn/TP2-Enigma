from p1_35477_35355_tp2 import pedir_clave, pedir_nombre_archivo, pedir_nombre_archivo_destino, des_encripcion, escribir_lineas

def main():
    print("≡≡Encriptador de Cifrado de Vigenère≡≡")
    arc_o = pedir_nombre_archivo("Ingrese nombre del archivo encriptado: ")
    clave = pedir_clave()
    arc_d = pedir_nombre_archivo_destino(True)
    l_final = des_encripcion(arc_o, clave,False)
    escribir_lineas(arc_d, l_final)

if __name__ == "__main__":
    main()
