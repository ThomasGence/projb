from os import sep
import json
import ijson
import pprint
import math


def parse_json_to_dict(filename):
    with open(filename, 'r') as read_file:
        data = json.load(read_file)
    return data

def save_dict_to_json(mydict, filename):
    json_dict = json.dumps(mydict)
    f = open(filename,"w")
    f.write(json_dict)
    f.close()

def number_of_storyids_of(testOrDev, filename):
    my_dict = parse_json_to_dict(filename)
    list = my_dict[testOrDev]
    nb_of_storyids = 0
    curr_story = ""
    max = 0
    nb_of_datapts_per_story=1
    for i in range(0, len(list)):
        if(list[i]['storyid'] != curr_story):
            #print(curr_story)
            #print(nb_of_datapts_per_story)
            #print(max)
            if(nb_of_datapts_per_story != 0): 
                nb_of_datapts_per_story =1
            curr_story = list[i]['storyid']
            nb_of_storyids += 1
        else: nb_of_datapts_per_story +=1
        if(nb_of_datapts_per_story > max): 
                max = nb_of_datapts_per_story
    return (nb_of_storyids)

def addChoicesToDataPts_of_MASLOW(testOrDev):
    stories_dict = parse_json_to_dict("maslow.json")
    for i in range(len(stories_dict[testOrDev])):
        stories_dict[testOrDev][i]["choice0"] = stories_dict[testOrDev][i]["char"] + " needs " + stories_dict[testOrDev][i]["question"]
        stories_dict[testOrDev][i]["choice1"] = stories_dict[testOrDev][i]["char"] + " does not need " + stories_dict[testOrDev][i]["question"]
    return stories_dict

def addChoicesToDataPts_of_REISS(testOrDev):
    stories_dict = parse_json_to_dict("reiss.json")
    for i in range(len(stories_dict[testOrDev])):
        stories_dict[testOrDev][i]["choice0"] = stories_dict[testOrDev][i]["char"] + " is motivated by " + stories_dict[testOrDev][i]["question"]
        stories_dict[testOrDev][i]["choice1"] = stories_dict[testOrDev][i]["char"] + " is not motivated by " + stories_dict[testOrDev][i]["question"]
    return stories_dict

def addChoicesToDataPts_of_PLUTCHIK(testOrDev):
    stories_dict = parse_json_to_dict("plutchik.json")
    for i in range(len(stories_dict[testOrDev])):
        stories_dict[testOrDev][i]["choice0"] = stories_dict[testOrDev][i]["char"] + " feels " + stories_dict[testOrDev][i]["question"]
        stories_dict[testOrDev][i]["choice1"] = stories_dict[testOrDev][i]["char"] + " does not feel " + stories_dict[testOrDev][i]["question"]
    return stories_dict

def take_percentage_of_nbstories_of(dictionary, percentage):
    limited = {k:dictionary["dev"][k] for k in range(0, math.ceil(percentage*len(dictionary["dev"])))}
    return limited


def formation_of_training_set_for(dictionary):
    dictio = take_percentage_of_nbstories_of(dictionary, 0.8)
    return dictio




dictionary0 = parse_json_to_dict("maslow.json")
dictionary1= addChoicesToDataPts_of_MASLOW("test")
print(dictionary0["test"][0])
print(dictionary1["test"][0])









"""classifier = pipeline("ner",grouped_entities = True)
#classifier(my_dict['test'
][
    0: 10
])
print(classifier("EPFL is great"))"""

"""tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
model = RobertaModel.from_pretrained('roberta-base')
text = "Replace me by any text you'd like."
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)"""
