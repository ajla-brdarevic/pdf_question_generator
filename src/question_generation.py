# Importovanje pipeline-a iz biblioteke transformers
from transformers import pipeline  # pipeline omogućava jednostavan pristup raznim modelima za zadatke obrade prirodnog jezika

# Učitaj model za generisanje pitanja
question_generator = pipeline("text2text-generation", model="Narrativa/mT5-base-finetuned-tydiQA-question-generation")  # Inicijalizuje model koji je obučen za generisanje pitanja iz tekstualnog sadržaja

# Definisanje funkcije za generisanje pitanja
def generate_questions(text):
    # Poziva question_generator sa zadatim tekstom i opcijama za generisanje pitanja
    questions = question_generator(
        text,  # Ulazni tekst iz kojeg se generišu pitanja
        max_length=50,  # Maksimalna dužina generisanih pitanja
        num_beams=5,  # Broj "beam search" pretraga za generisanje boljih pitanja
        num_return_sequences=2  # Broj generisanih pitanja koja će se vratiti
    )
    
    # Vraća listu generisanih pitanja iz rezultata
    return [question['generated_text'] for question in questions]  # Ekstraktuje generisana pitanja iz rezultata
