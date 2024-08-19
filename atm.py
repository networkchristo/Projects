from cardHolder import cardHolder

def print_menu():
    # Print options to the user 
    print("Please choose from one of the following options....")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

def deposit(cardHolder):
    try:
         deposit = float(input ("How much would you like to deposit: "))
         cardHolder.set_balance(cardHolder.get_balance() + deposit)
         print("Thank you for your money. Your new balance is: ", str(cardHolder.get_balance()))
    except:
        print("Invalid input")

def withdraw(cardHolder):
    try:
        withdraw = float(input ("How much money would like to withdraw: "))
        if cardHolder.get_balance() < withdraw:
            print("Insufficient funds in your account :(")
        else:
            cardHolder.set_balance(cardHolder.get_balance() - withdraw)
            print("You're good to go.")
    except:
        print("Invalid input")
    
def check_balance(cardHolder):
    print("Your current balance is : ", cardHolder.get_balance())

if __name__ == "__main__":
    current_user = cardHolder("", "", "", "", "")

    list_of_cardHolders = []
    list_of_cardHolders.append(cardHolder("4431728432192832", 1234, "Blesson", "Biju Abharam", 129.21))
    list_of_cardHolders.append(cardHolder("2830137428293423", 9182, "Joel", "Gigi", 928.32))
    list_of_cardHolders.append(cardHolder("8329201834744927", 1029, "Juby", "Jose Abharam", 239.09))
    list_of_cardHolders.append(cardHolder("2938470174387392", 1208, "Hadhi", "Haneef", 4328.32))
    list_of_cardHolders.append(cardHolder("0935826709237845", 8794, "Nikhil", "Thampi", 20937.73))
    list_of_cardHolders.append(cardHolder("0192387410983274", 3289, "Alan", "Biju Abharam", 2948.32))

    debitCardNum = ""
    while True:
        try:
            debitCardNum = input ("Please enter the debit card: ")
            # Checking the account
            debitMatch = [holder for holder in list_of_cardHolders if holder.cardNum == debitCardNum]
            if (len(debitMatch) > 0):
                current_user = debitMatch[0]
                break
            else:
                print("Card Number is not recognized. Please try again")
                 
        except:
            print("Card Number is not recognized. Please try again.")

# Asking for the pin

while True:
    try:
        userPin = int(input ("Please enter your pin : ").strip())
        if (current_user.get_pin() == userPin):
            break
        else:
            print("Invalid PIN. Please try again")
    except:
        print("Invalid Pin. Please try again")

# Printing the options

print("Welcome ", current_user.get_firstname(), " :)")
option = 0
while (option != 4):
    print_menu()
    try:
        option = int(input ())
    except:
        print("Invalid input. Please try again.")
    
    if option == 1:
        deposit(current_user)
    elif option == 2:
        withdraw(current_user)
    elif option == 3:
        check_balance(current_user)
    elif option == 4:
        break
    else:
        option = 0

print("Thank you. Have a nice day")    
