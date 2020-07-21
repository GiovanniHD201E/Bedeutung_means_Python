# Because one of my keyboards is problematic in some keys I searched a solution.

s3 = """´´O"""

s1 = ("´´a ´´e ´´o")
Text = s = s1 = ("angelapppsppplennnosaaahotnnnailpppconnn Esta certo issoiii \n"
          "Boas acoes mudam o mundo.")
s3 = "nnnzzzzzzNNNnnn"

print("O texto que você escreveu foi: \n", s, "\n")

def search(word, char):
        index = 0
        while index < len(word):
            if word[index] == char:
                return index
            index = index + 1
        return index

#The function using the for loop: 

def suchen(word, char):
        for index in range(len(word)):
            if word[index] == char:
                return index
        return len(word)

def ersetz(Text, alt, neu):
        neuText = ""
        len(alt) == len(neu)
        for i in range(len(Text)):
            if Text[i] == alt:
                neuText = neuText + neu
            else:
                neuText = neuText + Text[i]
        return neuText

while "´pv" in s:
    i = s.index('´pv')
    S = s[0:i] + ';' + s[i+3:len(s)]
    s = S

while "´n" in s:
    i = s.index('´n')
    S = s[0:i] + 'm' + s[i+2:len(s)]
    s = S

while "´dp" in s:
    i = s.index('´dp')
    S = s[0:i] + ':' + s[i+3:len(s)]
    s = S

while "iii" in s:
    i = s.index('iii')
    S = s[0:i] + '?' + s[i+3:len(s)]
    s = S

while "´ta" in s:
    i = s.index('´ta')
    S = s[0:i] + 'ã' + s[i+3:len(s)]
    s = S

while "´TA" in s:
    i = s.index('´TA')
    S = s[0:i] + 'Ã' + s[i+3:len(s)]
    s = S

while "´TO" in s:
    i = s.index('´TO')
    S = s[0:i] + 'Õ' + s[i+3:len(s)]
    s = S

while "´to" in s:
    i = s.index('´to')
    S = s[0:i] + 'õ' + s[i+3:len(s)]
    s = S

while "´b" in s:
    i = s.index('´b')
    S = s[0:i] + '/' + s[i+2:len(s)]
    s = S

while "´´a" in s:
    i = s.index('´´a')
    S = s[0:i] + 'â' + s[i+3:len(s)]
    s = S

while "´´A" in s:
    i = s.index('´´A')
    S = s[0:i] + 'Â' + s[i+3:len(s)]
    s = S

while "´´E" in s:
    i = s.index('´´E')
    S = s[0:i] + 'Ê' + s[i+3:len(s)]
    s = S

while "´´e" in s:
    i = s.index('´´e')
    S = s[0:i] + 'ê' + s[i+3:len(s)]
    s = S

while "nnn" in s:
    i = s.index('nnn')
    S = s[0:i] + 'm' + s[i+3:len(s)]
    s = S

while "´´i" in s:
    i = s.index('´´i')
    S = s[0:i] + '?' + s[i+3:len(s)]
    s = S

while "coes" in s:
    i = s.index('coes')
    S = s[0:i] + 'ções' + s[i+4:len(s)]
    s = S

while "NNN" in s:
    i = s.index('NNN')
    S = s[0:i] + 'M' + s[i+3:len(s)]
    s = S

while "zzz" in s:
    i = s.index('zzz')
    S = s[0:i] + "0" + s[i+3:len(s)]
    s = S

while "ppp" in s:
    i = s.index('ppp')
    S = s[0:i] + '.' + s[i+3:len(s)]
    s = S

while "´´p" in s:
    i = s.index('´´p')
    S = s[0:i] + '.' + s[i+3:len(s)]
    s = S

while "vvv" in s:
    i = s.index('vvv')
    S = s[0:i] + ',' + s[i+3:len(s)]
    s = S

while "´´v" in s:
    i = s.index('´´v')
    S = s[0:i] + ',' + s[i+3:len(s)]
    s = S

while "cao" in s:
    i = s.index('cao')
    S = s[0:i] + "ção" + s[i+3:len(s)]
    s = S

while "aaa" in s:
    i = s.index('aaa')
    S = s[0:i] + "@" + s[i+3:len(s)]
    s = S
    
while "´´o" in s:
    i = s.index('´´o')
    S = s[0:i] + 'ô' + s[i+3:len(s)]
    s = S 

while "´´O" in s:
    i = s.index('´´O')
    S = s[0:i] + 'Ô' + s[i+3:len(s)]
    s = S 

print("Ele foi substituído por: \n", s)
