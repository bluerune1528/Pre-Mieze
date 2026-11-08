import requests
try:
    response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto", timeout=5)
except requests.exceptions.Timeout:
    print("timed out")
else:
    if response.status_code >=400:
        print("failed:", response.status_code)
    else:
        data = response.json()
        # print(type(data))             list
        # print(data.keys())
        # data['abilities']))
        ab= data['abilities']
        # print(data['abilities'])
        # print(ab[0]['ability']['name'])

        for n in ab:
            print(f"Ability name: {n['ability']['name']}")