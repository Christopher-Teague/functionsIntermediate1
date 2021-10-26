from typing import List


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(x) :
# should output: (it's okay if each key-value pair ends up on 2 separate lines;

    # for idx in range(0, len(x)):
    #     my_dict = x[idx]
    #     print(my_dict)    
    #     for key,value in my_dict:
    #         print(key, value)
    for dict in x:
        # dict_string = ""
        # for key,val in dict.items():
        #     # print(key, ' - ', val)
        #     dict_string += f"{key} - {val}, "
        dict_string = ", ".join(f"{key} - {val}" for key,val in dict.items())
        # test=[f"{key} - {val}" for key,val in dict.items()]
        # print(test)
        # print(dict.items())
        print (dict_string)
iterateDictionary(students)

# a,b,*rest = (1,2,3,4)
# print(a)
# print(b)
# print(rest)

# bonus to get them to appear exactly as below!)


# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


#Thanks Christian!