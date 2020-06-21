from time import time
from datetime import date, datetime
import requests, re, math, os

clear = lambda: os.system('cls')
clear()

nicknames = input("\33[1mPlayers name: ")
nicknames_split = nicknames.split(",")
numbernicks = int(len(nicknames_split))

#change the API region if necessary
API_key = '?api_key=xxxx' #put your API key here
URL_nickfront = 'https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'
URL_activegame = 'https://br1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/'
URL_matchhistory = "https://br1.api.riotgames.com/lol/match/v4/matchlists/by-account/"
URL_match = "https://br1.api.riotgames.com/lol/match/v4/matches/"

def searcher():
    idfinder = requests.get(URL_nickfront + soloNick + API_key)
    information = idfinder.text
    dataplayer = information.split('"')    
    #pega o id no json
    encryptedid = dataplayer[3]
    #pega o accountid (para matchhistory)
    accountid = dataplayer[7]    

    #checa se está em jogo, repassando determinado codigo
    activegame = requests.get(URL_activegame + encryptedid + API_key)
    activegame_code = activegame.status_code
    #200 == ingame
    #404 == offline

    if activegame_code == 200:
        print(f"\033[1;31m{soloNick} => IN GAME")
        rawactivegame = activegame.text
        rawactivegame = rawactivegame.split('"')

        gameLength = rawactivegame[392]#posição do gameLength na lista do json da riot
        gameLength = re.sub(r'\D', '', gameLength)
        gameLength = math.ceil(int(gameLength)/60)

        print(f"The player has been in game for: {gameLength} minute(s)")
        return

    else:
        print(f"\033[1;36m{soloNick} => NOT PLAYING")

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

    lastmatch = timestampatual - endGame #intervalo de tempo em SEGUNDOS desde que acabou a última partida
    lastmatch_minutes = math.ceil(lastmatch/60)
    lastmatch_hours = math.ceil(lastmatch/3600)

    if lastmatch <= 900:
        print("Finished a match recently, probaly in queue.")
        print("Time since last match: ", lastmatch_minutes, " minutes")
    else:
        if lastmatch_minutes < 60:
            print("Time since last match: ", lastmatch_minutes, " minutes")
        elif lastmatch_minutes >= 60 and lastmatch_minutes <= 1440:
            print("Time since last match: ", lastmatch_hours, " hour(s)")
        else:
            print("This player is offline more than 1 day.")

#para pesquisar cada nick digitado e executar a função
for c in range(0, numbernicks):
    soloNick = nicknames_split[c]
    soloNick = soloNick.strip()
    searcher()
    print("-"*40)
