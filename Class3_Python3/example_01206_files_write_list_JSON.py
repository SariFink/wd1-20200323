import json
# JSON = JavaScript Object Notation
# can be used to save lists

planets = ["Merkur", "Venus", "Erde", "Mars", "Jupiter"]

filename = "planets.json"

json.dump       # --> write directly to file
json.dumps      # --> convert object to json string
json.load       # --> load directly from file
json.loads      # --> convert object from json string


with open(filename, "w") as f:
    # f.write(json.dumps(planets))  wäre eine möglichkeit
    json.dump(planets, f)           # so geht's besser

# the file is closed automatically after
# the "with" clause is over

print("FINISHED WRITING, START READING")

with open(filename, "r") as f:
    #content = json.loads(f.read())     #wäre eine möglichkeit
    content = json.load(f)              #so geht's besser
    print(content)


print("Done")