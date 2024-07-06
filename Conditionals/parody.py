'''
def main():
    x = int(input("what is x? "))
    if x % 2 == 0:
        print("even")
    else:
        print("odd")
'''

def main():
    x = int(input("what is x? "))
    if is_even(x):
        print("even")
    else:
        print("odd")
'''
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
'''
'''
def is_even(n):
    if n % 2 == 0:
        return True if n % 2 == 0 else False
'''
def is_even(n):
    return n % 2 == 0
main()