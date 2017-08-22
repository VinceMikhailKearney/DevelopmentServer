from django.http import JsonResponse
from django.conf import settings
from urllib.request import urlopen
import json
import csv


def local_ping(request):
    return JsonResponse({"status": "ok", "result": "Success"})

def fetchMlas(request):
    # file = urlopen('http://data.niassembly.gov.uk/api/members/')
    # jsonResp = json.loads(file.read())
    file = open('%s/JSON/MLAs.json' % settings.BASE_DIR, 'r')
    json_local = json.load(file)

    mlas_array = []
    for object in json_local:
        newDict = {}
        newDict['key'] = object['MemberPersonId']
        newDict['firstName'] = object['MemberFirstName']
        newDict['lastName'] = object['MemberLastName']
        newDict['party'] = object['PartyAbbreviation']
        newDict['partyName'] = object['PartyName']
        newDict['title'] = object['MemberTitle']
        newDict['constituency'] = object['ConstituencyName']
        newDict['imageURL'] = object['MemberImgUrl']
        newDict['email'] = str(checkForEmail(newDict['firstName'], newDict['lastName']))
        newDict['twitter'] = str(checkForTwitter(newDict['firstName'], newDict['lastName']))
        mlas_array.append(newDict)

    return JsonResponse({ "response": mlas_array })

def checkForTwitter(first, last):
    return checkForData(first, last, 13)

def checkForEmail(first, last):
    return checkForData(first, last, 7)

def checkForData(first, last, index):
    f = open('%s/elected-candidates.csv' % settings.BASE_DIR, 'r')
    csv_f = csv.reader(f)

    for row in csv_f:
        if row[12].lower() == first.lower() and row[11].lower() == last.lower():
            return row[index]

def fetchParties(request):
    with open('%s/party_json.json' % settings.BASE_DIR, 'r') as json_file:
        json_data = json.load(json_file)
        return JsonResponse({"response": json_data})
