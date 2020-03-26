# Was ist die Fehler?

a, b = 0, 1

while b < 10:
    a, b, c = b, a + b, a*b
    
print('a egal ',a, ', b = ',b,  ', c = ', a, ' x ', b,'; also c = ',c )

print('8x13 = 40?! Wo ist die Fehler?')    
