# Change the API region if necessary
# Other regions: br1, eun1, euw1, jp1, kr, la1, la2, na1, oc1, tr1, ru

region = 'br1'

URL_PLAYER_DATA = f'https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/'

URL_ACTIVE_GAME = f'https://{region}.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/'

URL_MATCH_HISTORY = f'https://{region}.api.riotgames.com/lol/match/v4/matchlists/by-account/'

URL_MATCH = f'https://{region}.api.riotgames.com/lol/match/v4/matches/'
