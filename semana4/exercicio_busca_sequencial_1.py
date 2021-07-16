'''EXEMPLO DE BUSCA SEQUENCIAL UTILIZANDO WHILE'''
def sequential_search(list,element):
    '''VARIAVEL PARA PERCORRER O INDICE DA LISTA'''
    pos = 0
    '''VARIAVEL BOLEANA PARA CONTROLAR A IDENTIFICAÇÃO DO ITEM NA LISTA'''
    found = False
    
    '''FAÇA ENQUANTO VARIAVEL POS MENOR QUE TAMANHO DA LISTA E VARIAVEL FOUND = FALSE'''
    while pos < len(list) and not found:
        if(element == list[pos]):
            found = True
        else:
            pos +=1
    
    return found

if __name__ == "__main__":
    lst = [2,3,4,54,-1,4334,0,9908,-435,8]
    print(sequential_search(lst,7))
    print(sequential_search(lst,0))