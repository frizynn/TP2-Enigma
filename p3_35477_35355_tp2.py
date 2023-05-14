import matplotlib.pyplot as plt
from p1_35477_35355_tp2 import pedir_nombre_archivo, des_encripcion, escribir_lineas, pedir_nombre_archivo_destino

def file_to_letters(arc:str) -> str:
    """
    Devuelve una cadena que contiene solo las letras minúsculas del alfabeto inglés, presentes en el archivo especificado.

    Args:
        arc (str): Una cadena que representa el nombre y la ruta del archivo.

    Returns:
        texto (str): Una cadena que contiene solo las letras minúsculas presentes en el archivo.
    """
    # Variable para almacenar las letras encontradas en el archivo
    texto = ""

    # Leer todas las líneas del archivo y almacenarlas en una lista.
    with open(arc) as f:  
        lineas = f.readlines() 
    
    # Itera sobre la lista con las lineas del archivo, y dentro de las mismas sobre cada caracter.
    for linea in lineas:  
        for caracter in linea:

            # Si el caracter es una letra minúscula del alfabeto inglés, lo agrega a la cadena.
            if ord(caracter) in range(97, 123):  
                texto += caracter
    
    return texto  
        
def fi(letra:str, texto:str) -> int:
    """
    Devuelve el número de veces que aparece una letra en un texto. Case sensitive.

    Args:
        letra (str): La letra a buscar.
        texto (str): El texto en el que se buscará la letra.

    Returns:
        (int): El número de veces que aparece la letra en el texto.

    """
    # Usamos el método count para contar el número de veces que aparece la letra en el texto
    return texto.count(letra)

def IoC(texto:str) -> float:
    """
    Calcula el índice de coincidencia de un texto. Sólo lo realiza con las letras minúsculas del alfabeto inglés.

    Args:
        texto (str): Una cadena de texto.

    Returns:
        promedio (float): El índice de coincidencia del texto.

        Si el valor devuelto es -1.0, significa que se produjo un error en el cálculo debido a que el texto es demasiado corto.

    """
    valores = []

    # Itera sobre todas las letras minúsculas del alfabeto inglés (en código ASCII).
    for letra in range(97,123):

        # Calcula el valor de frecuencia de la letra actual y lo agrega a la lista de valores.
        valores.append(fi(chr(letra), texto) * (fi(chr(letra), texto) - 1))
    
    # Calcula y devuelve el índice de coincidencia siempre y cuando sea posible.
    if len(texto) * (len(texto) - 1) != 0:
        promedio = sum(valores) / (len(texto) * (len(texto) - 1))
        return promedio
    
    # Si no lo fue, devuelve -1.0
    else:
        return -1.0

def aparicion_individual(texto: str) -> list[tuple[str, float]]:
    """
    Devuelve una lista de tuplas que contiene la frecuencia de aparición individual de cada letra minúscula del alfabeto inglés en el texto dado.

    Args:
        texto (str): Una cadena de caracteres que representa el texto.

    Returns:
        lista_final (list[tuple[str, float]]): Una lista de tuplas que contiene la frecuencia de aparición individual de cada letra minúscula en el texto.
                                               Cada tupla tiene dos elementos: la letra minúscula y su frecuencia de aparición en el texto.

    """
    #Crea la lista final como una lista vacía.
    lista_final = []

    # Itera sobre todas las letras minúsculas del alfabeto inglés (en código ASCII).
    for letra in range(97,123):

        # Calcula la frecuencia de aparición de la letra en el texto
        promedio = fi(chr(letra), texto) / (len(texto))

        # Agrega una tupla a la lista con la letra y su frecuencia de aparición.
        lista_final.append((chr(letra), round(promedio, 5)))
    
    return lista_final

