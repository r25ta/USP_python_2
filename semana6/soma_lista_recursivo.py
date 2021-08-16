def soma_lista(lst, item=0):

    if len(lst)-1 >= item:
        element = lst[item]
        item +=1
        return element + soma_lista(lst,item)
    else:
        return 0
"""    
if __name__=="__main__":
    lst = [1,2,3,2]
    print(soma_lista(lst))
"""