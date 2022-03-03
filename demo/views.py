from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    # return HttpResponse("Hello World")
    return render(request, 'sample.html', {'name': 'Pallavi'})


def sum(request):
    a = int(request.POST['no1'])
    b = int(request.POST['no2'])
    ans = a + b
    return render(request, 'result.html', {'result': ans})
