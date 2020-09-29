from Ozbargain import Ozbargain

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
            print("threshold option chosen")
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

print("Program Fin.")

# while((user_input := Menu.menu_options()) != "9"):
#     if user_input == "1":
#         Menu.frontpage()

#     if user_input not in ["1", "9"]:
#         print("Please type the number for your menu choice...")

#     input("Press 'Enter' to go back to menu...")

# print("Bye!")
