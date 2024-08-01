def main():
    mass = int(input("welcome to E=mc^2 converter, what is m? "))
    print(equation(mass))

def equation(mass):
    return mass * (300000000 ** 2)

main()
    