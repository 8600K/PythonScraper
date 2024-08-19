import pandas as pd
import datetime
from datetime import datetime

df_bovada = pd.read_csv('LoL_Bovada.csv')
df_thunderpick = pd.read_csv('LoL_Thunderpick.csv')
df_rivalry = pd.read_csv('LoL_Rivalry.csv')
df_betnow = pd.read_csv('LoL_BetNow.csv')
df_draftkings = pd.read_csv('LoL_Draftkings.csv')
df_espnbet = pd.read_csv('LoL_ESPNBet.csv')
df_everygame = pd.read_csv('LoL_Everygame.csv')
df_pinnacle = pd.read_csv('LoL_Pinnacle.csv')


win_dataframe_final = pd.DataFrame({"Win1_Team": [],
                                        "Win2_Team": [],
                                        "Win1_Decimal": [],
                                        "Win2_Decimal": [],
                                        "Win1_Probability": [],
                                        "Win2_Probability": [],
                                        "Win1_Ev": [],
                                        "Win2_Ev": [],
                                        "Win1_Site": [],
                                        "Win2_Site": [],
                                        "Date_Time": []
                                        
    })

spread_dataframe_final = pd.DataFrame({"Spread1_Team": [],
                                        "Spread2_Team": [],
                                        "Spread1_Decimal": [],
                                        "Spread2_Decimal": [],
                                        "Spread1_Ou": [],
                                        "Spread2_Ou": [],
                                        "Spread1_Probability": [],
                                        "Spread2_Probability": [],
                                        "Spread1_Ev": [],
                                        "Spread2_Ev": [],
                                        "Spread1_Site": [],
                                        "Spread2_Site": [],
                                        "Date_Time": []
                                        
    })

total_dataframe_final = pd.DataFrame({"Total1_Team": [],
                                        "Total2_Team": [],
                                        "Total1_Decimal": [],
                                        "Total2_Decimal": [],
                                        "Total_Over": [],
                                        "Total_Under": [],
                                        "Total1_Probability": [],
                                        "Total2_Probability": [],
                                        "Total1_Ev": [],
                                        "Total2_Ev": [],
                                        "Total1_Site": [],
                                        "Total2_Site": [],
                                        "Date_Time": []
                                        
    })


    


# Formula -> (highest payout)(average probability of winning) - (amount wagered)(average probability of losing)
# Decimal payout = bet * odds. Example: $100 bet with 3.0 odds = $300 dollars, $200 in profit


def remove_vigorish(odds_list, bet_str):
    for counter in range(len(odds_list)):
        print(odds_list[counter])
        win1_odds = 1 / odds_list[counter][2]
        win2_odds = 1 / odds_list[counter][3]

        print(win1_odds, win2_odds)
        odds_list[counter][2] = win1_odds / (win1_odds + win2_odds)
        odds_list[counter][3] = win2_odds / (win2_odds + win1_odds)

    if bet_str == 'win':
        dataframed = pd.DataFrame(odds_list, columns=['Team1', 'Team2', 'Win1', 'Win2'])
    elif bet_str == 'spread':
        dataframed = pd.DataFrame(odds_list, columns=['Team1', 'Team2', 'Spread1', 'Spread2'])
    elif bet_str == 'total':
        dataframed = pd.DataFrame(odds_list, columns=['Team1', 'Team2', 'Total1', 'Total2'])
    
    return dataframed

# ---------------------------------------------------------------------------------------------------------------------------------
# Function that returns a list of sites based on oddtype: Win1, Win2, Spread1, etc.
# --------------------------------------------------------------------------------------------------------------------------------- 

def get_sites(subset, oddtype):
    sites = []
    for key, group in subset:
        #print(duplicate_subset.get_group(key).to_string(), '\n\n')
        odd_group = group[oddtype] = pd.to_numeric(group[oddtype], errors='coerce')
    
        odd_max_index = odd_group.idxmax()  # Get the index of the row with maximum Win1
        #print("Index: ", win1_max_index)
        #print(group.to_string())
        try:
            odd_max_site = group.loc[odd_max_index, 'Site']  # Extract the site name from that row
            #print(oddtype)
            #print(odd_max_site)
        except:
            continue

        if isinstance(odd_max_site, pd.Series):
        # If there are ties for the maximum Win1, concatenate the site names into a single string
            odd_max_site = ', '.join(odd_max_site)
        
        # print(type(site_with_max_win1)) Perfect!!!
        
        #team1 = group.loc[max_win1_index, 'Team1']  # Extract Team1
        #team2 = group.loc[max_win1_index, 'Team2']  # Extract Team2
        sites.append(odd_max_site)
    return sites


