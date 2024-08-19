# Barstool Sports
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

import LoLTeamNames


lol_df = pd.DataFrame({'Time': [],
                       'Team1': [],
                       'Team2': [],
                       'Win1': [],
                       'Win2': []})

# time = []
team1 = []
team2 = []
win1 = []
win2 = []

delay = 5

driver = webdriver.Firefox()

# Might need to change this to be https://espnbet.com
url = 'https://barstoolsportsbook.com'

def get_data(url):
    try:
        driver.get(url)
        sleep(3)
        #WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.space-y-4')))

    
        
        driver.find_element(By.CSS_SELECTOR, 'button.btn-small:nth-child(2)').click()
        sleep(1)
        # Might need to clean this up... But right now it works like a charm. Think I need to check if this is LoL. 
        # Probably just run a loop
        #driver.find_element(By.CSS_SELECTOR, '.w-\[245px\] > li:nth-child(25)').click()

        for i in range(15, 35):
            name_element = driver.find_element(By.CSS_SELECTOR, f'.w-\[245px\] > li:nth-child({i}) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)')
            inner_text = name_element.get_attribute('innerHTML')

            if inner_text != 'CS:GO':
                continue
            else:
                name_element.click()

        


        # Also, maybe get rid of the second try except loop. Don't think I need it if I have this working consistantly.
        #.w-\[245px\] > li:nth-child(25) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) <- I think this is what I want for checking if innter_html is LoL
        # Sure is. So run a loop, check if li:nth-child(num) + all that innerhtml or element = LoL, if so, click, otherwise keep looking. Return after... 50?
                try:
                    for i in range(30):
                        driver.find_element(By.CSS_SELECTOR, f'.w-\[245px\] > li:nth-child({i + 1})').click()
                        sleep(1)
                        
                        elements = driver.find_elements(By.CSS_SELECTOR, 'div.space-y-4:nth-child(2)')
                        for element in elements:
                            fields = element.text.split('\n')
                            for i in range(0, len(fields), 5):
                                x = i
                                split_elements = fields[x:x+5]
                                
                                name1 = LoLTeamNames.standardize_names(str(split_elements[1]))
                                name2 = LoLTeamNames.standardize_names(str(split_elements[3]))

                                number1 = split_elements[2]
                                number2 = split_elements[4]

                                if number1 == 'Even':
                                    number1 = "+100"
                                if number2 == 'Even':
                                    number2 = "+100"

                                if name1 < name2:
                                    # Boolean_Alphabatize true
                                    team1.append(name1)
                                    team2.append(name2)

                                    win1.append(number1)
                                    win2.append(number2)
                                    print("This ran!")
                                else:
                                    team1.append(name2)
                                    team2.append(name1)
                                    win1.append(number1)
                                    win2.append(number2)
                                    print("No this ran!")
                            
                except:
                    print("End of the line...")
                
    except:
        print("Couldn't load the page...")
    


get_data(url)

lol_df['Team1'] = team1
lol_df['Team2'] = team2
lol_df['Win1'] = win1
lol_df['Win2'] = win2

print(lol_df)

lol_df.to_csv('Barstool.csv')











































































































'''


#url = "https://www.pinnacle.com/en/esports-hub/league-of-legends/"
            # We have 13, there are 22 total, just use these 13 now, find out from other sites what we need. This is a good test run.
lol_urls = ['https://barstoolsportsbook.com/sport/lol/organization/international/competition/world-championship', 'https://barstoolsportsbook.com/sport/lol/organization/international/competition/lcs', 'https://barstoolsportsbook.com/sport/lol/organization/international/competition/lck-spring', 'https://barstoolsportsbook.com/sport/lol/organization/international/competition/lla', 
            'https://barstoolsportsbook.com/sport/lol/organization/international/competition/european-masters', 'https://barstoolsportsbook.com/sport/lol/organization/international/competition/cblol']

def loop_data(url):
    try:
        driver.get(url)
        sleep(2)
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.space-y-4')))
    except:
        print("Driver couldn't get access...")
        return
    
    
    boolean_case = True
    num = 1

    # I NEED MORE DATA. BUT FOR NOW, I'LL KEEP IT SIMPLE

    #elements = driver.find_elements(By.CSS_SELECTOR, 'div.p-0:nth-child(2)')
    #for element in elements:
    #    print(element.text)

    #elements = driver.find_elements(By.CSS_SELECTOR, 'button.text-primary') 
    #for element in elements:
    #    print(element.text)

    elements = driver.find_elements(By.CSS_SELECTOR, '.space-y-4')
    for element in elements:
        # Test here, yeah?
        #print(element.text.split('\n'))
        text = element.text.split('\n')
        if text == ['']:
            return
        else:
            time.append(text[0])
            team1.append(text[1])
            win1.append(text[2])
            team2.append(text[3])
            win2.append(text[4])


for i in lol_urls:
    loop_data(i)

lol_df['Time'] = time
lol_df['Team1'] = team1
lol_df['Team2'] = team2
lol_df['Win1'] = win1
lol_df['Win2'] = win2

print(lol_df)

lol_df.to_csv("Barstool.csv")

# Complete last Dataframe here. Then compare all the dataframes somehow.s

'''