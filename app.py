# Importovanje potrebnih biblioteka
from flask import Flask, request, render_template  # Flask za web aplikaciju, request za rukovanje HTTP zahtjevima, render_template za renderovanje HTML šablona
from src.pdf_utils import extract_text_from_pdf  # Uvoz funkcije za ekstrakciju teksta iz PDF datoteka
from src.text_processing import process_text  # Uvoz funkcije za procesiranje teksta 
from src.question_generation import generate_questions  # Uvoz funkcije za generisanje pitanja
import spacy  # Uvoz spaCy biblioteke za obradu prirodnog jezika

# Učitavanje hrvatskog modela za spaCy
nlp = spacy.load('hr_core_news_sm')  # Učitava model za hrvatski jezik koji se koristi za analizu teksta

# Kreiranje instance Flask aplikacije
app = Flask(__name__)

# Povećavanje maksimalne veličine datoteke na 16 MB
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Podešava maksimalnu veličinu datoteke koja se može poslati na 16 megabajta

# Definisanje rute za glavni URL
@app.route('/', methods=['GET', 'POST'])  # Ova ruta može primati GET i POST zahtjeve
def index():
    if request.method == 'POST':  # Provjerava da li je zahtev POST (slanje podataka)
        
        input_type = request.form['input_type']  # Prepoznaj koji unos je odabran (PDF ili tekst)

        language = request.form['language']

        if input_type == 'pdf':
            file = request.files['pdf_file']
            text = extract_text_from_pdf(file)
        elif input_type == 'text':
            text = request.form.get('text', '').strip()  # Uzimanje teksta iz forme i brisanje viška praznih prostora
            if not text:
                return "No text provided"  # Prikaži poruku ako je tekst prazan
        
        # Procesiraj tekst sa spaCy
        doc = nlp(text)
        processed_text = " ".join([token.text for token in doc])

        # Generiši pitanja
        questions = generate_questions(processed_text)
        return render_template('results.html', questions=questions)

    return render_template('index.html')
        
# Pokretanje Flask aplikacije
if __name__ == '__main__':
    app.run(debug=True)  # Pokreće aplikaciju u režimu za debagovanje, omogućavajući automatsko osvježavanje kod promena
