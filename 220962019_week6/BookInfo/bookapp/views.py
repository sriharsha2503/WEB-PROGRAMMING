from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def metadata(request):
    return render(request, 'metadata.html')

def reviews(request):
    return render(request, 'reviews.html')

def publisher_info(request):
    return render(request, 'publisher_info.html')

