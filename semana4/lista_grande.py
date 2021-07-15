import random

def lista_grande(numero):
    lista = []
    
    for i in range(numero):
        lista.append(random.randint(i-numero,numero*i))
        
    return lista    

if __name__=="__main__":
    lst = lista_grande(20)
    print(lst)
