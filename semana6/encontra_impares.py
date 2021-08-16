def encontra_impares(lst,item=0,lst_impar=[]):
    if( len(lst)-1 >= item ):
        if(lst[item] % 2 != 0):
            lst_impar.append(lst[item])
        item += 1
        return encontra_impares(lst, item, lst_impar)
    
    else:
        return lst_impar
         
"""        
if __name__=="__main__":
    lst = [2,4,6,8]
    print(encontra_impares(lst))
"""