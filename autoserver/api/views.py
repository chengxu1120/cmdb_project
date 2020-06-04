from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def get_data(request):
    print(request.GET)
    print(request.POST)
    host = request.POST.get('host')
    info = request.POST.get('info')
    print('host:',host)
    print('info:',info)
    return HttpResponse('成功')