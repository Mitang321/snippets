def flatten_list(nested_list):
    if not(bool(nested_list)):
        return nestedList
 
    if isinstance(nested_list[0], list):
        return flatten_list(*nested_list[:1]) + flatten_list(nested_list[1:])
 
    return nested_list[:1] + flatten_list(nested_list[1:]) 