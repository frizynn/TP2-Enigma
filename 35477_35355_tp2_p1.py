print("≡≡Encriptador de Cifrado de Vigenère≡≡")
  
while True:
    arc_o = input("Ingrese nombre del archivo en texto plano: ") #Tomar archivo 
    try:
        open(arc_o).close() #Comprobar si se puede abrir
        break
    except:
        print("...\nNo se pudo abrir el archivo")

while True:
    clave = input("Ingrese la clave: ") #Ingresar la clave de encriptado
    if clave.isalpha():
        clave = clave.lower()
        break
    else:
        print("...\nLa clave solo puede contener letras del alfabeto inglés") #Chequear si es valida

while True:
    arc_d = input("Ingrese nombre del archivo para la encripción:") #Ingreso del nombre del archivo para la encripción
    if arc_d != arc_o or input("Ha ingresado el mismo archivo de origen que destino. Está seguro de que quiere sobreescribir los datos? (Y/N)").lower() == "y":
        break #Si es el mismo archivo de origen que destino, se pregunta si quiere sobreescribir los datos (Y/N)

l_final = [] 
index = 0

with open(arc_o) as f: #se vuelve a abrir el archivo para comenzar en la primera linea. Se ouede poner en el primer while. 
    for linea in f:
        l_chars = [] 
        for letra in linea.rstrip().lower():
            if letra.isalpha():
                cambio_letra = chr(((ord(letra) - 97 + ord(clave[index]) - 97) % 26) + 97)
                l_chars.append(cambio_letra)
                index = (index + 1) % len(clave) #Se va cambiando la letra de la clave para sumar respectivamente a la letra correspondiente. 
            else:
                l_chars.append(letra)
        l_final.append("".join(l_chars) + "\n") #Se agrega a la lista final el string encriptado 
        
l_final[-1] = l_final[-1][:-1] # se elimina el \n. 
with open(arc_d, "w") as f:
    f.writelines(l_final)

    
