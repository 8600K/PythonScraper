# RIVALRY
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep
import pandas as pd

import LoLTeamNames



lol_url = "https://www.rivalry.com/esports/league-of-legends-betting"
csgo_url = "https://www.rivalry.com/esports/csgo-betting"

driver = webdriver.Firefox()

'''
driver.get(url)


WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.betline:nth-child(2)')))

elements = driver.find_element(By.CSS_SELECTOR, 'div.betline:nth-child(2)')
if elements == []:
    print("Nothing found.")
else:
    elements.click()

    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.match-market-container:nth-child(1)')))

    elements = driver.find_elements(By.CSS_SELECTOR, 'div.match-market-container:nth-child(1)')

    while elements:

        for element in elements:
            print(element.text)

        num += 1
        elements = driver.find_elements(By.CSS_SELECTOR, f'div.match-market-container:nth-child({num})')
    
    driver.back()

    sleep(3)


    elements = driver.find_element(By.CSS_SELECTOR, 'div.betline:nth-child(4)')

    if elements == []:
        print("Error on the second run. Back might not work.")
    else:
        elements.click()

        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.match-market-container:nth-child(1)')))

    elements = driver.find_elements(By.CSS_SELECTOR, 'div.match-market-container:nth-child(1)')

    while elements:

        for element in elements:
            print(element.text)

        num += 1
        elements = driver.find_elements(By.CSS_SELECTOR, f'div.match-market-container:nth-child({num})')
    
    driver.back()

    sleep(3)

    print("Successful run!")


'''

    # -------------------------------------------------------------------------------------------

lol_df = pd.DataFrame({"Team1": [],
                       "Team2": [],
                       "Win1": [],
                       "Win2": [],
                       "Map1_0": [],
                       "Map1_1": [],
                       "Map2_0": [],
                       "Map2_1": [],
                       "Map3_0": [],
                       "Map3_1": [],
                        "Map4_0": [],
                         "Map4_1": [], })

team1 = []
team2 = []
win1 = []
win2 = []
map_lists = {'map1_0': [],
             'map1_1': [],
             'map2_0': [],
             'map2_1': [],
             'map3_0': [],
             'map3_1': [],
             'map4_0': [],
             'map4_1': [],
             'map5_0': [],
             'map5_1': []}

def convert_odds(odds):
    if odds >= 2.00:
        print("Greater or equal to 2.00")
        new_odds = round( ((odds - 1) * 100) )
    else:
        print("Nvm we are less than 2")
        new_odds = round( (-100 / (odds - 1)) )
    return new_odds

# TODO Double check and make sure this is working. Feels slightly off tonight.
# Actually looking pretty good. Keep checking!

