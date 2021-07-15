def multiplicar_matrizes(mtzA, mtzB):
    #RECUPERA DIMENSÕES DA MTZ A (LINHAS E COLUNAS)
    num_lin_a, num_col_a = len(mtzA), len(mtzA[0])
    #RECUPERA DIMENSÕES DA MTZ A (LINHAS E COLUNAS)
    num_lin_b, num_col_b = len(mtzB), len(mtzB[0])
    #CONSISTE SE O NUMERO DE COLUNAS DA MTZA É IGUAL NÚMERO DE LINHAS DA MTZB    
    assert num_col_a == num_lin_b
    
    #CRIA MTZ VAZIA
    mtz = []
    
    
    for linha in range(num_lin_a):
        #CRIA NOVA LINHA NA MTZ DE RETORNO
        mtz.append([])
        #PERCORRE AS COLUNAS DA MATRIZ B
        for coluna in range(num_col_b):
            #CRIA NOVA COLUNA NA MTZ DE RETORNO COM VALOR ZERO
            mtz[linha].append(0)
            #PERCORRE AS COLUNAS DA MATRIZ A
            for i in range(num_col_a):
                #ARMAZENA NA MTZ DE RETORNO O RESULTADO DA MULTIPLICAÇÃO DAS COLUNAS DA MTZ A POR LINHAS DA MTZ B
                mtz[linha][coluna] += mtzA[linha][i] * mtzB[i][coluna]    
    return mtz


if __name__ == "__main__":
    mtzA = [[1,2,3,4],[4,5,6,7]]
    mtzB = [[1,2],[3,4],[5,6],[7,8]]
    print(multiplicar_matrizes(mtzA,mtzB))