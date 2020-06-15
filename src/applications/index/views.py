# from django.template import context
# from django.template.context_processors import csrf
from django.views.generic import TemplateView
from django.shortcuts import render

import json
import urllib.request


class IndexView(TemplateView):
    template_name = "index/index.html"

def index(request):
    # context.update(csrf(request))
    if request.method == 'POST':
        city = request.POST['city']

        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q ='
            + city + '&appid = 32d9a26cf6c27dd72c75db62ea187822').read()

        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                          + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
        print(data)
    else:
        data = {}
    return render(request, "index/index.html", data)
