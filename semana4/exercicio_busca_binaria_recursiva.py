""" ALGORITIMO DE BUSCA BINARIA RECURSIVA 
O SISTEMA RECEBE UMA LISTA ORDENADA E O ELEMENTO A SER PROCURADO
"""
def search_binary_recursive(list,element):
    '''CONSISTE SE A LISTA ESTÁ VAZIA GERALMENTE PARA CASOS ONDE A LISTA FOI TOTALMENTE 
    EXPLORADA E O ELEMENTO NÃO ENCONTRADO'''
    if(len(list)==0):
        return False
    
    else:
        '''DIVIDE A LISTA NO MEIO'''
        midpoint = len(list)//2
        #VERIFICA SE O ELEMENTO É IGUAL AO INDICE CENTRAL DA LISTA
        if(element==list[midpoint]):
            return True
        
        else:
            #SE ELEMENTO FOR MENOR QUE ITEM CENTRAL DA LISTA
            if(element<list[midpoint]):
                #CHAMA A FUNÇÃO NOVAMENTE (RECURSIVIDADE) PASSANDO COMO PARAMETRO
                # A LISTA COM TODOS ITENS ATÉ A METADE A ESQUERDA (SLICE :)
                return search_binary_recursive(list[:midpoint],element)
            else:
                #SE ELEMENTO FORM MAIOR QUE ITEM CENTRAL DA LISTA
                # CHAMA A FUNÇÃO NOVAMENTE PASSANDO COMO PARAMETRO MIDPOINT + 1 E TODA 
                #METADE A DIREITA DA LISTA
                return search_binary_recursive(list[midpoint + 1:],element)
                
if __name__ == "__main__":
    list = [1,2,3,5,7,9,12,34,56,78,90]
    print(search_binary_recursive(list,34))
    print(search_binary_recursive(list,15))