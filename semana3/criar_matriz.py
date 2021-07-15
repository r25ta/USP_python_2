def criar(num_linhas, num_colunas, valor=0):
    matriz = []  #lista vazia
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(valor)
        matriz.append(linha)

    return matriz