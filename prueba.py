def sacar_clave(largo_clave, default:dict, all_IoC):
    str_final = ""
    default_only_appearances = []
    for val in default.values():
        default_only_appearances.append(val)
    for i in range(largo_clave):
        desplace = desplazamiento_calcular(default_only_appearances, all_IoC[i])
        str_final += chr(desplace + 97)
    return str_final
def desplazamiento_calcular(default_only_appearances, IoC_25_letras):
    euclidian_distances = []
    only_appearance_list = []
    menor = float("inf")
    desplace = -1
    for lista in IoC_25_letras:
        only_appearance_list.append(lista[1])
    for i in range(len(IoC_25_letras)): # Debería ser siempre 25...
        only_appearance_list_changed = only_appearance_list[i:] + only_appearance_list[:i]
        euclidian_distances.append((i,euclidian_distance(default_only_appearances, only_appearance_list_changed)))
    for i, v in euclidian_distances:
        if v < menor:
            menor = v
            desplace = i
    return desplace
def euclidian_distance(a:list[int], b:list[int]) -> int:
    summ = 0
    for num1, num2 in zip(a, b):
        summ += (num1 - num2) ** 2
    return summ ** (0.5)

default = {
    "a": 0.08167, "b": 0.01492, "c": 0.02782, "d": 0.04253, "e": 0.12702, "f": 0.02228,
    "g": 0.02015, "h": 0.06094, "i": 0.06966, "j": 0.00153, "k": 0.00772, "l": 0.04025,
    "m": 0.02406, "n": 0.06749, "o": 0.07507, "p": 0.01929, "q": 0.00095, "r": 0.05987,
    "s": 0.06327, "t": 0.09056, "u": 0.02758, "v": 0.00978, "w": 0.02360, "x": 0.00150,
    "y": 0.01974, "z": 0.00075
}

