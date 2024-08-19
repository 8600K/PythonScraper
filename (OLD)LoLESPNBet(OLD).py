from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep
import pandas as pd
from datetime import datetime
import string

import LoLTeamNames


def check_even(ele):
    if "Even" not in ele:
        return ele
    else:
        return '+100'
    
url = 'https://espnbet.com/'


lol_df = pd.DataFrame({"Team1": [],
                       "Team2": [],
                       "SpreadOU1": [],
                       "Spread1": [],
                       "SpreadOU2": [],
                       "Spread2": [],
                       "Win1": [],
                       "Win2": [],
                       "TotalOU1": [],
                       "Total1": [],
                       "TotalOU2": [],
                       "Total2": [],
                       "DateTime": []})

team1 = []
spreadou1 = []
spread1 = []
win1 = []
totalou1 = []
total1 = []
team2 = []
spreadou2 = []
spread2 = []
win2 = []
totalou2 = []
total2 = []
date_time = []

driver = webdriver.Firefox()
    
def get_data(url):

    try:
        driver.get(url)
        sleep(3)

        # Use this to get the length, then do CSS Selector and use a f string to increment. 
        # Click on LoL and then we should be off to the races.
        find_length = driver.find_elements(By.CSS_SELECTOR, '.w-\[245px\]')
        
        for sel in find_length:
            
            nav_length = len(sel.text.splitlines())
            #print(nav_length)

        # Iterate through the actual elements based on length found from sel.
        for i in range(nav_length):
            select_lol = driver.find_elements(By.CSS_SELECTOR, f'.w-\[245px\] > li:nth-child({i})')
            for sel1 in select_lol:
                selection = sel1.text.splitlines()
                # TEST to make sure this runs when LoL is not live!
                if selection[0] == 'LoL':
                    #print("Here we are...")
                    sel1.click()

                    # Next up!!! This works, might check to make sure I don't need to add + 1 to length. 
                    league_lengths = driver.find_elements(By.CSS_SELECTOR, '.w-\[245px\]')
                    for length_of_leagues in league_lengths:
                        #print(length_of_leagues.text)
                        #print(len(length_of_leagues.text.splitlines()))
                        league_length = len(length_of_leagues.text.splitlines())
                    
                    for i in range(league_length):
                        select_league = driver.find_elements(By.CSS_SELECTOR, f'.w-\[245px\] > li:nth-child({i + 1})')
                        for sel2 in select_league:
                            #print("This never runs, does it?")
                            sel2.click()
                            sleep(1)

             
                            entries = driver.find_elements(By.CLASS_NAME, 'bg-card-primary')
                            printable = set(string.printable)
                            for entry in entries:
                                #print("And here we go...")
                                #print(entry.text.splitlines())
                                n = entry.text.splitlines()

                                # Need to check if it's live and change things if it is.

                                print(n)
                                if n[2] == '--' or n[4] == '--':
                                    continue
                                if n == 12:
                                    # This means it is currently live and we need to handle it slightly differently.
                                    print(n) # TODO. When they are live see what we need to do for this. Very simple and fast fix. 
                                    # Everything else is working perfectly though!
                                else:
                                    #print("We ran!")
                                    team1.append(LoLTeamNames.standardize_names(n[1]))
                                    team2.append(LoLTeamNames.standardize_names(n[3]))
                                    win1.append(check_even(n[2]))
                                    win2.append(check_even(n[4]))
                                    time_fixed = ''.join(filter(lambda x: x in printable, n[0]))
                                    date_time.append(time_fixed)
                                    total1.append('None')
                                    total2.append('None')
                                    spread1.append('None')
                                    spread2.append('None')
                                    #print("We still ran!")


                                


                    
    except:
        print("Something in the main URL went wrong.")

get_data(url)

lol_df['Team1'] = team1
lol_df['Team2'] = team2
lol_df['Win1'] = win1
lol_df['Win2'] = win2
lol_df['Spread1'] = spread1
lol_df['Spread2'] = spread2
lol_df['Total1'] = total1
lol_df['Total2'] = total2
lol_df['DateTime'] = date_time

print(lol_df.to_string())

lol_df.to_csv('LoL_ESPNBet.csv')
