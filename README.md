# REGEXtoDFA
Conversia unei expresii regulate in DFA

## Programul implementat urmeaza urmatorii pasi in rezolvarea problemei:
1.  Se adauga la expresia regulata operatorul de concatenare.
2.  Se trece expresia rezultata in forma poloneza.
3.  Se construieste un NFA pentru expresia in forma poloneza, folosind algoritmul lui 
 Thompson.
4.  NFA-ul rezultat este convertit in DFA prin subset construction.
