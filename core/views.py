from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'aboutus.html')


def contact(request):
    return render(request, 'contact.html')
    

def magazine_list(request):
    return render(request, 'magazine-list.html')


def parts_select(request):
    return render(request, 'parts-select.html')


def result(request):
    return render(request, 'result.html')