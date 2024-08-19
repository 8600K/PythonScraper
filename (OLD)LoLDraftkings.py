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
                       "Total2": [],
                       "DateTime": []})

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


url = 'https://sportsbook.draftkings.com/'

def decode_and_preprocess(encoded_bytes):
    decoded_str = encoded_bytes.decode('utf-8')

    decoded_str = decoded_str.replace('\u2212', '-')

    return decoded_str

def get_data(url):

    try:
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

                    try:
                        find_lol = driver.find_elements(By.CSS_SELECTOR, '.sportsbook-sport-navigation > div:nth-child(3) > div:nth-child(2) > div:nth-child(9) > div:nth-child(2) > ul:nth-child(1)') # IMPORTANT. The numbers within these divs COULD change if more sports are added or taken away.
                        for found in find_lol:
                            esports_length = len(found.text.splitlines())

                        for j in range(esports_length):
                            click_lol = driver.find_elements(By.CSS_SELECTOR, f'.sportsbook-sport-navigation > div:nth-child(3) > div:nth-child(2) > div:nth-child(9) > div:nth-child(2) > ul:nth-child(1) > li:nth-child({j})') # Same here...
                            for to_click_lol in click_lol:
                                
                                if to_click_lol.text[:3] == 'LoL':
                                    to_click_lol.click()
                                    #print('completed')
                                    sleep(1)


                                    #print("Wait what?")
                                    entries_day = driver.find_elements(By.CLASS_NAME, 'sportsbook-table__body')
                                    

                                    for entry_day in entries_day:
                                        #print("Getting stuck here...")
                                        #print(str(entry_day.text.encode('utf-8').splitlines()))
                                        entry_length = len(entry_day.text.encode('utf-8').splitlines()) // 5
                                        day = (entry_day.text.encode('utf-8').splitlines())
                                        #print("Day: ", day)



                                        entries = driver.find_elements(By.CLASS_NAME, 'sportsbook-table__column-row')
                                        row1 = True
                                        row2 = False
                                        for count, entry in enumerate(entries):
                                            #print(entry.text.encode('utf-8').splitlines())
                                            n = entry.text.encode('utf-8').splitlines()
                                            #print("COUNT: ", count)
                                            #print("This is what n is: ", n)
                                            #print("Row 1: ", row1)
                                            #print("Row 2: ", row2)

                                            if count != 0:
                                                if count % 4 == 0:
                                                    # print("Uh oh we ran the very first time...")
                                                    # This means it is time to switch from row 1 to row 2.
                                                    if row1:
                                                        row1 = False
                                                        row2 = True
                                                    else:
                                                        row1 = True
                                                        row2 = False

                                            if row1:
                                                #print("Made it here.")                                                    
                                                if count % 4 == 0:
                                                    date_time.append(n[0].decode('utf-8'))
                                                    team1.append(LoLTeamNames.standardize_names(n[1].decode('utf-8')))
                                                elif count % 4 == 1:
                                                    if not n:
                                                        spread1.append('None')
                                                    else:
                                                        spread1.append(decode_and_preprocess(n[0]) + decode_and_preprocess(n[1]))
                                                elif count % 4 == 2:
                                                    if not n:
                                                        total1.append('None')
                                                    else:
                                                        #print("N In Total1: ", n)
                                                        #print("N decode and preprocessed: ", decode_and_preprocess(n[2]))
                                                        totals = n[0].decode('utf-8')  + n[1].decode('utf-8') + ' ' + decode_and_preprocess(n[2])
                                                        #print("TOTALS: ", totals)

                                                        total1.append(n[0].decode('utf-8')  + n[1].decode('utf-8') + ' ' + decode_and_preprocess(n[2]))
                                                elif count % 4 == 3:
                                                    if not n:
                                                        win1.append('None')
                                                    else:
                                                        win1.append(decode_and_preprocess(n[0]))

                                            else:
                                                if count % 4 == 0:
                                                    team2.append(LoLTeamNames.standardize_names(n[0].decode('utf-8')))
                                                elif count % 4 == 1:
                                                    if not n:
                                                        spread2.append('None')
                                                    else:
                                                        spread2.append(decode_and_preprocess(n[0]) + decode_and_preprocess(n[1]))
                                                elif count % 4 == 2:
                                                    if not n:
                                                        total2.append('None')
                                                    else:
                                                        total2.append(n[0].decode('utf-8') + n[1].decode('utf-8') + ' ' + decode_and_preprocess(n[2]))
                                                elif count % 4 == 3:
                                                    if not n:
                                                        win2.append('None')
                                                    else:
                                                        win2.append(decode_and_preprocess(n[0]))
                                                    
                                                
                                                # Count should always increment by 4 and then we switch. 
                                                # Modulo by 4 and if statement to check if 1 or 2 is on, turn it off and turn the other on.
                                                # Logic gate baby
                                                # TODO. Make some sort of a switch logic that lets team1, win1, etc append, and then switch to team2, win2, etc.



                                        

                                        # print(n[4].decode('utf-8'))

                                        # With the code I have now, we entries lets us know we have 2 days if we get its length. 
                                        # 

                                        

                                        # TODO CHECK THIS AND TEST THIS NEXT BIT. THE // 5 IS A THEORY RIGHT NOW. NOT PROVEN
                                        
                                        



                    except:
                        print("Could not find a suitable league to click on.")


    except:
        print("Could not connect to the URL.")


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

lol_df.to_csv('LoL_Draftkings.csv')