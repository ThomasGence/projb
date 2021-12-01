from os import sep
import json
import pprint

def parse_json_to_dict(filename):
    with open(filename, 'r') as read_file:
        data = json.load(read_file)
    return data

def save_dict_to_json(mydict, filename):
    json_dict = json.dumps(mydict)
    f = open(filename, "w")
    f.write(json_dict)
    f.close()
    qwdqwdqwq
    eqwq


my_dict = parse_json_to_dict("maslow.json")
print("\ntest:\n")
pprint.pprint(my_dict['test'][0:10])
print("\n\n\ndev:\n")
pprint.pprint(my_dict['dev'][0:10])


"""
classifier = pipeline('sentiment-analysis',model="nlptown/bert-base-multilingual-uncased-sentiment")
results = classifier()

for result in results:
    print(f"label: {result['label']}, with score: {round(result['score'], 4)}")
    
"""