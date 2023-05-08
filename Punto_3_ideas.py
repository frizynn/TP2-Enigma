# PONER ARCHIVOS CON BARRA BAJA AL PRINCIPIO 
# QUEDAR AL TANTO DE CÓMO QUEDA LA LÍNEA DE IoC / Friedman Graph
# GRAFICO PARA GUILLE SEGÚN EL LARGO DE LA CLAVE

# TENER EN CUENTA CASOS EN LOS QUE EL LARGO DEL TEXTO SEA MENOR DE 30 (con Y/N)

def pedir_nombre_archivo_destino(arc_o, opc):
    while True:
        arc_d = input(f"Ingrese nombre del archivo para la {'des' if opc else ''}encripción:")
        if arc_d != arc_o or input("Ha ingresado el mismo archivo de origen que destino. Está seguro de que quiere sobreescribir los datos? (Y/N)").lower() == "y":
            break
    return arc_d

# PREGUNTARLE A GUILLE SI LE GUSTÓ

# SOMOS CRACKS PANAAAAAAAAAAAAAAAAAAAAAAAA 🥺👉🏻👈🏻