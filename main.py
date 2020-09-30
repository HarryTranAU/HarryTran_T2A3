from Ozbargain import Ozbargain
from Catalogue import Catalogue
from Data import Data

main_menu = """
++++++++++++ Main Menu ++++++++++++
Please input a number option below.
1. Frontpage Deals\n
8. Options
9. Exit
Input: """

options_menu = """
+++++++++++++ Options +++++++++++++
Please input a number option below.
1. Change Upvote Threshold
2. Connect Discord Webhook\n
9. Back to Main Menu
Input: """

load_config = Data.load()
Catalogue.threshold = load_config["threshold"]


print("Welcome!")
user_input = input(main_menu)


def display_options():
    options_input = input(options_menu)
    while options_input != "9":
        if options_input == "1":
            print(f"\nCurrent Upvote threshold is {Catalogue.threshold}. "
                  "(Default=0)")
            num = input("Change Upvote Threshold to: ")
            try:
                Catalogue.set_threshold(int(num))
                print(f"Upvote threshold has been changed to {num}")
            except ValueError:
                print("Enter an Integer. Or reset to default using 0")
        elif options_input == "2":
            print("option 2 picked")
        else:
            print("Type a number, Please try again.")

        options_input = input(options_menu)


while user_input != "9":
    if user_input == "1":
        Ozbargain.frontpage()
    elif user_input == "8":
        display_options()
    else:
        print("Type a number, Please try again.")

    user_input = input(main_menu)

save_config = {"threshold": Catalogue.threshold}
Data.save(save_config)

print("Fin.")
