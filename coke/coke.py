def main():
    amount_due=50
    valid_amount=[25,5,10]

    while amount_due>0:

        print(f"Amount Due: {amount_due}")

        coin=int(input("Insert the Coin:"))

        if coin in valid_amount:
            amount_due-=coin
        else:
           pass
    print(f"Change Owed: {abs(amount_due)}")


main()



