# lists vs tuple
# mutable vs immutable

my_list = ["Merkur", "Venus", "Erde", "Mars"]
my_tuple = ("Merkur", "Venus", "Erde", "Mars"")

# print(my_list)
# my_list[0] = "Sonne"
# print(my_list)

# print(my_tuple)
# my_tuple[0] = "Sonne"
# print(my_tuple)

# is a string mutable or immutable?
# my_string = "Hello"
# print(my_string[0])
# my_tuple[0] = "K"     # --> "immutable"
# print(my_string[0])

def mumbojumbo(words):
    words.sort()
    first_word = words[0]
    return first_word

print(mumbojumbo(my_list))
print(my_list)

print(mumbojumbo(my_tuple))
print(my_tuple)


# INTERVIEW-QUESTION 2: get all unique values

my_new_list = [1,2,3,4,5,6,7,8,9,2,3,4,10,13,17,10]
print(my_new_list)
my_set = set(my_new_list)
print(my_set)               # set lässt alle doppelten werte weg
my_new_unique_list = list(set(my_new_list))
print(my_new_unique_list)   # jetzt werden die einzigartigen werte in einer liste rausgegeben


# INTERVIEW-QUESTION 3: check if there are any values in a list which are not unique?
# tip: len()
my_list = [1, 2, 3, 2]
has_only_unique_values = len(my_new_list) == len(set(my_new_list))
print(has_only_unique_values)

# tuple, set, list, dictionary --> WICHTIG ZU LERNEN!!!