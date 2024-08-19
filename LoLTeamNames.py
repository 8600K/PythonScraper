import pandas as pd

# FIRST ENTRY SHOULD ALWAYS BE THE STANDARD NAME. 


#    --------------------------------------------------------------------------------------------------
# EU --------------------------------------------------------------------------------------------------
#    --------------------------------------------------------------------------------------------------

# LFL --------------------------------------------------------------------------------------------------
aegis = ['AEGIS', 'team aegis', 'aegis esports']
bk_rog_esports = ['BK ROG Esports', 'bkrog', 'bkrog esports', 'bk rog']
gameward = ['GameWard', 'game ward', 'gameward esports']
gentle_mates = ['Gentle Mates', 'gentlemates', 'gentle mates esports']
karmine_corp_blue = ['Karmine Corp Blue', 'karmine corp blue esports', 'karmine corp academy']
solary = ['Solary', 'solary esports', 'team solary']
team_bds_academy = ['Team BDS Academy', 'team bds academy esports', 'bds academy', 'bds acad', 'team bds acad']
team_du_sud = ['Team du Sud', 'du sud', 'team du sud esports']
team_go = ['Team GO', 'GO', 'GO Esports']
vitality_bee = ['Vitality.Bee', 'vitality bee', 'team vitality bee']
# Prime League ----------------------------------------------------------------------------------------
austrian_force = ['Austrian Force', 'austrian force esports', 'austrian force willhaben']
big = ['BIG', 'big esports']
e_wie_einfach = ['E WIE EINFACH', 'e wie einfach esports']
orbit_anonymo_esports = ['Orbit Anonymo Esports', 'orbit anonymo', 'orbit anonymo gaming']
eintracht_frankfurt = ['Eintracht Frankfurt', 'eintracht frankfurt esports']
eintracht_spandau = ['Eintracht Spandau', 'eintracht spandau esports']
fc_schalke_04 = ['FC Schalke 04', 'fc schalke 04 esports', 'fc schalke esports', 'fc schalke', 'schalke 04', 'schalke 04 esports']
mouz_nxt = ['MOUZ NXT', 'mouz gaming', 'mouz esports', 'mouz']
nno_prime = ['NNO Prime', 'nno prime esports']
sk_gaming_prime = ['SK Gaming Prime', 'sk gaming prime esports', 'sk prime']
unicorns_of_love_se = ['Unicorns of Love SE', 'unicorns of love sexy edition', 'uol sexy edition']
# LEC -------------------------------------------------------------------------------------------------
fnatic = ['Fnatic', 'fnatic esports']
g2_esports = ['G2 Esports', 'g2']
giantx = ['GIANTX', 'giantx esports']
karmine_corp = ['Karmine Corp', 'karmine corp esports']
mad_lions_koi = ['MAD Lions KOI', 'mad lions koi esports', 'mad lions']
rogue = ['Rogue', 'rogue esports']
sk_gaming = ['SK Gaming', 'sk gaming esports', 'sk']
team_bds = ['Team BDS', 'team bds esports', 'bds', 'bds esports', 'bds esport']
team_heretics = ['Team Heretics', 'team heretics esports', 'heretics']
team_vitality = ['Team Vitality', 'vitality', 'vitality gaming']
# LVP -------------------------------------------------------------------------------------------------
barca_esports = ['Barca Esports', 'barca', 'barca gaming'] # CHECK THIS ONE. SPECIAL CHARACTER DETECTED. 
case_esports = ['Case Esports', 'case', 'case gaming']
giantx_pride = ['GIANTX Pride', 'giantx pride gaming', 'giantx pride esports', 'giantx acad', 'giantx academy', 'giantx acad.']
guasones_team = ['Guasones Team', 'guasones esports', 'guasones']
los_heretics = ['Los Heretics', 'los heretics esports', 'los heretics esports', 'heretics academy', 'team heretics academy', 'heretics acad.', 'heretics acad']
movistar_koi = ['Movistar KOI', 'movistar koi esports', 'movister koi']
movistar_riders = ['Movistar Riders']
rebels_gaming = ['Rebels Gaming', 'rebels gaming esports', 'rebels']
ucam_esports_club = ['UCAM Esports Club', 'ucam', 'ucam tokiers']
zeta = ['ZETA', 'zeta gaming', 'zeta esports']
ramboot_club = ['Ramboot Club', 'ramboot', 'ramboot esports', 'ramboot']
lua_gaming = ['Lua Gaming', 'lua esports', 'lua']
# Ultraliga -------------------------------------------------------------------------------------------
anonymo_esports = ['Anonymo Esports', 'Anonymo']
exeed = ['Exeed', 'exeed gaming', 'exeed esports']
forsaken = ['Forsaken', 'forsaken esports', 'forsaken gaming']
grypciocraft = ['Grypciocraft', 'grypciocraft esports', 'grypciocraft gaming']
iron_wolves = ['Iron Wolves', 'iron wolves esports', 'iron wolves gaming']
team_esca_gaming = ['Team ESCA Gaming', 'team esca', 'team esca gaming esports', 'esca gaming', 'esca']
zero_tenacity = ['Zero Tenacity', 'zero tenacity gaming']
# TCL -------------------------------------------------------------------------------------------------
besiktas_esports = ['Besiktas Esports', 'besiktas'] # ANOTHER SPECIAL CHARACTER HERE
boostgate_esports = ['Boostgate Esports', 'boostgate', 'boostgate gaming']
dark_passage = ['Dark Passage', 'dark passage gaming', 'dark passage esports']
fut_esports = ['FUT Esports', 'fut gaming', 'fut']
galakticos = ['Galakticos', 'galakticos gaming', 'galakticos esports']
misa_esports = ['Misa Esports', 'misa', 'misa gaming']
nasr_esports = ['NASR Esports', 'nasr gaming', 'nasr']
papara_supermassive = ['Papara SuperMassive', 'papara super massive', 'papara super massive gaming', 'papara super massive esports', 'supermassive esports', 'papara sm', 'super massive']
# EBL -------------------------------------------------------------------------------------------------
ankora_gaming = ['Ankora Gaming', 'ankora', 'ankora esports']
befive_esports = ['BeFive Esports', 'be five esports', 'befive']
crvena_zvezda = ['Crvena zvezda', 'crvena zvezda esports', 'crvena zvezda gaming']
cyber_wolves = ['Cyber Wolves', 'cyber wolves gaming', 'cyber wolves esports']
diamant_esports = ['Diamant Esports', 'diamant', 'diamant gaming']
lupus_esports = ['Lupus Esports', 'lupus gaming', 'lupus']
magaza_esports = ['MAGAZA Esports', 'magaza gaming', 'magaza']
partizan_esports = ['Partizan Esports', 'partizan gaming', 'partizan']
spike_syndicate = ['SPIKE Syndicate', 'spike syndicate gaming', 'spike']
# Elite Series ----------------------------------------------------------------------------------------
aoma_esports = ['AOMA Esports', 'aoma gaming', 'aoma', 'a one man army']
dynasty = ['Dynasty', 'dynasty gaming', 'dynasty esports']
mcon_esports = ['mCon Esports', 'mcon gaming', 'mcon']
nothern_lions = ['Nothern Lions', 'nothern lions gaming', 'nothern lions esports']
once_upon_a_team = ['Once Upon A Team', 'once upon a team gaming', 'once upon a team esports']
snooze_esports = ['SNOOZE Esports', 'snooze', 'snooze gaming']
zennit = ['ZennIT', 'zennit gaming', 'zennit esports']
krc_genk_esports = ['KRC Genk Esports', 'krc genk']
# Hitpoint Masters ------------------------------------------------------------------------------------
brute = ['BRUTE', 'brute gaming', 'brute esports']
dynamo_eclot = ['Dynamo Eclot', 'dynamo eclot gaming', 'dynamo eclot esports']
entropiq = ['Entropiq', 'entropiq gaming', 'entropiq esports']
esuba = ['eSuba', 'esuba gaming', 'esuba esports']
europe_saviors_club = ['Europe Saviors Club', 'europe saviors club gaming', 'europe saviors club esports']
glore = ['GLORE', 'glore esports', 'glore gaming']
sk_sigma_olomouc = ['SK Sigma Olomouc', 'sk sigma olomouc esports', 'sk sigma olomouc gaming', 'ogc sigma']
team_unity = ['Team UNiTY', 'unity', 'team unity gaming', 'team unity esports']
# GLL -------------------------------------------------------------------------------------------------
anorthosis_esports = ['Anorthosis Esports', 'anorthosis gaming', 'anorthosis', 'gamespace mediterranean college esports']
gamespace_mce = ['Gamespace MCE', 'gamespace mce esports', 'gamespace mce gaming', 'gamespace']
team_mythic = ['Team Mythic', 'team mythic esports', 'team mythic gaming', 'mythic']
team_phantasma = ['Team Phantasma', 'team phantasma esports', 'team phantasma gaming']
team_refuse = ['Team Refuse', 'team refuse gaming', 'team refuse esports', 'refuse']
wild_panthers_esports = ['Wild Panthers Esports', 'wild panthers', 'wild panthers gaming']
wl_gaming_esports = ['WLGaming Esports', 'wlgaming', 'wl gaming esports']
zerolag_esports = ['Zerolag Esports', 'zerolag gaming', 'zerolag', 'hell zerolag']
# LIT -------------------------------------------------------------------------------------------------
atleta_esports = ['Atleta Esport', 'atleta esports', 'atleta gaming', 'atleta']
axolotl = ['Axolotl', 'axolotl gaming', 'axolotl esports']
dren_esports = ['DREN Esports', 'dren gaming', 'dren']
dsyre = ['Dsyre', 'dsyre gaming', 'dsyre esports']
eko_academy = ['EKO Academy', 'eko academy esports', 'eko academy gaming']
enemi3s = ['ENEMI3S', 'enemi3s gaming', 'enemi3s esports']
macko_esports = ['Macko Esports', 'macko gaming', 'macko']
outplayed = ['Outplayed', 'outplayed gaming', 'outplayed esports', 'anc outplayed']
# LPLOL ------------------------------------------------------------------------------------------------
boavista_fc = ['Boavista FC', 'boavista fc gaming', 'boavista fc esports']
byteway_esports = ['Byteway Esports', 'byteway gaming', 'byteway']
egn_esports = ['EGN Esports', 'egn gaming', 'egn']
grow_up_esports = ['Grow uP Esports', 'grow up gaming', 'grow up']
gtz_esports = ['GTZ Esports', 'gtz gaming', 'gtz']
hurricane_of_feathers = ['Hurricane Of Feathers', 'hurricane of feathers esports', 'hurricane of feathers gaming']
keypulse_esports = ['Keypulse Esports', 'keypulse', 'keypulse gaming']
odivelas_sports_club = ['Odivelas Sports Club', 'odivelas sports club esports', 'odivelas esports club', 'odivelas sports club gaming']
saw = ['SAW', 'saw esports', 'saw gaming']
white_dragons = ['White Dragons', 'white dragons esports', 'white dragons gaming']
# NLC --------------------------------------------------------------------------------------------------
dmg_esports = ['DMG Esports', 'dmg gaming']
lionscreed = ['Lionscreed', 'lionscreed gaming', 'lions creed', 'lionscreed esports']
lundqvist_lightside = ['Lundqvist Lightside', 'lundqvist lightside gaming', 'lundqvist lightside esports']
nativz = ['Nativz', 'nativz esports', 'nativz gaming']
nord_esports = ['NORD Esports', 'nord gaming', 'nord']
ruddy_esports = ['Ruddy Esports', 'ruddy']
vanir = ['Vanir', 'vanir esports']
venomcrest_esports = ['Venomcrest Esports', 'venomcrest']
verdant = ['Verdant', 'verdant esports', 'verdant gaming']

