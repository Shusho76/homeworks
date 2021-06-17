from django.shortcuts import render
from django.http import HttpResponse
import json

def home(request):
    return HttpResponse("<H1>HELLO DJANGO WORLD</H1>")
def greeting(request):
    return HttpResponse("Hello Jonny")
def greeting1(request):
    return HttpResponse("<H1> Hello evrybody </H1>")

def hello_html(request):
    return render(request, "new_app/index.html")

def hello(request):
    context = {"name": "Shushan", "surname": "Avetisyan"}
    return render(request, "new_app/index.html", context)

def json_file(request):
    with open('C://Users/User/PycharmProjects/pythonProject1/example_json.json', 'r') as f:
        data = json.load(f)
    return render(request, "new_app/read_json.html", data)

def massege(request):
    if request.method == 'POST':
        print(request.POST)
        a = request.POST
        return HttpResponse(F"{a.get('adress') }")
    else:
        return render(request, "new_app/Myplace.html")



