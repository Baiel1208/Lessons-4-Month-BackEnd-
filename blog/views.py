from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Main page")


def test_page(request):
    return HttpResponse("Test",status=404)

#HW2
def get_contacts(request):
    return HttpResponse("Наши контакты!")


def get_about(request):
    return HttpResponse("В Австралии есть растение, известное как 'Gympie-Gympie', чьи листья покрыты мельчайшими жалящими иглами. Касание этого растения может вызывать интенсивную боль, которая может продолжаться месяцами.")