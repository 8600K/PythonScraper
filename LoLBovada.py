# BOVADA
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
from datetime import datetime, timedelta
import re

import LoLTeamNames

# Alright, let's do this one last time.
# Firstly -> sp-happning-now and sp-next-events. Now is for time = now, next is upcoming.
# coupon-content more info = Individual entry for game. 
# Period hidden-xs = date, clock = time (classes).
# Then we have competitors -> competitor-name -> name.
# bet-price = Spread, Win, and Total
# 

# TODO Add a check to make sure the btn class is not suspended. 
# If it is suspended I guess don't add it to the array.


url = 'https://www.bovada.lv/sports/esports/league-of-legends'


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

driver = webdriver.Firefox()

# Make this so every element runs through this before appending to 
# the array.


def convert_odds(odds):

    if odds == "EVEN":
        return 2.0

    odds = float(odds)
    if odds > 0:
        odds = round( (odds / 100) + 1, 2)
    else:
        odds = round( 1 - (100 / odds), 2)
    return odds

    

def get_data(url):

    namecheck0 = ''
    namecheck1 = ''
    name_bool = []

    try:
        driver.get(url)
        sleep(3)

        try: 
            next_event = driver.find_element(By.CLASS_NAME, 'next-events-bucket')

            if next_event:
                print("Success")
                # print(next_event.text) This works beautifully. But now let's try and
                # Divide and conquer each individual data spot we need. 
                # I think that should be a lot cleaner. 
                dates = next_event.find_elements(By.CLASS_NAME, 'scores')

                # Holy. This is clean as hell.
                for date_get in dates:
                    print("The First: ", date_get.text)
                    d = date_get.text
                    d = d.replace("\n", ' ')
                    parsed_d = datetime.strptime(d, "%m/%d/%y %I:%M %p")
                    parsed_d += timedelta(hours=4)
                    formatted_d = parsed_d.strftime("%b %d")
                    #print('formatted date: ', formatted_d)
                    formatted_t = parsed_d.strftime("%H:%M")
                    
                    #formatted_t += timedelta(hours=4)
                    #print('formatted time: ', formatted_t)
                    formatted_datetime = formatted_d + ' ' + formatted_t # CAN CHANGE THIS TO MATCH RIVALRY BY DROPPED THE ' '
                    print('final: ', formatted_datetime)
                    # Date comes out as yyyy-\n-time-timezone. 
                    # Fix it so it's a proper datetime.

                    
                    date_time.append(formatted_datetime)
                    
                names = next_event.find_elements(By.CLASS_NAME, 'competitors')
                for name in names:
                    #print("name: ", name.text.splitlines()) TODO This all runs before scores has a chance to eliminate certain tabs because they are invalid. Gotta fix this!!!
                    n = name.text.splitlines()
                    namecheck0 = LoLTeamNames.standardize_names(n[0])
                    namecheck1 = LoLTeamNames.standardize_names(n[1])
                    # Determines which team gets placed where by alphabetizing the names.
                    # Sets name_bool (default true) based on result, which we then use to determine where all other values go. 
                    if namecheck0 < namecheck1:
                        team1.append(LoLTeamNames.standardize_names(n[0]))
                        team2.append(LoLTeamNames.standardize_names(n[1]))
                        name_bool.append(0)
                    else:
                        team1.append(LoLTeamNames.standardize_names(n[1]))
                        team2.append(LoLTeamNames.standardize_names(n[0]))
                        name_bool.append(1)
                    site.append('Bovada')

                scores = next_event.find_elements(By.CLASS_NAME, 'markets-container')
                index = 0
                for score in scores:
                    print('score: ', score.text.splitlines())

                    # This runs if one of the betting odds is currently suspended.
                    # Thus ensuring it doesn't get sent to the database.
                    if score.find_elements(By.CLASS_NAME, 'suspended'):
                        print("ELEMENT TO BE SUSPENDED: ", index)
                        print(len(team1))
                        print(len(team2))
                        print(len(date_time))
                        print(len(site))
                        team1.pop(index)
                        team2.pop(index)
                        date_time.pop(index)
                        site.pop(index)
                        name_bool.pop(index)
                        print("GoTo next loop")
                        continue
                    
                    s = score.text.splitlines()
                    
                    # Logic to determine all the score elements.
                    # If score is spread, win, or total is all done here.
                    
                    # First checks to see if the s array is full (6)
                    # If it is that means each odd is present
                    # And we can go ahead and append all fields
                    # ABOUT SPREADS --> Spreads gets the list returned from convert_odds
                    # Spreadou1 recieves the first number and spread1 recieves the second.

                    print("VERY IMPORTANT: ", len(s))


                    if len(s) == 6:
                        if name_bool[index] == 0:
                            print("This ran!")
                            spreads = s[0].replace('(', '').replace(')', '').split(' ')
                            spreadou1.append(spreads[0])
                            spread1.append(convert_odds(spreads[1]))
                            spreads = s[1].replace('(', '').replace(')', '').split(' ')
                            spreadou2.append(spreads[0])
                            spread2.append(convert_odds(spreads[1]))
                            win1.append(convert_odds(s[2]))
                            win2.append(convert_odds(s[3]))
                            totals = s[4].replace('(', '').replace(')', '').split(' ')
                            total_over.append(totals[0].replace('O', ''))
                            print("This is what I want to know", totals)
                            total1.append(convert_odds(totals[1]))
                            totals = s[5].replace('(', '').replace(')', '').split(' ')
                            total_under.append(totals[0].replace('U', ''))
                            total2.append(convert_odds(totals[1]))
                        else: 
                            print("No This ran!")
                            spreads = s[1].replace('(', '').replace(')', '').split(' ')
                            spreadou1.append(spreads[0])
                            spread1.append(convert_odds(spreads[1]))
                            spreads = s[0].replace('(', '').replace(')', '').split(' ')
                            spreadou2.append(spreads[0])
                            spread2.append(convert_odds(spreads[1]))
                            win1.append(convert_odds(s[3]))
                            win2.append(convert_odds(s[2]))
                            totals = s[5].replace('(', '').replace(')', '').split(' ')
                            total_over.append(totals[0].replace('U', ''))
                            total1.append(convert_odds(totals[1]))
                            totals = s[4].replace('(', '').replace(')', '').split(' ')
                            total_under.append(totals[0].replace('O', ''))
                            total2.append(convert_odds(totals[1]))
                    # It s contains 4 elements, we know one of the 
                    # odds is missing. So we check to see if the first
                    # element is greater than 6 (to be safe) because 
                    # The Win odd should never have a length greater than
                    # 4. Whereas the Spread and Totals each are 11.
                    # So choosing 6 is just being safe. 
                    # Then, if this doesn't return true, that should mean
                    # Win comes first, and then Total, so we just do the opposite
                    # Of the if true statement. 
                    elif len(s) == 4:
                        if len(s[0]) > 6:
                            if name_bool[index] == 0:
                                spreads = s[0].replace('(', '').replace(')', '').split(' ')
                                spreadou1.append(spreads[0])
                                spread1.append(convert_odds(spreads[1]))
                                spreads = s[1].replace('(', '').replace(')', '').split(' ')
                                spreadou2.append(spreads[0])
                                spread2.append(convert_odds(spreads[1]))
                                win1.append(convert_odds(s[2]))
                                win2.append(convert_odds(s[3]))
                                total_over.append(pd.NA)
                                total1.append(pd.NA)
                                total_under.append(pd.NA)
                                total2.append(pd.NA)
                            else:
                                spreads = s[1].replace('(', '').replace(')', '').split(' ')
                                spreadou1.append(spreads[0])
                                spread1.append(convert_odds(spreads[1]))
                                spreads = s[0].replace('(', '').replace(')', '').split(' ')
                                spreadou2.append(spreads[0])
                                spread2.append(convert_odds(spreads[1]))
                                win1.append(convert_odds(s[3]))
                                win2.append(convert_odds(s[2]))
                                total_over.append(pd.NA)
                                total1.append(pd.NA)
                                total_under.append(pd.NA)
                                total2.append(pd.NA)
                        else:
                            if name_bool[index] == 0:
                                spreadou1.append(pd.NA)
                                spread1.append(pd.NA)
                                spreadou2.append(pd.NA)
                                spread2.append(pd.NA)
                                win1.append(convert_odds(s[0]))
                                win2.append(convert_odds(s[1]))
                                totals = s[2].replace('(', '').replace(')', '').split(' ')
                                total_over.append(totals[0].replace('O', ''))
                                total1.append(convert_odds(totals[1]))
                                totals = s[3].replace('(', '').replace(')', '').split(' ')
                                total_under.append(totals[0].replace('U', ''))
                                total2.append(convert_odds(totals[1]))
                            else: 
                                spreadou1.append(pd.NA)
                                spread1.append(pd.NA)
                                spreadou2.append(pd.NA)
                                spread2.append(pd.NA)
                                win1.append(convert_odds(s[1]))
                                win2.append(convert_odds(s[0]))
                                totals = s[3].replace('(', '').replace(')', '').split(' ')
                                total_over.append(totals[0].replace('O', ''))
                                total1.append(convert_odds(totals[1]))
                                totals = s[2].replace('(', '').replace(')', '').split(' ')
                                total_under.append(totals[0].replace('U', ''))
                                total2.append(convert_odds(totals[1]))
                    # This means there should only be 2 values up, which should
                    # Always be Win. Though a few more checks here wouldn't hurt.
                    else:
                        if name_bool[index] == 0:
                            spreadou1.append(pd.NA)
                            spread1.append(pd.NA)
                            spreadou2.append(pd.NA)
                            spread2.append(pd.NA)
                            win1.append(convert_odds(s[0]))
                            win2.append(convert_odds(s[1]))
                            total_over.append(pd.NA)
                            total1.append(pd.NA)
                            total_under.append(pd.NA)
                            total2.append(pd.NA)
                        else:
                            spreadou1.append(pd.NA)
                            spread1.append(pd.NA)
                            spreadou2.append(pd.NA)
                            spread2.append(pd.NA)
                            win1.append(convert_odds(s[1]))
                            win2.append(convert_odds(s[0]))
                            total_over.append(pd.NA)
                            total1.append(pd.NA)
                            total_under.append(pd.NA)
                            total2.append(pd.NA)

                    index += 1
                        
            else:
                print("Failed")
        except:
            print("Something went wrong with finding next events")
    


    except():
        print("Unable to load the webpage.")

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

lol_df.to_csv('LoL_Bovada.csv')

driver.quit()