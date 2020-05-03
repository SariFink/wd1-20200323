# write a list with the ingredients salad, orange, mango
# choose one element of the list
# and write it to a file called "fruit.txt"

#(1) --> write a fruit into a file called text
#(2) --> liste erstellen, eine fruit per index auswählen, dann ausgewählte fucht in das file schreiben
#(3) --> liste erstellen, mit random eine frucht wählen lassen, dann in file schreiben
#(4) --> dann rauslesen und printen

fruits = ["salad", "orange", "mango"]

for fruit in fruits:
    with open("fruit.txt", a) as f:
        f.write(fruit)

with open("fruit.txt", w) as f:
    all_fruits = " ".join(fruits)
    f.write(all_fruits)



