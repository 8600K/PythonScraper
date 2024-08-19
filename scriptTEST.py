import pandas as pd

# TODO Pinnacle gonna need some work. 
# DF 1 = Dead
# DF 2 = Luckbox - Dead 
# DF 3 = Bovada - CSV
# DF 4 = Rivalry - CSV
# DF 5 = Thunderpick - CSV
# DF 6 = Draftkings - CSV
# DF 7 = Pinnacle - CSV
# DF 8 = Barstool Sports - CSV 



df3 = pd.read_csv('Bovada.csv')
df4 = pd.read_csv('Rivalry.csv')#.sort_index(inplace=True)
df5 = pd.read_csv('Thunderpick.csv')
df6 = pd.read_csv('Draftkings.csv')
df7 = pd.read_csv('Pinnacle.csv')#.sort_index(inplace=True)
df8 = pd.read_csv('Barstool.csv')


#print(df.to_string())


#print(df.to_string())
#print("-----------------")
#print(df1.to_string())

#print(df.to_string())
#print(df1.to_string())


#y = df['Team1'][0]
#x = df1['Team1'][2]

#print(len(x))
#print(len(y))

#if x == y:
#    print("Whaaat")
#else:
#   print("HAAAH?")

tx = -55
ty = -100

if tx > ty:
    print("That makes sense.")
else:
    print("I guess I'm just dumb")


def find_winner(data0, data1, site_name0, site_name1):
    output = pd.merge(data0, data1, suffixes=(f'_{site_name0}', f'_{site_name1}'), how='inner',  on=['Team1', 'Team2'])

    print(output.to_string())

    size = len(output)

    # Perfect!

    for count in range(size):
        temp_left0 = output[f'Win1_{site_name0}'][count]
        temp_right0 = output[f'Win1_{site_name1}'][count]
        
        temp_left1 = output[f'Win2_{site_name0}'][count]
        temp_right1 = output[f'Win2_{site_name1}'][count]

        if temp_left0 == temp_right0:
            print("They're equal, I don't know what to do here.")
            winner0 = temp_left0

        elif temp_left0 > temp_right0:
            winner0 = temp_left0
        else:
            winner0 = temp_right0

        if temp_left1 == temp_right1:
            print("They're equal pt2, I don't know what to do here.")
            winner1 = temp_left1
        
        elif temp_left1 > temp_right1:
            winner1 = temp_left1
        else:
            winner1 = temp_right1
        
        print("Winner 0:", winner0, '\n', "Winner 1:", winner1)


    

# newdf = df.merge(df14, how='inner', on=['Team1', 'Team2'])

# print(newdf.to_string())

#find_winner(df7, df4, 'P', 'R')
print(df3)
print(df4)
find_winner(df3, df4, 'B', 'R')

#combine_and_find(df, dat)

# Pinnacle and Rivalry are good to go now!
# Let's try Pinnacle and Thunderpicks next... 

#find_winner(df5, df4, 'T', 'R')



# Test all the other CSVs, if they work we're good to go!!!!