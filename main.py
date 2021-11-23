import requests
requests = requests.get("http://api.open-notify.org/astros.json")

astros_json = requests.json()
print(astros_json)

peopleInSpace = astros_json["number"]
print("number of people in space: ", peopleInSpace)

i = 1
for people in astros_json["people"]:
    print("Space Dude",i,": ", people["name"])
    i +=1


