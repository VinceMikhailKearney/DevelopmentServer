from django.http import JsonResponse
import urllib2
import json

def fetchMlas(request):
    req = urllib2.Request('http://data.niassembly.gov.uk/api/members/')
    file = urllib2.build_opener().open(req)
    jsonResp = json.loads(file.read())
    return JsonResponse({ "response": jsonResp })
