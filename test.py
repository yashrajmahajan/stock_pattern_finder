import json

#print(json_object_string)

#json_object = json.loads(json_object_string)


#print(json_object["name"])

fp = open('output.json', 'r')
data=json.load(fp)

print('\n\n',data)

