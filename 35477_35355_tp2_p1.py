print("≡≡Encriptador de Cifrado de Vigenère≡≡")
while True:
    arc_o = input("Ingrese nombre del archivo en texto plano: ")
    try:
        open(arc_o).close()
        break
    except:
        print("No se pudo abrir el archivo")

while True:
    clave = input("Ingrese la clave: ")
    if clave.isalpha():
        clave = clave.lower()
        break
    else:
        print("La clave solo puede contener letras del alfabeto inglés")

#ESTO ES NECESARIO? SI
while True:
    arc_d = input("Ingrese nombre del archivo para la encripción:")
    if arc_d == arc_o:
        rta = input("Ha ingresado el mismo archivo de origen que distino. Está seguro de que quiere sobreescribir los datos? (Y/N)")
        if rta == "Y":
            break
    else:
        break

l_lineas = []
index = 0
s_aux = ""
l_final = []

with open(arc_o) as f:
    lineas = f.readlines()
for linea in lineas:
    l_lineas.append(linea.rstrip().lower())
for i in l_lineas:
    s_aux = ""
    for letra in i:
        if letra.isalpha():
            cambio_letra = chr(((ord(letra) - 97 + ord(clave[index]) - 97) % 26) + 97)
            s_aux += cambio_letra
            if len(clave) - 1 == index:
                index = 0
            else:
                index += 1
        else:
            s_aux += letra
    l_final.append(s_aux + "\n")
l_final[-1] = l_final[-1][:-1]
with open(arc_d, "w") as f:
    f.writelines(l_final)

