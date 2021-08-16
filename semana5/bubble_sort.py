def bubble_sort(list):
    total = len(list)-1
    while total >= 0: 
        for item in range(total):
            if list[item] > list[item + 1]:
                list[item], list[item + 1] = list[item + 1], list[item]
                print(list)
        
        total -= 1   
        
    return list
"""
if __name__=="__main__":
    lst = [1, 5, 3, 4, 2, 0]
    print(bubble_sort(lst))
 
"""