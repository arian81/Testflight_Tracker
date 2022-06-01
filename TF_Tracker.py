import requests
from bs4 import BeautifulSoup
from time import sleep
import asyncio

testflight_id = input(
    "Enter the testflight id or link to the testflight beta program    >   ")
CHAT_ID = int(
    input("Enter the user id recivied from t.me/userinfobot     >     "))
BOT_TOKEN = input(
    "Enter the bot token recived from t.me/botfather        >     ")
if len(testflight_id) == 8:
    url = "https://testflight.apple.com/join/" + testflight_id
else:
    url = testflight_id

# while True:
#     site = requests.get(url)
#     soup = BeautifulSoup(site.content, "html.parser")
#     beta_status = soup.find("div", class_="beta-status").span.text
#     if beta_status != "This beta is full.":
#         BOT_URL = "https://api.telegram.org/bot{}/sendMessage".format(
#             BOT_TOKEN)
#         message = "You can finally join the beta. Hooooray. \b" + url
#         requests.get(BOT_URL, params={"chat_id": CHAT_ID, "text": message,
#                      "parse_mode": "html", "disable_web_page_preview": "true"})
#     else:
#         print("Sadly the beta program is still full. Patience is a virtue so wait a bit longer. ")
#     sleep(5)


async def track():
    site = requests.get(url)
    soup = BeautifulSoup(site.content, "html.parser")
    beta_status = soup.find("div", class_="beta-status").span.text
    if beta_status != "This beta is full.":
        BOT_URL = "https://api.telegram.org/bot{}/sendMessage".format(
            BOT_TOKEN)
        message = "You can finally join the beta. Hooooray. \b" + url
        requests.get(BOT_URL, params={"chat_id": CHAT_ID, "text": message,
                     "parse_mode": "html", "disable_web_page_preview": "true"})
    else:
        print("Sadly the beta program is still full. Patience is a virtue so wait a bit longer. ")
    await asyncio.sleep(5)


# def start_track():
#     loop = asyncio.get_event_loop()
#     loop.create_task(track())


asyncio.run(track())
