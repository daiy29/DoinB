import requests

url = requests.get('https://127.0.0.1:2999/liveclientdata/playerlist', verify='./certificate/riotgames.pem')
gamedata = url.json()

for summoner in gamedata:
    summoner_name = summoner["summonerName"]
    team = summoner["team"]
    print(summoner_name)
    print(team)


