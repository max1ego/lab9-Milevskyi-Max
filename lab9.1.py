
list1 = [2, 3, 5, 7, 11]
list2 = [True, False, False, True]
tup = (1, -19, "af", list1, 25.9, "fa", list2)

nested_lists = []
    
for element in tup:
    if isinstance(element, list): 
        nested_lists.append(element)

print(nested_lists)