def expected_value(means1, maxes1, means2, maxes2):
    expected_values = []
    for i in range(len(means1)):

        print()
        payout_max = float((maxes1.values[i] * 100) - 100)

        amount_to_lose = 100

        print('Probability 1: ', means1.values[i])
        print('Max payout: ', payout_max)
        print('Probability 2: ', means2.values[i])
        print('Wager: ', amount_to_lose)

        print('--------------------------------------------')

        ev = (means1.values[i] * payout_max) - (means2.values[i] * amount_to_lose)


        ev = float(ev)
        ev = round(ev, 2)
        expected_values.append(ev)
        #print(ev)
        #print('--------------------------------------------')
    
    return expected_values
        

# Used to flatten 2D list to 1D
def flatten_list(two_d):
    one_d = []
    for ele in two_d:
        one_d.append(round(ele, 2))
    
    return one_d




def concat():
    frames = [df_bovada, df_thunderpick, df_betnow, df_pinnacle, df_draftkings, df_espnbet, df_rivalry, df_everygame]

    large_df = pd.concat(frames)

    # Yes these naming schemes suck. Unlucky.
    # The main duplicated subset that handles win and some other stuff.
    duplicate_subset_full = large_df[large_df.duplicated(subset=['Team1', 'Team2'], keep=False)].groupby(['Team1', 'Team2'])
    
    # Handles Spread and Total removal of NaN
    duplicate_spread_remove_nan = large_df.dropna(subset=(['Spread1', 'Spread2']))
    duplicate_total_remove_nan = large_df.dropna(subset=(['Total1', 'Total2']))

    # The main duplicated subset that handles spread.
    duplicate_subset_spread = duplicate_spread_remove_nan[duplicate_spread_remove_nan.duplicated(subset=['Team1', 'Team2'], keep=False)].groupby(['Team1', 'Team2'])

    # The main duplicated subset that handles total.
    duplicate_subset_total = duplicate_total_remove_nan[duplicate_total_remove_nan.duplicated(subset=['Team1', 'Team2'], keep=False)].groupby(['Team1', 'Team2'])
    

    #print(large_df.to_string())

    # ---------------------------------------------------------------------------------------------------------------------------------
    # Creation of lists from selected columns within dataframes.
    # ---------------------------------------------------------------------------------------------------------------------------------

    win_to_list_bovada = df_bovada[['Team1','Team2', 'Win1', 'Win2']].values.tolist()
    win_to_list_thunderpick = df_thunderpick[['Team1', 'Team2', 'Win1', 'Win2']].values.tolist()
    win_to_list_betnow = df_betnow[['Team1', 'Team2', 'Win1', 'Win2']].values.tolist()
    win_to_list_pinnacle = df_pinnacle[['Team1', 'Team2', 'Win1', 'Win2']].values.tolist()
    win_to_list_draftkings = df_draftkings[['Team1', 'Team2', 'Win1', 'Win2']].values.tolist()
    win_to_list_espnbet = df_espnbet[['Team1', 'Team2', 'Win1', 'Win2']].values.tolist()
    win_to_list_rivalry = df_rivalry[['Team1', 'Team2', 'Win1', 'Win2']].values.tolist()
    win_to_list_everygame = df_everygame[['Team1', 'Team2', 'Win1', 'Win2']].values.tolist()


    win_to_list_bovada = remove_vigorish(win_to_list_bovada, 'win')
    win_to_list_thunderpick = remove_vigorish(win_to_list_thunderpick, 'win')
    win_to_list_betnow = remove_vigorish(win_to_list_betnow, 'win')
    win_to_list_pinnacle = remove_vigorish(win_to_list_pinnacle, 'win')
    win_to_list_draftkings = remove_vigorish(win_to_list_draftkings, 'win')
    win_to_list_espnbet = remove_vigorish(win_to_list_espnbet, 'win')
    win_to_list_rivalry = remove_vigorish(win_to_list_rivalry, 'win')
    win_to_list_everygame = remove_vigorish(win_to_list_everygame, 'win')

    # For dates. 
    win_date_list_bovada = df_bovada[['Team1', 'Team2', 'DateTime', 'Site']]
    win_date_list_thunderpick = df_thunderpick[['Team1', 'Team2', 'DateTime', 'Site']]
    win_date_list_betnow = df_betnow[['Team1', 'Team2', 'DateTime', 'Site']]
    win_date_list_pinnacle = df_pinnacle[['Team1', 'Team2', 'DateTime', 'Site']]
    win_date_list_draftkings = df_draftkings[['Team1', 'Team2', 'DateTime', 'Site']]
    win_date_list_espnbet = df_espnbet[['Team1', 'Team2', 'DateTime', 'Site']]
    win_date_list_rivalry = df_rivalry[['Team1', 'Team2', 'DateTime', 'Site']]
    win_date_list_everygame = df_everygame[['Team1', 'Team2', 'DateTime', 'Site']]

    

    spread_to_list_bovada = df_bovada[['Team1', 'Team2', 'Spread1', 'Spread2']].values.tolist()
    spread_to_list_thunderpick = df_thunderpick[['Team1', 'Team2', 'Spread1', 'Spread2']].values.tolist() # No Spread on Thunderpick.
    spread_to_list_betnow = df_betnow[['Team1', 'Team2', 'Spread1', 'Spread2']].values.tolist() # Betnow is currently broken due to no LoL values on their website.
    spread_to_list_pinnacle = df_pinnacle[['Team1', 'Team2', 'Spread1', 'Spread2']].values.tolist()
    spread_to_list_draftkings = df_draftkings[['Team1', 'Team2', 'Spread1', 'Spread2']].values.tolist()
    spread_to_list_espnbet = df_espnbet[['Team1', 'Team2', 'Spread1', 'Spread2']].values.tolist()
    spread_to_list_rivalry = df_rivalry[['Team1', 'Team2', 'Spread1', 'Spread2']].values.tolist() # No Spread
    spread_to_list_everygame = df_everygame[['Team1', 'Team2', 'Spread1', 'Spread2']].values.tolist() # No Spread


    spread_to_list_bovada = remove_vigorish(spread_to_list_bovada, 'spread')
    spread_to_list_thunderpick = remove_vigorish(spread_to_list_thunderpick, 'spread')
    spread_to_list_betnow = remove_vigorish(spread_to_list_betnow, 'spread')
    spread_to_list_pinnacle = remove_vigorish(spread_to_list_pinnacle, 'spread')
    spread_to_list_draftkings = remove_vigorish(spread_to_list_draftkings, 'spread')
    spread_to_list_espnbet = remove_vigorish(spread_to_list_espnbet, 'spread')
    spread_to_list_rivalry = remove_vigorish(spread_to_list_rivalry, 'spread')
    spread_to_list_everygame = remove_vigorish(spread_to_list_everygame, 'spread')

    # For dates
    spread_date_list_bovada = df_bovada[['Team1', 'Team2', 'Spread1', 'Spread2', 'DateTime', 'Site']]
    spread_date_list_thunderpick = df_thunderpick[['Team1', 'Team2', 'Spread1', 'Spread2', 'DateTime', 'Site']]
    spread_date_list_betnow = df_betnow[['Team1', 'Team2', 'Spread1', 'Spread2', 'DateTime', 'Site']]
    spread_date_list_pinnacle = df_pinnacle[['Team1', 'Team2', 'Spread1', 'Spread2', 'DateTime', 'Site']]
    spread_date_list_draftkings = df_draftkings[['Team1', 'Team2', 'Spread1', 'Spread2', 'DateTime', 'Site']]
    spread_date_list_espnbet = df_espnbet[['Team1', 'Team2', 'Spread1', 'Spread2', 'DateTime', 'Site']]
    spread_date_list_rivalry = df_rivalry[['Team1', 'Team2', 'Spread1', 'Spread2', 'DateTime', 'Site']]
    spread_date_list_everygame = df_everygame[['Team1', 'Team2', 'Spread1', 'Spread2', 'DateTime', 'Site']]

    # Gets the OVER UNDER for spreads.
    spread_ou_bovada = df_bovada[['Team1', 'Team2', 'SpreadOU1', 'SpreadOU2']]
    spread_ou_thunderpick = df_thunderpick[['Team1', 'Team2', 'SpreadOU1', 'SpreadOU2']]
    spread_ou_betnow = df_betnow[['Team1', 'Team2', 'SpreadOU1', 'SpreadOU2']]
    spread_ou_pinnacle = df_pinnacle[['Team1', 'Team2', 'SpreadOU1', 'SpreadOU2']]
    spread_ou_draftkings = df_draftkings[['Team1', 'Team2', 'SpreadOU1', 'SpreadOU2']]
    spread_ou_espnbet = df_espnbet[['Team1', 'Team2', 'SpreadOU1', 'SpreadOU2']]
    spread_ou_rivalry = df_rivalry[['Team1', 'Team2', 'SpreadOU1', 'SpreadOU2']]
    spread_ou_everygame = df_everygame[['Team1', 'Team2', 'SpreadOU1', 'SpreadOU2']]



    total_to_list_bovada = df_bovada[['Team1', 'Team2', 'Total1', 'Total2']].values.tolist()
    total_to_list_thunderpick = df_thunderpick[['Team1', 'Team2', 'Total1', 'Total2']].values.tolist()
    total_to_list_betnow = df_betnow[['Team1', 'Team2', 'Total1', 'Total2']].values.tolist()
    total_to_list_pinnacle = df_pinnacle[['Team1', 'Team2', 'Total1', 'Total2']].values.tolist()
    total_to_list_draftkings = df_draftkings[['Team1', 'Team2', 'Total1', 'Total2']].values.tolist()
    total_to_list_espnbet = df_espnbet[['Team1', 'Team2', 'Total1', 'Total2']].values.tolist()
    total_to_list_rivalry = df_rivalry[['Team1', 'Team2', 'Total1', 'Total2']].values.tolist()
    total_to_list_everygame = df_everygame[['Team1', 'Team2', 'Total1', 'Total2']].values.tolist()

    total_to_list_bovada = remove_vigorish(total_to_list_bovada, 'total')
    total_to_list_thunderpick = remove_vigorish(total_to_list_thunderpick, 'total')
    total_to_list_betnow = remove_vigorish(total_to_list_betnow, 'total')
    total_to_list_pinnacle = remove_vigorish(total_to_list_pinnacle, 'total')
    total_to_list_draftkings = remove_vigorish(total_to_list_draftkings, 'total')
    total_to_list_espnbet = remove_vigorish(total_to_list_espnbet, 'total')
    total_to_list_rivalry = remove_vigorish(total_to_list_rivalry, 'total')
    total_to_list_everygame = remove_vigorish(total_to_list_everygame, 'total')

    # For dates
    total_date_list_bovada = df_bovada[['Team1', 'Team2', 'Total1', 'Total2', 'DateTime', 'Site']]
    total_date_list_thunderpick = df_thunderpick[['Team1', 'Team2', 'Total1', 'Total2', 'DateTime', 'Site']]
    total_date_list_betnow = df_betnow[['Team1', 'Team2', 'DateTime', 'Total1', 'Total2', 'Site']]
    total_date_list_pinnacle = df_pinnacle[['Team1', 'Team2', 'Total1', 'Total2', 'DateTime', 'Site']]
    total_date_list_draftkings = df_draftkings[['Team1', 'Team2', 'Total1', 'Total2', 'DateTime', 'Site']]
    total_date_list_espnbet = df_espnbet[['Team1', 'Team2', 'Total1', 'Total2', 'DateTime', 'Site']]
    total_date_list_rivalry = df_rivalry[['Team1', 'Team2', 'Total1', 'Total2', 'DateTime', 'Site']]
    total_date_list_everygame = df_everygame[['Team1', 'Team2', 'Total1', 'Total2', 'DateTime', 'Site']]

    total_ou_bovada = df_bovada[['Team1', 'Team2', 'TotalOver', 'TotalUnder']]
    total_ou_thunderpick = df_thunderpick[['Team1', 'Team2', 'TotalOver', 'TotalUnder']]
    total_ou_betnow = df_betnow[['Team1', 'Team2', 'TotalOver', 'TotalUnder']]
    total_ou_pinnacle = df_pinnacle[['Team1', 'Team2', 'TotalOver', 'TotalUnder']]
    total_ou_draftkings = df_draftkings[['Team1', 'Team2', 'TotalOver', 'TotalUnder']]
    total_ou_espnbet = df_espnbet[['Team1', 'Team2', 'TotalOver', 'TotalUnder']]
    total_ou_rivalry = df_rivalry[['Team1', 'Team2', 'TotalOver', 'TotalUnder']]
    total_ou_everygame = df_everygame[['Team1', 'Team2', 'TotalOver', 'TotalUnder']]


    
    # ---------------------------------------------------------------------------------------------------------------------------------
    # Creation of duplicated subsets for wins, spreads, and totals. 
    # ---------------------------------------------------------------------------------------------------------------------------------


    win_frames = [win_to_list_bovada, win_to_list_thunderpick, win_to_list_betnow, win_to_list_pinnacle, win_to_list_draftkings, win_to_list_espnbet, win_to_list_rivalry, win_to_list_everygame]
    spread_frames = [spread_to_list_bovada, spread_to_list_thunderpick, spread_to_list_betnow, spread_to_list_pinnacle, spread_to_list_draftkings, spread_to_list_espnbet, spread_to_list_rivalry, spread_to_list_everygame]
    total_frames = [total_to_list_bovada, total_to_list_thunderpick, total_to_list_betnow, total_to_list_pinnacle, total_to_list_draftkings, total_to_list_espnbet, total_to_list_rivalry, total_to_list_everygame]

    spread_ou_frames = [spread_ou_bovada, spread_ou_thunderpick, spread_ou_betnow, spread_ou_pinnacle, spread_ou_draftkings, spread_ou_espnbet, spread_ou_rivalry, spread_ou_everygame]
    total_ou_frames = [total_ou_bovada, total_ou_thunderpick, total_ou_betnow, total_ou_pinnacle, total_ou_draftkings, total_ou_espnbet, total_ou_rivalry, total_ou_everygame]

    large_win_df = pd.concat(win_frames)
    large_spread_df = pd.concat(spread_frames)
    large_total_df = pd.concat(total_frames)

    large_spread_ou_df = pd.concat(spread_ou_frames)
    large_total_ou_df = pd.concat(total_ou_frames)

    # Dates 
    win_date_frames = [win_date_list_bovada, win_date_list_thunderpick, win_date_list_betnow, win_date_list_pinnacle, win_date_list_draftkings, win_date_list_espnbet, win_date_list_rivalry, win_date_list_everygame]
    large_win_date_df = pd.concat(win_date_frames)
    spread_date_frames = [spread_date_list_bovada, spread_date_list_thunderpick, spread_date_list_betnow, spread_date_list_pinnacle, spread_date_list_draftkings, spread_date_list_espnbet, spread_date_list_rivalry, spread_date_list_everygame]
    large_spread_date_df = pd.concat(spread_date_frames)
    total_date_frames = [total_date_list_bovada, total_date_list_thunderpick, total_date_list_betnow, total_date_list_pinnacle, total_date_list_draftkings, total_date_list_espnbet, total_date_list_rivalry, total_date_list_everygame]
    large_total_date_df = pd.concat(total_date_frames)



    # Win
    duplicate_win_subset = large_win_df[large_win_df.duplicated(subset=['Team1', 'Team2'], keep=False)].groupby(['Team1', 'Team2'])


    # Dates
    # Have to dropna Spread and Total like with the other dataframes. Might be able to optimize this by using the same large_spread/total_df but for now this is working well.
    duplicate_win_date_subset = large_win_date_df[large_win_date_df.duplicated(subset=['Team1', 'Team2'], keep=False)].groupby(['Team1', 'Team2'])
    large_spread_date_dropped = large_spread_date_df.dropna(subset=['Spread1', 'Spread2', 'DateTime', 'Site'])
    duplicate_spread_date_subset = large_spread_date_dropped[large_spread_date_dropped.duplicated(subset=['Team1', 'Team2'], keep=False)].groupby(['Team1', 'Team2'])
    large_total_date_dropped = large_total_date_df.dropna(subset=['Total1', 'Total2', 'DateTime', 'Site'])
    duplicate_total_date_subset = large_total_date_dropped[large_total_date_dropped.duplicated(subset=['Team1', 'Team2'], keep=False)].groupby(['Team1', 'Team2'])

    # Spread
    large_spread_dropped = large_spread_df.dropna(subset=['Spread1', 'Spread2'])
    duplicate_spread_subset = large_spread_dropped[large_spread_dropped.duplicated(subset=['Team1', 'Team2'], keep=False)].groupby(['Team1', 'Team2'])

    large_spread_ou_dropped = large_spread_ou_df.dropna(subset=['SpreadOU1', 'SpreadOU2'])
    duplicate_spread_ou_subset = large_spread_ou_dropped[large_spread_ou_dropped.duplicated(subset=['Team1', 'Team2'], keep=False)].groupby(['Team1', 'Team2'])


    # Total
    large_total_dropped = large_total_df.dropna(subset=['Total1', 'Total2'])
    duplicate_total_subset = large_total_dropped[large_total_dropped.duplicated(subset=['Team1', 'Team2'], keep=False)].groupby(['Team1', 'Team2'])

    large_total_ou_dropped = large_total_ou_df.dropna(subset=['TotalOver', 'TotalUnder'])
    duplicate_total_ou_subset = large_total_ou_dropped[large_total_ou_dropped.duplicated(subset=['Team1', 'Team2'], keep=False)].groupby(['Team1', 'Team2'])


    #for key, value in duplicate_subset_full: TODO
        #print(value.to_string())

    # ---------------------------------------------------------------------------------------------------------------------------------
    # Please note that for win1 or spread2, etc they use different duplicated dataframes. 
    # The duplicate win subset has the vigorish removed and converted into probabilities. 
    # The duplicate subset is merely all frames put together as is. 
    # This next part creates the lists for the data we send into the dataframes that then get sent to a CSV file into the website.
    # ---------------------------------------------------------------------------------------------------------------------------------

    # List creation.
    win1_teams = []
    win2_teams = []
    win_date = []

    win1_sites = []
    win2_sites = []

    win1_ev = []
    win2_ev = []


    spread1_teams = []
    spread2_teams = []
    spread_date = []

    spread1_sites = []
    spread2_sites = []

    spread1_ev = []
    spread2_ev = []

    spread1_ou = []
    spread2_ou = []


    total1_teams = []
    total2_teams = []
    total_date = []

    total1_sites = []
    total2_sites = []

    total1_ev = []
    total2_ev = []

    total_over = []
    total_under = []



    win1_mean = duplicate_win_subset.agg({'Win1' : ['mean']})
    win1_max = duplicate_subset_full['Win1'].agg(['max'])
    win2_mean = duplicate_win_subset.agg({'Win2' : ['mean']}) 
    win2_max = duplicate_subset_full.agg({'Win2' : ['max']})


    spread1_mean = duplicate_spread_subset.agg({'Spread1' : ['mean']})
    spread1_max = duplicate_subset_spread['Spread1'].agg(['max'])
    spread2_mean = duplicate_spread_subset.agg({'Spread2' : ['mean']})
    spread2_max = duplicate_subset_spread['Spread2'].agg(['max'])

    total1_mean = duplicate_total_subset.agg({'Total1': ['mean']})
    total1_max = duplicate_subset_total['Total1'].agg(['max'])
    total2_mean = duplicate_total_subset.agg({'Total2': ['mean']})
    total2_max = duplicate_subset_total['Total2'].agg(['max'])

    for key, element in duplicate_win_subset:
        win1_teams.append(key[0])
        win2_teams.append(key[1])
    
    for key, element in duplicate_spread_subset:
        spread1_teams.append(key[0])
        spread2_teams.append(key[1])
    
    for key, element in duplicate_total_subset:
        total1_teams.append(key[0])
        total2_teams.append(key[1])

    
    # Over under for Spreads and Totals
    # TODO This would be a good place to check for if Over Under is not the same (Should never happen but you never know.)

    for key, element in duplicate_spread_ou_subset:
        spread1_ou.append(element['SpreadOU1'].tolist()[0])
        spread2_ou.append(element['SpreadOU2'].tolist()[0])

    for key, element in duplicate_total_ou_subset:
        total_over.append(element['TotalOver'].tolist()[0])
        total_under.append(element['TotalUnder'].tolist()[0])  
    



    # ---------------------------------------------------------------------------------------------------------------------------------
    # Expected Value 
    # ---------------------------------------------------------------------------------------------------------------------------------

    print("HELLO!")
    print(win1_mean)
    print("END OF")



    win1_ev = expected_value(win1_mean, win1_max, win2_mean, win2_max)
    win2_ev = expected_value(win2_mean, win2_max, win1_mean, win1_max)
    # Expected values are done. 
    win1_mean_rounded = flatten_list(win1_mean.values.flatten().tolist()) 
    win2_mean_rounded = flatten_list(win2_mean.values.flatten().tolist())

    spread1_ev = expected_value(spread1_mean, spread1_max, spread2_mean, spread2_max)
    spread2_ev = expected_value(spread2_mean, spread2_max, spread1_mean, spread1_max)

    spread1_mean_rounded = flatten_list(spread1_mean.values.flatten().tolist())
    spread2_mean_rounded = flatten_list(spread2_mean.values.flatten().tolist())

    total1_ev = expected_value(total1_mean, total1_max, total2_mean, total2_max)
    total2_ev = expected_value(total2_mean, total2_max, total1_mean, total2_max)

    total1_mean_rounded = flatten_list(total1_mean.values.flatten().tolist())
    total2_mean_rounded = flatten_list(total2_mean.values.flatten().tolist())


    # Converts rounded values to be more viewer friendly. Essentially removes the 0. from the percentage.
    win1_mean_rounded = [int(x * 100) for x in win1_mean_rounded]
    win2_mean_rounded = [int(x * 100) for x in win2_mean_rounded]

    spread1_mean_rounded = [int(x * 100) for x in spread1_mean_rounded]
    spread2_mean_rounded = [int(x * 100) for x in spread2_mean_rounded]

    total1_mean_rounded = [int(x * 100) for x in total1_mean_rounded]
    total2_mean_rounded = [int(x * 100) for x in total2_mean_rounded]
    
    


    # ---------------------------------------------------------------------------------------------------------------------------------
    # This handles getting the sites for all dataframes. 
    # ---------------------------------------------------------------------------------------------------------------------------------

    # TODO Make this a function. Each oddset, Win, Spread, Total will need to get their own site.

    win1_sites = get_sites(duplicate_subset_full, 'Win1')
    win2_sites = get_sites(duplicate_subset_full, 'Win2')

    
    
    spread1_sites = get_sites(duplicate_subset_spread, 'Spread1')
    spread2_sites = get_sites(duplicate_subset_spread, 'Spread2')



    total1_sites = get_sites(duplicate_subset_total, 'Total1')
    total2_sites = get_sites(duplicate_subset_total, 'Total2')


    # ---------------------------------------------------------------------------------------------------------------------------------
    # Dates. This is what appends dates to Win, Spread, and Total. 
    # ---------------------------------------------------------------------------------------------------------------------------------
    for key, value in duplicate_win_date_subset:

            # Creates essentially a pecking order. Rivalry is checked, then Bovada, then pinnacle etc etc. Appends the data to win.
            for v in (value.values):    
                if v[3] == 'Rivalry':
                    win_date.append(v[2])
                    break
                elif v[3] == 'Bovada':
                    win_date.append(v[2])
                    break
                elif v[3] == 'Everygame':
                    win_date.append(v[2])
                    break
                elif v[3] == 'Pinnacle':
                    win_date.append(v[2])
                    break
                else:
                    win_date.append(v[2])
                    break

    for key, value in duplicate_spread_date_subset:

            # Creates essentially a pecking order. Rivalry is checked, then Bovada, then pinnacle etc etc. Appends the data to win.
            for v in (value.values):  
                if v[3] == 'Rivalry':
                    spread_date.append(v[4])
                    break
                elif v[3] == 'Bovada':
                    spread_date.append(v[4])
                    break
                elif v[3] == 'Everygame':
                    spread_date.append(v[4])
                    break
                elif v[3] == 'Pinnacle':
                    spread_date.append(v[4])
                    break
                else:
                    spread_date.append(v[4])
                    break
        
    for key, value in duplicate_total_date_subset:

            # Creates essentially a pecking order. Rivalry is checked, then Bovada, then pinnacle etc etc. Appends the data to win.
            for v in (value.values):    
                if v[3] == 'Rivalry':
                    #print("Done", v[2])
                    total_date.append(v[4])
                    break
                elif v[3] == 'Bovada':
                    #print("Done 2", v[2])
                    total_date.append(v[4])
                    break
                elif v[3] == 'Everygame':
                    #print("Done 3", v[2])
                    total_date.append(v[4])
                    break
                elif v[3] == 'Pinnacle':
                    #print("Done 4", v[2])
                    total_date.append(v[4])
                    break
                else:
                    #print("Done 5", v[2])
                    total_date.append(v[4])
                    break

    # ---------------------------------------------------------------------------------------------------------------------------------
    # The lists to dataframe for Win, Spread, and Total. Now in website format with the values desired. 
    # ---------------------------------------------------------------------------------------------------------------------------------

    

    win_dataframe_final['Win1_Team'] = win1_teams
    win_dataframe_final['Win2_Team'] = win2_teams
    win_dataframe_final['Win1_Decimal'] = win1_max.values.flatten().tolist()
    win_dataframe_final['Win2_Decimal'] = win2_max.values.flatten().tolist()
    win_dataframe_final['Win1_Probability'] = win1_mean_rounded
    win_dataframe_final['Win2_Probability'] = win2_mean_rounded
    win_dataframe_final['Win1_Ev'] =  win1_ev
    win_dataframe_final['Win2_Ev'] = win2_ev
    win_dataframe_final['Win1_Site'] = win1_sites
    win_dataframe_final['Win2_Site'] = win2_sites
    win_dataframe_final['Date_Time'] = win_date

    spread_dataframe_final['Spread1_Team'] = spread1_teams
    spread_dataframe_final['Spread2_Team'] = spread2_teams
    spread_dataframe_final['Spread1_Decimal'] = spread1_max.values.flatten().tolist()
    spread_dataframe_final['Spread2_Decimal'] = spread2_max.values.flatten().tolist()
    spread_dataframe_final['Spread1_Ou'] = spread1_ou
    spread_dataframe_final['Spread2_Ou'] = spread2_ou
    spread_dataframe_final['Spread1_Probability'] = spread1_mean_rounded
    spread_dataframe_final['Spread2_Probability'] = spread2_mean_rounded
    spread_dataframe_final['Spread1_Ev'] = spread1_ev
    spread_dataframe_final['Spread2_Ev'] = spread2_ev
    spread_dataframe_final['Spread1_Site'] = spread1_sites
    spread_dataframe_final['Spread2_Site'] = spread2_sites
    spread_dataframe_final['Date_Time'] = spread_date

    total_dataframe_final['Total1_Team'] = total1_teams
    total_dataframe_final['Total2_Team'] = total2_teams
    total_dataframe_final['Total1_Decimal'] = total1_max.values.flatten().tolist()
    total_dataframe_final['Total2_Decimal'] = total2_max.values.flatten().tolist()
    total_dataframe_final['Total_Over'] = total_over
    total_dataframe_final['Total_Under'] = total_under
    total_dataframe_final['Total1_Probability'] = total1_mean_rounded
    total_dataframe_final['Total2_Probability'] = total2_mean_rounded
    total_dataframe_final['Total1_Ev'] = total1_ev
    total_dataframe_final['Total2_Ev'] = total2_ev
    total_dataframe_final['Total1_Site'] = total1_sites
    total_dataframe_final['Total2_Site'] = total2_sites
    total_dataframe_final['Date_Time'] = total_date




