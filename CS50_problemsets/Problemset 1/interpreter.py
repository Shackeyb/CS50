def main():
    expression = input("Enter an arithmetic expression (e.g., 1 + 1): ")
    
    x, y, z = expression.split(" ")
 
    x = float(x)
    z = float(z)
    
    if y == '+':
        result = x + z
    elif y == '-':
        result = x - z
    elif y == '*':
        result = x * z
    elif y == '/':
        result = x / z
    
    print(f"{result}")

if __name__ == "__main__":
    main()

