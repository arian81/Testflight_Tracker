from os.path import exists
from os import listdir
import requests
from bs4 import BeautifulSoup
import json
import re
from urllib import parse
import discord
from discord.ext import commands


class color:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


class Tracker:
    def __init__(self, session):
        self.data = self.read_data(session)
        self.url = self.data["url"]
        self.bot_token = self.data["bot_token"]
        self.chat_id = self.data["chat_id"]
        self.msg = ""
        self.key = self.data["simplepush_key"]  # fj7BvL
        self.discord_id = self.data["discord_id"]

    def read_data(self, file_name):
        with open(file_name, "r") as file:
            data = json.loads(file)
        return data

    def write_data(self, data_dict, session):
        with open(session, "w") as file:
            json.dumps(data_dict, file)

    def track(self):
        site = requests.get(self.url)
        soup = BeautifulSoup(site.content, "html.parser")
        title = re.search(
            "Join the (.*) beta - TestFlight - Apple", soup.title.text).group(1)
        beta_status = soup.find("div", class_="beta-status").span.text
        if beta_status == "This beta is full.":
            print(
                f"{color.RED}Sadly the beta program is still full. Patience is a virtue so wait a bit longer.{color.END}")
        else:
            print(f"{color.GREEN}Beta is Available!{color.END}")
            self.msg = f"Beta for {title} is availabe!"

    def send_telegram(self):
        bot_url = "https://api.telegram.org/bot{}/sendMessage".format(
            self.bot_token)
        requests.get(bot_url, params={"chat_id": self.chat_id, "text": self.msg,
                                      "parse_mode": "html", "disable_web_page_preview": "true"})
        print(f"{color.CYAN}Telegram Notification Sent!{color.END}")

    def send_simplepush(self):
        data = parse.urlencode(
            {'key': self.key, 'title': 'Beta is Open!', 'msg': self.msg, 'event': '69420'}).encode()
        requests.post("https://api.simplepush.io/send", data=data)
        print(f"{color.PURPLE}SimplePush Notification Sent!{color.END}")

    # TODO: Implement in different script so it can be quitted
    def send_discord(self):
        intents = discord.Intents.default()
        intents.members = True

        client = commands.Bot(command_prefix=',', intents=intents)

        @client.event
        async def on_ready():
            for user in client.users:
                if user.name + "#" + user.discriminator == self.discord_id:
                    await user.send(self.msg)
            return
