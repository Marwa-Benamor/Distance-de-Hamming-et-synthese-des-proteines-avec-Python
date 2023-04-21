seq = ""
while 1:
    y = input("Saisissez un caractère A C G T de la 1ère séquence: ")
    if y not in ["A","C","G","T"]:
        while 1:
            y = input("Saisissez un caractère A C G T svp: ")
            if y in ["A","C","G","T"]: break
    seq = seq+y
    f = input("Si vous voulez continuer saisir oui sinon cliquer sur n'importe quelle touche: ")
    if not (f == "oui" or f == "Oui" or f == "OUI"): break
print("Votre 1ère sequence est : ", seq)
seq2 = ""
while 1:
    y = input("Saisissez un caractère A C G T de la 2ème séquence: ")
    if y not in ["A","C","G","T"]:
        while 1:
            y = input("Saisissez un caractère A C G T svp: ")
            if y in ["A","C","G","T"]: break
    seq2 = seq2+y    
    if len(seq)==len(seq2): break
print("Les deux séquences sont successivement : ", seq, seq2)
d=0
for i in range(0, len(seq)):
    if seq[i]!=seq2[i]:
        d=d+1
print("La distance de Hamming est:", d)