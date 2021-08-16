import time

def insertion_sort(list):
    for index in range(1, len(list)):
        position = index
        current_value = list[index]
        
        while(position>0 and list[position-1]>current_value):
            list[position] = list[position-1]
            position = position -1
            
        list[position] = current_value
    
    return list    
        
if __name__=="__main__":
    lst_des = [54,26,93,17,77,31,44,55,20]
    print(lst_des)
    antes = time.time()
    lst_ord = insertion_sort(lst_des)
    depois = time.time()
    print(lst_ord)
    print("Tempo de execução: ", depois - antes)