# UNITED ARAB EMIRATES --------------------------------------------------------------------------------
nigma_galaxy = ['Nigma Galaxy', 'nigma galaxy esports']
mystic_gaming = ['Mystic Gaming', 'mystic', 'mystic esports']
lost_esports = ['Lost Esports', 'lost', 'lost gaming']
geekay_esports = ['Geekay Esports', 'geekay', 'geekay gaming']
fox_gaming = ['Fox Gaming', 'fox']
anubis_gaming = ['Anubis Gaming', 'anubis', 'anubis esports']
gng_amazigh = ['GnG Amazigh', 'gng esports']
raad= ['RA\'AD', 'team ra\'ad']
twisted_minds = ['Twisted Minds']
one_more_esports = ['One More Esports', 'one more']

#    --------------------------------------------------------------------------------------------------
# Brazil ----------------------------------------------------------------------------------------------
#    --------------------------------------------------------------------------------------------------

# CBLOL -----------------------------------------------------------------------------------------------
fluxo = ['Fluxo', 'fluxo gaming', 'fluxo esports']
intz = ['INTZ', 'intz gaming' 'intz esports', 'intz e-sports']
keyd_stars = ['Keyd Stars', 'keyd stars gaming', 'keyd stars esports', 'vivo keyd stars']
los = ['LOS', 'los grandes', 'los grandes esports', 'flamengo los grandes']
pain_gaming = ['paiN Gaming', 'pain esports', 'pain']
furia_esports = ['FURIA Esports', 'furia gaming', 'furia']
kabum_esports = ['KaBum! Esports', 'kabum!', 'kabum esports', 'kabum! gaming', 'kabum gaming', 'kabum', 'kabum! e-sports']
liberty = ['Liberty', 'liberty gaming', 'liberty esports']
loud = ['LOUD', 'loud esports', 'loud gaming']
red_canids = ['RED Canids', 'red canids esports', 'red canids gaming']
# Academy Teams ---------------------------------------------------------------------------------------
flamengo_academy = ['Flamengo Academy', 'flamengo academy esports', 'flamengo academy gaming', 'flamengo acad']
furia_academy = ['Furia Academy', 'furia academy esports', 'furia academy gaming', 'furia acad']
kabum_academy = ['KaBuM! Academy', 'kabum! academy gaming', 'kabum academy', 'kabum! academy esports', 'kabum acad']
liberty_academy = ['Liberty Academy', 'liberty academy gaming', 'liberty academy esports', 'liberty acad']
loud_academy = ['LOUD Academy', 'loud academy esports', 'loud academy gaming', 'loud acad']
red_academy = ['RED Academy', 'red academy esports', 'red academy gaming', 'red acad']
fluxo_academy = ['Fluxo Academy', 'fluxo academy esports', 'fluxo academy gaming', 'fluxo acad']
intz_academy = ['INTZ Academy', 'intz academy gaming', 'intz academy esports', 'intz acad']
keyd_academy = ['Keyd Academy', 'keyd academy esports', 'keyd academy gaming', 'vivo keyd stars acad', 'vivo keyd stars academy']
los_academy = ['LOS Academy', 'los academy esports', 'los academy gaming', 'los acad', 'los grandes academy']
pain_gaming_academy = ['paiN Gaming Academy', 'pain academy', 'pain gaming academy esports', 'pain acad']
tropa_xv = ['Tropa XV', 'tropa xv esports', 'tropa gaming', 'tropa raizen']
# Other Teams -----------------------------------------------------------------------------------------
coven_bats = ['Coven Bats', 'coven bats gaming', 'coven bats esports']
miners_gg_female = ['Miners.gg Female', 'miners female', 'miners.gg female esports']
raizen = ['Raizen', 'raizen esports', 'raizen gaming']
mibr = ['MIBR', 'mibr esports', 'mibr gaming']
pain_gaming_female = ['paiN Gaming Female', 'pain gaming female esports', 'pain female']
rise_gaming = ['Rise Gaming', 'Rise Esports', 'Rise']
#    --------------------------------------------------------------------------------------------------
# China -----------------------------------------------------------------------------------------------
#    --------------------------------------------------------------------------------------------------

