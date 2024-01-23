# python-algebra
 


# tools:
- aggr(a,s):
  - aggrega una lista di termini esponenziali passati come parametro formattata in formato listpol:
  - 
    ['a^5', 'b', '^', '2', 'c', '^', '3']

    diventa:
    ['a^5', 'b^2', 'c^3']

- letpart(mon):
  - restituisce la parte letterale di un monomio
- lispol(a):
  - converte una stringa in un array in formato listpol, fondamentale per tutte le operazioni

- semplmolt(a):
   accetta polinomi STRINGA originati da polmolt e li converte in formato  pronto per algsum SENZA SEGNO + chiama inoltre aglsum nuovo e ritorna il risultato
36x^2-60x^2+12x^2-20x^2



# operazioni:

- algmolt(a,b):
  - moltiplicazioni di due monomi, da passare in formato listpol
  
- newsum(a,b):
  - somma di due monomi 
  
- algsum(arr):
  - somma algebrica di un array di monomi
- polmolt(a,b):
  - moltiplicazione di polinomi

- sempl(a):
  - semplifica un polinomio facendo la somma algebrica tra i suoi termini dove possibilie