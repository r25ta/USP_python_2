def ordenada(lista):
    item = -1
    
    for i in range(len(lista)):
        if i == 0:
            item = lista[i]
        
        if item <= lista[i]:
            item = lista[i]
        
        else:
            return False        
        
    return True    

if __name__ == "__main__":
    lista_ordenada=[1,2,2,3,4,5,6,7,8,9]
    lista_desordenada = [-1,0,9,2,3,4,6,5,1,8,7]

    print(ordenada(lista_ordenada))
    print(ordenada(lista_desordenada))
  