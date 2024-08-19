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

import LoLTeamNames

driver = webdriver.Firefox()

lol_df = pd.DataFrame({"Team1": [],
                       "Team2": [],
                       "Spread1": [],
                       "Spread2": [],
                       "Win1": [],
                       "Win2": [],
                       "Total1": [],
                       "Total2": []})

team1 = []
team2 = []
win1 = []
win2 = []
spread1 = []
spread2 = []
total1 = []
total2 = []
date_time = []

# With how Pinnacle is setup I have to get the time of the match and then
# check match names, and time to find a proper match in the database. 


url = 'https://www.pinnacle.com/en/esports/league-of-legends/leagues/'

# Plan.
# Go to URL.
# leagueoflegends -> leagues. Click on top leagues and maybe search through a couple of special ones.
# Click on match and then get scores.
# ???
# Profit.

def convert_odds(odds):
    if odds >= 2.00:
        new_odds = round( ((odds - 1) * 100) )
    else:
        new_odds = round( (-100 / (odds - 1)) )
    return new_odds

def get_data(url):

    month_to_num = {name: num for num, name in enumerate(calendar.month_abbr) if num}
    

    driver.get(url)
    sleep(3)

    
    top_leagues = driver.find_elements(By.CLASS_NAME, 'style_list__2KTNR')

    print(len(top_leagues) - 1)
    for i in range(len(top_leagues) - 1):
        print("Do we run this at least twice?")
        # Run an if statement here to determine if it's still a league of legends tag.
        top = driver.find_elements(By.CLASS_NAME, 'style_listItem__1m5iG')[i]
        print(top.text)
        
        top.click()
        sleep(3)

        try:
            matches = driver.find_element(By.CSS_SELECTOR, '#period\:0')
            matches.click()
            sleep(1)
        except:
            print("The site is most likely down.")

        try:
            
            for i in range(3):
                day = driver.find_element(By.CSS_SELECTOR, f'.style_scroller__3LDSl > button:nth-child({i+2})')
                day.click()
                sleep(0.5)
                day_txt = day.text.split()
                
                day_txt = day_txt[1].title()
                day_txt = month_to_num[day_txt]
                sleep(1)

                entries = driver.find_elements(By.CLASS_NAME, 'style_row__12oAB')
                for entry in entries:
                    n = entry.text.splitlines()

                    name1 = n[0].split()
                    name1 = name1[:-1]
                    name1 = ' '.join(name1)

                    name2 = n[1].split()
                    name2 = name2[:-1]
                    name2 = ' '.join(name2)

                    # All fields are present.
                    print("This is how big it is: ", len(n))
                    if len(n) == 14:
                        team1.append(name1)
                        team2.append(name2)
                        date_time.append(n[2] + str(day_txt))
                        win1.append(convert_odds(n[3]))
                        win2.append(convert_odds(n[4]))
                        spread1.append(n[5] + ' ' + convert_odds(n[6]))
                        spread2.append(n[7] + ' ' + convert_odds(n[8]))
                        total1.append(n[9] + ' ' + convert_odds(n[10]))
                        total2.append(n[11] + ' ' +  convert_odds(n[12]))

                    # Either spread or total is missing.
                    # Note to self - Make sure win can never be missing. 
                    elif len(n) == 10:
                        team1.append(name1)
                        team2.append(name2)
                        date_time.append(n[2] + str(day_txt))
                        win1.append(convert_odds(n[3]))
                        win2.append(convert_odds(n[4]))

                        if n[5] == '+1.5' or n[5] == '-1.5':
                            spread1.append(n[5] + ' ' +  convert_odds(n[6]))
                            spread2.append(n[7] + ' ' + convert_odds(n[8]))
                            total1.append('None')
                            total2.append('None')
                        else:
                            spread1.append('None')
                            spread2.append('None')
                            total1.append(n[5] + ' ' + convert_odds(n[6]))
                            total2.append(n[7] + ' ' + convert_odds(n[8]))
                    
                    # This means both spread and total are missing. 
                    
                    elif len(n) == 6:
                        team1.append(name1)
                        team2.append(name2)
                        date_time.append(n[2] + str(day_txt))
                        win1.append(n[3])
                        win2.append(n[4])
                        spread1.append('None')
                        spread2.append('None')
                        total1.append('None')
                        total2.append('None')
                    
                    else:
                        continue
                        # No data in any field.

        except:
            print("Something broke")
    




        print("Cool cool, we look around here.")
        driver.execute_script("window.history.go(-1)")
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