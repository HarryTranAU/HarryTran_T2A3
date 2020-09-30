from Ozbargain import Ozbargain
from Catalogue import Catalogue
from Data import Data
from Bot import Bot_discord

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
Data.threshold = load_config["threshold"]
Bot_discord.url = load_config["discord_hook"]
save_config = load_config

print("Welcome!")
user_input = input(main_menu)


def display_options():
    options_input = input(options_menu)

    while options_input != "9":
        if options_input == "1":
            print(f"\nCurrent Upvote threshold is {Data.threshold}. "
                  "(Default=0)")
            num = input("Change Upvote Threshold to: ")
            try:
                Data.threshold = int(num)
                print(f"Upvote threshold has been changed to {num}")
                save_config["threshold"] = int(num)
                Data.save(save_config)
            except ValueError:
                print("Enter an Integer. Or reset to default using 0")

        elif options_input == "2":
            print("Go to README.md for instructions on how to obtain webhook.")
            user_webhook = input("Please paste your discord webhook below:\n")
            if Bot_discord.validate_url(user_webhook):
                Bot_discord.set_url(user_webhook)
                save_config["discord_hook"] = user_webhook
                Data.save(save_config)
                print("Discord webhook saved successfully!")

        else:
            print("Type a number, Please try again.")

        options_input = input(options_menu)


while user_input != "9":
    if user_input == "1":
        Ozbargain.frontpage(Data.threshold)
        to_discord = input("Would you like to send this to discord? (yes/no)")
        if to_discord == "yes":
            if Bot_discord.url == "":
                print("Please setup Discord webhooks in Options first.")
            else:
                Bot_discord.send_deals(Catalogue.deals)

    elif user_input == "8":
        display_options()

    else:
        print("Type a number, Please try again.")

    user_input = input(main_menu)

print("\nGoodbye!")
