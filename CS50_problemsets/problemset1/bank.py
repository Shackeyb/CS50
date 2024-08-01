def main():
    greeting = input("Greeting: ")
    bank(greeting)

def bank(greeting):
    if greeting == "hello" or "Hello":
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")
main()
