def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + int(minutes) / 60

def main():
    time_str = input("Enter the time in 24-hour format (HH:MM): ")
    time_float = convert(time_str)
    
    breakfast_start = convert("7:00")
    breakfast_end = convert("8:00")
    lunch_start = convert("12:00")
    lunch_end = convert("13:00")
    dinner_start = convert("18:00")
    dinner_end = convert("19:00")
    
    if breakfast_start <= time_float <= breakfast_end:
        print("It's breakfast time!")
    elif lunch_start <= time_float <= lunch_end:
        print("It's lunch time!")
    elif dinner_start <= time_float <= dinner_end:
        print("It's dinner time!")

if __name__ == "__main__":
    main()