# LPL -------------------------------------------------------------------------------------------------
anyones_legend = ['Anyone\'s Legend', 'anyones legend', 'anyone\'s legend esports']
edward_gaming = ['EDward Gaming', 'edward', 'edward esports']
invictus_gaming = ['Invictus Gaming', 'invictus', 'invictus esports']
lgd_gaming = ['LGD Gaming', 'lgd', 'lgd esports']
lng_esports_academy = ['LNG Esports Academy', 'lng esports academy', 'lng academy', 'lng gaming academy', 'lng acad']
o_m_g = ['Oh My God', 'omg', 'omg gaming']
o_m_g_a = ['Oh My God Academy', 'oh my god.a', 'omg academy']
royal_never_give_up = ['Royal Never Give Up', 'royal never give up gaming', 'rng']
thundertalk_gaming = ['ThunderTalk Gaming', 'thunder talk gaming', 'thundertalk', 'thundertalk esports', 'tt gaming']
ultra_prime = ['Ultra Prime', 'ultra prime esports', 'ultra prime gaming']
bilibili_gaming = ['Bilibili Gaming', 'bilibili', 'bilibili esports']
funplus_phoenix = ['FunPlus Phoenix', 'funplus phoenix esports', 'funplus phoenix gaming']
jd_gaming = ['JD Gaming', 'jd esports', 'jd']
lng = ['LNG Esports', 'lng gaming', 'lng esports gaming', 'lng']
ninjas_in_pyjamas = ['Ninjas in Pyjamas', 'ninjas in pyjamas esports']
rare_atom = ['Rare Atom', 'rare atom esports']
team_we = ['Team WE', 'team we esports', 'we esports', 'we']
top_esports = ['Top Esports', 'top gaming', 'top']
weibo_gaming = ['Weibo Gaming', 'weibo', 'weibo gaming esports']
# LDL -------------------------------------------------------------------------------------------------
anyones_legend_young = ['Anyone\'s Legend Young', 'anyone\'s legend young esports', 'anyone\'s young', 'anyones legend young', 'anyones legend.young']
edg_youth_team = ['EDG Youth Team', 'edg youth team esports', 'edg youth esports', 'edg youth gaming', 'edg youth', 'edward gaming youth', 'edgy']
invictus_gaming_young = ['Invictus Gaming Young', 'invictus gaming youth', 'invictus young']
lgd_gaming_youth_team = ['LGD Gaming Youth Team', 'lgd gaming youth', 'lgd gaming youth esports', 'lgd.y', 'lgd young']
miaojing = ['MiaoJing', 'miaojing esports', 'miao jing']
ji_jie_hao = ['Ji Jie Hao', 'ji jie hao gaming', 'ji jie hao esports', 'jijiehao']
suning_s = ['Suning-S', 'suning', 'suning-s esports']
top_esports_challenger = ['Top Esports Challenger', 'top esports challenger gaming', 'tes challenger', 'top esports chall']
v5_87 = ['V5 87', 'v587', 'v5 87 esports', 'v587 gaming']
bilibili_gaming_junior = ['Bilibili Gaming Junior', 'bilibili gaming junior esports', 'bilibili junior']
funplus_phoenix_blaze = ['FunPlus Phoenix Blaze', 'fun plus phoenix blaze', 'funplus phoenix blaze esports']
joy_dream = ['Joy Dream', 'joy dream esports', 'joy dream gaming']
max_gaming = ['MAX', 'max gaming', 'max esports', 'max e-sports club', 'max e-sports']
rare_atom_period = ['Rare Atom Period', 'rare atom period esports', 'rare atom period gaming']
team_we_academy = ['Team WE Academy', 'team we academy esports', 'we academy', 'team we acad']
ultra_prime_academy = ['Ultra Prime Academy', 'ultra prime academy esports', 'ultra prime academy gaming', 'ultra prime acad', 'up academy']
weibo_gaming_youth_team = ['Weibo Gaming Youth Team', 'weibo gaming youth', 'weibo youth', 'weibo youth esports']
thundertalk_gaming_young = ['ThunderTalk Gaming Young', 'thundertalk young']
royal_club = ['Royal Club', 'team royal club', 'royal club esports']
#    --------------------------------------------------------------------------------------------------
# Japan -----------------------------------------------------------------------------------------------
#    --------------------------------------------------------------------------------------------------

