# all inputs should have exception handling


class Coffee:
    
    def __init__(self):
        self.price = 1.10
        self.milk = 0
        self.sugar = 0

    def get_price(self):
        return self.price + 0.1 * self.sugar + 0.15 * self.milk

    def set_condiments(self):
        happy = False
        while happy == False:
            milk = int(input("How many milk shots would you like?\n"))
            sugar = int(input("How many sugar cubes would you like?\n"))
            if (milk + sugar) > 3:
                print("Sorry! You can only have 3 condiments!")
            else: 
                self.milk = milk
                self.sugar = sugar
                happy = True

    def __str__(self):
        return f"${self.get_price():.2f} Regular Coffee with {self.milk} milk shots and {self.sugar} sugar cubes."


class Espresso(Coffee):

    def __init__(self):
        super().__init__()

    def get_price(self):
        return super().get_price() * 1.2
    
    def __str__(self):
        return f"${self.get_price():.2f} Espresso with {self.milk} milk shots and {self.sugar} sugar cubes."

class Cappuccino(Coffee):

    def __init__(self):
        super().__init__()

    def get_price(self):
        return super().get_price() * 1.2 * 1.15

    def set_condiments(self):
        happy = False
        while happy == False:
            sugar = int(input("How many sugar cubes would you like?\n"))
            if sugar > 3: 
                print("Sorry! You can only have 3 condiments!\n")
            else:
                self.sugar = sugar
                happy = True

    def __str__(self):
        return f"${self.get_price():.2f} Cappuccino with {self.sugar} sugar cubes."


class CoffeeMachine:

    def __init__(self):
        interest = True
        while interest == True:
            coffee = int(input("What type of coffee would you like? \n Enter 1 for regular, 2 for Espresso, or 3 for Cappuccino\n"))
            if coffee == 1:
                purchase = Coffee()
                purchase.set_condiments()
                print(f"Here is your {str(purchase)}")

            if coffee == 2:
                purchase = Espresso()
                purchase.set_condiments()
                print(f"Here is your {str(purchase)}")
            if coffee == 3:
                purchase = Cappuccino()
                purchase.set_condiments()
                print(f"Here is your {str(purchase)}")

            interest = int(input("Would you like to order another coffee? 1 for yes, 2 for no.\n"))




def main():
    coffee_machine = CoffeeMachine()

if __name__ == "__main__":
  main()