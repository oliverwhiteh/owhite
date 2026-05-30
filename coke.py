def main():
    coke = int(50)

    while coke > 0:
        print(f"Amount Due: {coke}")
        coin = int(input("Insert Coin: "))

        if coin == 25 or coin == 10 or coin == 5:
            coke = coke - coin

        else:
            coke = coke
            continue



    if coke <= 0:
        coke = coke * -1
        print(f"Change Owed: {coke}")



main()
