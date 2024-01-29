import json
from django.shortcuts import render
from django.views import View

from . import views
from .models import Prenotazioni

class LoginMedico(View):
    def get(self, request):
        return render(request, "structure/login_medico.html")
    
    def post(self, request):
        return render(request, "structure/HomePageMedico.html")

def NuovoAssistito(request):

    elenco_provincie = [
        'Agrigento, AG', 'Alessandria, AL', 'Ancona, AN', 'Aosta/Aoste, AO'
        'Arezzo, AR' , 'Ascoli Piceno, AP',	 'Asti,	AT', 'Avellino,	AV', 'Bari,	BA',
        'Barletta-Andria-Trani,BT', 'Belluno, BL','Benevento, BN',  'Bergamo,BG',
        'Biella,BI	' ,'Bologna,BO'	 ,'Bolzano,BZ','Brescia,BS'	,'Brindisi,BR','Cagliari,CA',
        'Caltanissetta,CL' ,'Campobasso,CB','Caserta,CE', 'Catania,CT', "Catanzaro,CZ",
        "Chieti,CH","Como,CO","Cosenza,CS","Cremona,CR","Crotone,KR","Cuneo,CN","Enna,EN",
        "Fermo,FM","Ferrara,FE","Firenze,FI","Foggia,FG","Forlì-Cesena,FC","Frosinone,FR",
        "Genova,GE","Gorizia,GO","Grosseto,GR","Imperia,IM","Isernia,IS","L'Aquila,AQ",
        "La Spezia,SP","Latina,LT","Lecce,LE","Lecco,LC","Livorno,LI","Lodi,LO","Lucca,LU",
        "Macerata,MC","Mantova,MN","Massa-Carrara,MS","Matera,MT","Messina,ME","Milano,MI",
        "Modena,MO","Monza e Brianza, MB", "Novara, NO", "Nuoro, NU", "Oristano, OR", "Padova, PD",
        "Palermo, PA", "Parma, PR", "Pavia, PV", "Perugia, PG", "Pesaro e Urbino, PU",
        "Pescara, PE", "Piacenza, PC", "Pisa, PI", "Pistoia, PT", "Pordenone, PN",
        "Potenza, PZ", "Prato, PO", "Ragusa, RG", "Ravenna, RA", "Reggio Calabria, RC",
        "Reggio Emilia, RE", "Rieti, RI", "Rimini, RN", "Roma, RM", "Rovigo, RO",
        "Salerno, SA", "Sassari,SS", "Savona,SV", "Siena,SI", "Siracusa,SR", "Sondrio,SO",
        "Sud Sardegna,SU", "Taranto,TA", "Teramo,TE", "Terni,TR", "Torino,TO",
        "Trapani,TP", "Trento,TN", "Treviso,TV", "Trieste,TS", "Udine,UD",
        "Varese,VA", "Venezia,VE", "Verbano-Cusio-Ossola,VB", "Vercelli,VC",
        "Verona,VR", "Vibo Valentia,VV", "Vicenza,VI", "Viterbo,VT"
    ]
    return render(request, "structure/includes/nuovoassistito.html", {
        "province" : elenco_provincie
    })

def ArchivioPazienti(request):

    #IMPLEMENT THIS WITH BACKEND
    name_exam = ['Breath Test Helicobacter Pylori', 'Breath Test Lattosio', 'Breath Test Lattosio',
                 'Check Up Routine', 'Check Up Tiroide Base', 'Check Up Tiroide Avamzato', 
                 'Check Up Coagulazione', 'Check Up Malattie Sessualmente Trasmissibili', 'Check Up Menopausa', 
                 'Check up Sportivo', 'Check up Diagtnosi Celiachia', 'Check up Metabolico']

    name_example = [
    'Achille', 'Achille', 'Ada', 'Adam', 'Adelaide', 'Adele', 'Aden', 'Adolfo', 'Adriana', 'Adriano',
    'Agape', 'Agata', 'Agatha', 'Agnese', 'Agostina', 'Agostino', 'Aiace', 'Aida', 'Akira', 'Alba',
    'Albarosa', 'Alberico', 'Albert', 'Alberta', 'Alberto', 'Aldo', 'Alejandro', 'Alessandra', 'Alessandro',
    'Alessia', 'Alessio', 'Alexander', 'Alfio', 'Alfonso', 'Alfredo', 'Alice', 'Martina',
    'Achille', 'Achille', 'Ada', 'Adam', 'Adelaide', 'Adele', 'Aden', 'Adolfo', 'Adriana', 'Adriano',
    'Agape', 'Agata', 'Agatha', 'Agnese', 'Agostina', 'Agostino', 'Aiace', 'Aida', 'Akira', 'Alba',
    'Albarosa', 'Alberico', 'Albert', 'Alberta', 'Alberto', 'Aldo', 'Alejandro', 'Alessandra', 'Alessandro',
    'Alessia', 'Alessio', 'Alexander', 'Alfio', 'Alfonso', 'Alfredo', 'Alice', 'Martina'
    ]

    data = []
    result = 0

    for count in range(0, len(name_example)):
        result += 1
        data.append({
            'cognome': name_example[count] ,
            'nome': '',
            'Data di nascita': '',
            'Codice Fiscale': '',
            'Indirizzo': '',
            'Dettagli': '',
            'Fine attività': '',
            'id': count
        })
  
    data_json = json.dumps(data)
    return render(request, "structure/includes/archiviopazienti.html", {'data_json': data_json,
                                                                        'esami': name_exam,
                                                                        'result': result}, )

def Cartella_Paziente(request):

    #IMPLEMENT THIS WITH BACKEND
    patient_id = request.GET.get('id')

    name_example = [
    'Achille', 'Achille', 'Ada', 'Adam', 'Adelaide', 'Adele', 'Aden', 'Adolfo', 'Adriana', 'Adriano',
    'Agape', 'Agata', 'Agatha', 'Agnese', 'Agostina', 'Agostino', 'Aiace', 'Aida', 'Akira', 'Alba',
    'Albarosa', 'Alberico', 'Albert', 'Alberta', 'Alberto', 'Aldo', 'Alejandro', 'Alessandra', 'Alessandro',
    'Alessia', 'Alessio', 'Alexander', 'Alfio', 'Alfonso', 'Alfredo', 'Alice', 'Martina',
    'Achille', 'Achille', 'Ada', 'Adam', 'Adelaide', 'Adele', 'Aden', 'Adolfo', 'Adriana', 'Adriano',
    'Agape', 'Agata', 'Agatha', 'Agnese', 'Agostina', 'Agostino', 'Aiace', 'Aida', 'Akira', 'Alba',
    'Albarosa', 'Alberico', 'Albert', 'Alberta', 'Alberto', 'Aldo', 'Alejandro', 'Alessandra', 'Alessandro',
    'Alessia', 'Alessio', 'Alexander', 'Alfio', 'Alfonso', 'Alfredo', 'Alice', 'Martina'
    ]

    data = name_example[int(patient_id)]

    return render(request, "structure/includes/cartella_paziente.html",{
        'data': data
    })





def Calendario_Prenotazioni(request):

    



    return render(request, "structure/includes/calendario_prenotazioni.html")









def Elenco_Referti(request):
    return render(request, "structure/includes/elenco_referti.html")

def Tabella_Analisi(request):
    return render(request, "structure/includes/tabella_analisi.html")

def Sincronizzazione(request):
    return render(request, "structure/includes/sincronizzazione.html")