from django.http import HttpResponse, HttpResponseNotFound
from django.urls import path
from django.shortcuts import render
from DjangoCountries import country




def home(request):
    text = """<h1>"Buenos-dias, Pedrilas"</h1>
            <br><a href="countries-list">INFO</a></br>
        """
    return HttpResponse(text)


def countries_list(request):
    country_list = []
    path = f"/home/user/Projects/DjangoCountries/DjangoCountries/country.py"
    with open(path) as read_file:
        for item in country.COUNTRY:
            country_name = item["country"].replace(" ","_")
            country_list.append(f"<a href = http://127.0.0.1:8000/countries-list/{country_name}>")
            country_list.append("<h1>")
            country_list.append(item["country"])
            country_list.append("</h1>")
            country_list.append("</a>")
    return HttpResponse(country_list)


def get_country(request, value):
    text = []
    path = f"/home/user/Projects/DjangoCountries/DjangoCountries/country.py"
    with open(path) as read_file:
        for item in country.COUNTRY:
            if item["country"].replace(" ","_") == value:
                text.append("<h1>")
                text.append("В стране - ")
                text.append(item["country"])
                text.append(", ")
                text.append("говорят на этих языках: ")
                text.append(item["languages"])
                text.append("</h1>")
                text.append("</br>")
                text.append("<h1>")
                text.append(f"<a href = 'http://127.0.0.1:8000/countries-list'> Back </a>")
                text.append("</h1>")
        return HttpResponse(text)

                            
                            
    


