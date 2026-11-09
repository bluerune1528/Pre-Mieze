import requests
import json
url = "https://openrouter.ai/api/v1/models"
TIMEOUT = (3.05, 10)                            # (connect, read) in seconds
SNAPSHOT_FILE = "seen_models.json"

class FetchError(Exception):                        # custom exception (Exception is a built in class, FetchError inherits its functionality)
    pass    # do nothing for now/placeholder (not adding anything extra to the class)

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

def load_snapshot(path=SNAPSHOT_FILE):                  # path is a default param
    try:
        with open(path, encoding="utf-8") as f:             # with is a context manager (closes file automatically) & opened file is assigned to var f
            return json.load(f)     # reads file
    except (FileNotFoundError, json.JSONDecodeError):
        return {}           # first run or corrupted file

def save_snapshot(models, path=SNAPSHOT_FILE):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(models, f, indent=2)      # writes into file

def main():
    try:
        payload = fetch_json(url)
    except FetchError as err:
        print("Giving up:", err)
        return
    
    current = extract_models(payload)
    if not current:
        print("unexpected response shape, nothing saved")
        return

    previous = load_snapshot()
    print("total count: ", len(current))
    if not previous:
        print("first run - saved a baseline to compare")
    else:
        new_ids = current.keys() - previous.keys()
        if new_ids:
            for model_id in sorted(new_ids):
                print("NEW: ", model_id, current[model_id])
        else:
            print("no new models")

    save_snapshot(current)

if __name__ == "__main__":
    main()