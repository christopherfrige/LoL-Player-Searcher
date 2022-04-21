from flask import Flask, jsonify
from main import main
app = Flask(__name__)

@app.route('/search', methods=["POST"])
def data():
    players = main()
    return jsonify(players)

if __name__ == "__main__":
    app.run(debug=True)