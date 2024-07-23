def main():
    camel_case = input("camel case: ")
    snake_case = convert_to_snake_case(camel_case)
    print("snake case:", snake_case)

def convert_to_snake_case(camel_case):
    snake_case = camel_case[0].lower()  # Start with the first character in lowercase
    for char in camel_case[1:]:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    return snake_case

if __name__ == "__main__":
    main()
