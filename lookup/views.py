from django.shortcuts import render


def home(request): #to use API keys
    import json
    import requests #pip install requests

    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=EC9B07EB-7471-4AF5-9927-21D0B8158BA5")

    try:
        api = json.loads(api_request.content) #call json, load up content from this variable
    except Exception as e: #if no information in api excpetion called.
        api = "Error..."

    return render(request, 'home.html', {'api': api})#call the api into our home page

def about(request):
    return render(request, 'about.html', {})