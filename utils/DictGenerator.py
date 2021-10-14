from services.Analyzer import Analyzer

def generate_dict(player):
    player_analysis = Analyzer(player)

    player_info = {"name": player,
                "status": player_analysis.get_active_game_status(),
                "timeLastGame": player_analysis.get_time_since_last_game()                
                }


    is_playing = player_info['status']
    if is_playing:
        player_info.pop("timeLastGame")
        player_info.update({
            "status": "True",
            "gameLenght": player_info['status']
        })


    return player_info