def chop(lst):
    
    if len(lst) >= 2:
        del lst[0]  
        del lst[-1]   
    else:
        lst.clear()

def middle(lst):
    
    return lst[1:-1]


my_list = [1, 2, 3, 4]
print("my list before call chop function =>", my_list)


chop(my_list)
print("my list after call chop function =>", my_list)


my_list = [1, 2, 3, 4]
print("\nmy list before call middle function =>", my_list)


new_list = middle(my_list)
print("my list after call middle function =>", my_list)
print("new list after call middle function =>", new_list)
