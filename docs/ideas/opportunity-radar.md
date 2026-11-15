# Opportunity Radar — jubileusze kół wędkarskich

**Etap: koncepcja. Następny krok: ręczny pilotaż.**

Opportunity Radar ma znajdować organizacje, które przygotowują się do jubileuszu. Pierwszy przypadek to koła wędkarskie, którym można zaproponować jubileuszowy zestaw: koszulkę i żakardowe skarpety z motywem ryby, nazwą koła lub logo, barwami i rokiem jubileuszu. Fizyczna próbka dla prezesa lub zarządu pomoże pokazać, jak może wyglądać zamówienie grupowe.

## Zasięg i źródła

- **Niemcy:** Berlin i Brandenburgia. Zacząć od wykazów LAVB, związków okręgowych (Kreisanglerverbände), stron klubów i kalendarzy gmin.
- **Polska:** województwo lubuskie. Zacząć od stron okręgów i kół PZW, gmin, kalendarzy zawodów oraz lokalnych portali.
- Szukać zapowiedzi oraz wpisów historycznych, np. pod hasłami `jubileusz koła PZW`, `50-lecie koła wędkarskiego`, `Angelverein Jubiläum` i `Angelverein gegründet`.
- Rejestry, np. KRS i Vereinsregister, mogą pomóc ustalić tożsamość organizacji. Data wpisu do rejestru i data założenia to osobne pola. Wpisy społecznościowe służą jako wskazówka do dalszej weryfikacji.

## Od źródła do listy potencjalnych klientów

1. Znaleźć koło i połączyć powtarzające się wpisy po nazwie, miejscowości i oficjalnej stronie.
2. Sprawdzić zapowiedź obchodów albo odszukać wiarygodne źródło roku założenia. Wyliczyć lata 25-, 30- i 50-lecia. Zapisać osobno rok wynikający z obliczeń i datę ogłoszonego wydarzenia.
3. Ustalić priorytet na podstawie terminu, aktualnych wydarzeń, publicznego kontaktu organizacyjnego i możliwości dojazdu. Jeśli są dostępne, odnotować liczbę członków i informacje o wcześniejszych gadżetach lub odzieży klubowej.
4. Oddać listę do ręcznego przeglądu. Każdy wiersz powinien pokazywać dowód, status i powód priorytetu. Kontakt następuje po ręcznej decyzji.

**Status dowodu**

| Status | Jak go przypisać |
| --- | --- |
| Ogłoszone obchody | Organizacja, związek lub gmina opublikowała zapowiedź z terminem. |
| Jubileusz wyliczony | Wiarygodne źródło podaje datę lub rok założenia. Gdy znany jest tylko rok, dokładny termin pozostaje do sprawdzenia. |
| Do weryfikacji | Źródła są sprzeczne, zbyt ogólne albo podają tylko datę rejestracji. |

**Pola raportu:** organizacja, miejscowość, region, strona, rok założenia, typ jubileuszu, rok jubileuszu, data obchodów (jeśli ogłoszona), status dowodu, link i krótki opis dowodu, data sprawdzenia, aktywność, publiczny kanał kontaktu, priorytet i uzasadnienie.

## Rejestry i API (ustalenia z 2026-11-15)

- **KRS (Polska):** otwarte API Ministerstwa Sprawiedliwości działało w lipcu 2026 bez klucza, ale wyszukuje wyłącznie po numerze KRS, NIP lub REGON. Nie ma wyszukiwania po nazwie, więc nie nadaje się do znajdowania kół. Przed budową integracji sprawdzić aktualne zasady, bo pojawiły się zapowiedzi, że dostęp do API ma wymagać zgody Ministra Sprawiedliwości.
- **Koła PZW nie są w KRS:** koło PZW jest jednostką terenową bez osobowości prawnej, powoływaną uchwałą zarządu okręgu i wpisywaną do rejestru kół prowadzonego przez okręg. Osobowość prawną mogą mieć dopiero okręgi, i te są w KRS (np. Okręg w Zielonej Górze).
- **Wniosek:** w Polsce rok założenia koła brać ze stron okręgów i samych kół oraz z rejestru kół okręgu. KRS używać do weryfikacji okręgów oraz niezależnych klubów wędkarskich, które są osobnymi stowarzyszeniami.
- **Vereinsregister (Niemcy):** darmowego oficjalnego API do masowych zapytań nie znamy. Na razie ręczny pilotaż. Do sprawdzenia przed automatyzacją: regulamin rejestru wobec zautomatyzowanych zapytań.

## Pilotaż

Ręcznie przejrzeć **25–30 kół wędkarskich**, zaczynając od Brandenburgii. Priorytetem są okazje w horyzoncie **3–12 miesięcy**. Przypadki ze znanym tylko rokiem trafiają do sprawdzenia terminu. Na koniec policzyć, dla ilu kół udało się potwierdzić rok założenia, znaleźć przyszły jubileusz i znaleźć publiczny kontakt. Sprawdzić, które źródło dostarczyło najwięcej użytecznych wyników. Na tej podstawie wybrać pierwsze źródło do automatyzacji lub zmienić źródła, jeśli pokrycie okaże się zbyt słabe.

## Powiązane pomysły do rozwinięcia

| Pomysł | Co można sprawdzić po pilotażu |
| --- | --- |
| Jubileusze innych organizacji | Użyć tych samych pól dla kół łowieckich, OSP, klubów motocyklowych i sportowych. |
| Lokalne wydarzenia | Z kalendarzy gmin i organizatorów wyszukiwać zloty, zawody i festyny, przy których może przydać się odzież lub pamiątka dla uczestników. |
| Job Radar | W osobnym przepływie zbierać już opublikowane zlecenia, np. z Upwork, i oceniać dopasowanie do portfolio. |

Dzisiejszy ClientRadar AI analizuje firmy z CSV, sprawdza ich strony i generuje raport. Opportunity Radar rozszerzyłby ten przepływ o odkrywanie organizacji oraz weryfikację dowodów przed kwalifikacją potencjalnego klienta.
