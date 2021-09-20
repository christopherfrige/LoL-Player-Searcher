from services.Analyzer import get_active_game_message, get_last_game_message
import time

nicknames = input("\33[1mPlayers name: ")
nicknames_list = nicknames.split(",")

timeStart = time.time()
# To search every nickname and run the function
for nickname in nicknames_list:
    nickname = nickname.strip()
    ingame = get_active_game_message(nickname)
    if not ingame:
        get_last_game_message(nickname)
    print("-"*40)

timeEnd = time.time()

print(f"\33[1mThe total time of the analysis was: {timeEnd - timeStart:.2f}s")
