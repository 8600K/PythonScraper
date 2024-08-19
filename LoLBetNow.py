import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from datetime import datetime, timedelta

import LoLTeamNames

driver = webdriver.Firefox()

url = 'https://www.betnow.eu/sportsbook-info/esports/league-of-legends/' # Change this to LoL
 
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
                       "DateTime": []})

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
name_bool = []


# Quick note, this site handles over under and + - on spread a little differently. 
# As such I do not return a list, only the number_str. 
def convert_odds(odds):

    if odds == "EV":
        return 2
    
    if len(odds) > 10:
        start_index = odds.find('(') + 1
        end_index = odds.find(')')
        number_str = float(odds[start_index:end_index])
        over_under_str = (odds[:start_index - 2])
        over_under_str = (over_under_str)
        print("OVER UNDER: ", over_under_str)
        if number_str > 0:
            print("Positive Number Requested", number_str)
            number_str = round( 1 + (number_str / 100), 2)
        else:
            print("Negative Number Needed", number_str)
            number_str = round( 1 - (100 / number_str), 2)
        return number_str

    odds = float(odds)
    if odds > 0:
        odds = round( (odds / 100) + 1, 2)
    else:
        odds = round( 1 - (100 / odds), 2)
    return odds



def get_data(url):

    driver.get(url)
    sleep(3)


    # Before this, try and limit it to blocks. See how that goes. 
    entries = driver.find_elements(By.CLASS_NAME, 'odd-info-teams')
    for count, entry in enumerate(entries):
        n = entry.text.splitlines()
        if count % 2 == 0:
            # That means it's even
            name = n[0][7:]
            namecheck0 = LoLTeamNames.standardize_names(name)
            #team1.append(LoLTeamNames.standardize_names(name))

            # Spread
            if n[1] != '-':
                spreads1_temp = n[1].split(' ') # Perfect!
                print("IMPORTANT: ", spreads1_temp)
                spreads1_temp[0] = spreads1_temp[0][:2] + '.5'
                spreads1_temp[2] = convert_odds(spreads1_temp[2])
                #spreadou1.append(spreads[0])
                #spread1.append(convert_odds(spreads[2]))
            else: 
                print("Duh!")
                #spreadou1.append(pd.NA)
                #spread1.append(pd.NA)
                spreads2_temp[0] = pd.NA
                spreads2_temp[2] = pd.NA
                # TODO Think the website breaks if we don not have this setup to append 'None'. Just double check this when the site has enough data to do so.
            # Total
            if n[2] != '-':
                totals1_temp = n[2].split(' ')
                totals1_temp[0] = (totals1_temp[0][:1] + '.5')
                totals1_temp[2] = convert_odds(totals1_temp[2])
                #total_over.append(totals[0])
                #total1.append(convert_odds(totals[2]))
            else: 
                print("Duh! 1")
                #total_over.append(pd.NA)  
                #total1.append(pd.NA)
                totals1_temp[0] = pd.NA
                totals1_temp[2] = pd.NA
            # Win
            if n[3] != '-':
                win1_temp = convert_odds(n[3])
            else: 
                print("Duh! 2")
                #win1.append(pd.NA)
                win1_temp = pd.NA



        else:
            # This means it's odd
            name = n[0][7:]
            namecheck1 = LoLTeamNames.standardize_names(name)

            #team2.append(LoLTeamNames.standardize_names(name))
            spreads2_temp = n[1].split(' ')
            spreads2_temp[0] = spreads2_temp[0][:2]

            if n[1] != '-':
                spreads2_temp = n[1].split(' ') # Perfect!
                spreads2_temp[0] = spreads2_temp[0][:2] + '.5'
                spreads2_temp[2] = convert_odds(spreads2_temp[2])
                #spreadou2.append(spreads[0])
                #spread2.append(convert_odds(spreads[2]))
            else:
                print("Of course!") 
                #spreadou2.append(pd.NA)
                #spread2.append(pd.NA)
                spreads2_temp[0] = pd.NA
                spreads2_temp[2] = pd.NA
            # Total
            if n[2] != '-':
                totals2_temp = n[2].split(' ')
                totals2_temp[0] = (totals2_temp[0][:1] + '.5').replace('EV', '+100')
                totals2_temp[2] = convert_odds(totals2_temp[2])
                #total_under.append(totals[0])
                #total2.append(convert_odds(totals[2]))
            else:
                print("Of course!") 
                #total_under.append(pd.NA)
                #total2.append(pd.NA)
                totals2_temp[0] = pd.NA
                totals2_temp[2] = pd.NA
            # Win
            if n[3] != '-':
                #win2.append(convert_odds(n[3]))
                win2_temp = convert_odds(n[3])
            else:
                print("Of course!") 
                #win2.append(pd.NA)
                win2_temp = pd.NA
            
            # Normal. No change:
            if namecheck0 < namecheck1:
                team1.append(namecheck0)
                team2.append(namecheck1)
                win1.append(win1_temp)
                win2.append(win2_temp)
                spreadou1.append(spreads1_temp[0])
                spread1.append((spreads1_temp[2]))
                spreadou2.append(spreads2_temp[0])
                spread2.append((spreads2_temp[2]))
                total_over.append(totals1_temp[0])
                total1.append((totals1_temp[2]))
                total_under.append(totals2_temp[0])
                total2.append((totals2_temp[2]))
            else:
                team1.append(namecheck1)
                team2.append(namecheck0)
                win1.append(win2_temp)
                win2.append(win1_temp)
                spreadou1.append(spreads2_temp[0])
                spread1.append((spreads2_temp[2]))
                spreadou2.append(spreads1_temp[0])
                spread2.append((spreads1_temp[2]))
                total_over.append(totals1_temp[0])
                total1.append((totals1_temp[2]))
                total_under.append(totals2_temp[0])
                total2.append((totals2_temp[2]))


    times = driver.find_elements(By.CLASS_NAME, 'odd-time')
    for time in times:
        k = time.text.splitlines()
        parsed_t = datetime.strptime(k[0], "%I:%M %p")
        parsed_t += timedelta(hours=4)
        formatted_t = parsed_t.strftime("%H:%M")
        date_time.append(formatted_t)


get_data(url)

for i, value in enumerate(team1):
    print("This should run twice.")
    site.append('BetNow')


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

lol_df.to_csv('LoL_BetNow.csv')

driver.quit()