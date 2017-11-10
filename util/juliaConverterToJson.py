import json_lines
import json

def convertToJson():
    json = {}
    with open('c:\\Users\\williamaster\\Documents\\workspaces\\python\\indie-network\\products_all.jl', 'rb') as f:
        for item in json_lines.reader(f):
            try:
                json[item['id']] = item
            except:
                pass
    return json

def writeJson(data):
    with open('base.json', 'w') as outfile:
        json.dump(data, outfile)

writeJson(convertToJson())