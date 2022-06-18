from urllib import response
from django.shortcuts import render
import requests, json


def index(request):
    
    query = 'cars'
    url = "https://api.chucknorris.io/jokes/random"

    

    response = requests.request("GET", url)
    joke = json.loads(response.text)['value']
    
    context = {
        'title': 'Chuck Norris',
        'content': 'Chuck Norris',
        'definition': joke
    }
    return render(request=request, template_name='index.html', context=context)
