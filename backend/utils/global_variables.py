# Other regions: br1, eun1, euw1, jp1, kr, la1, la2, na1, oc1, tr1, ru

# The AMERICAS routing value serves NA, BR, LAN, LAS, and OCE. 
# The ASIA routing value serves KR and JP.
# The EUROPE routing value serves EUNE, EUW, TR, and RU.

region = 'na1'
continent = "americas"

URL_PLAYER_DATA = f'https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/'

URL_ACTIVE_GAME = f'https://{region}.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/'

URL_MATCHHISTORY_IDS = f'https://{continent}.api.riotgames.com/lol/match/v5/matches/by-puuid/'

URL_MATCH_DATA = f'https://{continent}.api.riotgames.com/lol/match/v5/matches/'
