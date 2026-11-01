# STRUCTURED/FOLLOW THIS SKELETON
import requests
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users/1", timeout=5)
except requests.exceptions.Timeout:
    print("timed out")
else:
    if response.status_code >= 400:
        print("failed:", response.status_code)
    else:
        data = response.json()
        # print(type(data))         dict
        # print(data)
        print("\n")
        # print(data.keys())
        temp = data["address"]
        # print(temp)
        # print(type(temp))         dict
        print(temp['city'])
        temp2 = temp['geo']
        # print(type(temp2))        dict
        print(temp2['lat'])
        # print(type(temp2['lat']))     string
        temp3 = data['company']
        print(temp3['name'])





# dict or list? then explore
# ... navigate, then print