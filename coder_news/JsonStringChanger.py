import json
from django.http import JsonResponse

def changeStringToDict(string):
    return json.loads(string)

def changeDictToString(dict):
    return json.dumps(dict)

def getAJsonRespondWithString(string):
    jsonObject = changeStringToDict(string)
    return JsonResponse(jsonObject)

def getAJsonRespondWithDict(dict):
    return JsonResponse(dict)