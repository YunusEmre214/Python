import random

def spin_row():
    symbols=["💀","👻","💩","🤖","👾"]
    reuslts=[]
    for symbol in range(3):
        reuslts.append(random.choice(symbols))
    return reuslts
def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")
def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=='💀':
            return bet*3
        elif row[0]=='👻':
            return bet*2
        elif row[0]=='💩':
            return bet*1
        elif row[0]=='🤖':
            return bet*5
        elif row[0]=='👾':
            return bet*10
    return 0

def main():
    balance=100
    print("Welcome to Python Slots")
    print("Symbols:💀👻💩🤖👾")

    while balance>0:
        print(f"Current balance:${balance}")

        bet=input("Place your bet amount:")

        if not bet.isdigit():
            print("\nPlease enter a valid amount:\n")
            continue

        bet=int(bet)
        if bet>balance:
            print("Insufficient fund")
            continue
        if bet<=0:
            print("Bet must be greater than zero")
            continue

        balance-=bet

        row=spin_row()
        print("Spinning...\n")
        print_row(row)

        payout=get_payout(row,bet)
        if payout>0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lost this round")
        balance+=payout

        play_again=input("Do you want to spin again?(Y/N):").upper()

        if play_again!='Y':
            break
    print("********************************************")
    print(f"Game over! Your final balance is ${balance}")
    print("********************************************")
                         


main()