# LJL -------------------------------------------------------------------------------------------------
axiz_crest = ['AXIZ CREST', 'axiz crest gaming', 'axiz crest esports']
detonation_focusme = ['DetonatioN FocusMe', 'detonation focus me', 'detonation fm']
sengoku_gaming = ['Sengoku Gaming', 'sengoku gaming esports']
burning_core_toyama = ['Burning Core Toyama', 'burning core toyama esports']
fukuoka_softbank_hawks = ['Fukuoka SoftBank HAWKS', 'fukuoka soft bank hawks', 'fukuoka softbank hawks gaming']
v3_esports = ['V3 Esports', 'v3 gaming', 'v3']
# LJL Academy -----------------------------------------------------------------------------------------
burning_core_toyama_academy = ['Burning Core Toyama Academy', 'burning core toyama academy esports']
fukuoka_hawks_academy = ['Fukuoka_hawks_academy', 'fukuoka_academy']
v3_esports_academy = ['V3 Esports Academy', 'v3 Academy']
detonation_academy = ['DetonatioN Academy', 'detonation youth', 'detonation academy esports']
sengoku_academy = ['Sengoku Academy', 'sengoku gaming academy', 'sengoku academy esports']
#    --------------------------------------------------------------------------------------------------
# Korea -----------------------------------------------------------------------------------------------
#    --------------------------------------------------------------------------------------------------

