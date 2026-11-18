import json
import random

def wczytaj_pytania(nazwa_pliku):
    try:
        with open(nazwa_pliku, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Nie znaleziono pliku {nazwa_pliku}. Upewnij się, że plik JSON jest w tym samym katalogu.")
        return []

def uruchom_quiz(pytania):
    if not pytania:
        return

    # Losowa kolejność pytań
    random.shuffle(pytania)
    
    punkty = 0
    liczba_pytan = len(pytania)

    print(f"Rozpoczęto quiz! Łącznie pytań w bazie: {liczba_pytan}\n")
    print("=" * 60)

    for i, q in enumerate(pytania, 1):
        print(f"\nPytanie {i}/{liczba_pytan}:")
        print(f"** {q['question']} **\n")

        # Wyświetlanie opcji odpowiedzi
        opcje = q['options']
        for opcja in opcje:
            print(f"  {opcja['id']}. {opcja['text']}")

        # Pobieranie odpowiedzi od użytkownika (obsługa wielu poprawnych odpowiedzi, np. w pytaniu 22 i 34)
        poprawne_id = [o['id'] for o in opcje if o['is_correct']]
        
        while True:
            odpowiedz_str = input("\nTwoja odpowiedź (podaj numer opcji lub numery oddzielone przecinkiem): ").strip()
            try:
                # Rozdzielenie po przecinku, jeśli użytkownik podaje kilka odpowiedzi
                wybrane_ids = [int(x.strip()) for x in odpowiedz_str.split(',') if x.strip()]
                if wybrane_ids:
                    break
            except ValueError:
                pass
            print("Nieprawidłowy format. Wpisz numer (np. 2) lub numery po przecinku (np. 1, 3).")

        # Sprawdzenie poprawności
        # Użytkownik musi podać dokładnie te same ID, które są oznaczone jako poprawne
        if set(wybrane_ids) == set(poprawne_id):
            print("✅ Poprawnie!")
            punkty += 1
        else:
            print("❌ Błędnie.")
            poprawne_teksty = [f"{o['id']}. {o['text']}" for o in opcje if o['is_correct']]
            print(f"Prawidłowa odpowiedź to: {', '.join(poprawne_teksty)}")

        print("-" * 60)
        
        kontynuacja = input("Naciśnij Enter, aby przejść dalej (lub wpisz 'koniec', aby przerwać): ").strip().lower()
        if kontynuacja == 'koniec':
            print("\nPrzerwano quiz.")
            break

    print(f"\nKoniec quizu! Twój wynik: {punkty} / {i}")

if __name__ == "__main__":
    plik_json = "pytania_sieci.json"
    baza_pytan = wczytaj_pytania(plik_json)
    uruchom_quiz(baza_pytan)