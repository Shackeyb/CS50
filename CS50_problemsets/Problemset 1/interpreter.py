def main():
    expression = input("Input an expression: ")
    
    x, y, z = expression.split(" ")

    x = float(x)
    z = float(z)
    
    if y == "+":
        expression = float(x + z)
    elif y == "-":
        expression = float(x - z)
    elif y == "*":
        expression = float(x * z)
    elif y == "/":
        expression = float(x / z)
    elif y != "+" or "-" or "*" or "/":
        print("nah bruh")
        
    print(expression)
    
main()