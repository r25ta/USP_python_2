def dimensao_matriz(matriz):
    l = 0
    for lin in matriz:
        l += 1
        c = 0
        c = len(lin)
    return ("{0}x{1}".format(l,c))
            

def simetrica(matriz):
    tamanho_mtz = dimensao_matriz(matriz)
    if int(tamanho_mtz[0]) == int(tamanho_mtz[-1]):
        return True
    else:
        return False
    
def main():
    matriz = [[11,-3,4,8],[-3,12,6,11],[4,6,5,13],[8,11,13,5],[1,3,4,5]]
    if simetrica(matriz):
         print("Passou no primeiro teste! :-)")
    else:
        print("Não passou no primeiro testes! :-(")
        
main()