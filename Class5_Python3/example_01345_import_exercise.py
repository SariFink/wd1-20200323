# create a new file called "my_library.py"
# write the functions from the previous exercise in that library

# import the file "my_library.py"
# use one of the functions and print it's result

# Hier eine andere Variante:

import Class5_Python3.math_functions

print(Class5_Python3.math_functions.digit_cutter(123.456789, 3))

# oder das gleiche mit "as" umgeschrieben:

import Class5_Python3.math_functions as MF

print(MF.digit_cutter(123.456789, 3))