def Friedman_graph(texto:str) -> int:
    """ 
    Calcula la longitud de clave más probable de un texto cifrado con el Cifrado de Vigenère, utilizando el Método Friedman.
    Este método consiste en calcular el índice de coincidencia (IoC) de subcadenas del texto según diferentes longitudes de clave.
    Luego, grafica los resultados y encuentra el punto en el que el IoC del texto supera 0.06 (un poco menos del IoC promedio de un texto en inglés).
    Si la longitud de la posible clave se encuentra entre 1 y 30, devuelve ese valor. 

    Args:
        texto: Una cadena que representa el texto cifrado con el Cifrado de Vigenère.

    Returns:
        (int): La longitud de clave más probable del texto cifrado. Puede valer entre 1 y 30
        Si no se puede encontrar una longitud de clave probable, devuelve -1.

    """
    # Threshold sobre el que buscar el IoC.
    IOC_THRESHOLD = 0.06

    # Lista de tuplas, que contendrán como primer valor el largo posible de la clave, y el IoC del texto en ese caso.
    l = [(0, 0)]

    # Itera a través de las posibles longitudes de clave.
    for num in range(1, 31):

        # Lista que almacena los IoC de los subgrupos creados a partir de cada clave.
        promedios_IoC = []

        # Itera sobre la cantidad de letras que tendría la clave en cada caso.
        for index in range(num):

            # Obtiene los caracteres de la cadena de texto que corresponden a la letra actual de la clave y los almacena en una subcadena.
            # En cada iteración, avanza la longitud de la clave para obtener el siguiente carácter correspondiente a la letra actual.
            subcadena = ""
            while index < len(texto):
                subcadena += texto[index]
                index += num 
            
            # Calcula el índice de coincidencia para la subcadena y lo agrega a la lista de todos los IoC con este largo supuesto.
            promedio = IoC(subcadena)
            if promedio != -1:
                promedios_IoC.append(promedio)
        
        # Calcula el promedio del índice de coincidencia para esta longitud de clave.
        if len(promedios_IoC) != 0:
            promedio_IoC = sum(promedios_IoC) / len(promedios_IoC)
            l.append((num, promedio_IoC))
        
    # Si no se encontró ninguna clave, retorna -1.
    if len(l) == 0:
        return -1

    # Grafica en el eje "x" los posibles largos, y en el "y" sus índices de coincidencias. 
    x = [i[0] for i in l]
    y = [i[1] for i in l]
    plt.bar(x, y)

    #Dibuja dos líneas: La roja reprensenta el IoC de un texto con caraceteres aleatorios, y la verde el IoC de un texto en inglés (el valor que estamos buscando).
    plt.axhline(y=0.0686, color="lime", linestyle="--",label = 'IOC texto inglés')
    plt.axhline(y=0.0385, color="red", linestyle="--", label = 'IOC texto aleatorio')
    plt.legend(loc="upper right",fontsize=7)
    plt.xlabel("Largo de la clave")
    plt.ylabel("Indice de coincidencia")
    plt.show()

    # Itera sobre la lista con los posibles largos y su IoC.
    for tupla in l:

        # Usamos un umbral para asegurarnos de encontrar una longitud de clave probable
        if tupla[1] >= IOC_THRESHOLD:  
            
            # Retorna la primera que encuentre que supere el threshhold
            return tupla[0]
    
    # Si ninguna lo supera, devuelve -1
    return -1

