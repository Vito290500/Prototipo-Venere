from django.shortcuts import render
from django.views import View

# Create your views here.
class LoginMedico(View):
    def get(self, request):
        return render(request, "structure/login_medico.html")
    
    def post(self, request):
        return render(request, "structure/HomePageMedico.html")

