# Importovanje biblioteke spaCy za obradu prirodnog jezika
import spacy  # spaCy se koristi za analizu i obradu teksta

# Učitaj modele za engleski i hrvatski jezik
nlp_en = spacy.load("en_core_web_sm")  # Učitava engleski jezički model
nlp_hr = spacy.load("hr_core_news_sm")  # Učitava hrvatski jezički model

# Definisanje funkcije za obradu teksta
def process_text(text, language='en'):
    if language == 'en':  # Provjerava da li je izabrani jezik engleski
        doc = nlp_en(text)  # Ako jeste, koristi engleski model za obradu teksta
    else:
        doc = nlp_hr(text)  # Ako nije, koristi hrvatski model za obradu teksta 

    return doc.text  # Vraća obrađeni tekst u formi stringa
