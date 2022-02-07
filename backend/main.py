from utils.dict_generator import generate_dict

def main():
    # For testing purposes
    nicknames = "Koshi o Duelista, Nishinoya141"
    nicknames_list = nicknames.split(",")

    players = []
    for nickname in nicknames_list:
        players.append(generate_dict(nickname)) 

    return players

if __name__ == "__main__":
    import time
    timeStart = time.time()
    print(main())
    timeEnd = time.time()
    print(f"The total time of the analysis was: {timeEnd - timeStart:.2f}s")
