def insertion_sort(list):
    for index in range(1, len(list)):
        current_value = list[index]
        position = index
        
        while position > 0 and current_value < list[position - 1]:
            list[position] = list[position - 1]
            position = position - 1
            
            
        list[position] = current_value

    return list

"""        
if __name__=="__main__":
    alist = [54,26,93,17,77,31,44,55,20]
    print(insertion_sort(alist))
"""