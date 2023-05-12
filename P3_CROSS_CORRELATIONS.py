import matplotlib.pyplot as plt
from p2_35477_35355_tp2 import pedir_nombre_archivo, des_encripcion, escribir_lineas, pedir_nombre_archivo_destino

def file_to_letters(arc:str) -> str:
    texto = ""
    with open(arc) as f:
        lineas = f.readlines()
    for linea in lineas:
        for caracter in linea:
            if ord(caracter) in range(97, 123):
                texto += caracter
    return texto


def comprobar_largo_txt(texto):
    descision = True
    if len(texto) <30:
        if input("El largo del texto no es suficiente para realizar el forzado, desea proceder igualmente? (Y/N)\n").lower() == "y":
            descision = True
        else:
            descision = False
    return descision
        
def fi(letra:str, texto:str) -> int:
    return texto.count(letra)

def IoC(texto:str) -> int:
    valores = []

    for letra in range(97,123):
        valores.append(fi(chr(letra), texto) * (fi(chr(letra), texto) - 1))
    
    if len(texto) * (len(texto) - 1) != 0:
        promedio = sum(valores) / (len(texto) * (len(texto) - 1))
        return promedio
    else:
        return -1

def aparicion_individual(texto:str) -> int:
    lista_final = []
    for letra in range(97,123):
        promedio = fi(chr(letra), texto) / (len(texto))
        lista_final.append((chr(letra), promedio))
    return lista_final

def Friedman_graph(texto:str) -> int:
    lista = []
    l = [(0, 0)]
   
    for num in range(1, 31):
        l_aux = []
        for index in range(num):
            str_aux = ""
            while index < len(texto):
                str_aux += texto[index]
                index += num
            
            promedio = IoC(str_aux)
            if promedio != -1:
                l_aux.append(promedio)
        if len(l_aux) != 0:
            promedio_IoC = sum(l_aux) / len(l_aux)
            if promedio_IoC >= 0.06:
                lista.extend(l_aux) 
            l.append((num, promedio_IoC))
        
    if len(l) == 0:
        return -1

        #GRÁFICO
    x = [i[0] for i in l]
    y = [i[1] for i in l]
    plt.bar(x, y)
    plt.axhline(y=0.0686, color="lime", linestyle="--",label = 'IOC texto inglés')
    plt.axhline(y=0.0385, color="red", linestyle="--", label = 'IOC texto aleatorio')
    plt.legend(loc="upper right",fontsize=7)
    plt.xlabel("Largo de la clave")
    plt.ylabel("Indice de coincidencia")
    plt.show()

    for tupla in l:
        if tupla[1] >= 0.06:             # NO ES EXACTAMENTE EL VALOR QUE NOS PASARON NINGUN VALOR QUE ALCANCEN LOS LARGOS NO CORRECTOS PARA 30 DE LARGO DE CLAVE, SUPERA EL 0.06, Y NINGUN LARGO CORRECTO NO LO ALCANZA. CON ESTE THRESHOLD, NOS ASEGURAMOS ENCONTRARLOS IGUAL, Y EVITAMOS PROBLEMAS.
            return tupla[0]
    return -1

