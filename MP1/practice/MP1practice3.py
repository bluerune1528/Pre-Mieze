import requests
try:
    response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=5", timeout=5)
except requests.exceptions.Timeout:
    print("timed out")
else:
    if response.status_code >=400:
        print("failed:", response.status_code)
    else:
        data = response.json()
        # print(type(data))         dict
        # print(data)
        # print(type(data["results"]))    list
        res = data["results"]
        # print(data["results"])
        for n in res[:5]:
            print(f"Name: {n['name']}")