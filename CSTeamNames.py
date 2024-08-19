navi = ['NaVi', 'navi gaming', 'navi esports']
astralis = ['Astralis', 'astralis gaming', 'astralis esports']
vitality = ['Vitality', 'vitality gaming', 'vitality esports']
liquid = ['Team Liquid', 'liquid', 'team liquid gaming', 'liquid esports', 'liquid gaming']
ence = ['ENCE', 'ence gaming', 'ence esports']
faze = ['FaZe Clan', 'faze', 'faze clan gaming']
nrg = ['NRG Esports', 'nrg gaming', 'nrg']
furia = ['FURIA', 'furia gaming', 'furia esports', 'team furia']
g2 = ['G2 Esports', 'G2', 'G2 gaming']
north = ['North', 'north gaming', 'north esports']
mouz = ['MOUZ', 'mouz gaming', 'mouz esports']
fnatic = ['fnatic', 'fnatic gaming', 'fnatic esports']
mibr = ['MIBR', 'mibr gaming', 'mibr esports']
nip = ['NiP', 'nip esports', 'nip gaming']
renegades = ['Renegades', 'renegades esports', 'renegades gaming']
big = ['BIG', 'big gaming', 'big esports']
heroic = ['Heroic', 'heroic gaming', 'heroic esports']
cr4zy = ['CR4ZY', 'cr4zy gaming', 'cr4zy esports']
optic = ['OpTic Gaming', 'optic esports', 'optic']
ghost = ['Ghost Gaming', 'ghost', 'ghost esports']
windigo = ['Windigo', 'windigo gaming', 'windigo esports']
valiance = ['Valiance', 'valiance gaming', 'valiance esports']
spirit = ['Team Spirit', 'spirit', 'team spirit esports', 'team spirit gaming']
avangar = ['AVANGAR', 'avangar gaming', 'avangar esports']
ancient = ['Ancient', 'ancient gaming', 'ancient esports']
sprout = ['Sprout', 'sprout gaming', 'sprout esports']
gamer_legion = ['GamerLegion', 'gamer legion', 'gamer legion gaming', 'gamer legion esports']
tricked = ['Tricked Esport', 'tricked esports', 'tricked', 'tricked gaming']
cloud9 = ['Cloud9', 'cloud9 Gaming', 'cloud9 esports']
complexity = ['Complexity Gaming', 'complexity', 'complexity esports']
sharks = ['Sharks', 'sharks esports', 'sharks gaming']
hellraisers = ['HellRaisers', 'hell raisers', 'hellraisers gaming', 'hellraisers esports']
aristocracy = ['Aristocracy', 'aristocracy gaming', 'aristocracy esports']
winstrike = ['Winstrike', 'winstrike gaming', 'winstrike esports']
forze = ['forZe', 'forze gaming', 'forze esports']
ldlc = ['LDLC', 'ldlc gaming', 'ldlc esports']
tylooo = ['TYLOO', 'tyloo gaming', 'tyloo esports']
threedmax = ['3DMAX', '3dmax gaming', '3dmax esports']
grayhound = ['Grayhound Gaming', 'grayhound esports', 'grayhound']
gambit = ['Gambit Esports', 'gambit', 'gambit gaming']
virtus = ['Virtus.pro', 'virtus pro', 'virtus', 'virtus gaming', 'virtus esports']
betboom = ['BetBoom', 'bet boom', 'betboom gaming', 'betboom esports']
rhyno = ['Rhyno Esports', 'rhyno', 'rhyno gaming']
natus = ['Natus Vincere', 'natus vincere gaming', 'natus vincere esports']
ninjas = ['Ninjas in Pyjamas', 'ninjas in pyjamas gaming', 'ninja in pyjamas esports']




names = [navi, astralis, vitality, liquid, ence, faze, nrg, furia, g2, north, mouz, fnatic, mibr, nip, renegades, big, heroic, cr4zy, optic, ghost, windigo, valiance, spirit, avangar, ancient, sprout, gamer_legion, tricked, cloud9, complexity, sharks, 
         hellraisers, aristocracy, winstrike, forze, ldlc, tylooo, threedmax, grayhound, gambit, virtus, betboom, rhyno, natus, ninjas]

data = [list(map(str.casefold, x)) for x in names]


# TODO Add the lower feature to LoLTeamNames and then you don't need to do the title bs. 
# Change names to more accurately represent their league names. 

def standardize_names(name):
    for i in range(len(names)):
        lower = [element.lower() for element in names[i]]
        if name.lower() in data[i]:
            #print(names[i])
            standard_name = str(names[i][0])
            print("Ah good.")
            return standard_name
    
    print("Name not found!")
    return name