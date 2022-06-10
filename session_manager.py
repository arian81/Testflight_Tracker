from aux import *
import requests
import re
from colors import Color as color
import webbrowser

def setup_session():
    session = {"url": None, "discord_id": None,
            "telegram_usr_id": None, "simplepush_key": None, "send_platform": []}
    
    while not session["url"]:
        inp = input(
            "Enter the URL/ID of the TestFlight app you want tracked \n> ")
        if re.match(r"https:\/\/testflight.apple.com\/join\/(.*)", inp):
            session["url"] = inp
        elif re.match(r"testflight.apple.com\/join\/(.*)", inp):
            session["url"] = "https://" + inp
        elif len(inp) == 8:
            inp = "https://testflight.apple.com/join/" + inp
            if requests.get(inp).status_code == 200:
                session["url"] = inp
            else:
                print(
                    f"{color.YELLOW}That's an invalid TestFlight ID.{color.YELLOW}")
        else:
            print(
                f"{color.YELLOW}That's not a proper TestFlight link. The links should be from https://TestFlight.apple.com website{color.END}")

    clear()

    session["send_platform"] = input(
        f"What platform do you wish to get notifications on ({color.BLUE}Telegram{color.END}/{color.PURPLE}Discord{color.END}/{color.RED}Simplepush{color.END}{color.DARKCYAN}Pushover{color.END})\nMultiple can be chosen!\n> ").lower().split(" ")
    for i in session["send_platform"]:
        if i == "telegram":
            get_telegram(session)
        elif i == "discord":
            get_discord(session)
        elif i == "simplepush":
            get_simplepush(session)
        elif i == "pushover":
            get_pushover(session)
        else:
            print("Platform not supported")
    return session
def edit_session(session):
    while to_edit != "exit":
        to_edit = input(f"What do you want to edit \nURL\n{color.BLUE}Telegram Info{color.End}\n{color.PURPLE}Discord Info{color.END}\n{color.DARKCYAN}Pushover Info{color.END}\n{color.RED}SimplePush Info{color.END}\nExit").lower()
        if "url" in to_edit:
            get_url(session)
        elif "telegram" in to_edit:
            get_telegram(session)
        elif "discord" in to_edit:
            get_discord(session)
        elif "pushover" in to_edit:
            get_pushover(session)
        elif "simplepush" in to_edit:
            get_simplepush(session)
        else:
            print(f"{color.CYAN}Not a valid response{color.END}")
    return session

def get_url(session):
    session["url"] = None
    while not session["url"]:
        inp = input(
            "Enter the URL/ID of the TestFlight app you want tracked \n> ")
        if re.match(r"https:\/\/testflight.apple.com\/join\/(.*)", inp):
            session["url"] = inp
        elif re.match(r"testflight.apple.com\/join\/(.*)", inp):
            session["url"] = "https://" + inp
        elif len(inp) == 8:
            inp = "https://testflight.apple.com/join/" + inp
            if requests.get(inp).status_code == 200:
                session["url"] = inp
            else:
                print(
                    f"{color.YELLOW}That's an invalid TestFlight ID.{color.YELLOW}")
        else:
            print(
                f"{color.YELLOW}That's not a proper TestFlight link. The links should be from https://TestFlight.apple.com website{color.END}")

def get_telegram(session):
    print("Get your user id from this bot")
    webbrowser.open("https://t.me/userinfobot")
    session["telegram_usr_id"] = input(
        f"Enter your {color.BLUE}Telegram{color.END} user ID\n> ")
    print("Start the following bot")
    webbrowser.open("https://t.me/TFtracker_bot")
def get_discord(session):
    print("You will need to add the following bot to one of your servers")
    webbrowser.open(
        "https://discord.com/api/oauth2/authorize?client_id=982089012330233857&permissions=2048&scope=bot")
    session["discord_id"] = input(
        "Enter your discord username(user#12345)\n> ")
def get_simplepush(session):
     session["simplepush_key"] = input(
            "Enter simplepush user key\n> ")
def get_pushover(session):
    session["pushover_usr_id"] = input(
            "Enter pushover user id\n> ")