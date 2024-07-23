def main():
    file = input("Enter a greeting: ").strip().lower()

    if file.endswith(".gif"):
        print("image/gif")
    elif file.endswith(("jpg","jpeg")):
        print("image/jpeg")
    elif file.endswith(".png"):
        print("image/png")
    elif file.endswith(".pdf"):
        print("application/pdf")
    elif file.endswith(".txt"):
        print("text/plain")
    elif file.endswith(".zip"):
        print("application/x-zip-compressed")
    else:
        print("application/octet-stream")
main()