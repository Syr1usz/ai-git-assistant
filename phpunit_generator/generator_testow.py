import os
import sys
from dotenv import load_dotenv
from google import genai # <-- Nowa, oficjalna biblioteka

# 1. Ładowanie klucza z Twojego bezpiecznego sejfu (.env)
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("Błąd: Nie znaleziono klucza API w pliku .env!")
    sys.exit()

# 2. Nowy sposób połączenia z AI
client = genai.Client(api_key=API_KEY)

# 3. Nazwa pliku, który chcemy przetestować
plik_z_kodem = 'Koszyk.php'
print(f"Czytam plik {plik_z_kodem}...")

# 4. Wczytywanie zawartości pliku PHP
try:
    with open(plik_z_kodem, 'r', encoding='utf-8') as plik:
        kod_php = plik.read()
except FileNotFoundError:
    print(f"Błąd: Nie znaleziono pliku {plik_z_kodem}!")
    sys.exit()

# 5. Tworzenie prompta dla AI (Zaktualizowana, twarda wersja)
polecenie = f"""
Jesteś ekspertem od testowania w PHP (PHPUnit).
Poniżej znajduje się kod klasy w PHP:

{kod_php}

Napisz kompletny, profesjonalny test jednostkowy w PHPUnit dla tej klasy.
Zwróć TYLKO czysty kod PHP zaczynający się od <?php, bez żadnego formatowania markdown, bez znaczników ```php i bez żadnych wyjaśnień.

ABSOLUTNIE WYMAGANE ZASADY:
1. Zaraz na początku pliku, pod deklaracjami 'use', MUSISZ dodać linijkę: require_once 'Koszyk.php';
2. Nie twórz ani nie odwołuj się do żadnych dodatkowych klas (np. Product), których nie ma w podanym kodzie.
"""

print("Wysyłam kod do AI i generuję testy (to może chwilę potrwać)...")

# 6. Nowy, zaktualizowany sposób wysyłania zapytania (używamy modelu gemini-2.5-flash)
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=polecenie,
)

# 7. Oczyszczanie odpowiedzi
wygenerowany_kod = response.text.replace('```php', '').replace('```', '').strip()

# 8. Zapisywanie wyniku do nowego pliku
nazwa_testu = 'KoszykTest.php'
with open(nazwa_testu, 'w', encoding='utf-8') as plik_testu:
    plik_testu.write(wygenerowany_kod)

print(f"Sukces! Wygenerowano plik z testami w najnowszym standardzie: {nazwa_testu}")