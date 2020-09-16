from django.shortcuts import render


def home(request): #to use API keys
    import json
    import requests #pip install requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']#getting this zipcode from name on base.html then adds to the url below..
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=EC9B07EB-7471-4AF5-9927-21D0B8158BA5")#concatanate the zip code into the url so user can search for others

        try:
            api = json.loads(api_request.content) #call json, load up content from this variable
        except Exception as e: #if no information in api excpetion called.
            api = "Error..." #print error
         
        if api[0]['Category']['Name'] == "Good": #inside api 0, inside category, inside name... if equals 'good'
            category_description = "(0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk."
            category_color = "good" #we are calling the color assigned in our base.html
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "(51 - 100) Air quality is acceptable; however for some pollutants there may be a moderate health concern for a very small number of people who are unusually sesnsitive to air pollution."
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "(101 - 150) Although general public is not likely to be affedcted at this AQI range, people with lung disease. older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older aldults and children are at greater risk from the presence of particles in the air."
            category_color = "unhealthyforsensitivegroups"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "(151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "(201 - 300) Health alert: everyone may experience more serious health effects."
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "(301 - 500) Health warnings of emergency conditions. The entire population is more likely to be affected." 
            category_color = "hazardous"    

        return render(request, 'home.html', {'api': api, 'category_description': category_description, 'category_color': category_color})#call the api into our home page


    else:
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=EC9B07EB-7471-4AF5-9927-21D0B8158BA5")

        try:
            api = json.loads(api_request.content) #call json, load up content from this variable
        except Exception as e: #if no information in api excpetion called.
            api = "Error..."
         
        if api[0]['Category']['Name'] == "Good": #inside api 0, inside category, inside name... if equals 'good'
            category_description = "(0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk."
            category_color = "good" #we are calling the color assigned in our base.html
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "(51 - 100) Air quality is acceptable; however for some pollutants there may be a moderate health concern for a very small number of people who are unusually sesnsitive to air pollution."
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "(101 - 150) Although general public is not likely to be affedcted at this AQI range, people with lung disease. older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older aldults and children are at greater risk from the presence of particles in the air."
            category_color = "unhealthyforsensitivegroups"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "(151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "(201 - 300) Health alert: everyone may experience more serious health effects."
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "(301 - 500) Health warnings of emergency conditions. The entire population is more likely to be affected." 
            category_color = "hazardous"    

        return render(request, 'home.html', {'api': api, 'category_description': category_description, 'category_color': category_color})#call the api into our home page

def about(request):
    return render(request, 'about.html', {})