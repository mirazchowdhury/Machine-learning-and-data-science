class Atm:
    #constructor(special function)->superpower->no need to call the constructor,when you make an object of a constructor,it will automatically call and the code inside will automatically execute

    def __init__(self):
        self.pin=''
        self.balance=0
        self.menu()
        print("Ami nije nije execute hoi jai")

    #menu function
    def menu(self):
        user_input=input("""
        1. Press 1 to create PIN
        2. Press 2 to change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw
        5. Exit
        """)
        if user_input=='1':
            #create pin
            self.create_pin()
        elif user_input == '2':
            #change pin
            self.change_pin()
        elif user_input == '3':
            #check balalnce
            self.check_balance()
        elif user_input == '4':
            #withdraw
            self.withdraw()
        else:
            exit()
    def create_pin(self):
        user_pin=input("Enter your PIN:")
        self.pin=user_pin

        user_balance=int(input("Input your balance:"))
        self.balance=user_balance

        print("Pin created successfully")
        self.menu() #again menu te chole jabe
    def change_pin(self):
        old_pin=input("Please enter your old PIN:")

        if old_pin == self.pin:
        #let change the pin
            new_pin = input("Enter the new PIN:")
            self.pin=new_pin
            print("PIN changed successfully")
            self.menu()
        else:
            print("Wrong PIN!!!!")
            self.menu()
    def check_balance(self):
        user_pin=input("Enter your PIN:")
        if user_pin==self.pin:
            print("Your balance in ",self.balance)
            self.menu()
        else:
            print("You have entered the wrong PIN")
            self.menu()
    def  withdraw(self):
        user_pin=input("Enter the PIN:")
        if user_pin == self.pin:
            #allow to withdraw
            amount = int(input("Enter the amount:"))
            if amount<=self.balance:
                self.balance=self.balance-amount
                print("Withdrawl Successful!!!")
                print("Your balance is ",self.balance)
                self.menu()
            else:
                print("Gareeb admi!!!")
                self.menu()
        else:
            print("You have entered wrong PIN")
            self.menu()

obj = Atm()
print(type(obj))
