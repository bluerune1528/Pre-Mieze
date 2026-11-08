import requests
import json
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

def extract_models(payload):        # extract imp info from payload (saves nav time)
    models = payload.get("data") if isinstance(payload, dict) else None
    if not isinstance(models, list):
        return {}       # unexpected shape -> empty result
    return{
        m['id']: m.get('name', '?')
        for m in models
        if isinstance(m, dict) and 'id' in m        # for each model m in the list, if it's a dict & has an id, add id:name to the new dict
    }

# def load_snapshot(path=SNAPSHOT_FILE):                  # path is a default param
#    try:
#        with open(path, encoding="utf-8") as f:             # with is a context manager (closes file automatically) & opened file is assigned to var f

def main():
    try:
        payload = fetch_json(url)
    except FetchError as err:
        print("Giving up:", err)
        return
    else:
        models = payload.get("data") if isinstance(payload, dict) else None
        if not isinstance(models, list):
            print("unexpected response shape")
        else:
            print("Request successful")
            for m in models[:3]:
                print(f"Name: {m.get('name', '?')}")
            print("Total count:", len(models))