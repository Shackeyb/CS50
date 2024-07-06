#integer Section
#Calculator
"""
x = input("what's x? ")
y = input("what's y? ")

z = int(x + y)
print(z)
"""

'''
x = int(input("what's x? "))
y = int(input("what's y? "))

print(x + y)
'''

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return pow(n, 2)

main()