def main():
    text = input("Enter a string of text: ")
    shortened_text = remove_vowels(text)
    print(shortened_text)

def remove_vowels(text):
    vowels = "AEIOUaeiou"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result

if __name__ == "__main__":
    main()
