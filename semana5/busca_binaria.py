def busca(lst, elemento):
    inicial = 0
    final = len(lst)-1
    while inicial <= final:
        meio = (inicial + final ) // 2
        print(meio)
        
        if(elemento == lst[meio]):
            return meio
         
        else:
            if(elemento < lst[meio]):
                final = meio - 1
                
            else:
                inicial = meio + 1

                
    return False

"""
if __name__ == "__main__":
    print(busca(['a', 'e', 'i'],'e'))
    print(busca([1, 2, 3, 4, 5], 6))
    print(busca([1, 2, 3, 4, 5, 6], 4))
"""