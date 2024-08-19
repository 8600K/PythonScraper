import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
from datetime import datetime, timedelta

import LoLTeamNames


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
    
url = 'https://espnbet.com/'


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
total_over = [] # TODO I think I'll need to mutiply total_under by -1 when I append. 
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
nav_length = 0

driver = webdriver.Firefox()

def get_data(url):

    
    driver.get(url)
    sleep(3)

    # Okay. Click hamburger button -> get LoL -> do leagues. 
    hamburger = driver.find_element(By.CSS_SELECTOR, '.p-2')
    hamburger.click()
    sleep(0.5)

    league = driver.find_element(By.ID, 'LoL-31')
    league.click()


    # IN CASE I NEED TO CALC WHERE LOL is. 

    #navbar_elements = driver.find_element(By.CSS_SELECTOR, '.simplebar-content > ul:nth-child(1)')

    #print(navbar_elements.text.splitlines())
    #nav_list = navbar_elements.text.splitlines()
    
    #nav_list = list(filter(('LIVE').__ne__, nav_list))

    #
    #subcount = 0
    #for count, find_in_list in enumerate(nav_list):
    #    print(find_in_list)
    #    print(count)

    #    if find_in_list == 'LoL':
    #        print("COUNT FOR LOL: ", (count - subcount))
    #        print("We found it!")

    #    if len(find_in_list) == 1:
    #        subcount += 1

    #    if find_in_list == 'LIVE':
    #        subcount += 1
            
    



    leagues = driver.find_elements(By., 'li.text-\[var\(--text-navigation-primary\)\]:nth-child(32) > div:nth-child(2)')


    for league in leagues:
        print(league.text)

    exit()


    

    
    for sel in find_length:
        
        nav_length = len(sel.text.splitlines())




    for i in range(nav_length):
        select_lol = driver.find_elements(By.CSS_SELECTOR, f'.w-\[245px\] > li:nth-child({i})')
        for sel1 in select_lol:
            selection = sel1.text.splitlines()
            # TEST to make sure this runs when LoL is not live!
            if selection[0] == 'LoL':
                #print("Here we are...")
                sel1.click()

                league_lengths = driver.find_elements(By.CSS_SELECTOR, '.w-\[245px\]')
                for length_of_leagues in league_lengths:
                    #print(length_of_leagues.text)
                    #print(len(length_of_leagues.text.splitlines()))
                    league_length = len(length_of_leagues.text.splitlines())
                
                for i in range(league_length):
                    select_league = driver.find_elements(By.CSS_SELECTOR, f'.w-\[245px\] > li:nth-child({i + 1})')
                    for sel2 in select_league:
                        #print("This never runs, does it?")            
                        sel2.click()
                        sleep(1)
       

                        # Here is the place where we click on each individual element for all stats.
                        entries = driver.find_elements(By.CLASS_NAME, 'items-start')
                        league_lengths = len(entries)
                        league_lengths = (league_lengths - 1) // 2
                        for i in range(league_lengths):
                            entry = driver.find_elements(By.CLASS_NAME, 'items-start')[i * 2]
                            entry.click()
                            sleep(1)


                            stats = driver.find_elements(By.CLASS_NAME, 'space-y-4')
                            for stat in stats:
                                n = stat.text.splitlines()
                                print(n)       
                                # Actual data here!!! 
                                # Since there are 2 stats (even though all the data is printed twice for some reason we break to limit data.)
                                # Optimizations could be made here if needed. Should not be much of a performance hit however.

                            

                                if 'Moneyline' in n:
                                    index = n.index('Moneyline')            
                                    namecheck0 = LoLTeamNames.standardize_names(n[index + 1])
                                    namecheck1 = LoLTeamNames.standardize_names(n[index + 3])
                                    #team1.append(n[index + 1])
                                    #team2.append(n[index + 3])
                                    if namecheck0 < namecheck1:
                                        name_bool = True
                                        team1.append(namecheck0)
                                        team2.append(namecheck1)
                                    
                                        win1.append(convert_odds(n[index + 2]))
                                        win2.append(convert_odds(n[index + 4]))
                                    else:
                                        team2.append(namecheck0)
                                        team1.append(namecheck1)
                                    
                                        win2.append(convert_odds(n[index + 2]))
                                        win1.append(convert_odds(n[index + 4]))
                                        name_bool = False
                                    site.append('ESPNBet')
                                else:
                                    continue

                                if 'Map Handicap' in n:
                                    if name_bool:
                                        index = n.index('Map Handicap')
                                        spreads = n[index + 1].split(' ')
                                        spreadou1.append(spreads[-1])
                                        spread1.append(convert_odds(n[index + 2]))
                                        spreads = n[index + 3].split(' ')
                                        spreadou2.append(spreads[-1])
                                        spread2.append(convert_odds(n[index + 4]))
                                    else:
                                        index = n.index('Map Handicap')
                                        spreads = n[index + 3].split(' ')
                                        spreadou1.append(spreads[-1])
                                        spread1.append(convert_odds(n[index + 4]))
                                        spreads = n[index + 1].split(' ')
                                        spreadou2.append(spreads[-1])
                                        spread2.append(convert_odds(n[index + 2]))
                                else:
                                    spreadou1.append(pd.NA)
                                    spread1.append(pd.NA)
                                    spreadou2.append(pd.NA)
                                    spread2.append(pd.NA)

                                if 'Total Maps' in n:
                                    index = n.index('Total Maps')
                                    print('INDEX: ', index)
                                    totals = n[index + 1].split(' ')
                                    total_over.append(totals[1])
                                    
                                    total1.append(convert_odds(n[index + 2]))
                                    totals = n[index + 3].split(' ')
                                    total_under.append(totals[1])
                                    total2.append(convert_odds(n[index + 4]))

                                else:
                                    total_over.append(pd.NA)
                                    total1.append(pd.NA)
                                    total_under.append(pd.NA)
                                    total2.append(pd.NA)

                                try:
                                    date = driver.find_element(By.CSS_SELECTOR, 'p.text-center:nth-child(2)')
                                    time = driver.find_element(By.CSS_SELECTOR, 'p.text-center:nth-child(3)')
                                    parsed_t = datetime.strptime(time.text, "%I:%M %p")
                                    parsed_t += timedelta(hours=4)
                                    print(parsed_t)
                                    formatted_t = parsed_t.strftime("%H:%M")
                                    formatted_d = (date.text + ' ' + formatted_t) # SAME THING HERE. REMOVE THE ' ' And we'd have the same as Rivalry 
                                    print('IMPORTANT', formatted_d)
                                    
                                    date_time.append(formatted_d)
                                except:
                                    print("Issue with DateTime detected...")
                                    date_time.append(pd.NA)
                            
                                
                                    

                                break
                                


                            driver.execute_script("window.history.go(-1)")

                                


        



     


get_data(url)

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

lol_df.to_csv('LoL_ESPNBet.csv')

driver.quit()


