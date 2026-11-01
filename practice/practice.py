import requests
response = requests.get("https://api.github.com")
print(response.status_code)
if response.status_code==200:
    print("\n Success! \n")
elif response.status_code==404:
    print("\n Not found! \n")

"""
If you use a Response instance in a Boolean context, 
such as a conditional statement, then it’ll evaluate to True when 
the status code is less than 400, and False otherwise.
"""

print(response.content) # .content gives 'bytes'
print("\n")
print(type(response.content))   # type tells you data type
print("\n")

print(response.text) # .text gives strings
print("\n")
print(type(response.text))
print("\n")

print(response.json()) # this gives deserialized output (converts JSON data into python objects)
print("\n")
print(type(response.json()))    # it's a dict
print("\n")

response_dict = response.json();
print("Using the key here's the value: ")
print(response_dict["emojis_url"])     # u can access values in the object by key
print("\n")

print("Headers:")
print(response.headers) # returns a dictionary-like object, allowing you to access header values by key
print("\n")
print(response.headers["Content-Type"])