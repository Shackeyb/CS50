def main():
    time = input("What time is it? ")
    x = convert(time)
    
    if x >= 18  and x <= 19:
        print("dinner time")
    elif x >= 12 and x <= 13:
        print("lunch time")
    elif x >= 7 and x <= 8:
        print("Breakfast time")

def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)/60

    return hours + minutes

if __name__ == "__main__":
    main()
