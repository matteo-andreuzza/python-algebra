from newsum import newsum
from listpol import listpol
from newmolt import algmolt
from main import algsum
from polmolt import polmolt
from semplmolt import sempl
print("""
      \_/
     (* *)
    __)#(__
   ( )...( )(_)
   || |_| ||//
>==() | | ()/
    _(___)_
   [-]   [-]
      ***** PYTHON-ALGEBRA ****
      scegli cosa fare!
      
      ## MONOMI ##
      + : somma due monomi
      * : moltiplica due monomi
      ++: somma più monomi
      ## POLINOMI ##
      ** : moltiplica due polinomi
      **/ : moltiplica e semplifica due polinomi
      
      """)

a = input("scegli:")

match a:
    case '+':
        print("""  
      \_/
     (* *)
    __)#(__
   ( )...( )(_)
   || |_| ||//
>==() | | ()/
    _(___)_
   [-]   [-]   
*** FORMATO ***
newsum("2a^2", '2a^2')
      """)
        a = input("inserire monomio 1")
        b = input("inserire monomio 2")
        print(newsum(a,b))
    case "*":
        print("""
      \_/
     (* *)
    __)#(__
   ( )...( )(_)
   || |_| ||//
>==() | | ()/
    _(___)_
   [-]   [-]
*** FORMATO ***
algmolt(listpol("6ab"), listpol("2ab"))
      """)
        a = input("inserire monomio 1")
        b = input("inserire monomio 2")
        print(algmolt(listpol(str(a)), listpol(str(b))))
    case '++':
        print("""
      \_/
     (* *)
    __)#(__
   ( )...( )(_)
   || |_| ||//
>==() | | ()/
    _(___)_
   [-]   [-]
*** FORMATO ***
algsum(['-5pq', '6pq', '-10pq'])
      """)
        n = input("inserire numero di elementi da inserire")
        x = []
        for i in range(int(n)):
            x.append(input("inserire monomio"))
        print(algsum(x))
        
    case "**":
        print("""      
      \_/
     (* *)
    __)#(__
   ( )...( )(_)
   || |_| ||//
>==() | | ()/
    _(___)_
   [-]   [-]
*** FORMATO ***
polmolt(['a^2b^2'], ['a^2c', '2ac']))
      """)
        n = input("inserire numero di elementi da inserire polinomio 1")
        n1 = input("elmenti polinomio 2")
        x = []
        x1 = []
        for i in range(int(n)):
            x.append(input("inserire monomio pol 1"))
        for i in range(int(n1)):
            x1.append(input("inserire monomio pol 2"))
        print(polmolt(x,x1))
        
    case "**/":
        print("""
      \_/
     (* *)
    __)#(__
   ( )...( )(_)
   || |_| ||//
>==() | | ()/
    _(___)_
   [-]   [-]
        *** FORMATO ***
        polmolt(['a^2b^2'], ['a^2c', '2ac']))
            """)
        n = input("inserire numero di elementi da inserire polinomio 1")
        n1 = input("elmenti polinomio 2")
        x = []
        x1 = []
        for i in range(int(n)):
            x.append(input("inserire monomio pol 1"))
        for i in range(int(n1)):
            x1.append(input("inserire monomio pol 2"))
        print(sempl(polmolt(x,x1)))

    case _ :
        print("\nErrore: comando sconosciuto.\nRiprova.")