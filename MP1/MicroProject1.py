import requests
try:
    response = requests.get("https://openrouter.ai/api/v1/models", timeout=5)
    if(response.status_code>=400):
        print("Request failed:", response.status_code)
    else:
        print("Request successful:", response.status_code)
        print("\n")
        rdict = response.json()
        rdictdata = rdict["data"]
        for n in rdictdata[:3]:
            print (f"Name: {n['name']}")
        print("Total count: ")
        print(rdict["total_count"])
except requests.exceptions.Timeout:     # if we use just 'except:' that catches all errors. this catches timeouts only
    print("request timed out")

# print(rdict)
# print("\n")
# print(rdict.keys())
# print(rdict["data"])
# print(type(rdict["data"]))  # it's a list
# print(rdict["data"][0])         # 1st model
# print(type(rdict["data"][0]))   # dict
# print(rdict["data"][0]["name"]) # prints name of 1st model

response2 = requests.get("https://openrouter.ai/api/v1/m")  # deliberately request a bad url
print("\n")
if(response2.status_code>=400):
    print("Request failed:", response2.status_code)