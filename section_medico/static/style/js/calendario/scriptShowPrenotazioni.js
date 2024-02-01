function openModal(event, i) {
    event.preventDefault();
    var value = i;

    var modalParagraph = document.getElementById('modalParagraph');
    modalParagraph.textContent = value;



    // Filter and show relevant prenotazioni based on the date
    var prenotazioniElements = document.querySelectorAll('.prenotazione');
    var selectedDate = new Date(value); // Assuming value is in a format parseable by Date
    prenotazioniElements.forEach(function (prenotazione) {
        var dataAttribute = prenotazione.getAttribute('data-data');
        var prenotazioneDate = new Date(dataAttribute);

        // Check if the prenotazione's date is the same day as the selected date or later
        if (
            prenotazioneDate.getFullYear() >= selectedDate.getFullYear() &&
            prenotazioneDate.getMonth() >= selectedDate.getMonth() &&
            prenotazioneDate.getDate() >= selectedDate.getDate()
        ) {
            prenotazione.style.display = 'block';
        } else {
            prenotazione.style.display = 'none';
        }
    });

    document.getElementById('myModal').style.display = 'block';
    document.getElementById('overlay').style.display = 'block';
}


function closeModal() {
    // Reset the modal content
    var prenotazioniElements = document.querySelectorAll('.prenotazione');
    prenotazioniElements.forEach(function (prenotazione) {
        prenotazione.style.display = 'block';
    });

    document.getElementById('myModal').style.display = 'none';
    document.getElementById('overlay').style.display = 'none';
}