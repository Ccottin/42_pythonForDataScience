def NULL_not_found(object: any) -> int :
 
    defined_objects = {
            float: 'Cheese',
            int: 'Zero',
            str: 'Empty',
            bool: 'Fake'
            }

    found = False
    type_of_object = type(object)
 
    for key, value in defined_objects.items() :
        if (object != "Brian" and type_of_object == key) :
            found = True
            print(value, ":", object, type_of_object)
        elif (type_of_object == type(None) and found != True) :
            found = True
            print("Nothing :", object, type_of_object)
    
    if found != True :
        print("Type not found")
        return 1
    return 0