def scrape(url):
    delay = 5
    boolean_case = True
    date_case = 0

    driver.get(url)
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.betline:nth-child(2)')))

    num = 2

    while boolean_case and date_case < 3:
        inner_num = 1 # Reset counter
        try:
            elements = driver.find_element(By.CSS_SELECTOR, f'div.betline:nth-child({num})')
        except:
            # Couldn't find another entry in that day...
            print("No entry found (1)")
            try:
                num += 1
                elements = driver.find_elements(By.CSS_SELECTOR, f'div.betline:nth-child({num})')
                date_case += 1
                if elements == []:
                    print("Entry found but empty (1.5)")
                    # ^^^ redundent but better safe than sorry.
                else:
                    continue
            except:
                print("No entry found (2)")
                # Legit nothing was found!
                boolean_case = False
                return
        else:
            elements.click()

        try:
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.match-market-container:nth-child(1)')))

            elements = driver.find_elements(By.CSS_SELECTOR, 'div.match-market-container:nth-child(1)')

            # Oh... this works too lol, lmao even.
            # This SHOULD always be the biggest, but if problems
            # happen come here. Make a check to ensure this is so.
            biggest = len(team1)

            if biggest > len(win1):
                win1.append('NaN')
                win2.append('NaN')
            if biggest > len(map_lists['map1_0']):
                map_lists['map1_0'].append('NaN')
                map_lists['map1_1'].append('NaN')
            if biggest > len(map_lists['map2_0']):
                map_lists['map2_0'].append('NaN')
                map_lists['map2_1'].append('NaN')
            if biggest > len(map_lists['map3_0']):
                map_lists['map3_0'].append('NaN')
                map_lists['map3_1'].append('NaN')
            if biggest > len(map_lists['map4_0']):
                map_lists['map4_0'].append('NaN')
                map_lists['map4_1'].append('NaN')
            if biggest > len(map_lists['map5_0']):
                map_lists['map5_0'].append('NaN')
                map_lists['map5_1'].append('NaN')
            

            while elements:

                for element in elements:
                    fields = element.text.split('\n')
                    fields_maps = element.text.split()
                    print(fields)
                    print('Fields_maps: ', fields_maps)
                    boolean_alphabetize = True
                    # Don't think I need to do this. As I'm basically checking it anyway. 
                    # So just do temp_x < temp_y and then continue the full loop from
                    # There. Good stuff.

                    # temp_x / temp_y names to be converted
                    temp_x = LoLTeamNames.standardize_names(fields[1])
                    temp_y = LoLTeamNames.standardize_names(fields[3])

                    print("TEMPX:: ", temp_x)
                    print("TEMPY:: ", temp_y)
                    if len(team1) > 1:
                        print("LAST TEAM1: ", team1[-1])
                        print("LAST TEAM2: ", team2[-1])

                    # Check to keep the lengths the same. 
                    # Okay, so I think I need to create a variable that stores team names. 
                    # Because fields[1] and[3] should always be the same for matches and maps. 
                    # So, when fields[1] != new fields[1] that means I should have switched to
                    # A new entry. 


                    # This means boolean_alphabetize is true.


                    if temp_x == temp_y:
                        continue

                    if temp_x < temp_y:

                        
                        if (biggest > 0 and temp_x != team1[-1]) or (biggest == 0):
                            #print("I'm lazy, does this ever run?")
                            #print('biggest: ', biggest, 'temp_x', temp_x)
                            if biggest > 0:
                                print("Important1: ", team1[-1])
                            # TODO This may or may not break!
                            #print("Woohoo! ", fields[1],  LoLTeamNames.standardize_names(fields[1]), fields[3], LoLTeamNames.standardize_names(fields[3]))
                            team1.append(LoLTeamNames.standardize_names(fields[1]))
                            team2.append(LoLTeamNames.standardize_names(fields[3]))
                            if team1[-1] == None or team2[-1] == None:
                                print("RED ALERT RED ALERT")
                            biggest += 1

                        
                        # Alphabetically correct, match winner:
                        if fields[0] == 'Match Winner':
                            
                            win1_temp = convert_odds(float(fields[2]))
                            win2_temp = convert_odds(float(fields[4]))
                            

                            win1.append(win1_temp)
                            win2.append(win2_temp)

                        if fields_maps[1] == '1':
                            map_lists['map1_0'].append(convert_odds(float(fields[2])))
                            map_lists['map1_1'].append(convert_odds(float(fields[4])))
                        if fields_maps[1] == '2':
                            map_lists['map2_0'].append(convert_odds(float(fields[2])))
                            map_lists['map2_1'].append(convert_odds(float(fields[4])))
                        if fields_maps[1] == '3':
                            map_lists['map3_0'].append(convert_odds(float(fields[2])))
                            map_lists['map3_1'].append(convert_odds(float(fields[4])))
                        if fields_maps[1] == '4':
                            map_lists['map4_0'].append(convert_odds(float(fields[2])))
                            map_lists['map4_1'].append(convert_odds(float(fields[4])))
                        if fields_maps[1] == '5':
                            map_lists['map5_0'].append(convert_odds(float(fields[2])))
                            map_lists['map5_1'].append(convert_odds(float(fields[4])))

                    # This means boolean_alphababetize is false.
                    else:
                        if (biggest > 0 and temp_x != team2[-1]) or (biggest == 0):
                            #print("I'm lazy, does this ever run part 2?")
                            #print('biggest: ', biggest, 'temp_x', temp_x)
                            if biggest > 0:
                                print("Important1: ", team1[-1])
                            #print("Woohoo! ", fields[1],  LoLTeamNames.standardize_names(fields[1]), fields[3], LoLTeamNames.standardize_names(fields[3]))
                            team1.append(LoLTeamNames.standardize_names(fields[3])) 
                            team2.append(LoLTeamNames.standardize_names(fields[1]))
                            if team1[-1] == None or team2[-1] == None:
                                print("RED ALERT RED ALERT")
                            biggest += 1

                            # TODO. CHECK THIS, MAKE SURE IT WORKS. BEFORE
                            # WE HAD NO WINNERS FOR IF ALPHABETIZE WAS FALSE LOL 
                            win1_temp = convert_odds(float(fields[4]))
                            win2_temp = convert_odds(float(fields[2]))
                            

                            win1.append(win1_temp)
                            win2.append(win2_temp)

                        

                        if fields_maps[1] == '1':
                            map_lists['map1_0'].append(convert_odds(float(fields[4])))
                            map_lists['map1_1'].append(convert_odds(float(fields[2])))
                            #print(map_lists['map1_0'])
                            #print(map_lists['map1_1'])
                        if fields_maps[1] == '2':
                            map_lists['map2_0'].append(convert_odds(float(fields[4])))
                            map_lists['map2_1'].append(convert_odds(float(fields[2])))
                        if fields_maps[1] == '3':
                            map_lists['map3_0'].append(convert_odds(float(fields[4])))
                            map_lists['map3_1'].append(convert_odds(float(fields[2])))
                        if fields_maps[1] == '4':
                            map_lists['map4_0'].append(convert_odds(float(fields[4])))
                            map_lists['map4_1'].append(convert_odds(float(fields[2])))
                        if fields_maps[1] == '5':
                            map_lists['map5_0'].append(convert_odds(float(fields[4])))
                            map_lists['map5_1'].append(convert_odds(float(fields[2])))
                    #print("This should tell me how many times this is running.")
                
        
                
                inner_num += 1
                try:
                    elements = driver.find_elements(By.CSS_SELECTOR, f'div.match-market-container:nth-child({inner_num})')
                except:
                    break
                
                
            
            driver.back()

            num += 1
            sleep(3)
        except:
            print("Just in case....")
    
    # Perform a final sweep to make sure 

    biggest = len(team1)
    if biggest > len(win1):
        win1.append('NaN')
        win2.append('NaN')
    if biggest > len(map_lists['map1_0']):
        map_lists['map1_0'].append('NaN')
        map_lists['map1_1'].append('NaN')
    if biggest > len(map_lists['map2_0']):
        map_lists['map2_0'].append('NaN')
        map_lists['map2_1'].append('NaN')
    if biggest > len(map_lists['map3_0']):
        map_lists['map3_0'].append('NaN')
        map_lists['map3_1'].append('NaN')
    if biggest > len(map_lists['map4_0']):
        map_lists['map4_0'].append('NaN')
        map_lists['map4_1'].append('NaN')
    if biggest > len(map_lists['map5_0']):
        map_lists['map5_0'].append('NaN')
        map_lists['map5_1'].append('NaN')