def freq_analysis(largo:int, texto:str) -> list:
    # Según el largo de la clave, recorremos el texto con indexado, y sacamos el IoC de cada letra, de cada array según el largo, y hacemos el gráfico.
    ENGLISH_LETTERS_FRECUENCIES = {
    "a": 0.08167, "b": 0.01492, "c": 0.02782, "d": 0.04253, "e": 0.12702, "f": 0.02228,
    "g": 0.02015, "h": 0.06094, "i": 0.06966, "j": 0.00153, "k": 0.00772, "l": 0.04025,
    "m": 0.02406, "n": 0.06749, "o": 0.07507, "p": 0.01929, "q": 0.00095, "r": 0.05987,
    "s": 0.06327, "t": 0.09056, "u": 0.02758, "v": 0.00978, "w": 0.02360, "x": 0.00150,
    "y": 0.01974, "z": 0.00075
}
    l_x = list(ENGLISH_LETTERS_FRECUENCIES.keys())
    l_y = list(ENGLISH_LETTERS_FRECUENCIES.values())

    if largo % 2 != 0:
        plt.subplot(largo // 2 + largo % 2,2,1)
    else:
        plt.subplot(largo // 2 + (largo+1) % 2,2,1)
    plt.bar(l_x, l_y, label = 'IoC')
    
    plt.xticks(fontsize=8, rotation=15)
    plt.yticks(fontsize=8)
    plt.title("Inglés",fontsize=8)
    plt.legend(loc="upper right",fontsize=8)
    plt.ylabel("Frecuencia",fontsize=8)
    plt.subplots_adjust(hspace=0.6, wspace=0.35, left = 0.114, bottom=0.083, right = 0.94, top = 0.933)

    pos = 2
    
    all_vals = []

    for index in range(largo):
        str_aux = ""

        if largo % 2 != 0:
            plt.subplot(largo // 2 + largo % 2,2,pos)
        else:
            plt.subplot(largo // 2 + (largo+1) % 2,2,pos)
        plt.title(f"Letra {index+1} de la clave",fontsize=8)

        while index < len(texto):
            str_aux += texto[index]
            index += largo

        valores = aparicion_individual(str_aux)

        all_vals.append(valores)

        x = [i[0] for i in valores]
        y = [i[1] for i in valores]

        
        
        plt.bar(x, y,label="IoC")
        plt.xticks(fontsize=8, rotation=15)
        plt.yticks(fontsize=8)
        plt.legend(loc="upper right",fontsize=8)
        plt.ylabel("Frecuencia",fontsize=8)
        
        pos +=1
        
    plt.show()

    return all_vals, ENGLISH_LETTERS_FRECUENCIES

def euclidian_distance(a:list[int], b:list[int]) -> int:
    summ = 0
    for num1, num2 in zip(a, b):
        summ += (num1 - num2) ** 2
    return summ ** (0.5)

def desplazamiento_calcular(default_only_appearances, IoC_25_letras):
    euclidian_distances = []
    only_appearance_list = []
    menor = float("inf")
    desplace = -1
    for lista in IoC_25_letras:
        only_appearance_list.append(lista[1])
    for i in range(len(IoC_25_letras)):  # Debería ser siempre 25...
        only_appearance_list_changed = only_appearance_list[i:] + only_appearance_list[:i]
        euclidian_distances.append((i,euclidian_distance(default_only_appearances, only_appearance_list_changed)))
    for i, v in euclidian_distances:
        if v < menor:
            menor = v
            desplace = i
    return desplace

def sacar_clave(largo_clave, default:dict, all_IoC):
    str_final = ""
    desplaces = []
    default_only_appearances = []
    for val in default.values():
        default_only_appearances.append(val)
    for i in range(largo_clave):
        desplace = desplazamiento_calcular(default_only_appearances, all_IoC[i])
        desplaces.append(desplace)
    for desplac in desplaces:
        str_final += chr(desplac + 97)
    return str_final

def main():
    arc = pedir_nombre_archivo("Ingrese nombre del archivo a forzar la clave: ")
    texto = file_to_letters(arc)
    if len(texto)==0:
        print('Error, archivo vacío')
        return None
    comprobar_largo = comprobar_largo_txt(texto)
    if not comprobar_largo:
        return None

    largo_clave = Friedman_graph(texto)
    if largo_clave == -1:
        print("No se pudo encontrar la clave.")
        return None
    all_IoC, default = freq_analysis(largo_clave, texto)
    clave = sacar_clave(largo_clave, default, all_IoC)
    print(f"\n---------------------------------\n\nLa clave es '{clave}'\n\n---------------------------------\n")
    lineas_escribir = des_encripcion(arc, clave, False)
    nombre = pedir_nombre_archivo_destino(False)
    escribir_lineas(nombre, lineas_escribir)

    print(f"\n---------------------------------\n\nSe guardó en el archivo {nombre}")

if __name__ == "__main__":
    main()