# LCK -------------------------------------------------------------------------------------------------
brion = ['BRION', 'brion gaming', 'brion esports']
drx = ['DRX', 'drx gaming', 'drx esports']
freecs = ['Freecs', 'freecs gaming', 'freecs esports', 'kwangdong freecs']
hanwha_life_esports = ['Hanwha Life Esports', 'hanwha life', 'hanwha life gaming', 'hle']
nongshim_redforce = ['Nongshim RedForce', 'nongshim redforce esports', 'nongshim redforce gaming', 'ns redforce']
dplus = ['Dplus', 'dplus gaming', 'dplus esports', 'dplus kia']
fear_x = ['FearX', 'fear x', 'fearx esports', 'fearx gaming']
gen_g_esports = ['Gen.G Esports', 'gen g', 'gen.g']
kt_rolster = ['KT Rolster', 'kt rolster esports', 'kt rolster gaming']
t1 = ['T1', 't1 gaming', 't1 esports', 't 1']
# LCK Challengers -------------------------------------------------------------------------------------
brion_challengers = ['Brion Challengers', 'brion challengers esports', 'brion challengers gaming', 'oksavingsbank brion challengers', 'oksavingsbank brion']
drx_challengers = ['DRX Challengers', 'drx challengers gaming', 'drx challengers esports']
freecs_challengers = ['Freecs Challengers', 'freecs challengers gaming', 'freecs challengers esports', 'kwangdong freecs chall', 'kwangdong freecs challengers']
hanwha_life_esports_challengers = ['HLE Challengers', 'hanwha life esports challengers', 'hanwha life challengers', 'hanwha life chall', 'hanwha life esports challenger']
nongshim_esports_academy = ['Nongshim Esports Academy', 'ns esports academy' 'ns esports academy gaming', 'nongshim redforce acad', 'nongshim redforce academy', 'nongshim rf challengers']
dplus_challengers = ['Dplus Challengers', 'dplus esports challengers', 'dplus challengers gaming', 'dplus kia chall', 'dplus kia challengers', 'dwg kia challengers']
fearx_youth = ['FearX Youth', 'fearx challengers', 'fearx youth esports', 'fearx youth challengers']
gen_g_global_academy = ['Gen.G Global Academy', 'gen.g global', 'gen.g challengers']
kt_rolster_challengers = ['KT Rolster Challengers', 'kt rolster challengers esports', 'kt rolster chall']
t1_esports_academy = ['T1 Esports Academy', 't1 challengers', 't1 esports challengers', 't1 acad']
# LCK Academy -----------------------------------------------------------------------------------------
brion_academy = ['Brion Academy', 'brion esports academy']
drx_academy = ['DRX Academy', 'drx esports academy']
gen_g_academy = ['Gen.G Academy', 'gen.g esports academy']
kt_rolster_academy = ['KT Rolster Academy', 'kt rolster esports academy']
fearx_academy = ['FearX Academy', 'fear x academy', 'fearx esports academy']
dplus_academy = ['Dplus Academy', 'dplus academy esports', 'dplus gaming academy']
freecs_academy = ['Freecs Academy', 'freecs esports academy']
hanwha_life_academy = ['Hanwha Life Academy', 'hle academy', 'hanwha life esports academy']
nongshim_academy = ['Nongshim Academy'] # This one might be tricky. This team has nongshim academy and nongshim esports academy. Like bruh.
t1_academy = ['T1 Academy', 't1 acad'] # Same here. 
#    --------------------------------------------------------------------------------------------------
# Latin America ---------------------------------------------------------------------------------------
#    --------------------------------------------------------------------------------------------------

