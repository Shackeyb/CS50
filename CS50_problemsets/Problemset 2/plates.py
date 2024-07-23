def main():
    plate = input("Plate: ")
    print("Valid" if is_valid(plate) else "Invalid")

def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False
    if not s[:2].isalpha():
        return False
    if not s.isalnum():
        return False
    
    digit_started = False
    for i, char in enumerate(s):
        if char.isdigit():
            digit_started = True
            if char == '0' and i < len(s) - 1 and s[i+1].isdigit():
                return False
        elif digit_started:
            return False
    return True

if __name__ == "__main__":
    main()
