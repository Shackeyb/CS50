#students = ["Hermione", "Harry", "Ron", "Draco"]
#houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
'''
students = {
    "Hermione" : "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin"
} #dictionary

for student in students:
    print(student, students[student], sep=", ")
'''
#list of dictionaries 

students = [
    {"name" : "Hermione", "house" : "Gryffindor", "patronus" : "otter"},
    {"name" : "Harry", "house" : "Gryffindor", "patronus" : "stg"},
    {"name" : "Ron", "house" : "Gryffindor", "patronus" : "Dog"},
    {"name" : "Draco", "house" : "Slytherin", "patronus" : None}
]
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")