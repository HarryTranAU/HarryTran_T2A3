from Ozbargain import Ozbargain
from Catalogue import Catalogue
from Data import Data
from Bot import BotDiscord

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

config_file = Data()
load_config = config_file.load()
config_file.threshold = load_config["threshold"]
BotDiscord.url = load_config["discord_hook"]
save_config = load_config

print("Welcome!")
user_input = input(main_menu)


def display_options() -> None:
    """ A function containing the Options Sub-menu """
    options_input = input(options_menu)

    while options_input != "9":
        if options_input == "1":
            print(f"\nCurrent Upvote threshold is {config_file.threshold}. "
                  "(Default=0)")
            num = input("Change Upvote Threshold to: ")
            try:
                config_file.threshold = int(num)
                print(f"Upvote threshold has been changed to {num}")
                save_config["threshold"] = int(num)
                config_file.save(save_config)
            except ValueError:
                print("Enter an Integer. Or reset to default using 0")

        elif options_input == "2":
            print("Refer to README.md on how to obtain Discord webhook.")
            user_webhook = input("Please paste your discord webhook below:\n")
            if BotDiscord.validate_url(user_webhook):
                BotDiscord.set_url(user_webhook)
                save_config["discord_hook"] = user_webhook
                config_file.save(save_config)
                print("Discord webhook saved successfully!")

        else:
            print("Type a number, Please try again.")

        options_input = input(options_menu)


while user_input != "9":
    if user_input == "1":
        Ozbargain.frontpage(config_file.threshold)
        to_discord = input("Would you like to send this to discord? (yes/no)")
        if to_discord == "yes":
            if BotDiscord.url == "":
                print("Please setup Discord webhooks in Options first.")
            else:
                BotDiscord.send_deals(Catalogue.deals)

    elif user_input == "8":
        display_options()

    else:
        print("Type a number, Please try again.")

    user_input = input(main_menu)

print("\nGoodbye!")
