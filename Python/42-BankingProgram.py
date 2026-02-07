def show_balance():
    print(f"\nYour balance is:${balance:.2f}\n")


def deposit():
    amount=float(input("\nEnter an amount to be deposited:"))
    if amount<=0:
        print("That's not a valid amount")
        return 0
    else:
        return amount
def withdraw():
    withdr=float(input("\nEnter a amount the withdraw:\n"))
    if withdr<=0:
        print("That's not a valid amount")
        return 0
    elif withdr>balance:
        print("You don't have a enough money to withdraw.")
        return 0
    else:
        return withdr
balance=0
def main():
    
    is_running=True


    while is_running:
        print("Banking Program")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")


        choice=int(input("Enter your choice(1-4):"))

        match choice:
            case 1:
                show_balance()
            case 2:
                amount_deposited=deposit()
                balance+=amount_deposited
                print(f"\nYou deposited ${amount_deposited} money the your account")
                print(f"Your new balance is:{balance}\n")
            case 3:
                amount_withdraw=withdraw()
                balance-=amount_withdraw
                print(f"\nYou withdrawed ${amount_withdraw} money the your account")
                print(f"Your new balance is:{balance}\n")
            case 4:
                is_running=False
            case _:
                print("\nPlease choice a valid option")
    print("\nThank you Have a nice day!")

main()
