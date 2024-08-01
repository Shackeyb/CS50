def convert(x):
    x = x.replace(":)", "🙂")
    x = x.replace(":(", "🙁")
    print(x)

def main():
    emoji = input("How are you feeling (Use emotocons): ")
    convert(emoji)

main()