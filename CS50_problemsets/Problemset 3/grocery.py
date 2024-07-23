def main():
    items_count = {}
    
    print("Enter grocery items (Ctrl-D to finish):")
    
    while True:
        try:
            item = input().strip().lower()
            if item:
                if item in items_count:
                    items_count[item] += 1
                else:
                    items_count[item] = 1
        except EOFError:
            break
    
    sorted_items = sorted(items_count.items())
    
    for item, count in sorted_items:
        print(f"{count} {item.upper()}")

if __name__ == "__main__":
    main()
