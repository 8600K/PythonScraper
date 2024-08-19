# Thunderpick
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
from datetime import datetime, timedelta

import LoLTeamNames

url = 'https://www.rivalry.com/esports/league-of-legends-betting'

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

url = 'https://sportsbook.draftkings.com/'

def convert_odds(odds):

    if odds == "EVEN":
        return 2.0

    odds = float(odds)
    if odds > 0:
        odds = round( (odds / 100) + 1, 2)
    else:
        odds = round( 1 - (100 / odds), 2)
    return odds



def decode_and_preprocess(encoded_bytes):
    decoded_str = encoded_bytes.decode('utf-8')

    decoded_str = decoded_str.replace('\u2212', '-')

    return decoded_str

def get_data(url):

    driver.get(url)
    sleep(3)
    # From here we get LoL and select. 

    select_lol = driver.find_elements(By.CSS_SELECTOR, '.sportsbook-sport-navigation > div:nth-child(3) > div:nth-child(2)')
    for selection in select_lol:
        #print(selection.text)
        sports_length = len(selection.text.splitlines())
        #print(sports_length)
    
    for i in range(sports_length):
        click_esports = driver.find_elements(By.CSS_SELECTOR, f'.sportsbook-sport-navigation > div:nth-child(3) > div:nth-child(2) > div:nth-child({i})')
        for to_click in click_esports:
            
            if to_click.text == 'E-SPORTS':
                print("Found ya!")
                to_click.click()
                sleep(0.5)

                # Gets the leagues after E-Sports has been clicked.
                leagues = driver.find_elements(By.CLASS_NAME, 'sportsbook-navigation-item-title--league')
                for league in leagues:
                    # print(league.text)
                    if 'LoL' == league.text[:3]:
                        print("We found a league.")
                        league.click()
                        sleep(0.5)

                        entries_day = driver.find_elements(By.CLASS_NAME, 'sportsbook-table__body')

                        for entry_day in entries_day:
                            #print("Getting stuck here...")
                            #print(str(entry_day.text.encode('utf-8').splitlines()))
                            entry_length = len(entry_day.text.encode('utf-8').splitlines()) // 5
                            day = (entry_day.text.encode('utf-8').splitlines())
                            print("How many times does this run? Should be 5 or 10 ")



                            entries = driver.find_elements(By.CSS_SELECTOR, '.sportsbook-table__body > tr:nth-child(1)')
                            row1 = True
                            row2 = False                            
                            for count, entry in enumerate(entries):
                                #print(entry.text.encode('utf-8').splitlines())
                                n = entry.text.encode('utf-8').splitlines()
                                print("COUNT: ", count)
                                print("This is what n is: ", n)
                                #print("Row 1: ", row1)
                                #print("Row 2: ", row2)
                                win1_temp = pd.NA
                                win2_temp = pd.NA
                                spread1ou_temp = pd.NA
                                spread2ou_temp = pd.NA
                                spread1_temp = pd.NA
                                spread2_temp = pd.NA
                                

                                if count % 2 == 0:
                                    print(n)
                                    add_space = n[0].decode('utf-8')
                                    added_space = (add_space[:-2] + ' ' + add_space[-2:])
                                    parsed_t = datetime.strptime(added_space, "%I:%M %p")
                                    parsed_t += timedelta(hours=4)
                                    formatted_t = parsed_t.strftime("%H:%M")
                                    date_time.append(formatted_t)
                                    site.append('Draftkings')
                                    namecheck0 = LoLTeamNames.standardize_names(n[1].decode('utf-8'))
                                else:
                                    print(n)
                                    

get_data(url)

#print(team1)
#print(team2)
#print(win1)
#print(win2)
#print(spreadou1)
#print(spreadou2)
#print(total_over)
#print(total_under)
#print(total1)
#print(total2)
#print(date_time)
#print(site)

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



print(lol_df.to_string())

lol_df.to_csv('LoL_Draftkings.csv')

driver.quit()