# LLA -------------------------------------------------------------------------------------------------
all_knights = ['All Knights', 'all knights esports', 'all knight']
infinity = ['Infinity', 'infinity gaming', 'infinity esports']
leviatan = ['Leviatan', 'leviatan gaming', 'leviatan esports'] # Special character
six_karma = ['Six Karma', 'six karma esports', 'six karma gaming']
estral_esports = ['Estral Esports', 'estral', 'estral gaming', 'estral e-sports']
isurus = ['Isurus', 'isurus gaming', 'isurus esports']
rainbow7 = ['Rainbow7', 'rainbow 7', 'rainbow7 esports', 'movistar r7'] # Might change this to movistar r7. 
# Regional Teams --------------------------------------------------------------------------------------
barcelona_bg = ['Barcelona BG', 'barcelona bg esports']
ebro = ['EBRO', 'ebro esports', 'ebro gaming']
fuego = ['Fuego', 'fuego gaming', 'fuego esports']
incubus = ['Incubus', 'incubus esports', 'incubus gaming']
meta_gaming = ['Meta Gaming', 'meta', 'meta esports']
pirates_idv = ['Pirates IDV', 'pirate dream', 'pirate dream esports', 'pirate dream gaming']
dsc3v = ['DSC3V', 'dsc3v esports']
undead_gaming = ['Undead Gaming', 'undead gaming esports', 'undead']
wap_esports = ['WAP Esports', 'wap', 'wap gaming']
descuydado_aucas = ['Descuydado Aucas', 'descuydado aucas esports', 'descuydado aucas gaming']
eclipse_gaming = ['Eclipse Gaming', 'eclipse esports', 'eclipse']
furious_gaming = ['Furious Gaming', 'furious', 'furious esports']
janus_panter = ['Janus Panter', 'janus esports', 'janus', 'janus gaming', 'panter esports']
newstar = ['Newstar', 'newstar esports', 'newstar gaming']
primate = ['PRIMATE', 'primate gaming', 'primate esports']
waia_snikt = ['waia snikt', 'waia snikt gaming', 'waia snikt esports']
malvinas_gaming = ['Malvinas Gaming', 'malvinas', 'malvinas rise', 'malvinas esports']
tomorrow_esports = ['Tomorrow Esports', 'tomorrow', 'tomorrow gaming']
peek_esports = ['PÊEK Gaming', 'pÊek', 'pÊek gaming']
osaka = ['Osaka', 'osaka esports', 'osaka gaming']
#    --------------------------------------------------------------------------------------------------
# North America  --------------------------------------------------------------------------------------
#    --------------------------------------------------------------------------------------------------

# LCS -------------------------------------------------------------------------------------------------
hundred_thieves = ['100 Thieves', '100 thieves gaming', '100 thieves esports']
dignitas = ['dignitas', 'dignitas gaming']
immortals = ['immortals', 'immortals gaming', 'immortals esports', 'immortals progressive']
shopify_rebellion = ['Shopify Rebellion', 'shopify rebellion esports', 'shopify rebellion gaming']
cloud9 = ['Cloud9', 'cloud9 gaming', 'cloud 9']
flyquest = ['Flyquest', 'fly quest', 'fly quest gaming']
nrg = ['NRG', 'nrg esports', 'nrg gaming']
team_liquid = ['Team Liquid', 'team liquid gaming', 'liquid', 'liquid esports']
# North American Challengers League -------------------------------------------------------------------
aoe_esports = ['AOE Esports', 'aoe', 'aoe gaming', 'area of effect', 'aoe gold']
disguised = ['Disguised', 'disguised gaming', 'disguised esports']
lit_esports = ['LiT Esports', 'lit', 'lit gaming']
mirage_alliance = ['Mirage Alliance', 'mirage alliance esports', 'mirage alliance gaming']
liquid_challengers = ['Liquid Challengers', 'liquid challengers esports', 'liquid chall', 'team liquid academy']
cincinnati_fear = ['Cincinnati Fear', 'cincinnati fear esports', 'cincinnati fear gaming']
flyquest_challengers = ['FlyQuest Challengers', 'flyquest challengers esports', 'flyquest chall', 'flyquest academy']
maryville_university = ['Maryville University', 'maryville university gaming', 'maryville university esports']
supernova = ['Supernova', 'supernova esports', 'supernova gaming']
wildcard_gaming = ['Wildcard Gaming', 'wildcard esports', 'wildcard']

# Collegiate Teams ------------------------------------------------------------------------------------
bethany_esports = ['Bethany Esports', 'bethany esports gaming', 'bethany gaming', 'bethany college']
fisher_college = ['Fisher College', 'fisher college esports', 'fisher college gaming']
harrisburg_university = ['Harrisburg University', 'harrisburg college', 'harrisburg']
saint_louis_university = ['Saint Louis University', 'saint louis college']
uc_irvine = ['UC Irvine', 'uc irvine gaming', 'uc irvine esports']
university_of_st_thomas = ['University of St. Thomas', 'uni of st. thomas', 'university of saint thomas']
converse_university = ['Converse University', 'converse college', 'university of converse']
grand_view_university = ['Grand View University', 'grand view college', 'university of grand view']
illinois_state_university = ['Illinois State University', 'illinois state', 'illinois state college']
st_clair_college = ['St. Clair College', 'st. clair university', 'saint clair college', 'st clair college']
university_of_mississippi = ['University of Mississippi', 'uni of mississippi', 'mississippi college']
winthrop_university = ['Winthrop University', 'winthrop college', 'winthrop university esports']
# Other Teams -----------------------------------------------------------------------------------------
black_rock_esports = ['Black Rock Esports', 'black rock', 'black rock gaming']
gentle_hearts_gaming = ['Gentle Hearts Gaming', 'gentle hearts', 'gentle hearts esports']
team_fish_taco = ['Team Fish Taco', 'fish taco', 'team fish taco esports']
ccg_esports = ['CCG Esports', 'ccg', 'ccg gaming']
lotus = ['Lotus', 'lotus esports', 'lotus gaming']
#    --------------------------------------------------------------------------------------------------
# Pacific  --------------------------------------------------------------------------------------------
#    --------------------------------------------------------------------------------------------------

