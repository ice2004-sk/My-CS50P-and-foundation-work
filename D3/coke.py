amount = 50
total = 0

while True:

    print(f"Amount Due: {amount-total}")
    coins = int(input("Insert Coin: "))

    if coins == 25 or coins == 10 or coins == 5:
        total += coins

    if total >= 50:
        print(f"Change Owned : {total-amount}")
        break