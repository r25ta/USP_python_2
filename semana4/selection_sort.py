def ordena(lista):
    for x in range(len(lista)):
        item = x        
        for y in range(x + 1, len(lista)):
            if(lista[item] > lista[y]):
                item = y
        lista[x],lista[item] = lista[item], lista[x]         

    return lista        
        
if __name__ == "__main__":
    lst_desordenada = [-19, -8, 21, 41, 25, 26, 47, 23, 36, 41, 191, 59, 100, 250, 208, 294, 264, 191, 66, 186]
    print(lst_desordenada)
    lst_ordenada = ordena(lst_desordenada)
    print(lst_ordenada)