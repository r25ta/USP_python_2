def tamanho_matriz(mtz):
    linha = 0
    for l in range(len(mtz)):
        coluna = 0
        for c in range(len(mtz[l])):
            coluna += 1;
            
        linha += 1    

    return linha,coluna

def soma_matrizes(m1, m2):
    mtz1 = tamanho_matriz(m1)
    mtz2 = tamanho_matriz(m2)
    
    if(mtz1!=mtz2):
        matriz = False
    else:
        matriz = []
        for a in range(len(m1)):
            matriz_interna = []
            for b in range(len(m1[a])):
                matriz_interna.append(int(m1[a][b]) + int(m2[a][b])) 

            matriz.append(matriz_interna)
    
    print(f"soma_matrizes(m1,m2) => {matriz}");
    return matriz

def main():
    m1 = [[2]]
    m2 = [[2]]
    
    soma_matrizes(m1,m2)
    
main()
