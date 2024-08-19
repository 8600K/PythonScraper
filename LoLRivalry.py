# RIVALRY TODO Fix date time to match other sites!
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep
import pandas as pd

from datetime import datetime, timedelta
import re

import LoLTeamNames

url = 'https://www.rivalry.com/esports/league-of-legends-betting'
#url = 'https://www.rivalry.com'

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

def get_data(url):

    
    driver.get(url)
    sleep(3)


    # Trying Find League of Legends from Esports tab:
    #header = driver.find_element(By.CSS_SELECTOR, '.navigation-menu-contents > div:nth-child(1)')
    #header.click()
    #sleep(1)
    #sports = driver.find_element(By.CSS_SELECTOR, 'a.text-white:nth-child(4)')
    #sports.click()
    #sleep(3)








    # IMPORTANT!!! This is very good to know, find_element will throw an exception if not found -
    # find_elements will simply return an empty list. So we don't need to try catch these if we just
    # check to see find_elements and then check if the list is empty! Very cool!
    for i in range(10):
        if driver.find_elements(By.CSS_SELECTOR, 'div.text-center:nth-child(1)'):
            print("Element exists!")
            click_for_more = driver.find_element(By.CSS_SELECTOR, 'div.text-center:nth-child(1)')
            click_for_more.click()
            sleep(1)
        else:
            print("Element no longer exists!")
            break

        

    # Now all the matches should be loaded. 
    entries = driver.find_elements(By.CLASS_NAME, "betline")
    for entry in entries:
        n = entry.text.splitlines()
        #print(entry.text)
        print(len(n))
        print("How often")
        if n[1] != 'Match Winner':
            print("This is not a match, therefore we don't care.")
            continue
        else:
            if len(n) == 9:
                namecheck0 = LoLTeamNames.standardize_names(n[2])
                namecheck1 = LoLTeamNames.standardize_names(n[5])
                
                if namecheck0 < namecheck1:
                    team1.append(namecheck0)
                    team2.append(namecheck1)
                    win1.append(n[3])
                    win2.append(n[6])
                else:
                    team1.append(namecheck1)
                    team2.append(namecheck0)
                    win1.append(n[6])
                    win2.append(n[3])

                spreadou1.append(pd.NA)
                spread1.append(pd.NA)
                spreadou2.append(pd.NA)
                spread2.append(pd.NA)
                total_over.append(pd.NA)
                total1.append(pd.NA)
                total_under.append(pd.NA)
                total2.append(pd.NA)
                
                # date_time.append(n[7]) DATE
                if n[7] == 'Live Now':
                    date_time.append(n[7])
                else: 
                    unformatted_date = n[7]
                    unformatted_date = unformatted_date[:-4]
                    month = unformatted_date[:3].title()
                    
                    time = unformatted_date[3:]
                    
                    time_for_edit = time[-5:]
                    parsed_t = datetime.strptime(time_for_edit, "%H:%M")
                    parsed_t += timedelta(hours=3)
                    formatted_t = parsed_t.strftime("%H:%M")
                
                    

                    formatted_datetime = f"{month.strip()} {time[:-5].strip()} {formatted_t}"
        
                    print(formatted_datetime)

                    

                    date_time.append(formatted_datetime)




                site.append('Rivalry')
            elif len(n) == 11:
                namecheck0 = LoLTeamNames.standardize_names(n[3])
                namecheck1 = LoLTeamNames.standardize_names(n[7])
                
                if namecheck0 < namecheck1:
                    team1.append(namecheck0)
                    team2.append(namecheck1)
                    win1.append(n[4])
                    win2.append(n[8])
                else:
                    team1.append(namecheck1)
                    team2.append(namecheck0)
                    win1.append(n[8])
                    win2.append(n[4])
                
                spreadou1.append(pd.NA)
                spread1.append(pd.NA)
                spreadou2.append(pd.NA)
                spread2.append(pd.NA)
                total_over.append(pd.NA)
                total1.append(pd.NA)
                total_under.append(pd.NA)
                total2.append(pd.NA)
                


                #date_time.append(n[9]) DATE
                if n[9] == 'Live Now':
                    date_time.append(n[9])
                else: 
                    unformatted_date = n[9]
                    unformatted_date = unformatted_date[:-4]
                    month = unformatted_date[:3].title()
                    time = unformatted_date[3:]

                    time_for_edit = time[-5:]
                    parsed_t = datetime.strptime(time_for_edit, "%H:%M")
                    parsed_t += timedelta(hours=3)
                    formatted_t = parsed_t.strftime("%H:%M")
                
                    

                    formatted_datetime = f"{month.strip()} {time[:-5].strip()} {formatted_t}"

                    date_time.append(formatted_datetime)
                


                site.append('Rivalry')
            else:
                print("We are not able to deal with this yet!")
                continue







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

lol_df.to_csv('LoL_Rivalry.csv')

driver.quit()