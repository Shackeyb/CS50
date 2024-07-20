'''
name = input("What is your name? ")

if name == "Harry" or name == "Hermine" or name == "Ron":
    print("Gryfindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("who?")
'''
''' Or you can use 
if name == "Harry":
    print("Gryfindor")
elif name == "Hermine":
    print("Gryfindor")
elif name == "Ron":
    print("Gryfindor")
'''

name = input("What is your name? ")

match name:
    case "Harry":
        print("Gryfindor")
    case "Hermine":
        print("Gryfindor")
    case "Ron":
        print("Gryfindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("who?")

''' or you can use 
case "Harry" | "Hermine" | "Ron":
    print("Gryfindor")
'''