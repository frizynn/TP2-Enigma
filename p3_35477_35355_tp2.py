import matplotlib.pyplot as plt
from p1_35477_35355_tp2 import pedir_nombre_archivo, des_encripcion, escribir_lineas, pedir_nombre_archivo_destino

def file_to_letters(arc:str) -> str:
    """
    Devuelve una cadena que contiene solo las letras minúsculas presentes en el archivo especificado.

    Args:
        arc (str): Una cadena que representa el nombre y la ruta del archivo.

    Returns:
        texto (str): Una cadena que contiene solo las letras minúsculas presentes en el archivo.

    """
    # Variable para almacenar las letras encontradas en el archivo
    texto = ""  
    with open(arc) as f:  
        # Leer todas las líneas del archivo y almacenarlas en una lista
        lineas = f.readlines() 
    # Iterar por todas las líneas del archivo
    for linea in lineas:  
        for caracter in linea:  
            # Si el caracter es una letra minúscula, agregarlo a la cadena
            if ord(caracter) in range(97, 123):  
                texto += caracter
    return texto  

def comprobar_largo_txt(texto: str) -> bool:
    """
    Comprueba si el texto es lo suficientemente largo para realizar una acción determinada.

    Args:
        texto (str): Una cadena que representa el texto a comprobar.

    Returns:
        decision(bool): True si el texto es lo suficientemente largo, False en caso contrario.

    """
    # Inicializar la variable de decisión como verdadera
    descision = True
    # Si el texto es demasiado corto, solicitar una confirmación para continuar
    if len(texto) < 30:
        if input("El largo del texto no es suficiente para realizar el forzado, desea proceder igualmente? (Y/N)\n").lower() == "y":
            descision = True
        else:
            descision = False
    # Devolver la variable de decisión
    return descision
        
def fi(letra:str, texto:str) -> int:
    """
    Devuelve el número de veces que aparece una letra en un texto.

    Args:
        letra (str): Una cadena que representa la letra a buscar.
        texto (str): Una cadena que representa el texto en el que se buscará la letra.

    Returns:
        (int) Un entero que representa el número de veces que aparece la letra en el texto.

    """
    # Usamos el método count para contar el número de veces que aparece la letra en el texto
    return texto.count(letra)

def IoC(texto:str) -> int:
    """
    Calcula el índice de coincidencia de un texto.

    Args:
        texto (str): Una cadena de texto.

    Returns:
        promedio (int): El índice de coincidencia del texto, como un número entero.

        Si el valor devuelto es -1, significa que se produjo un error en el cálculo debido a que el texto es demasiado corto.

    """
    valores = []

    # Iterar por todas las letras minúsculas en el alfabeto inglés
    for letra in range(97,123):
        # Calcular el valor de frecuencia de la letra actual y agregarlo a la lista de valores
        valores.append(fi(chr(letra), texto) * (fi(chr(letra), texto) - 1))
    
    # Calcular el promedio de los valores y devolverlo como el índice de coincidencia
    if len(texto) * (len(texto) - 1) != 0:
        promedio = sum(valores) / (len(texto) * (len(texto) - 1))
        return promedio
    else:
        return -1

def aparicion_individual(texto: str) -> list:
    """
    Devuelve una lista de tuplas que contiene la frecuencia de aparición individual de cada letra minúscula 
    en el texto dado.

    Args:
        texto (str): Una cadena de caracteres que representa el texto.

    Returns:
        lista_final (list): Una lista de tuplas que contiene la frecuencia de aparición individual de cada letra minúscula en el texto. Cada tupla tiene dos elementos: la letra minúscula y su frecuencia de aparición en el texto.

    """
    lista_final = []
    # Itera por todas las letras minúsculas en ASCII
    for letra in range(97,123):
        # Calcula la frecuencia de aparición de la letra en el texto
        promedio = fi(chr(letra), texto) / (len(texto))
        # Agrega una tupla a la lista con la letra y su frecuencia de aparición
        lista_final.append((chr(letra), round(promedio, 5)))
    return lista_final

