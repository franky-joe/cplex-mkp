def read_mkp_data(file_path):

    with open(file_path, 'rb') as file:
        file_content = file.read()
    
    # Leer todos los numeros del archivo y convertirlos a enteros
    numbers = list(map(int, file_content.split()))
    
    # Extraer n, m, y el valor óptimo de la primera línea

    n = numbers[0] # Numero de objetos
    m = numbers[1] # Numero de dimenciones
    optimal_value = numbers[2] # Optimo del problema, es 0 si no se conoce
    
    # Indice a partir del cual comenzamos a leer los datos
    index = 3
    
    ret = []
    # Leer los coeficientes de beneficios
    beneficios = numbers[index:index + n]
    index += n
    ret.append(beneficios)
    
    # Leer la matriz A
    Matriz_pesos = [[] for _ in range(n)]
    for i in range(m):
        for j in range(n):
            Matriz_pesos[j].append(numbers[index])
            index += 1

    # Traspuesta de la matriz de pesos
    Matriz_pesos = [list(fila) for fila in zip(*Matriz_pesos)]
    
    # Leer capacidades por dimencion
    capacidades = numbers[index:index + m]
    ret.append(capacidades)
    ret.append(Matriz_pesos)
    
    return ret

def test():
    mochila = read_mkp_data("mochila_multidimencional/datos/flei.data")
    print(mochila)
#test()