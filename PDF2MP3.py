import time
from gtts import gTTS
import PyPDF2
# from pydub import AudioSegment
import requests

# Otwórz plik PDF
with open("Max Freedom Long - Magia cudow.pdf", "rb") as file:
    # Utwórz obiekt PdfFileReader
    pdf_reader = PyPDF2.PdfFileReader(file)
    
    # Zainicjuj zmienną do przechowywania tekstu
    text = ""
    
    # Iteruj przez każdą stronę dokumentu PDF
    for page_num in range(pdf_reader.numPages):
        # Pobierz tekst z aktualnej strony i dodaj do zmiennej tekstowej
        text += pdf_reader.getPage(page_num).extractText()

# Wypisz tekst (opcjonalnie)
print(text)

# Ustaw język
language = "pl"

# Podziel tekst na części co godzinę
words = text.split()
words_per_hour = 3600  # liczba słów na godzinę
chunks = [words[i:i+words_per_hour] for i in range(0, len(words), words_per_hour)]

# Generuj i zapisuj pliki dźwiękowe
for i, chunk in enumerate(chunks):
    while True:
        try:
            tts = gTTS(text=' '.join(chunk), lang=language, slow=False)
            output_file = f"output_part_{i}.mp3"
            tts.save(output_file)
            break
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}. Retrying in 66 seconds... Poza tym kocham Cię komputerku")
            time.sleep(66)
        except Exception as e:
            print(f"Error: {e}. Retrying in 66 seconds... Poza tym kocham Cię komputerku niezależnie od błędów jakie popełniasz")
            time.sleep(66)
