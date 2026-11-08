import requests
url = "https://openrouter.ai/api/v1/models"
TIMEOUT = (3.05, 10)                            # (connect, read) in seconds
SNAPSHOT_FILE = "seen_models.json"

class FetchError(Exception):                        # custom exception
    pass    # do nothing for now/placeholder

def fetch_json(url):
    try:
        response = requests.get(url, timeout=TIMEOUT)
        response.raise_for_status()             # 4xx, 5xx -> HTTPError
    except requests.exceptions.Timeout as err:
        raise FetchError("timed out") from err
    except requests.exceptions.HTTPError as err:
        raise FetchError(f"Request failed: {err.response.status_code}") from err
    except requests.exceptions.RequestException as err:
        raise FetchError(f"network problem: {err}") from err
    try:
        return response.json()
    except ValueError as err:
        raise FetchError("response was not json") from err

try:
    rdict = fetch_json(url)
except FetchError as err:
    print("Giving up:", err)
else:
    models = rdict.get("data") if isinstance(rdict, dict) else None
    if not isinstance(models, list):
        print("unexpected response shape")
    else:
        print("Request successful")
        for m in models[:3]:
            print(f"Name: {m.get('name', '?')}")
        print("Total count:", len(models))


# print(rdict)
# print(rdict.keys())
# print(rdict["data"])
# print(type(rdict["data"]))  # it's a list
# print(rdict["data"][0])         # 1st model
# print(type(rdict["data"][0]))   # dict
# print(rdict["data"][0]["name"]) # prints name of 1st model