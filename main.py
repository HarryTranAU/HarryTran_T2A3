from Ozbargain import Ozbargain
from Catalogue import Catalogue

main_menu = """
Welcome! Please input a number option below.
1. Frontpage Deals\n
8. Options
9. Exit
Input: """

options_menu = """
Please input a number option below.
1. Threshold\n
9. Back to Main Menu
Input: """

user_input = input(main_menu)


def display_options():
    options_input = input(options_menu)
    while options_input != "9":
        if options_input == "1":
            num = input("Change Threshold to: ")
            # validate input here
            Catalogue.set_threshold(int(num))
            print(f"Upvote threshold has been changed to {num}")
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

print("Fin.")
