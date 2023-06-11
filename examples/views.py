from django.shortcuts import render
from django.http import HttpRequest,HttpResponse


# request = HttpRequest
# response = HttpResponse

# функциональный оброботчик(view), принимает request отдает response
# def index(request):
#     return HttpResponse("Hello")

# Передаем список python 
# def index(request):
#     my_list = [1,2,3,4]
#     return HttpResponse(my_list)

# Передаем текст, содержащий html-код
# def index(request):
#     text = "<h1>Hello</h1>"
#     return HttpResponse(text)


# Передаем текст, содержащий html-код
# def index(request):
#     body = """
#     <body>
#     <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1C8HMDleZTQG44cEo86g3_3JCmEoT9MdQ9g&usqp=CAU" alt="Моё тестовое изображение">
#     </body>
#     """
#     return HttpResponse(body)

# Передаем кастомные заголовки ответа
# def index(request):
#     headers = {
#         "Name": "Alex"
#     }
#     return HttpResponse("Hello",headers=headers )


# Делаем вид, что сервер передал файл на скачивание
# def index(request):
#     my_data = "Типа файл"
#     headers = {
#         'Content-Type': 'application/vnd.ms-excel',
#         'Content-Disposition': 'attachment; filename=test.xls',
#     }
#     return HttpResponse(my_data, headers=headers)


# Изменяем статус ответа, смтрим содержимое request
# def index(request):
    # if request.method == "GET":
#       print(request.get_host())
#     return HttpResponse("Hello", status=500)
