def eliminar_repeticoes(lista):
    item = ""
    lista_sem_repeticoes=[]
    
    for i in range(len(lista)):
        if item != lista[i]:
            item = lista[i]
            lista_sem_repeticoes.append(lista[i])
    
    return lista_sem_repeticoes        

def busca_sequencial(lista, elemento):
    
    for i in range(len(lista)):
        if(elemento == lista[i]):
            return i
        
    return None
    
    
if __name__=="__main__":
    lista_com_repeticoes=[1,2,2,3,4,5,5,6,7,8,8,9,12]
    lista_sem_repeticoes = eliminar_repeticoes(lista_com_repeticoes)
    print(lista_sem_repeticoes)
    print(busca_sequencial(lista_sem_repeticoes,8))