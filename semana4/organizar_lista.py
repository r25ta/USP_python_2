'''ALGORITIMO DE ORGANIZAÇÃO DE LISTAS'''
def organizar(lista):
    '''PRIMEIRO LOOP ARMAZENAR O ITEM A SER COMPARADO NA VARIAVEL'''
    for x in range(len(lista)):
        item = x
        
        '''SEGUNDO LOOP A PARTIR DO INDICE DO PRIMEIRO LOOP + 1, ATÉ TAMANHO MAXIMO DA LISTA'''
        for y in range (x+1, len(lista)):
            '''SE INDICE DO PRIMEIRO LOOP FOR MAIOR QUE INDICE DO SEGUNDO LOOP'''
            if(lista[item] > lista[y]):
                '''ARMAZENAR NA VARIAVEL O ITEM DE MENOR VALOR'''
                item = y
        '''AQUI É REALIZADA A TROCA DAS POSIÇÕES DA LISTA'''        
        lista[x],lista[item] = lista[item],lista[x]    
    
    return lista

if __name__=="__main__":
    seq1 = [54, 2, 11, 4, 17, 7, 21, 1]
    print("lista inicial ",seq1)
    lst= organizar(seq1)
    print("lista organizada ", lst)