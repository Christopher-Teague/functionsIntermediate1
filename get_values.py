students = [
        {'first_name' : 'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(key_name, some_list):
    for idx in range(0, len(some_list)):
        # print(key_name)
        my_dict = some_list[idx]
        # print(my_dict)
        print(my_dict[key_name])

iterateDictionary2('last_name', students)


