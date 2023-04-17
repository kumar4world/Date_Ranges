import json
from django.shortcuts import render
import requests

def index(request):
     url = "https://ip-geo-location4.p.rapidapi.com/"
     querystring = {"ip":"76.77.66.98"}
     headers = {
	"X-RapidAPI-Key": "54d89a050bmsh9b85f61a9659597p124bc9jsndf8c172f982b",
	"X-RapidAPI-Host": "ip-geo-location4.p.rapidapi.com"}    
  #   response = requests.request("GET", url, headers=headers, params=querystring)
#     data = response.json()
     return render(request, "index.html")    
