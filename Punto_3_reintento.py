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

def Friedman_graph(texto:str):
    l = [(0, 0)]
    # probamos con largos de clave de 1 a 30:
    for num in range(1, 31):
        index = 0
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
        l.append((num, promedio_IoC))
    print(l)
    # ACÁ IRÍA EL GRÁFICO
    for tupla in l:
        if tupla[1] >= 0.068:             # NO ES EXACTAMENTE EL VALOR QUE NOS PASARON
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
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    d_final = {}
    for i in range(largo):
        d_aux = {}
        str_aux = ""
        index = i
        while index < len(texto):
            str_aux += texto[index]
            index += largo
        for letra in letras:
            d_aux[letra] = IoC(letra, str_aux)
        d_final[i] = d_aux
    # Para este momento tenemos un diccionario con todos los valores de cada letra segun el IoC según el primer index del largo de la clave (o sea que en el ejemplo del profe tendríamos 5 diccionarios, con llaves 0, 1, 2, 3, 4)
    # Acá iría el gráfico


#LLAMAMOS FRIEDMAN GRAPH
# para cada largo, hacemos la formula del índice de coincidencia, y después lo promediamos (?
# ese valor que nos da por cada largo de la clave, lo almacenamos (lista?) ya que tenemos que imprimir un gráfico que muestre cuánto da ese valor para cada largo
# imprimimos el gráfico, con valores del 0 al 30 en x, y con valores del 0% al 7% en y. además, una recta y = 3,85% y otra y = 6,86%.

#   TENGO QUE DIVIDIR EL TEXTO SEGÚN LA CLAVE QUE ME QUEDÓ, Y ASI PUEDO ANALIZAR LA FRECUENCIA DE CADA LETRA SEGÚN ESAS POSICIONES. ESO ESO ESO, POSICIONES, NO DIVIDIR EL TEXTO GOOOD.

# mostrar los dos graficos.
def main():
    arc = pedir_nombre_archivo()
    texto = arc_to_only_letters(arc)
    largo_clave = Friedman_graph(texto)

if __name__ == "__main__":
    main()
