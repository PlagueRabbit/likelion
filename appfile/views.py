from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect


# Create your views here.
def calculator(request):
    if request.method=='POST':
        number=request.POST.get('result')
        return HttpResponseRedirect('/success/')
    else:
        return render(request, 'calc.html')