# PCS -------------------------------------------------------------------------------------------------
beyond_gaming = ['Beyond Gaming', 'beyond', 'beyond esports']
deep_cross_gaming = ['Deep Cross Gaming', 'deep cross', 'deep cross esports']
frank_esports = ['Frank Esports', 'frank', 'frank gaming']
impunity = ['Impunity', 'impunity esports', 'impunity gaming']
nate_a = ['Nate.A', 'nate a', 'natea esports', 'natea gaming']
psg_talon = ['PSG Talon', 'psg talon esports', 'psg talon gaming']
ctbc_flying_oyster = ['CTBC Flying Oyster', 'Flying Oyster']
dewish_team = ['Dewish Team', 'dewish', 'dewish esports', 'dewish gaming']
hell_pigs = ['HELL PIGS', 'hell pigs esports', 'hell pigs gaming']
j_team = ['J Team', 'j team esports', 'j team gaming']
nate9527 = ['Nate9527', 'nate9527 gaming', 'nate9527 esports']
west_point_esports = ['West Point Esports', 'west point gaming', 'west point']
# PCS Academy -----------------------------------------------------------------------------------------
ctbc_flying_oyster_academy = ['CTBC Flying Oyster Academy', 'Flying Oyster Academy']
psg_talon_academy = ['PSG Talon Academy', 'psg talon esports academy', 'psg talon academy gaming']
west_point_academy = ['West Point Academy', 'west point academy esports', 'west point academy gaming']
deep_cross_academy = ['Deep Cross Academy', 'deep cross academy gaming', 'deep cross academy esports']
taipei_bravo = ['Taipei Bravo', 'taipei bravo esports', 'taipei bravo gaming']
# LCO -------------------------------------------------------------------------------------------------
antic_esports = ['Antic Esports', 'antic', 'antic gaming']
fury_global = ['FURY Global', 'fury global', 'fury esports']
ion_global_esports = ['ION Global Esports', 'ion global', 'ion global gaming']
mammoth_ec = ['MAMMOTH EC', 'mammoth', 'mammoth ec esports', 'mammoth ec gaming']
dire_wolves = ['Dire Wolves', 'dire wolves esports', 'dire wolves gaming']
ground_zero_gaming = ['Ground Zero Gaming', 'ground zero esports', 'ground zero']
kanga_esports = ['Kanga Esports', 'kanga gaming', 'kanga']
team_bliss = ['Team Bliss', 'team bliss gaming', 'team bliss esports']
# LCO Academy -----------------------------------------------------------------------------------------
kanga_academy = ['Kanga Academy', 'kanga academy esports', 'kanga esports academy']
team_bliss_academy = ['Team Bliss Academy', 'bliss academy']
#    --------------------------------------------------------------------------------------------------
# Vietnam  --------------------------------------------------------------------------------------------
#    --------------------------------------------------------------------------------------------------

# VCS -------------------------------------------------------------------------------------------------
cerberus_esports = ['CERBERUS Esports', 'cerberus', 'cerberus gaming']
mgn_blue_esports = ['MGN Blue Esports', 'mgn blue', 'mgn blue gaming']
team_flash = ['Team Flash', 'flash', 'team flash esports', 'team flash gaming']
team_whales = ['Team Whales', 'whales', 'team whales esports', 'team whales gaming']
gam_esports = ['GAM Esports', 'gam', 'gam gaming']
rainbow_warriors = ['Rainbow Warriors', 'rainbow warriors esports', 'rainbow warriors gaming']
team_secret = ['Team Secret', 'secret', 'team secret esports', 'team secret gaming']
vikings_esports = ['Vikings Esports', 'vikings gaming', 'team vikings', 'vikings']



# Needs catagozing
# OTHERS ----------------------------------------------------------------------------------------------
evil_geniuses = ['Evil Geniuses', 'evil geniuses gaming', 'evil geniuses lg']
tsm = ['TSM', 'tsm esports', 'tsm esports']

golden_guardians = ['Golden Guardians', 'golden guardians gaming']













