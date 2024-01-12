import json
from django.shortcuts import render
from django.views import View

# Create your views here.
class LoginMedico(View):
    def get(self, request):
        return render(request, "structure/login_medico.html")
    
    def post(self, request):
        return render(request, "structure/HomePageMedico.html")


def NuovoAssistito(request):
    return render(request, "structure/includes/nuovoassistito.html")


def ArchivioPazienti(request):
    name_example = [
    'Achille', 'Achille', 'Ada', 'Adam', 'Adelaide', 'Adele', 'Aden', 'Adolfo', 'Adriana', 'Adriano',
    'Agape', 'Agata', 'Agatha', 'Agnese', 'Agostina', 'Agostino', 'Aiace', 'Aida', 'Akira', 'Alba',
    'Albarosa', 'Alberico', 'Albert', 'Alberta', 'Alberto', 'Aldo', 'Alejandro', 'Alessandra', 'Alessandro',
    'Alessia', 'Alessio', 'Alexander', 'Alfio', 'Alfonso', 'Alfredo', 'Alice',
]

    data = []

    for name in name_example:
        data.append({
            'cognome': name,
            'nome': '',
            'Data di nascita': '',
            'Codice Fiscale': '',
            'Indirizzo': '',
            'Dettagli': '',
            'Fine attività': ''
        })

    data_json = json.dumps(data)
    return render(request, "structure/includes/archiviopazienti.html", {'data_json': data_json})