import requests
try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts?userId=1", timeout=5)
except requests.exceptions.Timeout:
    print("Timed out")
else:
    if(response.status_code>=400):
        print("Failed:", response.status_code)
    else:
        data = response.json()
        # print(type(data))             it's a list
        # print(data)
        # print(type(data[2]))          it's a dict
        third = data[2]
        # print(third)
        print(third["title"])
        print(len(data))