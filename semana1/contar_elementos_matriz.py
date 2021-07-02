def contar_elementos(matriz):
    cont_linha = 0
    l=0
    for linha in matriz:
        cont_coluna = 0
        for c in range(len(linha)):
            if(int(matriz[l][c]) != 0):
                cont_coluna +=1
        l +=1
        if(cont_coluna==0):
            cont_linha +=1
        
    for x in matriz:
        for y in range(len(x)):
            
    
        
    print("Linhas nulas = {0}".format(cont_linha))
    print("Colunas nulas = {0}".format(cont_coluna))
    
def main():
    matriz = [[0,0,0,0,1],[0,0,0,0,0],[0,1,0,0,0],[0,0,0,0,0]]    
    contar_elementos(matriz)

main()