from app.utils.dict_generator import generate_dict

def main(names):
    players = names.split(",")

    players_info = []
    [players_info.append(generate_dict(player)) for player in players]

    return players_info
