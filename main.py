import re
import webbrowser
from colors import Color as color
from time import sleep
from os import listdir
from os.path import exists
from tracker import Tracker
import requests
import ascii
from aux import *
import webbrowser
from session_manager import *


if __name__ == "__main__":
    session = None

    clear()

    if not exists(".env"):
        print(f"{color.CYAN}.env file not found.\nPlease create a .env according to the GitHub instruction and try again{color.END}")
        exit()

    print(ascii.welcome_text_logo)
    sleep(1)
    for i in ascii.welcome_text_TFT.split("\n"):
        print(i)
        sleep(0.1)

    if exists("session1.json"):
        print(f"{color.CYAN}Previous sessions found!{color.END}")
        for i in listdir():
            if "session" in i:
                print(i)
        restore = input(
            "Do you wish to restore a previous session or start a new one\n> ")
        if ("restore" in restore) or ("previous" in restore):
            while True:
                session_inp = "session" + input("> ")
                if re.match(r"session\d*") and exists(session_inp):
                    resp = input("Do you wish to edit the saved session\n> ")
                    if "y" in resp:
                        session = edit_session(session_inp)
                    else:
                        session = read_data(session_inp)
                    break
        else:
            session = setup_session()
    else:
        session = setup_session()
    
    clear()
    #TODO: create the object
    #save the data to file

    

