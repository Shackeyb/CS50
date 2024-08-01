def convert():
    time = input("What time is it? ")
    #time = float(time.replace(":", "."))
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)/60

    print(hours + minutes)

convert()