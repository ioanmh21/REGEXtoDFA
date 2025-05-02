# REGEXtoDFA
Conversia unei expresii regulate in DFA

## Programul implementat urmeaza urmatorii pasi in rezolvarea problemei:
1. Se adauga la expresia regulata operatorul de concatenare.
2. Se trece expresia in forma poloneza.
3. Se construieste un NFA pentru expresia rezultata folosind algoritmul lui Thompson.
4. NFA-ul rezultat este convertit in DFA prin subset construction.
