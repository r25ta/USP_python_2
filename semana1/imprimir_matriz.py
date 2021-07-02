def dimensao_matriz(matriz):
    l = 0
    for lin in matriz:
        l += 1
        c = 0
        for col in lin:
            c += 1
    
    return str("Matriz: {0} X {1}").format(l,c)   

def imprima_matriz(matriz):
    tamanho_matriz = dimensao_matriz(matriz)
    
    print(tamanho_matriz)
    
    for lin in matriz:
        for col in lin:
            print("    ", col, end=" ")
    
        print(end="\n")
    
    



def main():
    matriz = [[1,2,3],[4,5,6],[7,8,9]]
    imprima_matriz(matriz)
    
main()