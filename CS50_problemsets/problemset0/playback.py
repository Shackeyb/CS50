def main():
    slow = input("You were hit by the slow beam, say anything: ")
    slowbeam(slow)

def slowbeam(words):
    print(words.replace(" ", "...").strip("..."))
main()