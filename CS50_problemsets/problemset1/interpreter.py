def main():
    expression = input("Input an expression (eg: 1 + 1, please you spaces) ")
    x, y, z = expression.split(" ")

    x = float(x)
    z = float(z)

    if y == "+":
         expression = x + z
    elif y == "-":
         expression = x - z
    elif y == "*":
         expression = x * z
    elif y == "/":
         expression = x / z
    else:
         print("try again")

    print(f"{expression:.1f}")

main()