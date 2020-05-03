capitals = {"France": "Paris",
            "Iceland": "Reykjavik",
            "Denmark": "Copenhagen",
            "Lithuania": "Vilnius",
            "Canada": "Ottawa",
            "Austria": "Vienna"}

# cities = ["Wien", "Linz", "Graz, Salzburg"]

# for city in cities:
#     print(city)

# ITERATE OVER KEYS
print(capitals.keys())
# methode 1
for capital in capitals.keys():
    print(capital)

# methode 2
for capital in capitals:
    print(capital)


# ITERATE OVER VALUES
print(capitals.values())
for capital_city in capitals.values():
    print(capital_city)


# ITERATE OVER ITEMS (item = key und value zusammen, also ein paerchen)
for entry in capitals.items():
    print(entry)

for k, v in capitals.items():
    print(k, v)
# k=key, v=value

pricelist = [("bread", 2), ("peanut-butter", 3)]
for pricetag in pricelist:
    print(pricetag)

for pricetag in pricelist:
    food, price = pricetag
    print(food, price)

for food, price in pricelist:
    print(food, price)

werte = [1, 200, 103.4, 188.7]
summe = sum(werte)
summe = round(summe, 2)
print(summe)