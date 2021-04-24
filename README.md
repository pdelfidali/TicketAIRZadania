# TicketAIRZadania
Zadania do prezentacji aplikacji TicketAIR

# Zadanie 1
W pliku TicketAir.py w klasie Database została stworzona funkcja create_tables(). Tworzymy w niej tabele lotów, użytkowników i biletów. Zmodyfikuj funkcję w ten sposób, aby została również stworzona tabela samolotów. Zwróć uwagę, żeby wartości miały odpowiedni typ tailNumber (text), year (integer), flightMiles (real), capacity (integer).


# Zadanie 2
W pliku TicketAir.py w klasie Database uzupełnij funkcję addPlane () tak, aby dodawała do tabeli nowy wiersz z odpowiednimi wartościami samolotu. Musisz dokonać połączenia z bazą danych, stworzyć obiekt cursor i wykonać na nim komendę SQL i na koniec zamknąć połączenie.
Dodatkowo: Upewnij się, że klasa Plane zwraca wartości: tailNumber, yearOfProduct, flightMiles, capacity oraz że jest zaimportowany moduł sqlite3.
Wskazówka: Sprawdź strukturę funkcji addFlight().


# Zadanie 3
Na razie cena biletu jest zależna jedynie od ilości osób i lotu, jednak w okienku z kupowaniem zostały stworzone dodatkowo radioboxy z rozmiarem bagażu. Spróbuj uzupełnić kod w taki sposób, żeby rodzaj bagażu miał wpływ na cenę końcową biletu. 
Uwaga: Bagaż poniżej 15kg powinien zwiększać cenę biletu o 5% a cięższy o 15%
