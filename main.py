class Atm:
    def __init__(self, cardnumber , pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def balanceinquiry(self):
        print("Your balance is $100")

    def cashwithdrawal(self , amount):
        new_amount = 100-amount
        print("You withdrawed" + str(amount) + "YOur reamining balance is : " + str(new_amount))

def main():
    name = input("Hello what is your name ? ")
    print("hello" + name)
    cardnumber = input("Insert your cradnumber : ")
    pin = input("Enter your pin : ")
    new_user = Atm(cardnumber , pin)

    print("Choose your activity")
    print("1. Balance inquiry")
    print("2. Cash withdrawal")
    activity = int(input("ENter activity choice : "))

    if (activity == 1):
        new_user.balanceinquiry()

    elif (activity == 2):
        amount = int(input("ENter the amoount : "))
        new_user.cashwithdrawal(amount)

    else:
        print("Enter a valid number")

if __name__ == "__main__":
    main()
