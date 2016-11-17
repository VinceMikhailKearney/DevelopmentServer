from django.http import JsonResponse
import urllib2
import json

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
        newDict['twitter'] = "test"
        mlas_array.append(newDict)

    return JsonResponse({ "response": mlas_array })

def niamh(request):
    return JsonResponse({"Who does Vince love?": "Vince loves Niamh <3"})
