balance = 0

while True:
    print ("\n1.Deposit 2.withdraw 3.check Balance 4.Exit")
    choice = input("choose:")

    if choice == "1":
        amount = float(input("Deposit amount: "))
        balance = balance + amount
        print("Deposit amount:",balance)

    elif choice == "2":
        amount = float(input("withdraw amount:"))
        if amount <= balance:
            balance = balance - amount
        else :
            print("Insufficient funds")

    elif choice == "3":
        print ("balance:",balance)

    elif choice == "4":
        break
