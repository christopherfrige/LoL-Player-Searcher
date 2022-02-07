from services.Analyzer import Analyzer

def generate_dict(player):
    player_analysis = Analyzer(player)
    main_structure = {
            "name": player,
            "inGame": 
                {                  
                    "status": player_analysis.get_active_game_status()
                },              
            }

    is_playing = main_structure['inGame']['status']

    if is_playing:
        game_info = {
            "inGame": 
                {
                    "status": True,                  
                    "gameLenght": is_playing} 
                }
    else:
        game_info = {"timeLastGame": player_analysis.get_time_since_last_game()}  
    
    main_structure.update(game_info)

    return main_structure