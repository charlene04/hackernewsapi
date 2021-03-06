
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
import requests
from itertools import islice
from .models import *
import json
import http.client

def syncdbtopstories():
    num = Item.objects.all().count()
    stories = []
    conn = http.client.HTTPSConnection("hacker-news.firebaseio.com")
    conn.request("GET", "/v0/topstories.json?print=pretty")
    res = conn.getresponse()
    if num > 0:
        data = res.read()[num+1:num+11]
    else:
        data = res.read()[0:10]
    for item in data:
        url = "https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty".format(item)
        querystring = {"print":"pretty"}
        response = requests.request("GET", url, params=querystring).json()
        stories.append(response.copy())
    
   
    
    batch_size = 10
    objs = (Item(item_id=i.get('id'), type=i.get('type'), by=i.get('by',None), text=i.get('text', None), kids=i.get('kids', None), parent=i.get('parent', None), descendants=i.get('descendants',None), score=i.get('score',None), url=i.get('url',None), parts=i.get('parts',None), title=i.get('title',None), time=i.get('time',None), dead=i.get('dead',None), deleted=i.get('deleted',None) ) for i  in stories)
    while True:
        batch = list(islice(objs, batch_size))
        if not batch:
            break
        Item.objects.bulk_create(batch, batch_size)
    print('done')
    return JsonResponse({'status':'done'})

