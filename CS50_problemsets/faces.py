def convert(question):
    question = question.replace(":)", "🙂")
    question = question.replace(":(", "🙁")
    return(question)

def main():
    question = input("How are you feeling today? ")
    question = convert(question)
    print(question)

main()