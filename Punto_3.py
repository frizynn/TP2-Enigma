import matplotlib.pyplot as plt
from P2 import pedir_nombre_archivo

def arc_to_only_letters(arc:str) -> str:
    texto = ""
    with open(arc) as f:
        lineas = f.readlines()
    for linea in lineas:
        for caracter in linea:
            if caracter.isalpha():
                texto += caracter
    return texto

def Fi(letra:str, texto:str) -> int:
    cantidad = 0
    for i in texto:
        if i == letra:
            cantidad += 1
    return cantidad

def IoC(texto:str) -> int:
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    valores = []
    for letra in letras:
        valores.append(Fi(letra, texto) * (Fi(letra, texto) - 1))
    promedio = sum(valores) / (len(texto) * (len(texto) - 1))
    return promedio

def IoC_individual(texto:str) -> int:
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lista_final = []
    for letra in letras:
        promedio = (Fi(letra, texto) * (Fi(letra, texto) - 1)) / (len(texto) * (len(texto) - 1))
        lista_final.append((letra, promedio))
    return lista_final

def Friedman_graph(texto:str):
    lista = []
    l = [(0, 0)]
    # probamos con largos de clave de 1 a 30:
    for num in range(1, 31):
        l_aux = []
        for index in range(num):
            str_aux = ""
            while index < len(texto):
            # HAY Q ESTAR SEGURO Q ESTO FUNCIONA
                str_aux += texto[index]
                index += num
            l_aux.append(IoC(str_aux))
            #l_aux.append(str_aux)         # Podría hacer directamente el IoC acá y dsp abajo un promedio
        promedio_IoC = sum(l_aux) / len(l_aux)
        if promedio_IoC >= 0.06:
            lista.extend(l_aux) # NO LOS TENGO PARA CADA LETRA, SINO PARA CADA VALOR (0, 1, 2, 3, 4) PHUCKIN SHIT
        l.append((num, promedio_IoC))

    #GRÁFICO
    x = [i[0] for i in l]
    y = [i[1] for i in l]
    plt.bar(x, y)
    plt.axhline(y=0.0686, color="black", linestyle="--")
    plt.axhline(y=0.0385, color="black", linestyle="--")
    plt.xlabel("Largo de la clave")
    plt.ylabel("Indice de coincidencia")
    plt.show()

    for tupla in l:
        if tupla[1] >= 0.06:             # NO ES EXACTAMENTE EL VALOR QUE NOS PASARON
            return tupla[0]

def freq_analysis(largo:int, texto:str):
    # Según el largo de la clave, recorremos el texto con indexado, y sacamos el IoC de cada letra, de cada array según el largo, y hacemos el gráfico.
    ENGLISH_LETTERS_FRECUENCIES = {
    "a": 0.08167, "b": 0.01492, "c": 0.02782, "d": 0.04253, "e": 0.12702, "f": 0.02228,
    "g": 0.02015, "h": 0.06094, "i": 0.06966, "j": 0.00153, "k": 0.00772, "l": 0.04025,
    "m": 0.02406, "n": 0.06749, "o": 0.07507, "p": 0.01929, "q": 0.00095, "r": 0.05987,
    "s": 0.06327, "t": 0.09056, "u": 0.02758, "v": 0.00978, "w": 0.02360, "x": 0.00150,
    "y": 0.01974, "z": 0.00075
    }
    l_x = []
    l_y = []
    for x, y in ENGLISH_LETTERS_FRECUENCIES.items():
        l_x.append(x)
        l_y.append(y)
    
    plt.subplot(largo // 2 + largo % 2,2,1)
    plt.bar(l_x, l_y)
    plt.title("Inglés")
    plt.ylabel("Frecuencia")

    pos = 2

    for index in range(largo):
        str_aux = ""
        while index < len(texto):
            str_aux += texto[index]
            index += largo

        valores = IoC_individual(str_aux)

        x = [i[0] for i in valores]
        y = [i[1] for i in valores]

        plt.subplot(largo // 2 + largo % 2, 2, pos)
        plt.bar(x, y)
        plt.ylabel("Frecuencia")
        plt.xlabel(f"Letra {index+1}")
        pos +=1


    
    plt.show()

def main():
    arc = pedir_nombre_archivo()
    texto = arc_to_only_letters(arc)
    largo_clave = Friedman_graph(texto)
    freq_analysis(largo_clave, texto)

if __name__ == "__main__":
    main()
