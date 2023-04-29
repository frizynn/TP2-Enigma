import matplotlib.pyplot as plt
from P2 import pedir_nombre_archivo

def arc_to_str(arc:str) -> str:
    texto = ""
    with open(arc) as f:
        l = f.readlines()
    for i in l:
        texto += i
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
    # probamos con largos de clave de 1 a 30:
    for i in range(1, 30):
        l = []
    # división del texto según el largo de la contra (i)
        for grupo in grupos_de_letras:
            l.append(IoC(grupo, texto))
        promedio = sum(l) / len(grupos_de_letras)
        pass
    if i == 0.0686:
        return i             # ESTO ES CUALQUIER COSA PARA ENTENDERME

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
