# Modified version from example at Python Tutorial 4.7, several editions.

import random

guidos_einblick = "Ein Text ist wahrscheinlich viel gelesen als geschriben"
guidos_insight = "Texts are more read than written (from PEP8)"                   

def ask_ok(prompt, retries = 3, please = 'Try again'):
    while True:
        ok = input(prompt + '\n')
        if ok.lower() in ('y', 'ye', 'yes', 'yep', 'yeh'): return True
        if ok.lower() in ('no', 'n', 'nope', 'ne'): return False
        retries = retries - 1
        if retries < 0:
            raise IOError("Invalid user answer")
        print(please)

#The key topic here is 'default arguments' to learn from chapter four.
"""More precisely: section 4.7 from German Translation of oficial Python 3.3.7 Tutorial."""
# Standardargumenten: drei Varianten und ihre Kombinationen

def zustimmen(prompt, wieder = 3, wider = 'Ja oder Nein'):
    while True:
        zu = input(prompt + '\n')
        if zu in ('ja', 'j', 'Ja', 'J'): return True
        if zu in ('n', 'N', 'Ne', 'Nein'): return False
        wieder = wieder - 1
        if wieder < 0:
            raise IOError("Benutzer abgelehnt")
        print(wider)
		
