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

url = 'https://thunderpick.io/esports/league-of-legends'

def convert_odds(odds):

    if odds == "EVEN":
        return 2
    else:
        odds = float(odds)
    if odds > 0:
        odds = round( (odds / 100) + 1, 2)
    else:
        odds = round( 1 - (100 / odds), 2)
    return odds

def get_data(url):
    
    
    driver.get(url)
    sleep(3)

    leagues = driver.find_elements(By.CLASS_NAME, 'competition')
    y = 100
    scrollable_element = driver.find_element(By.CLASS_NAME, 'thp-scrollbar')
    for league in leagues:
        #print(league.text)
        driver.execute_script(f"arguments[0].scroll(0, {y});", scrollable_element)
        sleep(1.5)
        league.click()
        sleep(2)
        
        y = y + 15

        entries = driver.find_elements(By.CLASS_NAME, 'QzK8vgVKUEUyLBC3LY8K')
        for count, entry in enumerate(entries):


            n = entry.text.splitlines()
            print('Important:', len(n))
            if len(n) < 8:
                continue
            elif len(n) == 8:
                try:
                    print("Oh man...", n)
                    namecheck0 = LoLTeamNames.standardize_names(n[2])
                    namecheck1 = LoLTeamNames.standardize_names(n[5])
                    if namecheck0 < namecheck1:
                        team1.append(namecheck0)
                        team2.append(namecheck1)
                        win1.append(convert_odds(n[3]))
                        win2.append(convert_odds(n[6]))
                        name_bool = True
                    else:
                        team1.append(namecheck1)
                        team2.append(namecheck0)
                        win1.append(convert_odds(n[6]))
                        win2.append(convert_odds(n[3]))
                        name_bool = False

                    # Date
                    # date_time.append(n[0][-5:]) # TODO - See if you can get date in here as well, right now it's just time.
                    print(n[0][-5:])
                    try:
                        parsed_t = n[0][-5:]
                        parsed_t = datetime.strptime(parsed_t, "%H:%M")
                        parsed_t += timedelta(hours=4)
                        formatted_t = parsed_t.strftime("%H:%M")
                        date_time.append(formatted_t)
                    except:
                        (date_time.append("Live"))

                    site.append('Thunderpick')
                    spreadou1.append(pd.NA)
                    spread1.append(pd.NA)
                    spreadou2.append(pd.NA)
                    spread2.append(pd.NA)
                    total_over.append(pd.NA)
                    total1.append(pd.NA)
                    total_under.append(pd.NA)
                    total2.append(pd.NA)
                except:
                    team1.pop()
                    team2.pop()
                    continue
            elif len(n) > 8:
                try: 
                    # TODO, check if n[4] or n[5] is len(2). If it's 5 we chill, if it's 4 we subtract 1 from n
                    if len(n[5]) == 2:
                        print("Here we go... ", n)
                        namecheck0 = LoLTeamNames.standardize_names(n[3])
                        namecheck1 = LoLTeamNames.standardize_names(n[6])
                        if namecheck0 < namecheck1:
                            team1.append(namecheck0)
                            team2.append(namecheck1)
                            win1.append(convert_odds(n[4]))
                            win2.append(convert_odds(n[7]))
                        else:
                            team1.append(namecheck1)
                            team2.append(namecheck0)
                            win1.append(convert_odds(n[7]))
                            win2.append(convert_odds(n[4]))
                    else:
                        print("Ah I'm a goofy goober. Here we are... ", n)
                        # TODO Fix this, right now this is just a stopgap
                        namecheck0 = LoLTeamNames.standardize_names(n[2])
                        namecheck1 = LoLTeamNames.standardize_names(n[5])
                        continue
                        

                        #if namecheck0 < namecheck1:
                        #    namecheck0 = LoLTeamNames.standardize_names(n[3])
                        #    namecheck1 = LoLTeamNames.standardize_names(n[6])
                        #    win1.append(convert_odds(n[4]))
                        #    win2.append(convert_odds(n[7]))
                        #else:
                        #    namecheck0 = LoLTeamNames.standardize_names(n[6])
                        #    namecheck1 = LoLTeamNames.standardize_names(n[3])
                        #    win1.append(convert_odds(n[7]))
                        #    win2.append(convert_odds(n[4]))


                except:
                    continue

                # Date
                # date_time.append(n[0][-5:]) # TODO - See if you can get date in here as well, right now it's just time.
                print(n[0][-5:])
                try:
                    parsed_t = n[0][-5:]
                    parsed_t = datetime.strptime(parsed_t, "%H:%M")
                    parsed_t += timedelta(hours=4)
                    formatted_t = parsed_t.strftime("%H:%M")
                    date_time.append(formatted_t)
                except:
                    date_time.append("Live")
                site.append('Thunderpick')
                spreadou1.append(pd.NA)
                spread1.append(pd.NA)
                spreadou2.append(pd.NA)
                spread2.append(pd.NA)
                total_over.append(pd.NA)
                total1.append(pd.NA)
                total_under.append(pd.NA)
                total2.append(pd.NA)
            else:
                print("Not able to deal with this.")
                continue


    # For some reason this is already in a clicked state when we first open the site.
    #to_click = driver.find_element(By.CLASS_NAME, 'toggle-opener--left')
    #to_click.click()

    #blocks = driver.find_elements(By.CLASS_NAME, 'match-group')
    #for block in blocks:
    #y = 50
    #entries = driver.find_elements(By.CLASS_NAME, 'QzK8vgVKUEUyLBC3LY8K')
    #for entry in entries:
    #    n = entry.text.splitlines()
    #    print(n)
    #    driver.execute_script(f"window.scrollTo(0, {y})")
    #    sleep(1.5)
    #    y = y + 150






get_data(url)

print(team1)
print(team2)

print(len(team1))
print(len(team2))
print(len(spreadou1))
print(len(spread1))
print(len(spreadou2))
print(len(spread2))
print(len(total_over))
print(len(total1))
print(len(total_under))
print(len(total2))
print(len(date_time))
print(len(site))


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

lol_df.to_csv('LoL_Thunderpick.csv')

driver.quit()