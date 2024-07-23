def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert_to_percentage(fraction)
            display_output(percentage)
            break
        except (ValueError, ZeroDivisionError):
            pass

def convert_to_percentage(fraction):
    x, y = fraction.split('/')
    x = int(x)
    y = int(y)
    if x > y or y == 0:
        raise ValueError
    return round((x / y) * 100)

def display_output(percentage):
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")

if __name__ == "__main__":
    main()
