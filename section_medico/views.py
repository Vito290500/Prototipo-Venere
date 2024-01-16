import json
from django.shortcuts import render
from django.views import View

class LoginMedico(View):
    def get(self, request):
        return render(request, "structure/login_medico.html")
    
    def post(self, request):
        return render(request, "structure/HomePageMedico.html")

def NuovoAssistito(request):
    return render(request, "structure/includes/nuovoassistito.html")

def ArchivioPazienti(request):
    name_exam = ['Breath Test Helicobacter Pylori', 'Breath Test Lattosio', 'Breath Test Lattosio',
                 'Check Up Routine', 'Check Up Tiroide Base', 'Check Up Tiroide Avamzato', 
                 'Check Up Coagulazione', 'Check Up Malattie Sessualmente Trasmissibili', 'Check Up Menopausa', 
                 'Check up Sportivo', 'Check up Diagtnosi Celiachia', 'Check up Metabolico']

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
    return render(request, "structure/includes/archiviopazienti.html", {'data_json': data_json,
                                                                        'esami': name_exam}, )


def Calendario_Prenotazioni(request):
    return render(request, "structure/includes/calendario_prenotazioni.html")

def Elenco_Referti(request):
    return render(request, "structure/includes/elenco_referti.html")

def Tabella_Analisi(request):
    return render(request, "structure/includes/tabella_analisi.html")

def Sincronizzazione(request):
    return render(request, "structure/includes/sincronizzazione.html")