def main():
    emoji_dict = {
        ":thumbs_up:": "👍",
        ":thumbsup:": "👍",
        ":grinning:": "😀",
        ":smiley:": "😃",
        ":smile:": "😄",
        ":wink:": "😉",
        ":heart:": "❤️",
        ":sad:": "😢",
        ":clap:": "👏",
        ":party:": "🎉",
        ":star:": "⭐",
        ":fire:": "🔥",
        ":sparkles:": "✨"
    }
    
    text = input("Enter text with emoji codes: ")
    
    for code, emoji in emoji_dict.items():
        text = text.replace(code, emoji)
    
    print(text)

if __name__ == "__main__":
    main()
