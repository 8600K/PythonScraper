# BOVADA
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep
import pandas as pd

import LoLTeamNames


url = 'https://www.bovada.lv/sports/esports/counter-strike-2'


lol_df = pd.DataFrame({"Team1": [],
                       "Team2": [],
                       "Spread1": [],
                       "Spread2": [],
                       "Win1": [],
                       "Win2": [],
                       "Total1": [],
                       "Total2": []})

team1 = []
spread1 = []
win1 = []
total1 = []
team2 = []
spread2 = []
win2 = []
total2 = []

driver = webdriver.Firefox()


# TODO Add a thing to check if EVEN == +100 DOUBLE CHECK.

def check_even(ele):
    if ele != 'EVEN':
        return ele
    else:
        return '+100'
    
# Might add element to be clickable in the future. Right now this is working very well. 

def get_data(url):

    try:
        driver.get(url)
        sleep(3)

        for i in range(1, 11):
            try:
                leagues = driver.find_element(By.CSS_SELECTOR, f'div.grouped-events:nth-child({i}) > h4:nth-child(1) > a:nth-child(1)')
                leagues.click()
                sleep(3)

                for i in range(30):
                    try:
                        elements = driver.find_elements(By.CSS_SELECTOR, f'.grouped-events > sp-coupon:nth-child({i})')
                        for element in elements:
                            # Ensure this still works when spread, win and or total are empty. Right now this assumes Bovada only fills data. 
                            # Will probably need a logic gate based on length of fields. 
                            # Then use the find function to base it off of spread, win, and or total.
                            
                            fields = element.text.split('\n')
                            print("IMPORTANT!!! Fields!", fields)

                            length = len(fields)
                            name1 = LoLTeamNames.standardize_names(fields[2])
                            name2 = LoLTeamNames.standardize_names(fields[3])

                            if length == 14 or length == 10 or length == 12:
                                fields = fields[3:]
                                length = len(fields)
                            
                            print("LENGTH: ", len(fields))
                            if name1 < name2:
                                # Alphabetized
                                team1.append(name1)
                                team2.append(name2)
                                # 11 Means everything is there, spread, total, win. 
                                if length == 11: 
                                    spread1.append(check_even(fields[5][fields[5].find('(')+1:fields[5].find(')')]))
                                    spread2.append(check_even(fields[6][fields[6].find('(')+1:fields[6].find(')')]))
                                    win1.append(fields[7])
                                    win2.append(fields[8])
                                    total1.append(check_even(fields[9][fields[9].find('(')+1:fields[9].find(')')]))
                                    total2.append(check_even(fields[10][fields[10].find('(')+1:fields[10].find(')')]))
                                elif length == 9:
                                    # 9 Means something is missing. 
                                    # TODO Try and find some data for when there is Win and Total but no Spread.
                                    # If that is even possible.
                                    # Right now I have it set up as if it is impossible. 
                                    print("Right here!!")
                                    if fields[5][0:4] == '+1.5' or fields[5][0:4] == '-1.5':
                                        spread1.append(check_even(fields[5][fields[5].find('(')+1:fields[5].find(')')]))
                                        spread2.append(check_even(fields[6][fields[6].find('(')+1:fields[6].find(')')]))
                                        win1.append(fields[7])
                                        win2.append(fields[8])
                                        total1.append('NaN')
                                        total2.append('NaN')
                                    # Right here just add an else and then do win = fields 5 and 6, and Total would be 7 and 8 most likely.
                                elif length == 7:
                                    spread1.append('NaN')
                                    spread2.append('NaN')
                                    win1.append(fields[5])
                                    win2.append(fields[6])
                                    total1.append('NaN')
                                    total2.append('NaN')
                                else:
                                    print("Please see an administator. Something has gone awry.")
                                        
                                    

                            # Other alphabetize
                            else:
                                team1.append(name2)
                                team2.append(name1)
                                if length == 11:
                                    spread1.append(check_even(fields[6][fields[6].find('(')+1:fields[6].find(')')]))
                                    spread2.append(check_even(fields[5][fields[5].find('(')+1:fields[5].find(')')]))
                                    win1.append(fields[8])
                                    win2.append(fields[7])
                                    total1.append(check_even(fields[10][fields[10].find('(')+1:fields[10].find(')')]))
                                    total2.append(check_even(fields[9][fields[9].find('(')+1:fields[9].find(')')]))
                                elif length == 9:
                                    # 9 Means something is missing. 
                                    spread1.append(check_even(fields[6][fields[6].find('(')+1:fields[6].find(')')]))
                                    spread2.append(check_even(fields[5][fields[5].find('(')+1:fields[5].find(')')]))
                                    win1.append(fields[8])
                                    win2.append(fields[7])
                                    total1.append('NaN')
                                    total2.append('NaN')
                                elif length == 7:
                                    spread1.append('NaN')
                                    spread2.append('NaN')
                                    win1.append(fields[8])
                                    win2.append(fields[7])
                                    total1.append('NaN')
                                    total2.append('NaN')
                                else:
                                    print("Please see an administator. Something has gone wrong.")
                                            
                                
                            #print(fields)
                            x = fields[5]
                            x = x[x.find("(")+1:x.find(")")]
                            #print(x)


                            #print(team1)
                            #print(team2)
                    except:
                        print("End of the line.")
                        
                    



            except:
                print("End of the leagues.")
                driver.back()
                sleep(3)

        

    except:
        print("Couldn't load the webpage.")

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

lol_df.to_csv('CS_Bovada.csv')
