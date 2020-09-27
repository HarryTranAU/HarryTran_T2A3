from Menu import Menu


while((user_input := Menu.menu_options()) != "9"):
    if user_input == "1":
        Menu.frontpage()

    if user_input not in ["1", "9"]:
        print("Please type the number for your menu choice...")

    input("Press 'Enter' to go back to menu...")

print("Bye!")
