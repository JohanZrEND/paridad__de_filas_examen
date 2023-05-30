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

def comprobar_bytes_linea():
    contador = 0
    for linea in bytes_a_comprobar[contador]:
        total_de_1 = linea.count(1)
        print(total_de_1)
        contador += 1
        
comprobar_bytes_linea()
