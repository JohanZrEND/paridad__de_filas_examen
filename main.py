bytes_a_comprobar = [
    [1, 0, 0, 1, 1, 1, 0, 1, 1],
    [0, 1, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 0, 1, 0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 1, 0, 0, 0, 0, 1]
]

def comprobar_bytes_linea(bytes_a_comprobar):
    resultados = []
    for linea in bytes_a_comprobar:
        total_de_1 = linea.count(1)
        par_o_impar = total_de_1 % 2
        resultados.append("OK" if not par_o_impar else "FAIL")

    return resultados


lista_de_resultados = comprobar_bytes_linea(bytes_a_comprobar)
print(lista_de_resultados)
