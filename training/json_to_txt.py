import json

f = open('data.json', 'r', encoding='utf-8')
r = open('result.txt', 'w', encoding='utf-8')

data = json.load(f)

for joke in data["jokes"]:
    r.write(joke['question'] + " " + joke["answer"] + "\n")

print("Finished converting json to txt. {0} jokes converted".format(len(data["jokes"])))