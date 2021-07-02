
def sao_multiplicaveis(m1,m2):
# RETORNA AS DIMENSÕES DA MATRIZ E TRANSFORMA O RESULTADO EM STRING
    d_m1 = str(dimensoes(m1))
    d_m2 = str(dimensoes(m2))
#    print(d_m1)
#    print(d_m2)
# COMPARA QTDE DE COLUNAS DA PRIMEIRA MATRIZ COM A QTDE LINHAS DA SEGUNDA MATRIZ
    if(d_m1[-1] == d_m2[0]):
        return True
    
    else: 
        return False
    
def dimensoes(matriz):
    linhas = 0
    for l in range(len(matriz)):
        colunas = 0
        for c in range(len(matriz[l])):
            colunas += 1
        linhas += 1
    
    return (f"{linhas}X{colunas}") 
"""            
def main():
    m1 = [[1], [2], [3]]
    m2 = [[1, 2, 3]]
    
    print(sao_multiplicaveis(m1,m2))    

main()
"""