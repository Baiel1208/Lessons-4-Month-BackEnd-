from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

def get_template(request):
    context = {
        "zagolovok": "Заголовок из контекста",
        "my_list": [1,2,3,4,5],
    }
    return render(request, "examples/test_template.html", context=context)