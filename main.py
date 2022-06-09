import re
import webbrowser
from colors import Color as color
from time import sleep
from os import listdir
from os.path import exists
from tracker import Tracker as tracker
from logging import exception
from platform import platform
import requests
import ascii
from aux import *
import webbrowser


if __name__ == "__main__":
    # url = None
    # telegram_bot_token = None
    # discord_id = None
    # telegram_usr_id = None
    # key = None
    session = {"url": None, "telegram_bot_token": None, "discord_id": None,
               "telegram_usr_id": None, "simplepush_key": None}

    clear()
    print(ascii.welcome_text_logo)
    sleep(1)
    for i in ascii.welcome_text_TFT.split("\n"):
        print(i)
        sleep(0.1)

    if exists("session1.json"):
        print("Enter session number to be restored")
        for i in listdir():
            if "session" in i:
                print(i)
        while True:
            session_inp = "session" + input("> ")
            if re.match(r"session\d*") and exists(session_inp):
                session = read_data(session_inp)

    else:
        while not session["url"]:
            inp = input(
                "Enter the URL/ID of the TestFlight app you want tracked \n> ")
            if re.match(r"https:\/\/TestFlight.apple.com\/join\/(.*)", inp):
                session["url"] = inp
            elif re.match(r"TestFlight.apple.com\/join\/(.*)", inp):
                session["url"] = "https://" + inp
            elif len(inp) == 8:
                inp = "https://TestFlight.apple.com/join/" + inp
                if requests.get(inp).status_code == 200:
                    session["url"] = inp
                else:
                    print(
                        f"{color.YELLOW}That's an invalid TestFlight ID.{color.YELLOW}")
            else:
                print(
                    f"{color.YELLOW}That's not a proper TestFlight link. The links should be from https://TestFlight.apple.com website{color.END}")

        clear()
        send_platform = input(
            f"What platform do you wish to get notifications on ({color.BLUE}Telegram{color.END}/{color.PURPLE}Discord{color.END}/{color.RED}Simplepush{color.END})\nMultiple can be chosen!\n> ").lower()
        if (send_platform == "telegram"):
            print("Get your user id from this bot")
            webbrowser.open("https://t.me/userinfobot")
            session["telegram_usr_id"] = input(
                f"Enter your {color.BLUE}Telegram{color.END} user ID\n >")
            print("Start the following bot")
            webbrowser.open("")
        if (send_platform == "discord"):
            print("You will need to add the following bot to one of your servers")
            webbrowser.open(
                "https://discord.com/api/oauth2/authorize?client_id=982089012330233857&permissions=2048&scope=bot")
            session["discord_id"] = input(
                "Enter your discord username(user#12345)\n> ")
