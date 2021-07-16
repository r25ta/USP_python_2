'''BUSCA SEQUENCIAL EM LISTA ORDENADA
    ESSE ALGORITIMO TEM UMA PERFORMANCE UM POUCO MELHOR PORQUE SE A LISTA É ORDENADA 
    É POSSIVEL COMPARAR O ITEM PROCURADO 
    SE ITEM PROCURADO FOR MENOR QUE CONTEÚDO DA LISTA QUE DIZER QUE O ITEM NÃO ESTÁ PRESENTE
    E AUTOMATICAMENTE ABORTA A ITERAÇÃO
    
    O MESMO ACONTECE QUANDO ENCONTRA O ELEMENTO
'''
def sequencial_search_ordered_list(list,element):
    pos=0
    found = False
    stop = False
    #FAÇA ENQUANTO POS < QUE TAMANHO TOTAL DA LISTA E FOUND=FALSE E STOP = FALSE
    while pos < len(list) and not found and not stop:
        #SE ENCONTRAR O ELEMENTO NA LISTA ATUALIZA A VARIAVEL DE CONTROLE
        if(element == list[pos]):
            found = True
        else:
            if(element<list[pos]):
                stop = True
            else:
                pos += 1
    
    return found


if __name__ == "__main__":
    list_ordered = [1,2,3,4,5,7,8,9,10,11,12,13,14,15,16,20,30,40,50]
    print(sequencial_search_ordered_list(list_ordered,9))
    print(sequencial_search_ordered_list(list_ordered,21))