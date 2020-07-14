# Attention is freely modeled by a so clammed Smart Hiperaktiv. 

import random

Liste = "Learn a Liste"
Tupel = Liste, "Lern Listen", "Make a class"
Lern = Liste, Tupel

Optionen = "Lerne Listen", "Lerne über Tupel", "Python", "English", "German"

goal = random.choice(Optionen)

class Fokus:
    def __init__(self, goal):   
        self.goal = goal
        self.any = Optionen
    pass
