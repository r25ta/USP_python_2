'''ALGORITIMO DE BUSCA BINARIA
    PARA LOCALIZAR UM ELEMENTO NA LISTA ORDENADA
    AQUI A LISTA É DIVIDA EM PARTES ATÉ LOCALIZAR O ELEMENTO'''
def search_binary(list,element):
    
    found = False
    first = 0
    last = len(list) - 1
    
    
    while first <= last and not found:
        #RETORNA O INDICE METADE DA LISTA 
        midpoint = (first + last) //2

        
        if (element == list[midpoint]):
            found = True
            
        else:
            #SE ELEMENTO FOR MENOR QUE ITEM DA LISTA
            # DECREMENTAR DA VARIAVEL MIDPOINT E ATRIBUIR NA VARIAVEL LAST
            if(element < list[midpoint]):
                last = midpoint - 1
            else:
                #SE ELEMENTO FOR MAIOR QUE ITEM DA LISTA
                #INCREMENTAR NA VARIAVEL MIDPOINT E ATRIBUIR NA VARIAVEL FIRST
                first = midpoint + 1
    
    return found    
    
    
if __name__ == "__main__":
    list = [1,2,3,4,6,8,12,34,45,56,67,78,90]
    print(search_binary(list,34))
    print(search_binary(list,5))