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


                        i = 1
                        k = 1
                        while True:
                            
                            entries_day = driver.find_elements(By.CSS_SELECTOR, f'div.parlay-card-10-a:nth-child({k}) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child({i})')

                            if not entries_day:
                                
                                # Caps at 3 divs right now. Change this number if more or less is required. So far I've seen a max of 2...
                                if k >= 3:
                                    break
                                
                                # This resets i back to 1 and adds one to k, then continues to see if there is another div. 
                                k += 1
                                i = 1
                                continue
                                
                                

                            for entry_day in entries_day:
                                print("I wish to know how often this runs. Thank you. Also here is i", i)

                                #name_and_time = driver.find_element(By.CSS_SELECTOR, f'div.parlay-card-10-a:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child({i})')
                                #print("IMPORTANT: ", name_and_time.text.encode('utf-8').splitlines())

                                name_box1 = driver.find_element(By.CSS_SELECTOR, f'div.parlay-card-10-a:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child({i}) > th:nth-child(1)')
                                name_box2 = driver.find_element(By.CSS_SELECTOR, f'div.parlay-card-10-a:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child({i + 1}) > th:nth-child(1)')

                                spread_box1 = driver.find_element(By.CSS_SELECTOR, f'div.parlay-card-10-a:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child({i}) > td:nth-child(2)')
                                spread_box2 = driver.find_element(By.CSS_SELECTOR, f'div.parlay-card-10-a:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child({i + 1}) > td:nth-child(2)')

                                total_box1 = driver.find_element(By.CSS_SELECTOR, f'div.parlay-card-10-a:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child({i}) > td:nth-child(3)') 
                                total_box2 = driver.find_element(By.CSS_SELECTOR, f'div.parlay-card-10-a:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child({i + 1}) > td:nth-child(3)') 

                                win_box1 = driver.find_element(By.CSS_SELECTOR, f'div.parlay-card-10-a:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child({i}) > td:nth-child(4)')
                                win_box2 = driver.find_element(By.CSS_SELECTOR, f'div.parlay-card-10-a:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child({i}) > td:nth-child(4)')

                                # TODO, Might need to see if we actually need to encode and decode names and such. Might only need to do that on win, total, spread. Low priority 
                                name_box1 = name_box1.text.encode('utf-8').splitlines()
                                name_box2 = name_box2.text.encode('utf-8').splitlines()

                                spread_box1 = spread_box1.text.encode('utf-8').splitlines()
                                spread_box2 = spread_box2.text.encode('utf-8').splitlines()

                                total_box1 = total_box1.text.encode('utf-8').splitlines()
                                total_box2 = total_box2.text.encode('utf-8').splitlines()

                                win_box1 = win_box1.text.encode('utf-8').splitlines()
                                win_box2 = win_box2.text.encode('utf-8').splitlines()
                                
                                # TODO Create some kind of holding cell or way to format if Team 1 name is < Team 2 name so everything is standard. 

                                # Row 1
                            
                                add_space = name_box1[0].decode('utf-8')
                                added_space = (add_space[:-2] + ' ' + add_space[-2:])
                                parsed_t = datetime.strptime(added_space, "%I:%M %p")
                                parsed_t += timedelta(hours=4)
                                formatted_t = parsed_t.strftime("%H:%M")
                                date_time.append(formatted_t)
                                site.append('Draftkings')

                                if LoLTeamNames.standardize_names(name_box1[1]) < LoLTeamNames.standardize_names(name_box2[0]):
                                    team1.append(LoLTeamNames.standardize_names(name_box1[1].decode('utf-8')))
                                    team2.append(LoLTeamNames.standardize_names(name_box2[0].decode('utf-8')))

                                    if not win_box1:
                                        win1.append(pd.NA)
                                        win2.append(pd.NA)
                                    else:
                                        moneyline1 = win_box1[0].decode('utf-8').replace('\u2212', '-')
                                        moneyline2 = win_box2[0].decode('utf-8').replace('\u2212', '-')
                                        win1.append(moneyline1)
                                        win2.append(moneyline2)

                                    
                                    if not total_box1:
                                        total_over.append(pd.NA)
                                        total1.append(pd.NA)
                                        total_under.append(pd.NA)
                                        total2.append(pd.NA)
                                    else:
                                        total_over.append(total_box1[1].decode('utf-8'))
                                        total1.append(total_box1[2].decode('utf-8').replace('\u2212', '-'))
                                        total_under.append(total_box2[1].decode('utf-8'))
                                        total2.append(total_box2[2].decode('utf-8').replace('\u2212', '-'))

                                    if not spread_box1:
                                        spreadou1.append(pd.NA)
                                        spreadou2.append(pd.NA)
                                        spread1.append(pd.NA)
                                        spread2.append(pd.NA)
                                    else:
                                        spreadou1.append(spread_box1[0].decode('utf-8'))
                                        spreadou2.append(spread_box2[0].decode('utf-8'))
                                        spread1.append(spread_box1[1].decode('utf-8').replace('\u2212', '-'))
                                        spread2.append(spread_box2[1].decode('utf-8').replace('\u2212', '-'))

                                    

                                    
                                else:
                                    # Name is false

                                    team2.append(LoLTeamNames.standardize_names(name_box1[1].decode('utf-8')))
                                    team1.append(LoLTeamNames.standardize_names(name_box2[0].decode('utf-8')))

                                    if not win_box1:
                                        win1.append(pd.NA)
                                        win2.append(pd.NA)
                                    else:
                                        moneyline2 = win_box1[0].decode('utf-8').replace('\u2212', '-')
                                        moneyline1 = win_box2[0].decode('utf-8').replace('\u2212', '-')
                                        win2.append(moneyline2)
                                        win1.append(moneyline1)

                                    
                                    if not total_box1:
                                        total_over.append(pd.NA)
                                        total1.append(pd.NA)
                                        total_under.append(pd.NA)
                                        total2.append(pd.NA)
                                    else:
                                        total_over.append(total_box2[1].decode('utf-8'))
                                        total2.append(total_box1[2].decode('utf-8').replace('\u2212', '-'))
                                        total_under.append(total_box1[1].decode('utf-8'))
                                        total1.append(total_box2[2].decode('utf-8').replace('\u2212', '-'))

                                    if not spread_box1:
                                        spreadou1.append(pd.NA)
                                        spreadou2.append(pd.NA)
                                        spread1.append(pd.NA)
                                        spread2.append(pd.NA)
                                    else:
                                        spreadou2.append(spread_box1[0].decode('utf-8'))
                                        spreadou1.append(spread_box2[0].decode('utf-8'))
                                        spread2.append(spread_box1[1].decode('utf-8').replace('\u2212', '-'))
                                        spread1.append(spread_box2[1].decode('utf-8').replace('\u2212', '-'))

                            
                                        
                                # Row 2
                               
                                i += 2


                            

get_data(url)

print(team1)
print(team2)
print(win1)
print(win2)
print(spreadou1)
print(spreadou2)
print(total_over)
print(total_under)
print(total1)
print(total2)
print(date_time)
print(site)

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