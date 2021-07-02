def leia_matriz():
    '''(None) -> matriz (lista de listas)

    Funcao que le do teclado o numero n_linhas de linhas
    e o numero n_colunas de colunas e os elementos de
    uma matriz de inteiros dimensao n_linha x n_colunas.

    A funcao cria e retorna a matriz lida.
    '''
    input_linhas = int(input("Digite o número de linhas:"))
    input_colunas = int(input("Digite o número de colunas:"))

    matriz = []
    
    
    for lin in range(input_linhas):
        linha = []
        print("linha {0} = {1}".format(lin,linha))
        for col in range(input_colunas):
            input_elemento = int(input("Digite o elemento ({0},{1}): ".format(lin,col)))
            linha.append(input_elemento)
            print("linha {0} = {1}".format(lin,linha))    

        
        matriz.append(linha)
        print("matriz =".format(0))
        
    return matriz
#-----------------------------------------------------
# teste
a_mat = leia_matriz()
print(a_mat)