#Python Banking Program

balance = 0.0
print()
print("---------Welcome to Python Banking Program.---------")
while True:
    print()
    print("1. See Balance | 2. Deposit | 3. Withdraw | 4. Exit")
    print()
    choice = input("Enter your choice (1-4) : ")
    if choice=="1":
        print()
        print(f"Your current balance is : {balance:.2f} BDT")

    elif choice=="2":
        print()
        deposit_amount = float(input("Enter deposit amount : "))

        if deposit_amount<=0:
            print()
            print("Deposite amount can't be negative or zero.")
        else:
            balance+=deposit_amount
            print()
            print(f"{deposit_amount:.2f} BDT added to current balance\nPress 1 to see balance.")

    elif choice=="3":
        print()
        withdraw_amount = float(input("Enter withdraw amount : "))
        if withdraw_amount>balance:
            print()
            print("Insufficient Fund.")
        elif withdraw_amount<=0:
            print()
            print("Withdraw amount can't be negative or zero : ")
        else: 
            print()
            balance-=withdraw_amount
            print(f"{withdraw_amount:.2f} BDT withdrawn from current balance\nPress 1 to see balance.")

    elif choice=="4":
        break
    else:
        print("Invalid choice. Please try again.")

print("Thank you. Have a nice day!")
