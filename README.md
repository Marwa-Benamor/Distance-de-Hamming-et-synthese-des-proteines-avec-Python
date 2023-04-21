# Distance-de-Hamming-et-synthese-des-proteines-avec-Python
Ceci est un projet Python qui contient trois scripts pour calculer la distance de Hamming de deux séquences de nucléotides, transformer une séquence d'ARNm en une séquence protéique, et synthétiser des protéines à partir d'une séquence d'ARNm en utilisant le code génétique. Les scripts sont conçus pour être conviviaux et vérifient que les entrées de l'utilisateur sont valides avant de commencer le calcul. Le projet utilise un dictionnaire Python pour représenter le code génétique et permet de synthétiser des protéines à partir de n'importe quelle séquence d'ARNm en identifiant les codons initiateurs et stop.
"Distance de Hamming.py" est un script Python qui calcule la distance de Hamming de deux séquences de nucléotides:
L'utilisateur saisit les deux séquences et le script calcule la distance de Hamming (le nombre de différences entre les deux séquences)
Le script doit vérifier :
- les deux séquences sont composées de nucléotides (A, C, G, T)
- les deux séquences ont la même taille
Si dans l'une des deux séquences il existe un caractère n'appartenant pas à (A, C, G, T) ou les
deux séquences ne sont pas de même taille, l'utilisateur doit resaisir la séquence.
"Transformation d'ARNm en protéine.py" est un un script python qui transforme une séquence d'ARN messager (séquence de A,C,G et U) en une séquence protéique formée par des acides aminés.
Le script doit définir la structure de données python Dictionnaire pour représenter le code génétique. Le dictionnaire CG est composé de deux éléments : la clé contenant le codon et la valeur contenant l'abrégé de l'acide aminé correspondant.
Exemple :
CG = { "UUU" : "F" ,
"UUC" : "F" ,
"UUA" : "L", ...}
- L'utilisateur saisit une séquence d'ARN messager.
- Le script extrait les codons (3 nucléotides) de l'ARN messager, cherche dans le dictionnaire l'acide aminé correspondant et l'insère dans la séquence protéique.
- A la fin de l'exécution, le script retourne la séquence protéique synthétisée.
"Séquence protéique.py" est un script python qui utilise le script de "Transformation d'ARNm en protéine.py" pour synthétiser les protéines à partir d'une séquence d'ARN messager.
Sachant qu'une protéine commence à partir du codon initiateur : AUG (méthionine) et se termine par un codon Stop (UAA, UAG ou UGA).
Le script cherche dans la séquence d'ARN messager le point de départ c-à-d le codon initiateur, il synthétise la protéine et s'arrête quand il rencontre un codon Stop.
