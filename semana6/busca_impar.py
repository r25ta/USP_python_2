def busca_impar(lst):
    lst_impar = []
    for i in range(len(lst)):
        if(lst[i]%2!=0):
            lst_impar.append(lst[i])

    return lst_impar

def busca_impar_recursiva(lst, item=0, lst_impar=[]):
    if(len(lst)-1 >= item):
        if(lst[item]%2!=0):
            lst_impar.append(lst[item])
        
        item +=1
        return busca_impar_recursiva(lst,item,lst_impar)
    else:
        return lst_impar    
    
    
if __name__=="__main__":
#    print(busca_impar([0,1,2,3,4,5,6,7,8,9]))
    print(busca_impar_recursiva([0,1,2,3,4,5,6,7,8,9]))