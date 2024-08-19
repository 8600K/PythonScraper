import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
from datetime import datetime, timedelta
import re

import LoLTeamNames

# Alright, let's do this one last time.
# Firstly -> sp-happning-now and sp-next-events. Now is for time = now, next is upcoming.
# coupon-content more info = Individual entry for game. 
# Period hidden-xs = date, clock = time (classes).
# Then we have competitors -> competitor-name -> name.
# bet-price = Spread, Win, and Total
# 

# TODO Add a check to make sure the btn class is not suspended. 
# If it is suspended I guess don't add it to the array.


url = 'https://www.bovada.lv/sports/esports/league-of-legends'


lol_df = pd.DataFrame({"Team1": [],
                       "Team2": [],
                       "SpreadOU1": [],
                       "Spread1": [],
                       "SpreadOU2": [],
                       "Spread2": [],
                       "Win1": [],
                       "Win2": [],
                       "TotalOver": [],
                       "Total1": [],
                       "TotalUnder": [],
                       "Total2": [],
                       "DateTime": [],
                       "Site": []})

team1 = []
spreadou1 = []
spread1 = []
win1 = []
total_over = []
total1 = []
team2 = []
spreadou2 = []
spread2 = []
win2 = []
total_under = []
total2 = []
date_time = []
site = []

driver = webdriver.Firefox()

# Make this so every element runs through this before appending to 
# the array.


def convert_odds(odds):

    if odds == "EVEN":
        return 2.0

    odds = float(odds)
    if odds > 0:
        odds = round( (odds / 100) + 1, 2)
    else:
        odds = round( 1 - (100 / odds), 2)
    return odds

    

def get_data(url):

    namecheck0 = ''
    namecheck1 = ''
    name_bool = []

    try:
        driver.get(url)
        sleep(3)

    except:
        print("Something went very wrong. Exiting program.")


get_data(url)