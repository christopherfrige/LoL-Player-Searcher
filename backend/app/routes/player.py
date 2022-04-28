from api import app
from app.main import main
from flask import jsonify


@app.route('/player/<summoner_names>', methods=["GET"])
def get_players(summoner_names):

    players = main(summoner_names)

    return jsonify(players)