largo_clave = 29
all_IoC = [[('a', 0.02287), ('b', 0.04158), ('c', 0.06029), ('d', 0.0), ('e', 0.00624), ('f', 0.04366), ('g', 0.03534), ('h', 0.05821), ('i', 0.08732), ('j', 0.00832), ('k', 0.00208), ('l', 0.08316), ('m', 0.07277), ('n', 0.09148), ('o', 0.02287), ('p', 0.01247), ('q', 0.01871), ('r', 0.0), ('s', 0.01455), ('t', 0.00208), ('u', 0.08732), ('v', 0.01871), ('w', 0.02911), ('x', 0.02911), ('y', 0.12266), ('z', 0.02911)], 
           [('a', 0.0), ('b', 0.02495), ('c', 0.0), ('d', 0.08108), ('e', 0.00832), ('f', 0.01247), ('g', 0.02703), ('h', 0.13514), ('i', 0.01871), ('j', 0.02079), ('k', 0.04158), ('l', 0.05405), ('m', 0.00208), ('n', 0.0104), ('o', 0.02703), ('p', 0.02911), ('q', 0.06861), ('r', 0.09148), ('s', 0.02911), ('t', 0.00208), ('u', 0.05613), ('v', 0.08316), ('w', 0.10603), ('x', 0.04158), ('y', 0.01455), ('z', 0.01455)], 
           [('a', 0.04782), ('b', 0.06237), ('c', 0.00416), ('d', 0.00416), ('e', 0.04158), ('f', 0.03326), ('g', 0.07277), ('h', 0.05821), ('i', 0.02079), ('j', 0.00208), ('k', 0.06653), ('l', 0.0499), ('m', 0.11642), ('n', 0.03119), ('o', 0.00832), ('p', 0.01871), ('q', 0.0), ('r', 0.02287), ('s', 0.00208), ('t', 0.08316), ('u', 0.0104), ('v', 0.02287), ('w', 0.04366), ('x', 0.1289), ('y', 0.02911), ('z', 0.01871)], 
           [('a', 0.01871), ('b', 0.0), ('c', 0.079), ('d', 0.01455), ('e', 0.02287), ('f', 0.03534), ('g', 0.14345), ('h', 0.01247), ('i', 0.01247), ('j', 0.05198), ('k', 0.08108), ('l', 0.00208), ('m', 0.00624), ('n', 0.05821), ('o', 0.01247), ('p', 0.04782), ('q', 0.06237), ('r', 0.02287), ('s', 0.00208), ('t', 0.05613), ('u', 0.06653), ('v', 0.12682), ('w', 0.02287), ('x', 0.0104), ('y', 0.02703), ('z', 0.00416)], 
           [('a', 0.02079), ('b', 0.0), ('c', 0.08316), ('d', 0.02079), ('e', 0.01247), ('f', 0.03742), ('g', 0.11227), ('h', 0.01871), ('i', 0.01455), ('j', 0.05198), ('k', 0.07277), ('l', 0.00208), ('m', 0.01247), ('n', 0.04158), ('o', 0.02911), ('p', 0.06237), ('q', 0.07069), ('r', 0.01871), ('s', 0.00208), ('t', 0.05613), ('u', 0.06653), ('v', 0.12266), ('w', 0.04158), ('x', 0.00624), ('y', 0.01871), ('z', 0.00416)], 
           [('a', 0.05613), ('b', 0.00208), ('c', 0.00208), ('d', 0.04366), ('e', 0.03119), ('f', 0.06237), ('g', 0.05821), ('h', 0.0104), ('i', 0.0), ('j', 0.06653), ('k', 0.06445), ('l', 0.12266), ('m', 0.03534), ('n', 0.01663), ('o', 0.02911), ('p', 0.0), ('q', 0.03119), ('r', 0.00416), ('s', 0.08524), ('t', 0.01871), ('u', 0.02911), ('v', 0.02287), ('w', 0.11642), ('x', 0.02911), ('y', 0.02703), ('z', 0.03534)], 
           [('a', 0.07692), ('b', 0.00208), ('c', 0.02287), ('d', 0.04366), ('e', 0.03326), ('f', 0.06237), ('g', 0.07277), ('h', 0.01663), ('i', 0.0), ('j', 0.05405), ('k', 0.05613), ('l', 0.09148), ('m', 0.01871), ('n', 0.00624), ('o', 0.01871), ('p', 0.00208), ('q', 0.03326), ('r', 0.0), ('s', 0.08524), ('t', 0.01455), ('u', 0.02495), ('v', 0.0395), ('w', 0.13098), ('x', 0.0104), ('y', 0.03119), ('z', 0.05198)], 
           [('a', 0.01871), ('b', 0.06653), ('c', 0.09979), ('d', 0.01455), ('e', 0.00416), ('f', 0.0499), ('g', 0.08316), ('h', 0.09771), ('i', 0.02703), ('j', 0.01871), ('k', 0.01455), ('l', 0.00624), ('m', 0.01663), ('n', 0.0), ('o', 0.08108), ('p', 0.00832), ('q', 0.02911), ('r', 0.03534), ('s', 0.1185), ('t', 0.00624), ('u', 0.01455), ('v', 0.05198), ('w', 0.0894), ('x', 0.0), ('y', 0.00624), ('z', 0.04158)], 
           [('a', 0.07484), ('b', 0.08316), ('c', 0.01871), ('d', 0.0), ('e', 0.06237), ('f', 0.07692), ('g', 0.10187), ('h', 0.03326), ('i', 0.0104), ('j', 0.02079), ('k', 0.00208), ('l', 0.02495), ('m', 0.0), ('n', 0.06029), ('o', 0.0104), ('p', 0.02287), ('q', 0.03326), ('r', 0.11227), ('s', 0.03326), ('t', 0.02079), ('u', 0.04158), ('v', 0.07277), ('w', 0.00208), ('x', 0.00832), ('y', 0.04366), ('z', 0.02911)], 
           [('a', 0.00208), ('b', 0.02495), ('c', 0.00208), ('d', 0.06861), ('e', 0.01247), ('f', 0.02495), ('g', 0.04366), ('h', 0.12058), ('i', 0.01247), ('j', 0.01871), ('k', 0.0499), ('l', 0.06237), ('m', 0.0), ('n', 0.00208), ('o', 0.03534), ('p', 0.03742), ('q', 0.07484), ('r', 0.07484), ('s', 0.02287), ('t', 0.00208), ('u', 0.04158), ('v', 0.10187), ('w', 0.10603), ('x', 0.02703), ('y', 0.0104), ('z', 0.02079)], 
           [('a', 0.02703), ('b', 0.07692), ('c', 0.08732), ('d', 0.02703), ('e', 0.00208), ('f', 0.08524), ('g', 0.06445), ('h', 0.08108), ('i', 0.03534), ('j', 0.00832), ('k', 0.01663), ('l', 0.0), ('m', 0.02287), ('n', 0.0), ('o', 0.08316), ('p', 0.01247), ('q', 0.01871), ('r', 0.03326), ('s', 0.12474), ('t', 0.00832), ('u', 0.01663), ('v', 0.04574), ('w', 0.06237), ('x', 0.0), ('y', 0.01455), ('z', 0.04574)], 
           [('a', 0.0), ('b', 0.025), ('c', 0.0), ('d', 0.07083), ('e', 0.01042), ('f', 0.03542), ('g', 0.04375), ('h', 0.10625), ('i', 0.02292), ('j', 0.02083), ('k', 0.02917), ('l', 0.06042), ('m', 0.00208), ('n', 0.01667), ('o', 0.03125), ('p', 0.04167), ('q', 0.04792), ('r', 0.10417), ('s', 0.03333), ('t', 0.0), ('u', 0.06458), ('v', 0.06667), ('w', 0.0875), ('x', 0.05), ('y', 0.01667), ('z', 0.0125)], 
           [('a', 0.0375), ('b', 0.07083), ('c', 0.0), ('d', 0.01042), ('e', 0.04167), ('f', 0.02292), ('g', 0.05417), ('h', 0.10417), ('i', 0.01667), ('j', 0.0), ('k', 0.06875), ('l', 0.05417), ('m', 0.10208), ('n', 0.03333), ('o', 0.00833), ('p', 0.0125), ('q', 0.00208), ('r', 0.01458), ('s', 0.0), ('t', 0.07083), ('u', 0.01458), ('v', 0.03542), ('w', 0.025), ('x', 0.15), ('y', 0.025), ('z', 0.025)], 
           [('a', 0.03125), ('b', 0.0), ('c', 0.075), ('d', 0.0125), ('e', 0.025), ('f', 0.04583), ('g', 0.11875), ('h', 0.01875), ('i', 0.02708), ('j', 0.05), ('k', 0.06667), ('l', 0.0), ('m', 0.0125), ('n', 0.04583), ('o', 0.01875), ('p', 0.075), ('q', 0.0875), ('r', 0.01875), ('s', 0.0), ('t', 0.04792), ('u', 0.07083), ('v', 0.07292), ('w', 0.02917), ('x', 0.02083), ('y', 0.02708), ('z', 0.00208)], 
           [('a', 0.00833), ('b', 0.04167), ('c', 0.02292), ('d', 0.0875), ('e', 0.07292), ('f', 0.0125), ('g', 0.00417), ('h', 0.05833), ('i', 0.0625), ('j', 0.10208), ('k', 0.02917), ('l', 0.01667), ('m', 0.02083), ('n', 0.00417), ('o', 0.02708), ('p', 0.00417), ('q', 0.06458), ('r', 0.01458), ('s', 0.02292), ('t', 0.03125), ('u', 0.13125), ('v', 0.02083), ('w', 0.02708), ('x', 0.04792), ('y', 0.06458), ('z', 0.0)], 
           [('a', 0.00208), ('b', 0.02292), ('c', 0.0), ('d', 0.05625), ('e', 0.01458), ('f', 0.01875), ('g', 0.03542), ('h', 0.13333), ('i', 0.01875), ('j', 0.02708), ('k', 0.03958), ('l', 0.05833), ('m', 0.0), ('n', 0.00625), ('o', 0.025), ('p', 0.02708), ('q', 0.07083), ('r', 0.09167), ('s', 0.02083), ('t', 0.00208), ('u', 0.0625), ('v', 0.0875), ('w', 0.10833), ('x', 0.03125), ('y', 0.00833), ('z', 0.03125)], 
           [('a', 0.0), ('b', 0.02083), ('c', 0.00208), ('d', 0.09167), ('e', 0.01875), ('f', 0.02917), ('g', 0.025), ('h', 0.13333), ('i', 0.03333), ('j', 0.02083), ('k', 0.04167), ('l', 0.07708), ('m', 0.0), ('n', 0.01667), ('o', 0.03958), ('p', 0.02708), ('q', 0.05417), ('r', 0.07083), ('s', 0.01875), ('t', 0.0), ('u', 0.08333), ('v', 0.04167), ('w', 0.09375), ('x', 0.03333), ('y', 0.0125), ('z', 0.01458)], 
           [('a', 0.00208), ('b', 0.03542), ('c', 0.0), ('d', 0.075), ('e', 0.02083), ('f', 0.03125), ('g', 0.04167), ('h', 0.13958), ('i', 0.01875), ('j', 0.02292), ('k', 0.04583), ('l', 0.04792), ('m', 0.00208), ('n', 0.00417), ('o', 0.03958), ('p', 0.04167), ('q', 0.06667), ('r', 0.07708), ('s', 0.02083), ('t', 0.00208), ('u', 0.05), ('v', 0.07083), ('w', 0.08542), ('x', 0.0375), ('y', 0.00625), ('z', 0.01458)], 
           [('a', 0.0), ('b', 0.02083), ('c', 0.0), ('d', 0.08542), ('e', 0.01458), ('f', 0.01875), ('g', 0.02917), ('h', 0.12708), ('i', 0.01667), ('j', 0.02083), ('k', 0.03125), ('l', 0.0875), ('m', 0.00417), ('n', 0.00833), ('o', 0.0375), ('p', 0.03333), ('q', 0.05208), ('r', 0.07083), ('s', 0.02083), ('t', 0.00208), ('u', 0.06667), ('v', 0.075), ('w', 0.11875), ('x', 0.03333), ('y', 0.00833), ('z', 0.01667)], 
           [('a', 0.01458), ('b', 0.02083), ('c', 0.04375), ('d', 0.06458), ('e', 0.00417), ('f', 0.0125), ('g', 0.04583), ('h', 0.04792), ('i', 0.07083), ('j', 0.08542), ('k', 0.02292), ('l', 0.00208), ('m', 0.05417), ('n', 0.04375), ('o', 0.10625), ('p', 0.03333), ('q', 0.01042), ('r', 0.00417), ('s', 0.00417), ('t', 0.04167), ('u', 0.00208), ('v', 0.06042), ('w', 0.01667), ('x', 0.02708), ('y', 0.03333), ('z', 0.12708)], 
           [('a', 0.02292), ('b', 0.02708), ('c', 0.03958), ('d', 0.05833), ('e', 0.0), ('f', 0.01042), ('g', 0.03542), ('h', 0.02708), ('i', 0.06458), ('j', 0.07292), ('k', 0.01667), ('l', 0.0), ('m', 0.06667), ('n', 0.05417), ('o', 0.09167), ('p', 0.05), ('q', 0.00833), ('r', 0.01667), ('s', 0.0), ('t', 0.01667), ('u', 0.00208), ('v', 0.11042), ('w', 0.01875), ('x', 0.03542), ('y', 0.01458), ('z', 0.13958)], 
           [('a', 0.01458), ('b', 0.0375), ('c', 0.04375), ('d', 0.07083), ('e', 0.0), ('f', 0.00833), ('g', 0.05208), ('h', 0.02917), ('i', 0.075), ('j', 0.06667), ('k', 0.03125), ('l', 0.00208), ('m', 0.0625), ('n', 0.06042), ('o', 0.09375), ('p', 0.0375), ('q', 0.0125), ('r', 0.01042), ('s', 0.00417), ('t', 0.02292), ('u', 0.0), ('v', 0.07708), ('w', 0.00833), ('x', 0.02708), ('y', 0.03125), ('z', 0.12083)], 
           [('a', 0.01875), ('b', 0.02708), ('c', 0.04792), ('d', 0.06042), ('e', 0.0), ('f', 0.00417), ('g', 0.0375), ('h', 0.01667), ('i', 0.05), ('j', 0.06875), ('k', 0.02292), ('l', 0.0), ('m', 0.07292), ('n', 0.0875), ('o', 0.11458), ('p', 0.02917), ('q', 0.00625), ('r', 0.02292), ('s', 0.0), ('t', 0.025), ('u', 0.0), ('v', 0.075), ('w', 0.01458), ('x', 0.02292), ('y', 0.03125), ('z', 0.14375)], 
           [('a', 0.01667), ('b', 0.025), ('c', 0.05833), ('d', 0.06667), ('e', 0.0), ('f', 0.0125), ('g', 0.04583), ('h', 0.02292), ('i', 0.05417), ('j', 0.07917), ('k', 0.02292), ('l', 0.00208), ('m', 0.07292), ('n', 0.07917), ('o', 0.10625), ('p', 0.025), ('q', 0.00625), ('r', 0.02292), ('s', 0.00417), ('t', 0.02083), ('u', 0.0), ('v', 0.07083), ('w', 0.00833), ('x', 0.01667), ('y', 0.03333), ('z', 0.12708)], 
           [('a', 0.0125), ('b', 0.01667), ('c', 0.0375), ('d', 0.06875), ('e', 0.0), ('f', 0.00417), ('g', 0.04167), ('h', 0.04167), ('i', 0.05), ('j', 0.09167), ('k', 0.01667), ('l', 0.0), ('m', 0.04375), ('n', 0.05833), ('o', 0.12292), ('p', 0.03542), ('q', 0.0125), ('r', 0.01458), ('s', 0.00833), ('t', 0.025), ('u', 0.0), ('v', 0.07708), ('w', 0.025), ('x', 0.02917), ('y', 0.04167), ('z', 0.125)], 
           [('a', 0.01875), ('b', 0.01875), ('c', 0.05), ('d', 0.08125), ('e', 0.0), ('f', 0.00625), ('g', 0.03333), ('h', 0.01875), ('i', 0.08125), ('j', 0.08125), ('k', 0.01458), ('l', 0.0), ('m', 0.06042), ('n', 0.06042), ('o', 0.09792), ('p', 0.03333), ('q', 0.01458), ('r', 0.02083), ('s', 0.00417), ('t', 0.01875), ('u', 0.0), ('v', 0.08125), ('w', 0.01042), ('x', 0.02292), ('y', 0.04167), ('z', 0.12917)], 
           [('a', 0.02083), ('b', 0.025), ('c', 0.03542), ('d', 0.06042), ('e', 0.0), ('f', 0.01875), ('g', 0.04167), ('h', 0.02292), ('i', 0.08958), ('j', 0.07292), ('k', 0.01042), ('l', 0.0), ('m', 0.07708), ('n', 0.08542), ('o', 0.10208), ('p', 0.025), ('q', 0.00417), ('r', 0.01667), ('s', 0.0), ('t', 0.02708), ('u', 0.00208), ('v', 0.09583), ('w', 0.02083), ('x', 0.02708), ('y', 0.03333), ('z', 0.08542)], 
           [('a', 0.01458), ('b', 0.01667), ('c', 0.04375), ('d', 0.08125), ('e', 0.00208), ('f', 0.01042), ('g', 0.02292), ('h', 0.02917), ('i', 0.07292), ('j', 0.07708), ('k', 0.01875), ('l', 0.00208), ('m', 0.04583), ('n', 0.07917), ('o', 0.0875), ('p', 0.025), ('q', 0.0125), ('r', 0.0125), ('s', 0.00625), ('t', 0.03333), ('u', 0.0), ('v', 0.07917), ('w', 0.0125), ('x', 0.03125), ('y', 0.04375), ('z', 0.13958)], 
           [('a', 0.04375), ('b', 0.06667), ('c', 0.0), ('d', 0.0125), ('e', 0.025), ('f', 0.01458), ('g', 0.08125), ('h', 0.09792), ('i', 0.02917), ('j', 0.00208), ('k', 0.03958), ('l', 0.07708), ('m', 0.10833), ('n', 0.02917), ('o', 0.02083), ('p', 0.025), ('q', 0.0), ('r', 0.02083), ('s', 0.0), ('t', 0.07083), ('u', 0.02083), ('v', 0.03958), ('w', 0.0375), ('x', 0.09792), ('y', 0.01458), ('z', 0.025)]]


clave = sacar_clave(largo_clave, default, all_IoC)
print(clave)