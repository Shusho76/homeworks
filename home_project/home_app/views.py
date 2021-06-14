from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from datetime import datetime

def greeting(request):
    return HttpResponse("Hello everybody")

def introduction(request):
    return HttpResponse("<H1> My name is Shushan Avetisyan </H1>")

def data_time(request):

    return HttpResponse(F"<H1> Today is {date.today()} and now is {datetime.now().time()}</H1>")

def dictionary_(request):
    new_dict = []
    for i in range(1, 16):
        dict_ = {i: i * i}
        new_dict.append(dict_)
    return HttpResponse (F" There is a dictionary where the keys are numbers between 1 and 15 and the values are square of keys.{new_dict}")








