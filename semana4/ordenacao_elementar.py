def crescente(lista):
    for i in range(len(lista)):
        if(i==0):
            item_anterior = lista[i]
            
        else:
            if(item_anterior > lista[i]):
                return False
    
            else:
                item_anterior = lista[i]
    
    return True

if __name__=="__main__":
    seq1 = [2, 4, 5, 8, 9,25, 11, 17, 21]
    print(seq1)
    if crescente(seq1):
        print("eh crescente")
    else:
        print("nao eh crescente")