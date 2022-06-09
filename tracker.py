import requests
from bs4 import BeautifulSoup
import json
import re
from urllib import parse
import discord
from discord.ext import commands
from colors import Color as color


class Tracker:
    def __init__(self, session):
        self.data = session
        self.url = self.data["url"]
        self.telegram_bot_token = self.data["telegram_bot_token"]
        self.discord_id = self.data["discord_id"]
        # OTgyMDg5MDEyMzMwMjMzODU3.G_yHnN.GJdeFcua5Fhpz-etvHby5ib7kup1RqYPIhu_B0
        self.discord_bot_token = self.data["discord_bot_token"]
        self.telegram_usr_id = self.data["telegram_usr_id"]
        self.simplepush_key = self.data["simplepush_key"]    # fj7BvL
        # av28dsrg8xaj1yfyz49rzv8xj1sgf7
        self.pushover_token = self.data["pushover_token"]
        # uszvd8xhs424xphpwhz3i7n6u6tkp7
        self.pushover_usr_id = self.data["pushover_usr_id"]
        self.msg = None
        self.logo = None

    def track(self):
        site = requests.get(self.url)
        soup = BeautifulSoup(site.content, "html.parser")
        title = re.search(
            "Join the (.*) beta - TestFlight - Apple", soup.title.text).group(1)
        self.logo = re.search("background-image: url\((.*)\);",
                              soup.find("div", class_="app-icon")["style"]).group(1)
        beta_status = soup.find("div", class_="beta-status").span.text
        if beta_status == "This beta is full.":
            print(
                f"{color.RED}Sadly the beta program is still full. Patience is a virtue so wait a bit longer.{color.END}")
        else:
            print(f"{color.GREEN}Beta is Available!{color.END}")
            self.msg = f"Beta for {title} is availabe!"

    def send_telegram(self):
        bot_url = f"https://api.telegram.org/bot{self.telegram_bot_token}/sendPhoto"
        requests.get(bot_url, params={
                     "chat_id": self.telegram_usr_id, "photo": self.logo, "caption": self.msg})
        print(f"{color.BLUE}Telegram Notification Sent!{color.END}")

    def send_simplepush(self):
        data = parse.urlencode(
            {'key': self.simplepush_key, 'title': 'Beta is Open!', 'msg': self.msg, 'event': '69420'}).encode()
        requests.post("https://api.simplepush.io/send", data=data)
        print(f"{color.RED}SimplePush Notification Sent!{color.END}")

    def send_pushover(self):
        r = requests.post("https://api.pushover.net/1/messages.json", data={
            "token": self.pushover_token,
            "user": self.pushover_usr_id,
            "message": self.msg
        },
            files={
            "attachment": ("appicon.png", open(self.logo, "rb"), "image/jpeg")
        })
        print(f"{color.DARKCYAN}Pushover Notification Sent!{color.END}")

    def send_discord(self):
        intents = discord.Intents.default()
        intents.members = True

        client = commands.Bot(command_prefix=',', intents=intents)

        @client.event
        async def on_ready():
            for user in client.users:
                if user.name + "#" + user.discriminator == self.discord_id:
                    await user.send(file=discord.File('logo.png'), content=self.msg)
                    print(f"{color.PURPLE}Discord Notification Sent!{color.END}")
                    await client.close()
        client.run(self.discord_bot_token)
