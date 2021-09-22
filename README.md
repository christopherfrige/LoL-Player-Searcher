# league-player-searcher

The league-player-searcher is a project that helps people who want to know the status of others League of Legends players,maybe for some scouting or champion select sniping.

It works using Riot Games API, and you can just run the program and type the nickname of the players (separated by commas) that you want to look into.


<div align="center">
	<img width=60% src="https://i.imgur.com/HyKDvcX.png"><br>
	<p>A simple example of querying 3 nicknames.</p>
</div>

## Requirements
- [Python 3.8+](https://www.python.org/downloads/ "Download Python")
- Requests library

## Introduction

Clone the repository to a local folder and configure as described in the following topics.
## Configurando o ambiente

- **Setting the Environment Variables:**

    O projeto atualmente utiliza as seguintes variáveis de ambiente:

	The project uses the following environment variable:

        RIOT_API_KEY -> An API key for development purposes

    To get your own Riot API Key you need to go on their [Developer Portal](https://developer.riotgames.com/) and login (or create) your account. Then, get your key and follow the next steps.

	**PS:** Keys works for 1 day, then you must regenerate it in the same place as before.


    **Linux example:**<br>

    Type, in the Linux Terminal:

		RIOT_API_KEY=YOUR-API-KEY-HERE
		export RIOT_API_KEY

    Check if the variable was created:

        echo $RIOT_API_KEY

    **Windows example:** <br>

    Type, in the Windows CMD:

        setx RIOT_API_KEY "YOUR_API_KEY_HERE"

	It also can be done through Windows GUI, in the control painel of your OS.

## Running

You can run the project and search for players just typing:

    python3 main.py

Or in the Windows CMD:

    python main.py