# All maps after map_1_1 have 1 less count. Why???

scrape(lol_url)

print(team1)
print(team2)
print(win1)
print(win2)
print(map_lists)
print(len(team1))
print(len(team2))
print(len(win1))
print(len(win2))
print(len(map_lists['map1_0']))
print(len(map_lists['map1_1']))
print(len(map_lists['map2_0']))
print(len(map_lists['map2_1']))
print(len(map_lists['map3_0']))
print(len(map_lists['map3_1']))
print(len(map_lists['map4_0']))
print(len(map_lists['map4_1']))
print(len(map_lists['map5_0']))
print(len(map_lists['map5_1']))

lol_df['Team1'] = team1
lol_df['Team2'] = team2
lol_df['Win1'] = win1
lol_df['Win2'] = win2
lol_df['Map1_0'] = map_lists['map1_0']
lol_df['Map1_1'] = map_lists['map1_1']
lol_df['Map2_0'] = map_lists['map2_0']
lol_df['Map2_1'] = map_lists['map2_1']
lol_df['Map3_0'] = map_lists['map3_0']
lol_df['Map3_1'] = map_lists['map3_1']
lol_df['Map4_0'] = map_lists['map4_0']
lol_df['Map4_1'] = map_lists['map4_1']
lol_df['Map5_0'] = map_lists['map5_0']
lol_df['Map5_1'] = map_lists['map5_1']

print(lol_df)

lol_df.to_csv('Rivalry.csv')


#scrape(csgo_url)
