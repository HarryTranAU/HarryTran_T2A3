## **Harry Tran T2A3**

[Github Repo](https://github.com/HarryTranAU/HarryTran_T2A3)

[Trello Project Management](https://trello.com/b/b249dqpt/api-ci-cd-terminal-app)

![Ozbargain to Discord](docs/summary.png "Ozbargain to Discord")

# Summary

[Ozbargain](https://www.ozbargain.com.au/) is a popular deal site where site members post deals they have come across. This program will scrape the frontpage for active deals (not "out of stock" or "expired") and print them to the terminal. Optional: the output can also be sent to a Discord Server via Discord Webhook.

# Features

 - Scrape frontpage(www.ozbargain.com.au) to Discord channel
 - Filter deals by upvotes (options > change threshold)
 - Connect discord webhook to program
 - Save/load configurations (webhook and threshold persistent through sessions)

# Tools

`Beautiful Soup 4` was used to scrape the frontpage of Ozbargain.

`Discord webhooks` was used as an optional output for the program.

### CI/CD

`Github Actions` was used to automate the workflow.

`AWS EC2` was used for deployment

# Screenshots

**Deal on Ozbargain**

![Ozbargain Deal](docs/ozbargain_deal_ss.png "Ozbargain Deal")


**Terminal Output**

![Ozbargain Deal: Terminal Output](docs/terminal_deal_ss.png "Ozbargain Deal: Terminal Output")


**Discord Output**

![Ozbargain Deal: Discord Output](docs/discord_deal_ss.png "Ozbargain Deal: Discord Output")

# Installation (Linux)

Install Python and git
```
sudo apt-get update
sudo apt-get install git
sudo apt-get install python3
```

Git clone and Open Folder
```
git clone https://github.com/HarryTranAU/HarryTran_T2A3.git
cd HarryTran_T2A3
```

Optional Virtual Environment (Recommended)

```
sudo apt-get install python3-venv
python3 -m venv venv
source venv/bin/activate
```

Install Pip/requirements
```
sudo apt-get install python3-pip
pip install -r requirements.txt
```

Program Start
```
python main.py
```

# Discord/Webhook Guide

[1. Discord Download](https://discord.com/download)

[2. How to create a Discord Server (howtogeek.com)](https://www.howtogeek.com/318890/how-to-set-up-your-own-discord-chat-server/#:~:text=To%20create%20your%20own%20server,a%20Server%E2%80%9D%20on%20the%20left.)

[3. Creating a Webhook on your Server](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks#:~:text=Choose%20the%20repository%20that%20you,the%20%22Payload%20URL%22%20blank.)

# Flowchart

![Flowchart](docs/flowchart.png "Flowchart")

# Version History

### `NEXT UPDATE: Remembering deals sent to Discord (Prevent Duplicates)`

Version goal: remembering which deals have been sent to discord to only send new deals.

To be implemented:
 - deals.JSON to save sent deals
 - function to find the difference between scraped deals and known deals

### `Version 0.5: Discord Output`

Version goal: Output Deals to a discord server

To be implemented:
 - Discord webhook
 - Saving discord url
 - Discord message formatting/embed

### `Version 0.4: User Options`

Version goal: Allow user to set upvote threshold.

To be implemented:
 - Add options to Menu
 - Save options to file

### `Version 0.3: Filters`

Version goal: Filter out expired deals

To be implemented:
 - Changes to how catalogue is populated

### `Version 0.2: User Interface`

Version goal: Create interface for user interaction and choices.

To be implemented:
 - Menu

### `Version 0.1: Foundation`

Version goal: Implement web scraper for site 1 (ozbargain.com.au) and output to terminal.

To be implemented:
 - Entry point
 - Scraper
 - Deal
 - Catalogue
