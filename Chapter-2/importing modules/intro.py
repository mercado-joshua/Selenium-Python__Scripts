# import my_module
# import my_module as mm
# from my_module import find_index
# from my_module import * (NOT RECOMMENDED)
from my_module import find_index, test
# from my_module import find_index as fi, test

courses = ['History', 'Math', 'Physics', 'CompSci']

# index = mm.find_index(courses, 'Math')
index = find_index(courses, 'Math')
# index = fi(courses, 'Math')
print(index)
print(test)


"""
from my_module import find_index
* only the specified function will be called
"""