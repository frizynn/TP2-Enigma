import matplotlib.pyplot as plt
from P2 import pedir_nombre_archivo

def file_to_letters(arc:str) -> str:
    with open(arc) as f:
        lineas = f.readlines()
    print(''.join(caracter for linea in lineas for caracter in linea if caracter.isalpha()))
    return ''.join(caracter for linea in lineas for caracter in linea if caracter.isalpha())

def fi(letra:str, texto:str) -> int:
    return texto.count(letra)

def IoC(texto:str) -> int:
        
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    valores = []
    for letra in letras:
        valores.append(fi(letra, texto) * ( fi(letra, texto) - 1))
    
    divisor = (len(texto) * (len(texto) - 1))
    print(divisor)
    if divisor == 0: #EST0 HAY QUE MEJORARLO Y CORREJIRLO PERO BASICAMENTE ES ALGO ASI. SE TENDRIA QUE PONER UN RETURN 0 Y QUE SE TERMINE EL PROGRAMA. PEDIR AYUDA WA WA WA AAAAA :( es la facuseñal
        print('Divisor es 0 ')
        return None
    else:
        promedio = sum(valores) / divisor
        return promedio
    
    

def aparicion_individual(texto:str) -> int:
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lista_final = []
    for letra in letras:
        promedio = fi(letra, texto) / (len(texto))
        lista_final.append((letra, promedio))
    return lista_final


def Friedman_graph(texto:str) -> int:
    lista = []
    l = [(0, 0)]
    for num in range(1, 31):
        l_aux = []
        for index in range(num):
            texto_aux = texto[index::num]
            print(texto_aux)
            if len(texto_aux) > 1:
                l_aux.append(IoC(texto_aux)) #SOY UN SIGMA A TU PUTA CASA WHILE DE MIERDA. este metodo lo puedo usar en freq analisis (largo de la clave)
        
        if len(l_aux) > 0:
            promedio_IoC = sum(l_aux) / len(l_aux)
            if promedio_IoC >= 0.06:
                lista.extend(l_aux) #GOD FACU CON ESTO ALTO CRACK CHABON 200IQ
            l.append((num, promedio_IoC))

    x, y = zip(*l) #A TU PUTA CASA. GRACIAS GUILLE POR EL PROTIP. Recorre a la vez los elem de l
    plt.bar(x, y)
    plt.axhline(y=0.0686, color="black", linestyle="--")
    plt.axhline(y=0.0385, color="black", linestyle="--")
    plt.xlabel("Largo de la clave")
    plt.ylabel("Indice de coincidencia")
    plt.show()

    for tupla in l:
        if tupla[1] >= 0.06:
            return tupla[0]
    return -1
        
def freq_analysis(largo:int, texto:str):
    if largo == -1:
        return None # O UN MENSAJE DE ERROR
    # Según el largo de la clave, recorremos el texto con indexado, y sacamos el IoC de cada letra, de cada array según el largo, y hacemos el gráfico.
    ENGLISH_LETTERS_FRECUENCIES = {
    "a": 0.08167, "b": 0.01492, "c": 0.02782, "d": 0.04253, "e": 0.12702, "f": 0.02228,
    "g": 0.02015, "h": 0.06094, "i": 0.06966, "j": 0.00153, "k": 0.00772, "l": 0.04025,
    "m": 0.02406, "n": 0.06749, "o": 0.07507, "p": 0.01929, "q": 0.00095, "r": 0.05987,
    "s": 0.06327, "t": 0.09056, "u": 0.02758, "v": 0.00978, "w": 0.02360, "x": 0.00150,
    "y": 0.01974, "z": 0.00075
    }

    l_x = list(ENGLISH_LETTERS_FRECUENCIES.keys()) # A TU PUTA CASA, HES DONE IT AGAIN. 
    l_y = list(ENGLISH_LETTERS_FRECUENCIES.values())
    
    plt.subplot(largo // 2 + largo % 2, 2, 1)
    plt.bar(l_x, l_y)
    plt.title("Inglés", fontsize=8)
    plt.ylabel("Frecuencia", fontsize=8)
    plt.subplots_adjust(hspace=0.6, wspace=0.45)

    pos = 2
    for index in range(largo):
        str_aux = ""
        plt.subplot(largo // 2 + largo % 2, 2, pos)
        plt.title(f"Letra {index + 1} de la clave", fontsize=8)

        for j in texto[index::largo]: #es esto de "saltar" x letras. EJ: holanda = hlna. así me ahorro el fucking while 
            str_aux += j

        valores = aparicion_individual(str_aux)

        x = [i[0] for i in valores]
        y = [i[1] for i in valores]

        plt.bar(x, y, label="IoC")
        plt.legend(loc="upper right", fontsize=6.8) #COMO SE VE EL GRAFICO DEPENDE DE COMO LO ABRA LA PC DE CADA UNO. EN LA MIA SE VE BIEN PERO EN LA DE OTRO SE PUEDE VER MAL. TAMBIEN DEPENDE DE QUE TAN GRANDE HAGAS LA PESTANIA
        plt.ylabel("Frecuencia", fontsize=8)

        pos += 1

    plt.show()
    plt.show()

def main():
    arc = pedir_nombre_archivo()
    texto = file_to_letters(arc)
    if len(texto)==0:
        print('Error, archivo vacío')
    else:
        largo_clave = Friedman_graph(texto)
        freq_analysis(largo_clave, texto)


if __name__ == "__main__":
    main()