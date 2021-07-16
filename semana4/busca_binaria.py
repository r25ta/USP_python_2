def busca_binaria(lista, elemento):

    first = 0
    last = len(lista)-1
        
    while first <= last:
        midpoint = (first+last)//2
        if(elemento == lista[midpoint]):
            return midpoint
        
        else:
            if(elemento < lista[midpoint]):
                last = midpoint - 1
            else:
                first = midpoint + 1
                
    return None    

if __name__=="__main__":
    lst_sequencia = [4, 10, 80, 90, 91, 99, 100, 101]
    lst_elementos = [80,50]
    
    for elemento in lst_elementos:
        indice = busca_binaria(lst_sequencia,elemento)
        if indice is None:
            print("Não achou elemento ",elemento)
        else:
            print("O elemento ",elemento, "está no indice", indice)
