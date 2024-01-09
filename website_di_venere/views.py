from django.shortcuts import render

def home_page(request):
    return render(request, "structure/website_starting_page.html")

