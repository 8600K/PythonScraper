import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

import CSTeamNames

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

# Could have this handle both CS and LoL. But I think keeping it seperate in case something goes arwy is fine for now. 
# Can always add it right before launch.


#url = 'https://www.pinnacle.com/en/esports/games/league-of-legends/nest/matchups/#all'
url = 'https://www.pinnacle.com/en/esports/games/cs2/blast-premier-final/matchups/#all'

def convert_odds(odds):
    if odds >= 2.00:
        new_odds = round( ((odds - 1) * 100) )
    else:
        new_odds = round( (-100 / (odds - 1)) )
    return new_odds

def get_data(url):
    driver.get(url=url)
    sleep(3)
    driver.find_element(By.CSS_SELECTOR, '#period\:0').click()
    sleep(1)
    try:
        for i in range(1, 3):
            
            for k in range(3, 30):                           
                elements = driver.find_elements(By.XPATH, f'/html/body/div[2]/div[1]/div[2]/main/div/div[4]/div[{i}]/div/div[{k}]')
                if elements:
                    for element in elements:
                        print(element.text.split('\n')) # 6 For only Moneyline. -> 14 for Everything. I would assume 10 for Moneyline + one other. TODO Found it. Over / Under will always have a 2.5 before the value. Whereas Handicap will always have a -1.5 or +1.5 before value. EASY BABY.
                
                        fields = element.text.split('\n')

                        # This is untested!
                        name1 = fields[0].replace('(Match)', '')
                        name2 = fields[1].replace('(Match)', '')

                        name1 = name1[:len(name1)-1]
                        name2 = name2[:len(name2)-1]

                        name1 = CSTeamNames.standardize_names(name1)
                        name2 = CSTeamNames.standardize_names(name2)

                        print(name1)
                        print(name2)
                        if fields[3] != None:
                            moneyline0 = fields[3]
                        if fields[4] != None:
                            moneyline1 = fields[4]
                        if fields[5] != None:
                            if fields[5] == '-1.5' or fields[5] == '+1.5':
                                # This means Handicap is online. 
                                handicap0 = fields[6]
                                handicap1 = fields[8]
                        elif fields[5] == '2.5':
                            # This means Handicap is offline. Over/Under is online. 
                            over_under0 = fields[6]
                            over_under1 = fields[8]
                        if fields[9] == '2.5':
                            over_under0 = fields[10]
                            over_under1 = fields[12]


                        if name1 < name2:
                            team1.append(name1)
                            team2.append(name2)
                            win1.append(convert_odds(float(moneyline0)))
                            win2.append(convert_odds(float(moneyline1)))
                            spread1.append(convert_odds(float(handicap0)))
                            spread2.append(convert_odds(float(handicap1)))
                            total1.append(convert_odds(float(over_under0)))
                            total2.append(convert_odds(float(over_under1)))
                        else:
                            team1.append(name2)
                            team2.append(name1)
                            win1.append(convert_odds(float(moneyline1)))
                            win2.append(convert_odds(float(moneyline0)))
                            spread1.append(convert_odds(float(handicap1)))
                            spread2.append(convert_odds(float(handicap0)))
                            total1.append(convert_odds(float(over_under1)))
                            total2.append(convert_odds(float(over_under0)))
                
                else:
                    print("Nothing found. End of the line.")
    except:
        print('ERROR!')

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

lol_df.to_csv('CSPinnacle.csv')
