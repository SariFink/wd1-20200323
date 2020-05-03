a_list = []
b_list = [1, 2, 3, 4]

# append (immer nur ein element hinzufuegbar
b_list.append(5)
print(b_list)  # [1, 2, 3, 4, 5]

# remove
b_list.remove(3)
print(b_list)  # [1, 2, 4, 5]
# extend (immer nur mehrere elemente hinzufuegbar)
b_list.extend([0, 77, 99])
print(b_list)  # [1, 2, 4, 5, 0, 77, 99]
b_list += [100, 101]
print(b_list)  # [1, 2, 4, 5, 0, 77, 99, 100, 101]
