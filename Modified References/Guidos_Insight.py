# Modified version from example at Python Tutorial 4.7, several editions.

import random

Guidos_Einblick = "Ein Text ist wahrscheinlich viel gelesen als geschriben"
Guidos_Insight = "Texts are more read than written (from PEP8)"                   

def ask_ok(prompt, retries = 3, please = 'Try again'):
    while True:
        ok = input(prompt + '\n')
        if ok.lower() in ('y', 'ye', 'yes', 'yep', 'yeh'): return True
        if ok.lower() in ('no', 'n', 'nope', 'ne'): return False
        retries = retries - 1
        if retries < 0:
            raise IOError("Invalid user answer")
        print(please)

