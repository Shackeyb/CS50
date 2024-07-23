import inflect

def main():
    p = inflect.engine()
    names = []

    try:
        while True:
            name = input("Name: ")
            if name:
                names.append(name)
    except EOFError:
        pass

    if names:
        formatted_names = p.join(names)
        print(f"Adieu, adieu, to {formatted_names}")

if __name__ == "__main__":
    main()
