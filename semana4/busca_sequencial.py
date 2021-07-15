def busca(lista, elemento):
    
    for i in range(len(lista)):
        if (lista[i] == elemento):
            return i
        
    return False


if __name__ == "__main__":
    print(busca(["Ronaldo","Camila","Diego"],"Olivia"))
    print(busca([2,45,98,-89,25],10))
    print(busca(["Ronaldo","Camila","Diego"],"Camila"))
    print(busca([2,45,98,-89,25],-89))