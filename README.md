# Regular Expression to DFA Converter

Acest repository conține un script Python care transformă o expresie regulată într-un automat finit determinist (DFA). Procesul implică următorii pași principali, implementați în fișierul `functions.py` și utilizați în `main.py`:

## Pașii Procesului

1.  **Adăugarea Operatorului de Concatenare:**
    La expresia regulată inițială se adaugă explicit operatorul de concatenare (de exemplu, '.') acolo unde este cazul (ex. `ab` devine `a.b`, `a(bc)` devine `a.(b.c)`). Acest lucru este realizat de funcția `add_operatori_concatenare(regex)` din `functions.py`.

2.  **Conversia în Forma Poloneză (Postfix):**
    Expresia regulată, acum cu operatorii de concatenare expliciți, este convertită în forma poloneză (notație postfix). Această transformare ajută la construirea mai ușoară a NFA-ului. Conversia este gestionată de funcția `forma_poloneza(regex)` din `functions.py`.

3.  **Construcția NFA-ului (Algoritmul lui Thompson):**
    Pe baza expresiei în formă poloneză, se construiește un automat finit nedeterminist (NFA) utilizând algoritmul lui Thompson. Fiecare operator și operand din forma poloneză corespunde unei construcții specifice în NFA. Această etapă este implementată în funcția `thompson_nfa(postfix)` din `functions.py`.

4.  **Conversia NFA în DFA (Construcția prin Submulțimi):**
    NFA-ul rezultat este apoi convertit într-un automat finit determinist (DFA) prin metoda construcției prin submulțimi (subset construction). Acest algoritm elimină nedeterminismul și tranzițiile epsilon. Funcția responsabilă pentru această conversie este `nfa_to_dfa(nfa, alphabet)` din `functions.py`. Alfabetul necesar pentru construcția DFA este extras inițial din expresia regulată folosind funcția `alfabet(regex)`.

## Utilizare

Fișierul `main.py` încarcă expresii regulate dintr-un fișier JSON (în exemplu, `LFA-Assignment2_Regex_DFA_v2.json`), aplică pașii de conversie de mai sus și apoi testează DFA-ul rezultat cu șiruri de test specificate în același fișier JSON. Simularea DFA-ului pe un șir de intrare este realizată de funcția `simulate_dfa(dfa, word)`.

## Fișiere

* `main.py`: Scriptul principal care orchestrează procesul de conversie și testare.
* `functions.py`: Modulul care conține implementările pentru toți pașii algoritmici (adăugare concatenare, formă poloneză, construcție NFA Thompson, conversie NFA-DFA, simulare DFA).
* `LFA-Assignment2_Regex_DFA_v2.json` (exemplu): Fișier JSON care conține expresiile regulate de procesat și cazurile de test.
