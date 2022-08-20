import requests

name_list = {"Hulk", "Captain America", "Thanos"}
result = {}

url = 'https://akabab.github.io/superhero-api/api/all.json'

resp = requests.get(url)
list = resp.json()

for a in list:
  name = a["name"]
  if name in name_list:
    powerstats = a.get("powerstats")
    intelligence = powerstats.get('intelligence')
    result[name] = intelligence

print(f'Самый умный герой: {max(result, key=result.get)}')