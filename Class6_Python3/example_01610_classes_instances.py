class Human(object):
    def __init__(self, age, name):
        self.age = age
        self.name = name

# Klasse <--> Instanz
# Instanz ist eine Verwirklichung der Klasse (ein tatsächliches Objekt, mit dem man was machen kann)


if __name__ == '__main__':
    x = Human(19, "alfred")
    print(x.age)  # access attributes with "."
    print(x.name)

    beatrix = Human(22, "beatrix")
    print(beatrix.age)
    print(beatrix.name)

    sari = Human(42, "sari")
    print(sari.age)
    print(sari.name)
