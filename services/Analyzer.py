from time import time
import requests, math
from utils.tokens import API_KEY
from utils.GlobalVariables import URL_PLAYER_DATA, URL_ACTIVE_GAME, URL_MATCH_HISTORY, URL_MATCH

def get_player_data(nickname):
    idfinder = requests.get(URL_PLAYER_DATA + nickname + API_KEY)
    playerData = idfinder.json()

    return {
        "encryptedid": playerData['id'],
        "accountid": playerData['accountId']
    }

def get_active_game_data(nickname):
    playerID = get_player_data(nickname)
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
        return True
    else:
        print(f"\033[1;36m{nickname} => NOT PLAYING")

def get_last_game_id(nickname):
    playerData = get_player_data(nickname)
    matchHistory = requests.get(URL_MATCH_HISTORY + playerData['accountid'] + API_KEY)
    matchHistoryData = matchHistory.json()
    
    return matchHistoryData['matches'][0]['gameId']

def get_game_data(nickname):
    gameID = get_last_game_id(nickname)
    game = requests.get(URL_MATCH + str(gameID) + API_KEY)

    return game.json()

def get_time_since_last_game(nickname):
    gameData = get_game_data(nickname)

    timeStartGame = gameData['gameCreation']
    gameDuration = gameData['gameDuration']

    timeEndGame = (timeStartGame + gameDuration)/1000
    nowTime = time()

    timeGap = nowTime - timeEndGame

    return {
        "inSeconds": timeGap,
        "inMinutes": round(timeGap/60),
        "inHours": round(timeGap/3600),
        "inDays": round(timeGap/86400)        
    }

def get_last_game_message(nickname):
    timeLastGame = get_time_since_last_game(nickname)

    if timeLastGame['inSeconds'] <= 900:
        print(f"Finished a match recently, probaly in queue.")
        print(f"Time since last match: {timeLastGame['inMinutes']} minutes")
    elif timeLastGame['inMinutes'] < 60:
        print(f"Time since last match: {timeLastGame['inMinutes']} minutes")
    elif timeLastGame['inMinutes'] >= 60 and timeLastGame['inMinutes'] <= 1440:
        print(f"Time since last match:  {timeLastGame['inHours']} hour(s)")
    else:
        print(f"This player is offline more than {timeLastGame['inDays']} day(s).")

