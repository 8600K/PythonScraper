import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import json
import re
from time import sleep
import calendar 

from datetime import datetime, timedelta

import LoLTeamNames

driver = webdriver.Firefox()

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

namecheck0 = ''
namecheck1 = ''
name_bool = True

# With how Pinnacle is setup I have to get the time of the match and then
# check match names, and time to find a proper match in the database. 


url = 'https://www.pinnacle.com/en/esports/league-of-legends/leagues/'

# Plan.
# Go to URL.
# leagueoflegends -> leagues. Click on top leagues and maybe search through a couple of special ones.
# Click on match and then get scores.
# ???
# Profit.

# Function to convert odds to American.
# It also checks for the case the odds are labaled as EVEN.
def convert_odds(odds):

    if odds == "EVEN":
        return 2.0
    else:
        return odds

# Main function
def get_data(url):
    y = 100
    # month_to_num = {name: num for num, name in enumerate(calendar.month_abbr) if num} Not needed at this time. 
    

    driver.get(url)
    sleep(3)

    # Get the top and all leagues' columns
    top_leagues = driver.find_elements(By.CSS_SELECTOR, '.style_desktop_middle__2fvpO > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(2)')
    all_leagues = driver.find_elements(By.CSS_SELECTOR, '.style_desktop_middle__2fvpO > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(2)')

    all_num = 0
    top_num = 0

    
    

    # Get length of columns for 'top leagues'
    for top_length in top_leagues:
        top_num = len(top_length.text.splitlines())
        print(top_num)
    # Get length of columns for 'all leagues'
    for all_length in all_leagues:
       all_num = len(all_length.text.splitlines())
       print(all_num)

    # This is in response to in case top leagues is missing. In this case only top leagues will have values and all leagues will be empty.
    if not all_leagues:
        all_num = top_num
        top_num = 0
    
    print('All Leagues: ', len(all_leagues))
    # Add top_num and all_num together (see above for loops) and then divide by 2. 
    # The reason for the divide is every column has the name and then a number, so by dividing by 2 we ignore the added number.
    
    
    
    for i in range((top_num // 2), (top_num + all_num // 2) ):
        print("What is i right now?", i)
        top = driver.find_elements(By.CLASS_NAME, 'style_listItem__1m5iG')[i]
        print(top.text)
    
        if 'League of Legends' not in top.text:
            continue
            # Just an added check to make sure we're going to the right place. This should never run but figured it'd be worth it to check.
        top.click()
        
        sleep(2.5)

    

        try:
            matches = driver.find_element(By.CSS_SELECTOR, '#period\:0')
            matches.click()
            sleep(1.5)
        except:
            driver.execute_script("window.history.go(-1)")
            
            # Clicks on matches so we don't have to filter ourselves.

        # Here we go, the actual entries. This is where all the data is gathered. 
        entries = driver.find_elements(By.CLASS_NAME, 'style_row__12oAB')
        for entry in entries:
            n = entry.text.splitlines()
            print(n) # ------------! 

            name1 = n[0].split()
            name1 = name1[:-1]
            name1 = ' '.join(name1)

            name2 = n[1].split()
            name2 = name2[:-1]
            name2 = ' '.join(name2)

            # This is if all elements are detected.
            if len(n) == 14:
                print("This ran! (1)")
                namecheck0 = LoLTeamNames.standardize_names(name1)
                namecheck1 = LoLTeamNames.standardize_names(name2)
                if namecheck0 < namecheck1:
                    team1.append(namecheck0)
                    team2.append(namecheck1)
                    name_bool = True
                else:
                    team1.append(namecheck1)
                    team2.append(namecheck0)
                    name_bool = False
                #date_time.append(n[2])

                try: 
                    parsed_t = datetime.strptime(n[2], "%H:%M")
                    parsed_t -= timedelta(hours=4)
                    formatted_t = parsed_t.strftime("%H:%M")
                    date_time.append(formatted_t)
                except:
                    date_time.append(n[2])

                site.append('Pinnacle')
                if name_bool:
                    win1.append(convert_odds(n[3]))
                    win2.append(convert_odds(n[4]))
                    spreadou1.append(n[5])
                    spread1.append(convert_odds(n[6]))
                    spreadou2.append(n[7])
                    spread2.append((convert_odds(n[8])))
                    total_over.append(n[9])
                    total1.append((convert_odds(n[10])))
                    total_under.append(n[11])
                    total2.append((convert_odds(n[12])))
                else:
                    win1.append(convert_odds(n[4]))
                    win2.append(convert_odds(n[3]))
                    spreadou1.append(n[7])
                    spread1.append(convert_odds(n[8]))
                    spreadou2.append(n[5])
                    spread2.append((convert_odds(n[6])))
                    total_over.append(n[9])
                    total1.append((convert_odds(n[10])))
                    total_under.append(n[11])
                    total2.append((convert_odds(n[12])))
            # This is a bit trickier, this means either total or spread is missing. Therefore it runs its own checks.
            elif len(n) == 10:
                print("This ran! (2)")
                namecheck0 = LoLTeamNames.standardize_names(name1)
                namecheck1 = LoLTeamNames.standardize_names(name2)
                if namecheck0 < namecheck1:
                    team1.append(namecheck0)
                    team2.append(namecheck1)
                    name_bool = True
                else:
                    team1.append(namecheck1)
                    team2.append(namecheck0)
                    name_bool = False

                try:
                    parsed_t = datetime.strptime(n[2], "%H:%M")
                    parsed_t -= timedelta(hours=4)
                    formatted_t = parsed_t.strftime("%H:%M")
                    date_time.append(formatted_t)
                except:
                    date_time.append(n[2])
                site.append('Pinnacle')
                win1.append(convert_odds(n[3]))
                win2.append(convert_odds(n[4]))

                if n[5] == '+1.5' or n[5] == '-1.5':
                    
                    if name_bool:
                        spreadou1.append(n[5])
                        spread1.append((convert_odds(n[6])))
                        spreadou2.append(n[7])
                        spread2.append((convert_odds(n[8])))
                        total_over.append(pd.NA)
                        total1.append(pd.NA)
                        total_under.append(pd.NA)
                        total2.append(pd.NA)
                    else:
                        spreadou1.append(n[7])
                        spread1.append((convert_odds(n[8])))
                        spreadou2.append(n[5])
                        spread2.append((convert_odds(n[6])))
                        total_over.append(pd.NA)
                        total1.append(pd.NA)
                        total_under.append(pd.NA)
                        total2.append(pd.NA)
                else:
                    if name_bool:
                        spreadou1.append(pd.NA)
                        spread1.append(pd.NA)
                        spreadou2.append(pd.NA)
                        spread2.append(pd.NA)
                        total_over.append(n[5])
                        total1.append((convert_odds(n[6])))
                        total_under.append(n[7])
                        total2.append((convert_odds(n[8])))
                    else: 
                        spreadou1.append(pd.NA)
                        spread1.append(pd.NA)
                        spreadou2.append(pd.NA)
                        spread2.append(pd.NA)
                        total_over.append(n[5])
                        total1.append((convert_odds(n[6])))
                        total_under.append(n[7])
                        total2.append((convert_odds(n[8])))
            
            # This means both spread and total are missing. 
            elif len(n) == 6:
                print("This ran! (4)")
                namecheck0 = LoLTeamNames.standardize_names(name1)
                namecheck1 = LoLTeamNames.standardize_names(name2)
                if namecheck0 < namecheck1:
                    team1.append(namecheck0)
                    team2.append(namecheck1)
                    name_bool = True
                else:
                    team1.append(namecheck1)
                    team2.append(namecheck0)
                    name_bool = False
                try:
                    parsed_t = datetime.strptime(n[2], "%H:%M")
                    parsed_t -= timedelta(hours=4)
                    formatted_t = parsed_t.strftime("%H:%M")
                    date_time.append(formatted_t)
                except:
                    date_time.append(n[2])
                site.append('Pinnacle')
                if name_bool:
                    win1.append(convert_odds(n[3]))
                    win2.append(convert_odds(n[4]))
                    spreadou1.append(pd.NA)
                    spreadou2.append(pd.NA)
                    spread1.append(pd.NA)
                    spread2.append(pd.NA)
                    total_over.append(pd.NA)
                    total_under.append(pd.NA)
                    total1.append(pd.NA)
                    total2.append(pd.NA)
                else:
                    win1.append(convert_odds(n[4]))
                    win2.append(convert_odds(n[3]))
                    spreadou1.append(pd.NA)
                    spreadou2.append(pd.NA)
                    spread1.append(pd.NA)
                    spread2.append(pd.NA)
                    total_over.append(pd.NA)
                    total_under.append(pd.NA)
                    total1.append(pd.NA)
                    total2.append(pd.NA)
            
            else:
                print("This ran! (5)")
                continue

    
        driver.execute_script("window.history.go(-1)")
        # This brings the page down slightly after every league. This is so everything loads correctly. May need to play around with the specific y value.
        driver.execute_script(f"window.scrollTo(0, {y})")
        y = y + 5 # This is working well for now, changed from 20 -> 15. If program is breaking check here first. 
        sleep(2)
                

get_data(url)


print(len(team1))
print(len(team2))
print(len(win1))
print(len(win2))
print(len(total1))
print(len(total2))
print(len(spread1))
print(len(spread2))
print(len(date_time))
print(len(spreadou1))
print(len(spreadou2))
print(len(total_over))
print(len(total_under))


lol_df['Team1'] = team1
lol_df['Team2'] = team2
lol_df['Win1'] = win1
lol_df['Win2'] = win2
lol_df['SpreadOU1'] = spreadou1
lol_df['Spread1'] = spread1
lol_df['SpreadOU2'] = spreadou2
lol_df['Spread2'] = spread2
lol_df['TotalOver'] = total_over
lol_df['Total1'] = total1
lol_df['TotalUnder'] = total_under
lol_df['Total2'] = total2
lol_df['DateTime'] = date_time
lol_df['Site'] = site

lol_df = lol_df.drop_duplicates()

print(lol_df.to_string())

lol_df.to_csv('LoL_Pinnacle.csv')

driver.quit()