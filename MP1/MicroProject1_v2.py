import requests
url = "https://openrouter.ai/api/v1/models"

class FetchError(Exception):                        # custom exception
    pass    # do nothing for now/placeholder

def fetch_json(url):
    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.Timeout as err:
        raise FetchError("timed out") from err
    except requests.exceptions.RequestException as err:
        raise FetchError(f"network problem: {err}") from err

    if response.status_code >=400:
        raise FetchError(f"Request failed: {response.status_code}")
    return response.json()

try:
    rdict = fetch_json(url)
except FetchError as err:
    print("Giving up:", err)
else:
    print("Request successful")
    print("\n")
    rdictdata = rdict["data"]
    for n in rdictdata[:3]:
        print(f"Name: {n['name']}")
    print("Total count: ")
    print(rdict["total_count"])


# print(rdict)
# print(rdict.keys())
# print(rdict["data"])
# print(type(rdict["data"]))  # it's a list
# print(rdict["data"][0])         # 1st model
# print(type(rdict["data"][0]))   # dict
# print(rdict["data"][0]["name"]) # prints name of 1st model