def Friedman_graph(texto:str) -> int:
    """ 
    Calcula la longitud de clave más probable en el cifrado Vigenère de un texto dado utilizando el método de Friedman.
    Este método consiste en calcular el índice de coincidencia (IoC) para subcadenas del texto con diferentes longitudes de clave
    y luego graficar los resultados para encontrar el punto en el que el IoC promedio se acerca más a 0.0667 (para el idioma inglés).
    Luego devuelve la longitud de clave más probable. 

    Args:
        texto: Una cadena que representa el texto cifrado con el cifrado Vigenère.

    Returns:
        (int) Un número entero que representa la longitud de clave más probable del cifrado Vigenère utilizado para cifrar el texto dado.
        Si no se puede encontrar una longitud de clave probable, devuelve -1.

    """
    # Inicializar listas y tuplas
    lista = []
    l = [(0, 0)]

    # Iterar a través de las posibles longitudes de clave
    for num in range(1, 31):
        promedios_IoC = []
        # Iterar a través de cada posición en la clave
        for index in range(num):
            # Crear una subcadena a partir del texto original, tomando los caracteres que están separados por una distancia fija igual a la longitud de la clave que se está probando
            subcadena = ""
            while index < len(texto):
                subcadena += texto[index]
                index += num 

            
            # Calcular el índice de coincidencia para la subcadena
            promedio = IoC(subcadena)
            if promedio != -1:
                promedios_IoC.append(promedio)
        
        # Calcular el promedio del índice de coincidencia para esta longitud de clave
        if len(promedios_IoC) != 0:
            promedio_IoC = sum(promedios_IoC) / len(promedios_IoC)
            if promedio_IoC >= 0.06:
                lista.extend(promedios_IoC) 
            l.append((num, promedio_IoC))
        
    # Si no se encontró ninguna clave, devolver -1
    if len(l) == 0:
        return -1

    # Graficar IoC vs longitud de clave
    x = [i[0] for i in l]
    y = [i[1] for i in l]
    plt.bar(x, y)
    plt.axhline(y=0.0686, color="lime", linestyle="--",label = 'IOC texto inglés')
    plt.axhline(y=0.0385, color="red", linestyle="--", label = 'IOC texto aleatorio')
    plt.legend(loc="upper right",fontsize=7)
    plt.xlabel("Largo de la clave")
    plt.ylabel("Indice de coincidencia")
    plt.show()

    # Encontrar la longitud de clave más probable
    for tupla in l:
        if tupla[1] >= 0.06:  # Usamos un umbral para asegurarnos de encontrar una longitud de clave probable
            return tupla[0]
    return -1

