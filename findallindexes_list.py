def all_indexes(listed_items, item):
    index_list = []
    for index , value in enumerate(listed_items):
        if value == item:
            index_list.append([index])
        elif isinstance(value , list):
            for ind in all_indexes(value, item):
                index_list.append([index]+ ind)
    return index_list
# enumerate makes the list to access both the index and value of the list

print(all_indexes([[1,2,3,],3,[3,4,5,6],3,3],4))

# can also be done as 
def all_indexes1(listed_items, item):
    index_list = []
    for index , value in enumerate(listed_items):
        if value == item:
            index_list.append([index])
        elif isinstance(listed_items[index] , list):
            for ind in all_indexes1(listed_items[index], item):
                index_list.append([index] + ind)
    return index_list


    
print(all_indexes1([[1,2,3,],3,[3,4,5,6],3,3],3))

