def main():
    # Dictionary to store fruit calories
    fruit_calories = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "Tangerine": 86
    }

    fruit = input("Enter a fruit: ").strip().lower()
    if fruit in fruit_calories:
        print(f"Calories: {fruit_calories[fruit]}")
    else:
        print("Invalid fruit")

if __name__ == "__main__":
    main()
