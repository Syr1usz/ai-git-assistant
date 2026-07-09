import subprocess
import sys
import os
import google.genai as genai
from dotenv import load_dotenv

# Wczytujemy zmienne z pliku .env
load_dotenv()

# 1. Definiujemy kolory
GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'

# 2. Konfiguracja AI (Klucz pobierany jest bezpiecznie z ukrytego pliku!)
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print(f"{RED}Błąd: Nie znaleziono klucza API w pliku .env!{RESET}")
    sys.exit()

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-flash-latest')

def pobierz_zmiany():
    wynik = subprocess.run(['git', 'diff', '--cached'], capture_output=True, text=True)
    return wynik.stdout

print(f"{CYAN}Uruchamiam skaner AI...{RESET}")
zmiany = pobierz_zmiany()

if not zmiany.strip():
    print(f"{RED}Brak plików do analizy! Najpierw zrób 'git add nazwa_pliku.py'{RESET}")
    sys.exit()

print(f"{GREEN}Znaleziono zmiany. Wysyłam do Google...{RESET}\n")

# Polecenie z restrykcyjnym formatem
polecenie = f"""
Jesteś rygorystycznym Code Reviewerem. Przeanalizuj poniższe zmiany:

{zmiany}

Zwróć odpowiedź DOKŁADNIE w tym formacie (nie używaj pogrubień, gwiazdek ani markdowna):

PROPOZYCJA COMMITA:
[Jedno krótkie zdanie podsumowujące zmianę, bez kropki na końcu]

UWAGI:
[Twoje uwagi w punktach]
"""

response = model.generate_content(polecenie)
raport = response.text

# 3. Kolorowy wydruk w konsoli
print(f"{YELLOW}================ RAPORT BĘDŹ_BOLD(ARE) ================={RESET}")
print(raport)
print(f"{YELLOW}========================================================{RESET}\n")

# 4. Magia wyciągania samej wiadomości do commita
linie = raport.split('\n')
wiadomosc = ""
for i, linia in enumerate(linie):
    if "PROPOZYCJA COMMITA:" in linia.upper():
        # Pobieramy to, co jest w linijce pod spodem
        wiadomosc = linie[i+1].strip()
        # Jeśli sztuczna inteligencja dodała pustą linię, bierzemy kolejną
        if not wiadomosc and i + 2 < len(linie):
            wiadomosc = linie[i+2].strip()
        break

# Usuwamy ewentualne formatowanie
wiadomosc = wiadomosc.replace('**', '').replace('"', '')

# 5. Pytanie do użytkownika i automatyczny commit
if wiadomosc:
    decyzja = input(f"{CYAN}Czy chcesz zapisać ten kod w Gicie z powyższą wiadomością? [Y/N]: {RESET}")
    
    if decyzja.lower() == 'y':
        print(f"\nWykonuję: git commit -m \"{wiadomosc}\"")
        wynik_commit = subprocess.run(['git', 'commit', '-m', wiadomosc], capture_output=True, text=True)
        
        if wynik_commit.returncode == 0:
            print(f"{GREEN}Sukces! Zmiany zostały oficjalnie zapisane.{RESET}")
        else:
            print(f"{RED}Coś poszło nie tak:{RESET}\n{wynik_commit.stderr}")
    else:
        print(f"{YELLOW}Anulowano. Kod nie został zapisany.{RESET}")
else:
    print(f"{RED}Błąd parsowania: Nie udało się wyciągnąć wiadomości z tekstu.{RESET}")