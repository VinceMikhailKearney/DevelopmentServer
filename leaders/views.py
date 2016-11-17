from django.http import JsonResponse
from django.conf import settings
import urllib2
import json
import csv

def fetchMlas(request):
    req = urllib2.Request('http://data.niassembly.gov.uk/api/members/')
    file = urllib2.build_opener().open(req)
    jsonResp = json.loads(file.read())

    mlas_array = []
    for i in jsonResp:
        newDict = {}
        newDict['key'] = i['MemberPersonId']
        newDict['firstName'] = i['MemberFirstName']
        newDict['lastName'] = i['MemberLastName']
        newDict['party'] = i['PartyAbbreviation']
        newDict['partyName'] = i['PartyName']
        newDict['title'] = i['MemberTitle']
        newDict['constituency'] = i['ConstituencyName']
        newDict['imageURL'] = i['MemberImgUrl']
        newDict['email'] = "test"
        newDict['twitter'] = str(checkForTwitter(newDict['firstName'], newDict['lastName']))
        mlas_array.append(newDict)

    return JsonResponse({ "response": mlas_array })


def checkForTwitter(first, last):
    f = open('%s/elected-candidates.csv' % settings.BASE_DIR, 'r')
    csv_f = csv.reader(f)

    for row in csv_f:
        if row[12].lower() == first.lower() and row[11].lower() == last.lower():
            return row[13]


def niamh(request):
    return JsonResponse({"Who does Vince love?": "Vince loves Niamh <3"})