concat()
# This needs to run before to.csvs. Duh. 

if spread_dataframe_final.empty:
    spread_dataframe_final['Spread1_Team'] = ['Match not found', 'Match not found']
    spread_dataframe_final['Spread2_Team'] = ['Match not found', 'Match not found']
    spread_dataframe_final['Spread1_Decimal'] = [0, 0]
    spread_dataframe_final['Spread2_Decimal'] = [0, 0]
    spread_dataframe_final['Spread1_Ou'] = [0, 0]
    spread_dataframe_final['Spread2_Ou'] = [0, 0]
    spread_dataframe_final['Spread1_Probability'] = [0, 0]
    spread_dataframe_final['Spread2_Probability'] = [0, 0]
    spread_dataframe_final['Spread1_Ev'] = [0, 0]
    spread_dataframe_final['Spread2_Ev'] = [0, 0]
    spread_dataframe_final['Spread1_Site'] = [0, 0]
    spread_dataframe_final['Spread2_Site'] = [0, 0]
    spread_dataframe_final['Date_Time'] = [pd.NA, pd.NA]

if total_dataframe_final.empty:
    total_dataframe_final['Total1_Team'] = ['Match not found', 'Match not found']
    total_dataframe_final['Total2_Team'] = ['Match not found', 'Match not found']
    total_dataframe_final['Total1_Decimal'] = [0, 0]
    total_dataframe_final['Total2_Decimal'] = [0, 0]
    total_dataframe_final['Total_Over'] = [0, 0]
    total_dataframe_final['Total_Under'] = [0, 0]
    total_dataframe_final['Total1_Probability'] = [0, 0]
    total_dataframe_final['Total2_Probability'] = [0, 0]
    total_dataframe_final['Total1_Ev'] = [0, 0]
    total_dataframe_final['Total2_Ev'] = [0, 0]
    total_dataframe_final['Total1_Site'] = [0, 0]
    total_dataframe_final['Total2_Site'] = [0, 0]
    total_dataframe_final['Date_Time'] = [pd.NA, pd.NA]


win_dataframe_final.to_csv('Win_Dataframe.csv')
spread_dataframe_final.to_csv('Spread_Dataframe.csv')
total_dataframe_final.to_csv('Total_Dataframe.csv')


