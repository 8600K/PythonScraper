# Thunderpick
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep
import pandas as pd

import LoLTeamNames



driver = webdriver.Firefox()

lol_url = "https://thunderpick.io/en/esports/league-of-legends"
csgo_url = "https://thunderpick.io/en/esports/csgo"


lol_df = pd.DataFrame({"Team1": [],
                       "Win1": [],
                       "Team2": [],
                       "Win2": []})

team1 = []
team2 = []
win1 = []
win2 = []

# ACTUALLY MIGHT USE UPCOMING - LIVE for an easier time. CHECK IF YOU CAN SEE IF SELENIUM CAN TELL IF SOMETHING IS DISABLED. IF SO CHANGE, IF NOT, OH WELL.

def divide_elements(lst, number):
    for i in range(0, len(lst), number):
        yield lst[i:i + number]

def convert_odds(odds):
    if odds >= 2.00:
        print("Greater or equal to 2.00")
        new_odds = round( ((odds - 1) * 100) )
    else:
        print("Nvm we are less than 2")
        new_odds = round( (-100 / (odds - 1)) )
    return new_odds

def get_data(url):
    #try:
        driver.get(url)
        sleep(3)

        for i in range(30):
            print("This run?")
            elements = driver.find_elements(By.CSS_SELECTOR, f'div.match-group:nth-child({i + 1})')
            print("Hey?")
            for element in elements:
                fields = element.text.split('\n')
                #print('Aha!', fields[4], fields[6])


                
                name1 = LoLTeamNames.standardize_names(fields[3])
                name2 = LoLTeamNames.standardize_names(fields[5])

                print(name1, name2)

                if name1 < name2:
                    print(fields[4], fields[6])
                    team1.append(name1)
                    team2.append(name2)
                    win1.append(convert_odds(float(fields[4])))
                    win2.append(convert_odds(float(fields[6])))
                else:
                    print(fields[4], fields[6])
                    team1.append(name2)
                    team2.append(name1)
                    win1.append(convert_odds(float(fields[6])))
                    win2.append(convert_odds(float(fields[4])))
    #except:
        print("There was an error with the website.")


get_data(lol_url)


lol_df['Team1'] = team1
lol_df['Team2'] = team2
lol_df['Win1'] = win1
lol_df['Win2'] = win2

print(lol_df)

lol_df.to_csv("Thunderpick.csv")