# PINNACLE This one has a lot of sleeps, so it will take longer than most other pages. Might need to thread this or find some way
# To speed it up.
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



url = 'https://www.pinnacle.com/en/esports/league-of-legends/leagues/'

def convert_odds(odds):
    if odds >= 2.00:
        new_odds = round( ((odds - 1) * 100) )
    else:
        new_odds = round( (-100 / (odds - 1)) )
    return new_odds

def get_data(url):
    try:
        driver.get(url)
        sleep(3)
        for i in range(30):
            leagues = driver.find_element(By.XPATH,  f'/html/body/div[2]/div[1]/div[2]/main/div/div[2]/div/div/ul/li[{i + 1}]')
            leagues.click()
            sleep(2)

            driver.find_element(By.CSS_SELECTOR, '#period\:0').click()


            for j in range(3, 30):
                elements = driver.find_elements(By.XPATH, f'/html/body/div[2]/div[1]/div[2]/main/div/div[4]/div[2]/div/div[{j}]')
                if elements:
                    for element in elements:
                        print(element.text.split('\n'))
                        fields = element.text.split('\n')

                        # This is untested! Think it won't work cause I need to slice off last character in the string.
                        name1 = LoLTeamNames.standardize_names(fields[0].replace('(Match)', ''))
                        name2 = LoLTeamNames.standardize_names(fields[1].replace('(Match)', ''))

                        print(name1, name2)

                        if name1 < name2:
                            team1.append(name1)
                            team2.append(name2)
                            win1.append(convert_odds(float(fields[3])))
                            win2.append(convert_odds(float(fields[4])))
                            spread1.append(convert_odds(float(fields[6])))
                            spread2.append(convert_odds(float(fields[8])))
                            total1.append(convert_odds(float(fields[10])))
                            total2.append(convert_odds(float(fields[12])))
                        else:
                            team1.append(name2)
                            team2.append(name1)
                            win1.append(convert_odds(float(fields[4])))
                            win2.append(convert_odds(float(fields[3])))
                            spread1.append(convert_odds(float(fields[8])))
                            spread2.append(convert_odds(float(fields[6])))
                            total1.append(convert_odds(float(fields[12])))
                            total2.append(convert_odds(float(fields[10])))
                        
                        print(name1, name2, win1, win2, spread1, spread2, total1, total2)

                else:
                    driver.back()
                    
                
                

            
#/html/body/div[2]/div[1]/div[2]/main/div/div[4]/div[2]/div/div[2]
#/html/body/div[2]/div[1]/div[2]/main/div/div[4]/div[2]/div/div[3] #  START HERE

        
    except:
        print("Could not get access to the site.")

get_data(url)

lol_df['Team1'] = team1
lol_df['Team2'] = team2
lol_df['Win1'] = win1
lol_df['Win2'] = win2
lol_df['Spread1'] = spread1
lol_df['Spread2'] = spread2 
lol_df['Total1'] = total1
lol_df['Total2'] = total2

print(lol_df)

lol_df.to_csv('Pinnacle.csv')