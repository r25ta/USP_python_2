def dimensoes(matriz):
    linhas = 0
    for l in range(len(matriz)):
        colunas = 0
        for c in range(len(matriz[l])):
            colunas += 1
        linhas += 1
    
    print(f"{linhas}X{colunas}") 


def main():
    matriz = [[1,3,2],[3,1,4]]
    dimensoes(matriz)

main()
