
CG = {
      "UUU" : "F" ,
      "UUC" : "F" ,
      "UUA" : "L" ,
      "UUG" : "L" ,
      "CUU" : "L" ,
      "CUC" : "L" ,
      "CUA" : "L" ,
      "CUG" : "L" ,
      "AUU" : "I" ,
      "AUC" : "I" ,
      "AUA" : "I" ,
      "AUG" : "M" ,
      "GUU" : "V" ,
      "GUC" : "V" ,
      "GUA" : "V" ,
      "GUG" : "V" ,
      "UCU" : "S" ,
      "UCC" : "S" ,
      "UCA" : "S" ,
      "UCG" : "S" ,
      "CCU" : "P" ,
      "CCC" : "P" ,
      "CCA" : "P" ,
      "CCG" : "P" ,
      "ACU" : "T" ,
      "ACC" : "T" ,
      "ACA" : "T" ,
      "ACG" : "T" ,
      "GCU" : "A" , 
      "GCC" : "A" ,
      "GCA" : "A" ,
      "GCG" : "A" ,
      "UAU" : "Y" ,
      "UAC" : "Y" ,
      "UAA" : "X",
      "UAG" : "X",
      "CAU" : "H" ,
      "CAC" : "H" ,
      "CAA" : "Q" ,
      "CAG" : "Q" ,
      "AAU" : "N" ,
      "AAC" : "N" ,
      "AAA" : "K" ,
      "AAG" : "K" ,
      "GAU" : "D" ,
      "GAC" : "D" ,
      "GAA" : "E" ,
      "GAG" : "E" ,
      "UGU" : "C" ,
      "UGC" : "C" ,
      "UGA" : "X",
      "UGG" : "W" ,
      "CGU" : "R" ,
      "CGC" : "R" ,
      "CGA" : "R" ,
      "CGG" : "R" ,
      "AGU" : "S" ,
      "AGC" : "S" ,
      "AGA" : "R" , 
      "AGG" : "R" ,
      "GGU" : "G" ,
      "GGC" : "G" ,
      "GGA" : "G" ,
      "GGG" : "G" 
           
      }
seq = input ("saisir une séquence d'ARN :")
d=0
for i in range (0,len (seq)): 
        if seq[i] not in ["A","U","G","C"]:
            d=d+1
if d!=0:
    while 1:
        d=0
        seq = input ("saisir une autre séquence d'ARN :")
        for i in range (0,len (seq)): 
            if seq[i] not in ["A","U","G","C"]:
                d=d+1        
        if d==0:break 
i = 0
d=""
if seq[0:3]=="AUG":
    i=0
else:
    while i <len(seq)-2 and d != "AUG":
        i=i+1
        d=seq[i]+ seq[i+1]+seq[i+2]
        
b="M"
j=i+3
a=""
while j <len(seq)-2 and not (a in ["UAA","UGA","UAG"]):
    
    a=seq[j]+seq[j+1]+seq[j+2]
    b=b+CG[a]
    j=j+3
print ("La séquence protéique est: ",b)