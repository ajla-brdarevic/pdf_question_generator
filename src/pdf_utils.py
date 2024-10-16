# Importovanje potrebne biblioteke za rad sa PDF datotekama
import PyPDF2  # PyPDF2 se koristi za čitanje i obradu PDF datoteka

# Definisanje funkcije za ekstrakciju teksta iz PDF datoteke
def extract_text_from_pdf(pdf_file):
    text = ''  # Inicijalizuje prazan string za čuvanje ekstraktovanog teksta
    # Otvaranje PDF datoteke kao stream
    with pdf_file.stream as file:  # Koristi 'with' da automatski zatvori datoteku nakon upotrebe
        reader = PyPDF2.PdfReader(file)  # Učitava PDF datoteku u PdfReader objekat
        for page in reader.pages:  # Iterira kroz sve stranice u PDF-u
            text += page.extract_text() + '\n'  # Ekstrakuje tekst sa svake stranice i dodaje ga u string, uz novi red

    return text  # Vraća kompletan ekstraktovani tekst iz PDF datoteke
