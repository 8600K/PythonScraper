import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import calendar 
from datetime import datetime, timedelta

import LoLTeamNames



driver = webdriver.Firefox()

def convert_odds(odds):

    if odds == "Even":
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


url = 'https://sports.everygame.eu/en/Bets/Esports/40'

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

def get_data(url):
    driver.get(url)
    sleep(3)

    leagues = driver.find_elements(By.CLASS_NAME, 'sl')
    for league in leagues:
        # print(league.text)
        if 'League of Legends' in league.text:
            league.click()
            sleep(2)

            entries = driver.find_elements(By.CLASS_NAME, 'trw')
            for entry in entries:
                n = entry.text.splitlines()
                if len(n) != 4:
                    continue
                else:
                    
                    teams = n[1].split(' v ')
                    namecheck0 = LoLTeamNames.standardize_names(teams[0])
                    namecheck1 = LoLTeamNames.standardize_names(teams[1])

                    if namecheck0 < namecheck1:
                        team1.append(namecheck0)
                        team2.append(namecheck1)
                        name_bool = True
                    else:
                        team1.append(namecheck1)
                        team2.append(namecheck0)
                        name_bool = False

                    #team1.append(LoLTeamNames.standardize_names(teams[0]))
                    #team2.append(LoLTeamNames.standardize_names(teams[1]))
                    # Date
                    try:
                        parsed_d = datetime.strptime(n[0], "%m/%d/%y")
                        formatted_d = parsed_d.strftime("%b %d") 
                        date_time.append(formatted_d)
                    except:
                        try:
                            # G

                            parsed_t = datetime.strptime(n[0], "%I:%M %p")
                            #parsed_t -= timedelta(hours=4) Don't need this because Everygame is already in UTC format
                            formatted_t = parsed_t.strftime("%H:%M")
                            date_time.append(formatted_t)
                        except:
                            date_time.append("Live")
                  
                    
                    if name_bool:
                        win1.append(convert_odds(n[2]))
                        win2.append(convert_odds(n[3]))
                        spreadou1.append(pd.NA)
                        spreadou2.append(pd.NA)
                        spread1.append(pd.NA)
                        spread2.append(pd.NA)
                        total_over.append(pd.NA)
                        total1.append(pd.NA)
                        total_under.append(pd.NA)
                        total2.append(pd.NA)
                        site.append('Everygame')
                    else:
                        win1.append(convert_odds(n[3]))
                        win2.append(convert_odds(n[2]))
                        spreadou1.append(pd.NA)
                        spreadou2.append(pd.NA)
                        spread1.append(pd.NA)
                        spread2.append(pd.NA)
                        total_over.append(pd.NA)
                        total1.append(pd.NA)
                        total_under.append(pd.NA)
                        total2.append(pd.NA)
                        site.append('Everygame')
                



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

lol_df.to_csv('LoL_Everygame.csv')

driver.quit()