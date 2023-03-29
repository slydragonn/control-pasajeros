import json

def create_json_file(Dic: dict):
    json_string = json.dumps(Dic, indent=4)
    json_file = open("buses.json", "w")
    json_file.write(json_string)
    json_file.close()