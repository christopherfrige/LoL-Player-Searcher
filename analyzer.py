from time import time
from datetime import date, datetime
import requests, re, math, os


nicknames = input("\33[1mPlayers name: ")
nicknames_list = nicknames.split(",")


# Change the API region if necessary
# Other regions: br1, eun1, euw1, jp1, kr, la1, la2, na1, oc1, tr1, ru
API_KEY = '?api_key=RIOT_API_KEY_HERE' #put your API key here
URL_PLAYER_DATA = 'https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'
URL_ACTIVE_GAME = 'https://br1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/'
URL_matchhistory = "https://br1.api.riotgames.com/lol/match/v4/matchlists/by-account/"
URL_match = "https://br1.api.riotgames.com/lol/match/v4/matches/"

def get_player_data(nickname):
    idfinder = requests.get(URL_PLAYER_DATA + nickname + API_KEY)
    playerData = idfinder.json()

    return {
        "encryptedid": playerData['id'],
        "accountid": playerData['accountId']
    }

def get_active_game_data(nickname):
    playerID= get_player_data(nickname)
    # Checks if the player is in an active game, returning a status code
    activegame = requests.get(URL_ACTIVE_GAME + playerID['encryptedid'] + API_KEY)

    return {
        "response": activegame.json(), 
        "status_code": activegame.status_code
    }

def get_active_game_message(nickname):
    activeGameData = get_active_game_data(nickname)
    if activeGameData['status_code'] == 200:
        gameLength = activeGameData['response']['gameLength']
        gameLength = math.ceil(gameLength/60)
        if gameLength < 0:
            print("IN LOADING SCREEN")
        else:
            print(f"\033[1;31m{nickname} => IN GAME")
            print(f"The player has been in game for: {gameLength} minute(s)")
    else:
        print(f"\033[1;36m{nickname} => NOT PLAYING")

'''
def searcher():    
    #Match History part =====================

    matchhistory = requests.get(URL_matchhistory + accountid + API_key)#pega o timestamp da ultima partida    
    rawhistory  = matchhistory.text
    rawhistory = rawhistory.split('"')

    startGame = rawhistory[16]#pega os numeros do timestamp
    startGame = re.sub(r'\D', '', startGame)#tira os não-numéricos
    startGame = (int(startGame)/1000) #transforma em milissegundos em segundos

    gameid = rawhistory[8]#pega os numeros do gameid
    gameid = re.sub(r"\D", '', gameid)#remove os não-numéricos

    match = requests.get(URL_match + gameid + API_key)#usando o gameid que pegou acima, adquire outras informações
    rawinfomatch = match.text
    rawinfomatch = rawinfomatch.split('"')

    gameDuration = rawinfomatch[10]#pega o timestamp de duração do jogo
    gameDuration = re.sub(r"\D", "", gameDuration)#remove os não-numéricos
    #print(gameDuration)
    gameDuration = int(gameDuration)

    endGame = startGame + gameDuration #timestamp de quando finalizou o jogo
    timestampatual = time() #timestamp do momento atual

    lastmatch_seconds = timestampatual - endGame #intervalo de tempo em SEGUNDOS desde que acabou a última partida
    lastmatch_minutes = math.ceil(lastmatch_seconds/60)
    lastmatch_hours = math.ceil(lastmatch_seconds/3600)

    if lastmatch_seconds <= 900:
        print("Finished a match recently, probaly in queue.")
        print("Time since last match: ", lastmatch_minutes, " minutes")
    else:
        if lastmatch_minutes < 60:
            print("Time since last match: ", lastmatch_minutes, " minutes")
        elif lastmatch_minutes >= 60 and lastmatch_minutes <= 1440:
            print("Time since last match: ", lastmatch_hours, " hour(s)")
        else:
            print("This player is offline more than 1 day.")
'''

# To search every nickname and run the function
for nickname in nicknames_list:
    nickname = nickname.strip()
    get_active_game_message(nickname)
    print("-"*40)
