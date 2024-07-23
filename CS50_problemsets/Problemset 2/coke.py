def main():
    amount_due = 50
    accepted_coins = [25, 10, 5]
    
    while amount_due > 0:
        print(f"Amount due: {amount_due} cents")
        coin = int(input("Insert coin: "))
        
        if coin in accepted_coins:
            amount_due -= coin
        else:
            print("Invalid coin. Accepted denominations are 25, 10, and 5 cents.")
    
    change_owed = abs(amount_due)
    print(f"Change owed: {change_owed} cents")

if __name__ == "__main__":
    main()
