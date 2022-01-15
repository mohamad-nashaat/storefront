from django.shortcuts import render
from django.http import HttpResponse


def sayHello(request):
    # return HttpResponse('Hello world')
    return render(request, 'hello.html', {'name': 'Mohamad'})
