lang_map = {
    "A": "@",
    "B": "8",
    "C": "(",
    "D": "|)",
    "E": "3",
    "F": "#",
    "G": "6",
    "H": "[-]",
    "I": "|",
    "J": "_|",
    "K": "|<",
    "L": "1",
    "M": "[]\\/[]",
    "N": "[]\\[]",
    "O": "0",
    "P": "|D",
    "Q": "(,)",
    "R": "|Z",
    "S": "$",
    "T": "']['",
    "U": "|_|",
    "V": "\\/",
    "W": "\\/\\/",
    "X": "}{",
    "Y": "`/",
    "Z": "2"
}

sentence = input()
s = ""
for ch in sentence:
    o = ord(ch)
    if 97 <= o <= 122:
        s += "".join(lang_map[chr(o - 32)])  
    elif 65 <= o <= 90:
        s += "".join(lang_map[ch])
    else:
        s += "".join(ch)
print(s)