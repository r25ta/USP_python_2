import criar_matriz

def soma_matrizes(mtzA, mtzB):
    #DEFINE O NÚMERO DE LINHAS DA NOVA MATRIZ, RESPEITANDO O TAMANHO DAS MATRIZES PARAMETRO
    num_lin = len(mtzA)
    #DEFINE O NÚMERO DE COLUNAS DA NOVA MATRIZ, RESPEITANDO O TAMANHO DAS MATRIZES PARAMETRO
    num_col = len(mtzA[0])
    #MATRIZ CRIADA COM VALOR ZERO
    mtz = criar_matriz.criar(num_lin,num_col)
    
    for lin in range(num_lin):
        for col in range(num_col):
            #SOMA OS VALORES DAS MATRIZES A e B E POSICIONA NA NOVA MATRIZ
            mtz[lin][col] = mtzA[lin][col] + mtzB[lin][col]

    return mtz

if __name__ == "__main__":
    mtzA=[[1,2,3],[4,5,6],[7,8,9]]
    mtzB=[[10,20,30],[40,50,60],[70,80,90]]
    print(soma_matrizes(mtzA, mtzB))