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

def IoC(letras:list, texto:str) -> int:
    valores = []
    for letra in letras:
        valores.append(Fi(letra, texto) * (Fi(letra, texto) - 1))
    promedio = sum(valores) / len(texto) * (len(texto) - 1)
    return promedio

def Friedman_graph(texto:str):
    l = []
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
            l_aux.append(IoC(str_aux, texto))
            #l_aux.append(str_aux)         # Podría hacer directamente el IoC acá y dsp abajo un promedio
        promedio_IoC = sum(l_aux) / len(l_aux)
        l.append(promedio_IoC)
    # ACÁ IRÍA EL GRÁFICO
    for promedio in l:
        if promedio >= 0.068:             # NO ES EXACTAMENTE EL VALOR QUE NOS PASARON
            return promedio

def freq_analysis(ing_dict:dict, i:int):
    # Según el largo de la clave, recorremos el texto con indexado, y sacamos el IoC de cada letra, de cada array según el largo, y hacemos el gráfico.
    pass

# leer el archivo


#LLAMAMOS FRIEDMAN GRAPH
# para cada largo, hacemos la formula del índice de coincidencia, y después lo promediamos (?
# ese valor que nos da por cada largo de la clave, lo almacenamos (lista?) ya que tenemos que imprimir un gráfico que muestre cuánto da ese valor para cada largo
# imprimimos el gráfico, con valores del 0 al 30 en x, y con valores del 0% al 7% en y. además, una recta y = 3,85% y otra y = 6,86%.

#   TENGO QUE DIVIDIR EL TEXTO SEGÚN LA CLAVE QUE ME QUEDÓ, Y ASI PUEDO ANALIZAR LA FRECUENCIA DE CADA LETRA SEGÚN ESAS POSICIONES. ESO ESO ESO, POSICIONES, NO DIVIDIR EL TEXTO GOOOD.

# mostrar los dos graficos.
def main():
    arc = pedir_nombre_archivo()
