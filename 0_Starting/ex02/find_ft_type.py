def all_thing_is_obj(object: any) -> int:
    defined_objects = {
            list: 'List',
            tuple: 'Tuple',
            str: 'is in the kitchen',
            set: 'Set',
            dict: 'Dict'
            }

    found = False
    type_of_object = type(object)
    
    for key, value in defined_objects.items() :
        if (type_of_object == key) :
            found = True
            if (type_of_object == str) :
                print(object, end=' ')
            print(value, ":", type_of_object)
    if found != True :
        print("Type not found")
    return 42
