import art
import resources

current_resources = resources.resources
should_stop = False

# 3. Print report.
    # a. When the user enters “report” to the prompt, a report should be generated that shows the current resource values. e.g.
        # Water: 100ml
        # Milk: 50ml
        # Coffee: 76g
        # Money: $2.5
def print_report():
    print(f"Report:")
    print(f"    Water: {current_resources["water"]}")
    print(f"    Milk: {current_resources["milk"]}")
    print(f"    Coffee: {current_resources["coffee"]}")
    print(f"    Money: {current_resources["money"]}") 

# 5. Process coins.
    # a. If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
    # b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    # c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
def prompt_payment():
    pass

# 6. Check transaction successful?
    # a. Check that the user has inserted enough money to purchase the drink they selected. E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program should say “Sorry that's not enough money. Money refunded.”.
    # b. But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time “report” is triggered. E.g.
        # Water: 100ml
        # Milk: 50ml
        # Coffee: 76g
        # Money: $2.5
    # c. If the user has inserted too much money, the machine should offer change. E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.
def transaction_successful():
    return True

    # 7. Make Coffee.
        # a. If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink should be deducted from the coffee machine resources.
        # E.g. report before purchasing latte:
            # Water: 300ml
            # Milk: 200ml
            # Coffee: 100g
            # Money: $0
        # Report after purchasing latte:
            # Water: 100ml
            # Milk: 50ml
            # Coffee: 76g
            # Money: $2.5
        # b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink.
def make_coffee(menu_option):
    print("Here is your latte. Enjoy!")

# 4. Check resources sufficient?
    # a. When the user chooses a drink, the program should check if there are enough resources to make that drink.
    # b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: “Sorry there is not enough water.”
    # c. The same should happen if another resource is depleted, e.g. milk or coffee.
def suficient_resources(menu_option):
    missing = []
    if current_resources["water"] < resources.MENU[menu_option]["ingredients"]["water"]:
        missing.append ("water")
    if current_resources["milk"] < resources.MENU[menu_option]["ingredients"]["milk"]:
        missing.append ("milk")
    if current_resources["coffee"] < resources.MENU[menu_option]["ingredients"]["coffee"]:
        missing.append ("coffee")
    if len(missing) > 0: 
        print(f"Sorry there is not enough {missing}.")
        return False
    else:    
        return True

while not should_stop:
    print(art.logo)
    # 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
        # a. Check the user’s input to decide what to do next.
        # b. The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer
    valid_option = False
    while not valid_option:
        option = input("What would you like? (espresso/latte/cappuccino): ").lower()
        # 2. Turn off the Coffee Machine by entering “off” to the prompt. For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine. Your code should end execution when this happens.
        if option == "off":
            valid_option = True
            should_stop = True
            print("Good Bye!")
        elif option == "report":
            valid_option = True
            print_report()
        elif option in resources.MENU:
            valid_option = True
            if suficient_resources(option):
                prompt_payment()
                if transaction_successful():
                    make_coffee(option)
        else:
            print("You typed an invalid option. Please choose again.")