def freq_analysis(largo:int, texto:str, letter_freq:dict) -> list[list[tuple[str, float]]]:
    """ 
    Analiza la frecuencia de aparición de cada letra minúscula del alfabeto inglés en el texto según la longitud de la clave (case sensitive).
    Muestra un gráfico con el índice de aparición de cada letra en un texto inglés promedio.
    Crea un gráfico para cada letra de la clave que muestre lo mismo que el anteriormente descripto.

    Args:
        largo (int): La longitud de la clave.
        texto (str): El texto a analizar.
        letter_freq (dict): Diccionario con la frecuencia de aparición de las letras en un texto inglés promedio.

    Returns:
        all_vals (list[list[tuple[str, float]]]): Una lista con las frecuencias de aparición de cada letra del alfabeto inglés, en cada letra de la clave.
    """
    # Crea dos listas, una con las letras de un texto inglés promedio y otra con sus correspondientes frecuencias.
    l_x = list(letter_freq.keys())
    l_y = list(letter_freq.values())

    # Crea el gráfico para el alfabeto inglés, y lo posiciona arriba a la izquierda.
    if largo % 2 != 0:
        plt.subplot(largo // 2 + largo % 2,2,1)
    else:
        plt.subplot(largo // 2 + (largo+1) % 2,2,1)
    plt.bar(l_x, l_y, label = 'IoC')
    plt.xticks(fontsize=8, rotation=-15)
    plt.yticks(fontsize=8)
    plt.title("Inglés",fontsize=8)
    plt.legend(loc="upper right",fontsize=8)
    plt.ylabel("Frecuencia",fontsize=8)
    plt.subplots_adjust(hspace=0.6, wspace=0.35, left = 0.114, bottom=0.083, right = 0.94, top = 0.933)

    # Lista para almacenar las frecuencias de cada letra de la clave.
    all_vals = []
    
    # Empieza a cargar los gráficos desde la segunda posición (la primera ya está ocupada).
    pos = 2

    # Itera sobre el largo de la clave y creamos un gráfico para cada una.
    for index in range(largo):
        str_aux = ""

        # Crea el gráfico para la letra actual de la clave.
        if largo % 2 != 0:
            plt.subplot(largo // 2 + largo % 2,2,pos)
        else:
            plt.subplot(largo // 2 + (largo+1) % 2,2,pos)
        plt.title(f"Letra {index+1} de la clave",fontsize=8)

        # Obtiene los caracteres de la cadena de texto que corresponden a la letra actual de la clave.
        # En cada iteración, avanza la longitud de la clave para obtener el siguiente carácter correspondiente a la letra actual.
        while index < len(texto):
            str_aux += texto[index]
            index += largo

        # Obtiene la frecuencia de cada letra en la cadena de texto de la letra actual de la clave.
        valores = aparicion_individual(str_aux)

        # Almacena las frecuencias en la lista "all_vals".
        all_vals.append(valores)

        # Crea el gráfico de barras con las frecuencias obtenidas ("x" son las letras, "y" son las frecuencias de aparición).
        x = [i[0] for i in valores]
        y = [i[1] for i in valores]

        plt.bar(x, y,label="IoC")
        plt.xticks(fontsize=8, rotation=-15)
        plt.yticks(fontsize=8)
        plt.legend(loc="upper right",fontsize=8)
        plt.ylabel("Frecuencia",fontsize=8)
        
        pos +=1
    

    plt.show()


    return all_vals

def euclidian_distance(a: list[float], b: list[float]) -> float:
    """
    Calcula la distancia euclidiana entre dos listas de números.

    Args:
        a (list[float]): La primera lista de números.
        b (list[float]): La segunda lista de números.

    Returns:
        (float): La distancia euclidiana entre las dos listas de números.
    """
    # Inicializa la variable suma en cero.
    summ = 0

    # Recorre los elementos de ambas listas simultáneamente.
    for num1, num2 in zip(a, b):

        # Calcula el cuadrado de la diferencia de los elementos de las listas en la misma posición.
        diff = (num1 - num2) ** 2

        # Añade la diferencia al total acumulado.
        summ += diff
    
    # Calcula la raíz cuadrada del total acumulado.
    return summ ** (0.5)

def desplazamiento_calcular(default_only_appearances:list, freq_25_letras:list[tuple[str, float]]) -> int: 
    """
    Calcula el desplazamiento generado por una letra de la clave en un texto encriptado según el Cifrado de Vigenère. Case sensitive.
    
    Args:
        default_only_appearances (list): Lista con las apariciones de cada letra minúscula del alfabeto inglés, respectivamente (la lista está ordenada de la "a" a la "z").
        freq_25_letras (list[tuple[str, float]]): Lista con una frecuencia de aparición de cada letra minúscula del alfabeto inglés en un respectivo texto.

    Returns:
        desplace (int): El desplazamiento de la clave.
    """
    # Inicializa variables necesarias
    euclidian_distances = []
    only_appearance_list = []
    menor = float("inf")
    desplace = -1

    # Crea una lista que contiene sólo las apariciones de cada letra en el texto.
    for tupla in freq_25_letras:
        only_appearance_list.append(tupla[1])
    
    # Calcula la distancia euclidiana para cada posible desplazamiento de la clave.
    for i in range(len(freq_25_letras)):

        # Cambia la lista de apariciones de cada letra según el desplazamiento actual.
        only_appearance_list_changed = only_appearance_list[i:] + only_appearance_list[:i]

        # Calcula la distancia euclidiana entre la lista de apariciones desplazada y las apariciones por defecto.
        euclidian_distances.append((i,euclidian_distance(default_only_appearances, only_appearance_list_changed)))
    
    # Busca el desplazamiento con la menor distancia euclidiana.
    for i, v in euclidian_distances:
        if v < menor:
            menor = v
            desplace = i
    
    # Retorna el desplazamiento con menor distancia euclidiana.
    return desplace

def sacar_clave(largo_clave:int, default:dict, all_IoC:list[list[tuple[str, float]]]) -> str:
    """
    Calcula la clave para un texto encriptado con el Cifrado de Vigenère.
    Lo hace a partir de la frecuencia de aparición de las letras minúsculas del alfabeto inglés en cada caracter de la clave,
    y la frecuencia de aparición común de un texto inglés.

    Args:
        largo_clave (int): La longitud de la clave.
        default (dict): Un diccionario con la frecuencia de aparición de las letras en un texto inglés promedio.
        all_IoC (list[list[tuple[str, float]]]): Lista que contiene una lista con tuplas, que a su vez que contienen cada letra minúscula del alfabeto inglés con su respectiva frecuencias de aparición en el texto.
                                                 Dentro de la listsa "madre", hay una lista de frecuencias por cada letra de la clave.

    Returns:
        clave (str): Clave forzada.
    """
    # Cadena vacía que se rellenará con las letras de la clave.
    clave = ""

    # Crea una lista que solo contiene la frecuencia de aparición de cada letra en un texto inglés promedio.
    default_only_appearances = []
    for val in default.values():
        default_only_appearances.append(val)

    # Itera sobre el largo de la clave y calcula el desplazamiento necesario para obtener la letra correcta de la clave.
    for i in range(largo_clave):

        # Calcula el desplazamiento.
        desplace = desplazamiento_calcular(default_only_appearances, all_IoC[i])

        # Agrega la letra correspondiente a la cadena.
        clave += chr(desplace + 97)

    return clave

def main():
    """
    Función principal. Fuerza la clave de un archivo cifrado.
    Pide al usuario el nombre del archivo a descifrar, lo lee y lo procesa para encontrar la clave.
    Muestra un gráfico de barras con el valor posible de la clave como más alto.
    Además, muestra otro grupo de gráficos de barras, donde el primero es la frecuencias de aparición de cada letra en un texto inglés promedio, y los demás son lo mismo pero con cada subgrupo del texto generado a partir del largo de la clave.
    Al final, escribe las líneas descifradas en un archivo destino elegido por el usuario.
    """
    
    # Un diccionario con las frecuencias de aparición de cada letra en un texto inglés promedio.
    ENGLISH_LETTERS_FRECUENCIES = {
    "a": 0.08167, "b": 0.01492, "c": 0.02782, "d": 0.04253, "e": 0.12702, "f": 0.02228,
    "g": 0.02015, "h": 0.06094, "i": 0.06966, "j": 0.00153, "k": 0.00772, "l": 0.04025,
    "m": 0.02406, "n": 0.06749, "o": 0.07507, "p": 0.01929, "q": 0.00095, "r": 0.05987,
    "s": 0.06327, "t": 0.09056, "u": 0.02758, "v": 0.00978, "w": 0.02360, "x": 0.00150,
    "y": 0.01974, "z": 0.00075
    }
    
    # Pide al usuario el nombre del archivo a forzar la clave.
    arc = pedir_nombre_archivo("Ingrese nombre del archivo a forzar la clave: ")
    
    # Lee el archivo y lo procesa para obtener las letras.
    texto = file_to_letters(arc)
    
    # Comprueba si el archivo está vacío y si lo está, imprime un mensaje de error y retorna "None".
    if len(texto) == 0:
        print('El archivo está vacío, no se puede forzar la clave.')
        return None
    
    # Utiliza el método Friedman para encontrar el largo de la clave.
    largo_clave = Friedman_graph(texto)
    
    # Si no se puede encontrar la clave, imprime un mensaje de error y retorna "None".
    if largo_clave == -1:
        print("No se pudo encontrar la clave.")
        return None
    
    # Realiza un análisis de frecuencia de cada letra del abecedario en el subgrupo del texto generado a partir del largo de la clave encontrado.
    all_IoC= freq_analysis(largo_clave, texto, ENGLISH_LETTERS_FRECUENCIES)
    
    # Encuentra la clave que mejor se ajusta a las frecuencias de las letras.
    clave = sacar_clave(largo_clave, ENGLISH_LETTERS_FRECUENCIES, all_IoC)
    
    # Imprime la clave encontrada y desencripta el archivo.
    print(f"\n---------------------------------\n\nLa clave es '{clave}'.\n\n---------------------------------\n")
    lineas_escribir = des_encripcion(arc, clave, False)
    
    # Pide un archivo destino para escribir el archivo desencriptado.
    nombre = pedir_nombre_archivo_destino(True)
    escribir_lineas(nombre, lineas_escribir)

    print(f"\n---------------------------------\n\nSe guardó como archivo desencriptado en {nombre}.\n")

# Si este es el archivo principal, ejecuta la función principal.
if __name__ == "__main__":
    main()