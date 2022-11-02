import requests

BASE = "http://127.0.0.1:5000/"

data = [{"name": "kashish", "views": 6900, "likes": 69},
        {"name": "millo", "views": 1000000, "likes": 1000000},
        {"name": "mit is a lil bitch", "views": -100, "likes": 10},
        {"name": "Sai is good though", "views": 123123, "likes": 12412},
        ]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), json=data[i])
    print(response.json())

input()
response = requests.get(BASE + "video/2")
print(response.json())

response = requests.patch(BASE + "video/2", json=data[1])

input()
response = requests.get(BASE + "video/2")
print(response.json())