def freq_analysis(largo:int, texto:str, letter_freq:dict) -> list:
    """ 
    Analiza la frecuencia de aparición de cada letra en el texto según la longitud de la clave.
    Crea un gráfico con el Índice de Coincidencia (IoC) de las letras de un alfabeto inglés, y para cada letra de la clave. 

    Args:
        largo (int): La longitud de la clave.
        texto (str): El texto a analizar.
        letter_freq (dict): Diccionario con la frecuencia de aparición de las letras en el alfabeto inglés.

    Returns:
        all_vals (list): Una lista con las frecuencias de aparición de cada letra en cada letra de la clave.
    
    
    """
    # Creamos dos listas, una con las letras del alfabeto inglés y otra con sus correspondientes frecuencias
    l_x = list(letter_freq.keys())
    l_y = list(letter_freq.values())

    # Creamos el gráfico para el alfabeto inglés
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

    # Creamos una lista para almacenar las frecuencias de cada letra de la clave
    all_vals = []
    
    # Recorremos cada letra de la clave y creamos un gráfico para cada una
    pos = 2
    for index in range(largo):
        str_aux = ""

        # Creamos el gráfico para la letra actual de la clave
        if largo % 2 != 0:
            plt.subplot(largo // 2 + largo % 2,2,pos)
        else:
            plt.subplot(largo // 2 + (largo+1) % 2,2,pos)
        plt.title(f"Letra {index+1} de la clave",fontsize=8)

        # Obtenemos los caracteres de la cadena de texto que corresponden a la letra actual de la clave
        # En cada iteración, avanzamos la longitud de la clave para obtener el siguiente carácter correspondiente a la letra actual
        while index < len(texto):
            str_aux += texto[index]
            index += largo

        # Obtenemos la frecuencia de cada letra en la cadena de texto de la letra actual de la clave
        valores = aparicion_individual(str_aux)

        # Almacenamos las frecuencias en la lista all_vals
        all_vals.append(valores)

        # Creamos el gráfico de barras con las frecuencias obtenidas
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

def euclidian_distance(a: list[int], b: list[int]) -> int:
    """
    Calcula la distancia Euclidiana entre dos listas de enteros.

    Args:
        a (list[int]): La primera lista de enteros.
        b (list[int]): La segunda lista de enteros.

    Returns:
        int: La distancia Euclidiana entre las dos listas de enteros.
    """
    # Inicializamos la variable suma en cero
    summ = 0
    # Recorremos los elementos de ambas listas simultáneamente
    for num1, num2 in zip(a, b):
        # Calculamos la diferencia entre los elementos de la misma posición en ambas listas, y la elevamos al cuadrado
        diff = (num1 - num2) ** 2
        # Añadimos la diferencia al total acumulado
        summ += diff
    # Calculamos la raíz cuadrada del total acumulado
    return summ ** (0.5)

def desplazamiento_calcular(default_only_appearances:list, IoC_25_letras:list) -> int: 
    """
    Calcula el desplazamiento de la clave a partir de una lista de 25 IoCs y una lista de apariciones de cada letra en el idioma
    en el que está escrito el texto cifrado.
    
    Args:
        default_only_appearances (list): Una lista con las apariciones de cada letra en el idioma en el que está escrito el
        texto cifrado.
        IoC_25_letras (list): Una lista de 25 IoCs para cada letra de la clave.

    Returns:
        desplace (int): El desplazamiento de la clave.
    """
    # Inicializamos las variables necesarias
    euclidian_distances = []
    only_appearance_list = []
    menor = float("inf")
    desplace = -1

    # Creamos una lista con las apariciones de cada letra en cada IoC de la clave
    for lista in IoC_25_letras:
        only_appearance_list.append(lista[1])
    
    # Calculamos la distancia euclidiana para cada posible desplazamiento de la clave
    for i in range(len(IoC_25_letras)):
        # Cambiamos la lista de apariciones de cada letra según el desplazamiento actual
        only_appearance_list_changed = only_appearance_list[i:] + only_appearance_list[:i]
        # Calculamos la distancia euclidiana entre la lista de apariciones y las apariciones por defecto
        euclidian_distances.append((i,euclidian_distance(default_only_appearances, only_appearance_list_changed)))
    
    # Buscamos el desplazamiento con la menor distancia euclidiana
    for i, v in euclidian_distances:
        if v < menor:
            menor = v
            desplace = i
    
    # Devolvemos el desplazamiento
    return desplace

def sacar_clave(largo_clave:int, default:dict, all_IoC:list) -> str:
    """
    Calcula la clave para un cifrado Vigenere a partir de la frecuencia de aparición de las letras en el texto original
    y los Índices de Coincidencia (IoC) obtenidos para cada letra de la clave.

    Args:
        largo_clave (int): La longitud de la clave.
        default (dict): Un diccionario con la frecuencia de aparición de las letras en el alfabeto inglés.
        all_IoC (list): Una lista con las frecuencias de aparición de cada letra en cada letra de la clave.

    Returns:
        str_final (str): La clave calculada para el cifrado Vigenere.

    """
    # Creamos una lista que solo contenga la frecuencia de aparición de cada letra en el alfabeto inglés
    default_only_appearances = []
    for val in default.values():
        default_only_appearances.append(val)

    # Iteramos por cada letra de la clave y calculamos el desplazamiento necesario para obtener la letra correcta de la clave
    str_final = ""
    for i in range(largo_clave):
        # Calculamos el desplazamiento
        desplace = desplazamiento_calcular(default_only_appearances, all_IoC[i])

        # Agregamos la letra correspondiente a la clave
        str_final += chr(desplace + 97)

    return str_final

def main():
    """Función principal que realiza la tarea de forzar la clave de un archivo cifrado.
    Pide al usuario el nombre del archivo a descifrar, lo lee y lo procesa para encontrar la clave
    mediante análisis de frecuencia. Luego escribe las líneas descifradas en un archivo de destino."""
    
    # Un diccionario con las frecuencias de cada letra en inglés
    ENGLISH_LETTERS_FRECUENCIES = {
    "a": 0.08167, "b": 0.01492, "c": 0.02782, "d": 0.04253, "e": 0.12702, "f": 0.02228,
    "g": 0.02015, "h": 0.06094, "i": 0.06966, "j": 0.00153, "k": 0.00772, "l": 0.04025,
    "m": 0.02406, "n": 0.06749, "o": 0.07507, "p": 0.01929, "q": 0.00095, "r": 0.05987,
    "s": 0.06327, "t": 0.09056, "u": 0.02758, "v": 0.00978, "w": 0.02360, "x": 0.00150,
    "y": 0.01974, "z": 0.00075
    }
    
    # Pide al usuario el nombre del archivo a forzar la clave
    arc = pedir_nombre_archivo("Ingrese nombre del archivo a forzar la clave: ")
    
    # Lee el archivo y lo procesa para obtener las letras
    texto = file_to_letters(arc)
    
    # Comprueba si el archivo está vacío y si lo está, imprime un mensaje de error y devuelve None
    if len(texto)==0:
        print('El archivo está vacío, no se puede forzar la clave.')
        return None
    
    # Comprueba si el archivo es lo suficientemente largo para que se pueda analizar
    comprobar_largo = comprobar_largo_txt(texto)
    if not comprobar_largo:
        return None
    
    # Utiliza el método Friedman para encontrar el largo de la clave
    largo_clave = Friedman_graph(texto)
    
    # Si no se puede encontrar la clave, imprime un mensaje de error y devuelve None
    if largo_clave == -1:
        print("No se pudo encontrar la clave.")
        return None
    
    # Realiza un análisis de frecuencia para todas las posibles claves de la longitud encontrada
    all_IoC= freq_analysis(largo_clave, texto, ENGLISH_LETTERS_FRECUENCIES)
    
    # Encuentra la clave que mejor se ajusta a las frecuencias de letras en inglés
    clave = sacar_clave(largo_clave, ENGLISH_LETTERS_FRECUENCIES, all_IoC)
    
    # Imprime la clave encontrada y desencripta el archivo
    print(f"\n---------------------------------\n\nLa clave es '{clave}'.\n\n---------------------------------\n")
    lineas_escribir = des_encripcion(arc, clave, False)
    
    # Pide un archivo destino para escribir el archivo desencriptado
    nombre = pedir_nombre_archivo_destino(True)
    escribir_lineas(nombre, lineas_escribir)

    print(f"\n---------------------------------\n\nSe guardó como archivo desencriptado en {nombre}.\n")

if __name__ == "__main__":
    main()