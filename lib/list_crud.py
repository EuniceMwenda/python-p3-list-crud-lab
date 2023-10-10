def create_an_empty_list():
    return []

def create_a_list():
    return [1, 2, 3, 4]

def add_element_to_end_of_list(create_a_list, element):
    create_a_list.append(5)
    return create_a_list
    

def add_element_to_start_of_list(create_a_list, element):
    create_a_list.insert(0, element) 
    return create_a_list

def remove_element_from_end_of_list(create_a_list):
    create_a_list.pop()
    return create_a_list

def remove_element_from_start_of_list(create_a_list):
    del create_a_list [0]
    return create_a_list
    

def retrieve_first_element_from_list(create_a_list):
    return create_a_list [0] 

def retrieve_element_from_index(create_a_list, index):
    return create_a_list [index]

def retrieve_last_element_from_list(create_a_list):
    return create_a_list [-1]
