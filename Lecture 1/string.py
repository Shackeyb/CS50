#strings section

#name = "hi"
#print(name)

#name = input("What is your name? ")
#print("Hello", name)

#name = input("What is your name? ")
#print(f"Hello, {name}")

"""
name = input("What is your name? ")
name = name.strip() #Method, strips whitespace from str
name = name.capitalize() #Method, Caps the first leter of str
name = name.title() #Method, Caps the first leter of each word 
print(f"Hello, {name}")
"""

'''
name = input("What is your name? ")
name = name.strip().capitalize().title()
print(f"Hello, {name}")
'''

'''
name = input("What is your name? ")
first, last = name.split(" ") #Method splits the string into segments, First/last name 
print(f"Hello, {last}")
'''
"""
def hello(to="world"):
    print("hello,", to)

hello()
name = input ("what's your name? ")
hello(name)
"""

def main():
    name = input ("what's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()