names = [fluxo, intz, keyd_stars, los, pain_gaming, furia_esports, kabum_esports, liberty, loud, red_canids, 
         flamengo_academy, furia_academy, kabum_academy, liberty_academy, loud_academy, red_academy, fluxo_academy, intz_academy, keyd_academy, los_academy, pain_gaming_academy, tropa_xv,
         coven_bats, miners_gg_female, raizen, mibr, pain_gaming_female, rise_gaming,
         anyones_legend, edward_gaming, invictus_gaming, lgd_gaming, lng_esports_academy, o_m_g, o_m_g_a, royal_never_give_up, thundertalk_gaming, royal_club, ultra_prime, bilibili_gaming, funplus_phoenix, jd_gaming, lng, ninjas_in_pyjamas, rare_atom, team_we, top_esports, weibo_gaming,
         anyones_legend_young, edg_youth_team, invictus_gaming_young, lgd_gaming_youth_team, miaojing, suning_s, top_esports_challenger, v5_87, bilibili_gaming_junior, funplus_phoenix_blaze, joy_dream, max_gaming, rare_atom_period, team_we_academy, ultra_prime_academy, weibo_gaming_youth_team, thundertalk_gaming_young, ji_jie_hao,
         aegis, bk_rog_esports, gameward, gentle_mates, karmine_corp_blue, solary, team_bds_academy, team_du_sud, team_go, vitality_bee, 
         austrian_force, big, e_wie_einfach, eintracht_frankfurt, orbit_anonymo_esports, eintracht_spandau, fc_schalke_04, mouz_nxt, nno_prime, sk_gaming_prime, unicorns_of_love_se,
         fnatic, g2_esports, giantx, karmine_corp, mad_lions_koi, rogue, sk_gaming, team_bds, team_heretics, team_vitality,
         barca_esports, case_esports, giantx_pride, guasones_team, los_heretics, movistar_koi, movistar_riders, rebels_gaming, ucam_esports_club, zeta, ramboot_club, lua_gaming,
         anonymo_esports, exeed, forsaken, grypciocraft, iron_wolves, team_esca_gaming, zero_tenacity, 
         besiktas_esports, boostgate_esports, dark_passage, fut_esports, galakticos, misa_esports, nasr_esports, papara_supermassive,
         ankora_gaming, befive_esports, crvena_zvezda, cyber_wolves, diamant_esports, lupus_esports, magaza_esports, partizan_esports, spike_syndicate,
         aoma_esports, dynasty, mcon_esports, nothern_lions, once_upon_a_team, snooze_esports, zennit, krc_genk_esports,
         brute, dynamo_eclot, entropiq, esuba, europe_saviors_club, glore, sk_sigma_olomouc, team_unity,
         anorthosis_esports, gamespace_mce, team_mythic, team_phantasma, team_refuse, wild_panthers_esports, wl_gaming_esports, zerolag_esports,
         atleta_esports, axolotl, dren_esports, dsyre, eko_academy, enemi3s, macko_esports, outplayed, 
         boavista_fc, byteway_esports, egn_esports, grow_up_esports, gtz_esports, hurricane_of_feathers, keypulse_esports, odivelas_sports_club, saw, white_dragons,
         dmg_esports, lionscreed, lundqvist_lightside, nativz, nord_esports, ruddy_esports, vanir, venomcrest_esports, verdant,
         nigma_galaxy, mystic_gaming, lost_esports, geekay_esports, fox_gaming, anubis_gaming, gng_amazigh, raad, twisted_minds, one_more_esports ,
         axiz_crest, detonation_focusme, sengoku_gaming, burning_core_toyama, fukuoka_softbank_hawks, v3_esports,
         burning_core_toyama_academy, fukuoka_hawks_academy, v3_esports_academy, detonation_academy, sengoku_academy,
         brion, drx, freecs, hanwha_life_esports, nongshim_redforce, dplus, fear_x, gen_g_esports, kt_rolster, t1,
         brion_challengers, drx_challengers, freecs_challengers, hanwha_life_esports_challengers, nongshim_esports_academy, dplus_challengers, fearx_youth, gen_g_global_academy, kt_rolster_challengers, t1_esports_academy,
         brion_academy, drx_academy, gen_g_academy, kt_rolster_academy, fearx_academy, dplus_academy, freecs_academy, hanwha_life_academy, nongshim_academy, t1_academy,
         all_knights, infinity, leviatan, six_karma, estral_esports, isurus, rainbow7, 
         barcelona_bg, ebro, fuego, incubus, meta_gaming, pirates_idv, dsc3v, undead_gaming, wap_esports, descuydado_aucas, eclipse_gaming, furious_gaming, janus_panter, newstar, primate, waia_snikt, malvinas_gaming, tomorrow_esports, peek_esports, osaka,
         hundred_thieves, dignitas, immortals, shopify_rebellion, cloud9, flyquest, nrg, team_liquid, 
         aoe_esports, disguised, lit_esports, mirage_alliance, liquid_challengers, cincinnati_fear, flyquest_challengers, maryville_university, supernova, wildcard_gaming,
         bethany_esports, fisher_college, harrisburg_university, saint_louis_university, uc_irvine, university_of_st_thomas, converse_university, grand_view_university, illinois_state_university, st_clair_college, university_of_mississippi, winthrop_university,
         black_rock_esports, gentle_hearts_gaming, team_fish_taco, ccg_esports, lotus,
         beyond_gaming, deep_cross_gaming, frank_esports, impunity, nate_a, psg_talon, ctbc_flying_oyster, dewish_team, hell_pigs, j_team, nate9527, west_point_esports,
         ctbc_flying_oyster_academy, psg_talon_academy, west_point_academy, deep_cross_academy, taipei_bravo, 
         antic_esports, fury_global, ion_global_esports, mammoth_ec, dire_wolves, ground_zero_gaming, kanga_esports, team_bliss, 
         kanga_academy, team_bliss_academy,
         cerberus_esports, mgn_blue_esports, team_flash, team_whales, gam_esports, rainbow_warriors, team_secret, vikings_esports]

data = [list(map(str.casefold, x)) for x in names]

test_name = 'BLG'

testtitle = 't1 gaming'


def standardize_names(name):
    for i in range(len(names)):
        lower = [element.lower() for element in names[i]]
        if name.lower() in data[i]:
            #print(names[i])
            standard_name = str(names[i][0])
            print("Success.", standard_name)
            return standard_name
    
    print("         Name not found! ", name)
    return name





