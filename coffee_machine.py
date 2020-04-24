# Write your code here
# print("Starting to make a coffee")
# print("Grinding coffee beans")
# print("Boiling water")
# print("Mixing boiled water with crushed coffee beans")
# print("Pouring coffee into the cup")
# print("Pouring some milk into the cup")
# print("Coffee is ready!")

# how_many_water = int(input("Write how many ml of water the coffee machine has: "))
# how_many_milk = int(input("Write how many ml of milk the coffee machine has: "))
# how_many_coffee = int(input("Write how many grams of coffee beans the coffee machine has: "))
# how_many_cups = int(input("Write how many cups of coffee you will need: \n"))

# volume = [how_many_water, how_many_milk, how_many_coffee]
class CoffeeMachine():

    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def ingredients(self, amount):
        return [200 * amount, 50 * amount, 15 * amount]

    def coffee_machine_has(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")

    def how_many_cups_can_make(self, amount_required):
        if int(self.water - amount_required[0]) <= 0:
            print("Sorry, not enough water!")
        elif int(self.milk - amount_required[1]) <= 0:
            print("Sorry, not enough milk!")
        elif int(self.beans - amount_required[2]) <= 0:
            print("Sorry, not enough coffee beams!")
        elif int(self.cups - amount_required[3]) < 0:
            print("Sorry, not enough coffee cups!")
        else:
            return True

    def what_to_make(self, choice):
        if choice == '1':
            return [250, 0, 16, 1, 4]
        elif choice == '2':
            return [350, 75, 20, 1, 7]
        elif choice == '3':
            return [200, 100, 12, 1, 6]

    def want_to_fill(self):
        how_many_water = int(input("Write how many ml of water do you want to add: "))
        how_many_milk = int(input("Write how many ml of milk do you want to add: "))
        how_many_coffee = int(input("Write how many grams of coffee beans do you want to add: "))
        how_many_cups = int(input("Write how many disposable cups of coffee do you want to add: "))
        return [how_many_water, how_many_milk, how_many_coffee, how_many_cups]

    def action(self):
        while True:
            actions = input("Write action (buy, fill, take, remaining, exit): ")
            if actions == "buy":
                what_buy = (input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main "
                                  "menu: "))
                if what_buy == "back":
                    continue
                volume = self.what_to_make(what_buy)
                if not self.how_many_cups_can_make(volume):
                    continue
                print("I have enough resources, making you a coffee!")
                self.water -= volume[0]
                self.milk -= volume[1]
                self.beans -= volume[2]
                self.cups -= volume[3]
                self.money += volume[4]

            elif actions == "fill":
                volume = self.want_to_fill()
                self.water += volume[0]
                self.milk += volume[1]
                self.beans += volume[2]
                self.cups += volume[3]

            elif actions == "take":
                print(f"I gave you ${self.money}")
                self.money = 0

            elif actions == "remaining":
                self.coffee_machine_has()

            elif actions == "exit":
                break


my_coffee = CoffeeMachine(400, 540, 120, 9, 550)
my_coffee.action()
