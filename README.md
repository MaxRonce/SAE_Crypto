# SAE_Crypto
### Etudiants : 
- Antonin Reydet
- Maxime Ronceray
## Sujet : 

----------------------------
Les services secrets de l’empire de Kaota ont intercepté une série de 5 
messages qui semblent avoir été cryptés avec diverses méthodes un peu 
anciennes par les services de la planète oubliée Alfolol. </br>
Saurez-vous aider les services de Kaota à décrypter ces messages et trouver 
leur provenance ? </br>



PS :les messages sont listés dans les fichiers ``Texte1.txt ... Texte5.txt`` </br>

----------------------------
## Démarche suivie

### Methode 1 :

La première méthode utilisée est la plus triviale, nous avons simplement implémenté
5 fonctions de déchiffrements : 
- Caesar
- Vigenere
- Substitution
- Affine
- Hill 

Nous allons simplement "Brute Force", afin de trouver le texte déchiffré et la méthode utilisée
pour chaque message. </br>
Nous avons donc implémenté une fonction qui va tester toutes les méthodes de déchiffrement. </br>
Puis pour chaque méthode, nous allons tester toutes les clés possibles. </br>
Pour chaque clé, nous allons déchiffrer le message et la fréquence d'apparition des lettres. </br>
Enfin, nous allons comparer cette fréquence avec les occurences moyennes d'un texte en français.
Et ainsi en déduire le texte qui a la meilleure probabilité d'être en clair. </br>

----------------------------
## Requirements

- Python 3.7 minimum : https://www.python.org/downloads/
- numba : ``pip install numba``
- numpy : ``pip install numpy``
- unidecode : ``pip install unidecode``
----------------------------
## Comment lancer le programme

- ``python3 main.py``
- run ``main.py``

----------------------------

## Résultats
Tout les résulats sont disponibles dans le dossier ``out/Text_i_decrypted``  une fois le programme lancé une première fois correctement</br>

### Texte 1

```
ANTON VOYL N'ARRIVAIT PAS A DORMIR. IL ALLUMA. SON JAZ MARQUAIT MINUIT VINGT. IL POUSSA UN PROFOND SOUPIR, S'ASSIT DANS SON LIT, S'APPUYANT SUR SON POLOCHON. IL PRIT UN ROMAN, IL L'OUVRIT, IL LUT; MAIS IL N'Y SAISISSAIT QU'UN IMBROGLIO CONFUS, IL BUTAIT A TOUT INSTANT SUR UN MOT DONT IL IGNORAIT LA SIGNIFICATION. IL ABANDONNA SON ROMAN SUR SON LIT. IL ALLA A SON LAVABO; IL MOUILLA UN GANT QU'IL PASSA SUR SON FRONT, SUR SON COU.
```

### Texte 2

```
SON POULS BATTAIT TROP FORT. IL AVAIT CHAUD. IL OUVRIT SON VASISTAS, SCRUTA LA NUIT. IL FAISAIT DOUX. UN BRUIT INDISTINCT MONTAIT DU FAUBOURG. UN CARILLON, PLUS LOURD QU'UN GLAS, PLUS SOURD QU'UN TOCSIN, PLUS PROFOND QU'UN BOURDON, NON LOIN, SONNA TROIS COUPS. DU CANAL SAINT-MARTIN, UN CLAPOTIS PLAINTIF SIGNALAIT UN CHALAND QUI PASSAIT.
```

### Texte 3

```
SUR L'ABATTANT DU VASISTAS, UN ANIMAL AU THORAX INDIGO, A L'AIGUILLON SAFRAN, NI UN CAFARD, NI UN CHARANCON, MAIS PLUTOT UN ARTISON, S'AVANCAIT, TRAINANT UN BRIN D'ALFA. IL S'APPROCHA, VOULANT L'APLATIR D'UN COUP VIF, MAIS L'ANIMAL PRIT SON VOL, DISPARAISSANT DANS LA NUIT AVANT QU'IL AIT PU L'ASSAILLIE.Z
```

### Texte 4

```
IL TAPOTA D'UN DOIGT UN AIR MARTIAL SUR L'OBLONG CHASSIS DU VASISTAS.ILO UVRITS ONF RIGOM URALI, LP RITD UL AITF ROIDI, LB UTU NG RANDB OLI. LS A'PAISAITI. LS A'SSITS URS ONC OSYI, LP RITU NJ OURNALQ UI'LP ARCOURUTD U'NA IRD ISTRAITI. LA LLUMAU NC IGARILLOQ UI'LF UMAJ USQUA'UB OUTQ UOIQUI'LT ROUVATS ONP ARFUMI RRITANTI. LT OUSSA.
```


### Texte 5

```
WIP
```

----------------------------
## Fonctionnement des fonctions annexes

Avant toute chose, il est nécésaire de présenter les fichiers ``file.py``, ``text_input.py`` et ``is_french.py``
### text_input.py

````python
def text_format(text_input : str) -> str:
````
Permet de formater le texte en entrée, retire les accents en les convertissants en leur lettre non accentuée</br>

````python
def strip_puntuation(text: str):
````
Permet de retirer la ponctuation du texte, et la retourne dans un
dictionnaire, la clé est l'index dans le texte du caractère retiré
```Exemple : strip_punctuation("Hello World!!) -> ('HELLOWORLD', {5: ' ', 11: ' ', 12: '!', 13: '!'}) ```</br>

````python
def insert_punctuation(text: str, punctuation: dict):
````
Fonction inverse de celle du dessus, insère la ponctuation dans le texte en utilisant le dictionnaire précédemment généré.</br>


### is_french.py
````python
def is_french(text_list: list) -> tuple:
````
Prend une liste de texte, et retourne un tuple contenant le texte le plus probable d'être en français, et l'index de ce texte dans la liste.</br>

````python
def calculate_euclidean_difference(text: str) -> float:
````

Prend un texte, utilise la fonction ``calculate_percentage(text: str) -> dict:`` pour calculer la fréquence des lettres dans le texte, puis retourne la différence euclidienne entre la fréquence des lettres du texte et la fréquence des lettres du français.</br>


### file.py
Ce fichier contient des fonctions permettant de lire et écrire dans des fichiers.</br>
Notamment stocker la ponctuation des différents textes dans des fichiers ``.json``</br>

### file.py

## Fonctionnement des différents déchiffrements

Les différentes méthodes de déchiffrement sont appelées dans la fonction ``main()`` du fichier ``main.py``</br>
Les méthodes de déchiffrement sont appelées dans l'ordre suivant : </br>
- Caesar
- Affine
- Vigenere
- Hill
- Substitution

L'ordre d'appel est défini par le temps de calcul de chaque méthode, en éliminant des méthodes à chaque texte déchiffré, les plus longues à calculer 
sont appliquées à un nombre de texte restant plus faible.</br>

Etant donné que les textes donnés sont plutôt cours, certaines méthodes de 
déchiffrement présentent des incertitudes lors de l'utilisation d'attaques statistiques
sur les texte. Ainsi avec des textes plus long, il serait possible de déterminer automatiquement quel est le texte 
Français et quelle méthode de chiffrement.
Afin de contrer ce problème, la fonction ````main```` demande une petite intervention humaine, où il est demandé à l'utilisateur
de choisir entre ````n```` textes restants tirés des  ````n```` fichiers restants à déchiffrer, quel est celui en français</br>

### Caesar

Un texte chiffré par un décalage de C, est un texte où chaque lettre est décalée de C caractères dans l'alphabet.</br>
Il y a donc au maximum 26 possibilités de décalage, et donc 26 possibilités de texte déchiffré.</br>
La façon la plus rapide de forcer un chiffrement de Caesar est de tester toutes les possibilités, puis de faire une attaque statistique sur les textes déchiffrés, en effectuant une différence euclidienne entre la fréquence des lettres du texte déchiffré et la fréquence des lettres du français.</br> 
Les fonctions étant très faciles à comprendre, elles ne sont pas plus détaillées que dans le docstring.
### Affine

La méthode d'attaque du chiffrement Affine est similaire à celle du chiffrement Caesar, sauf que le décalage est calculé par la formule suivante : </br>
``
x = (a * y + b) mod 26
``</br>
Il y a donc au maximum 26 * 26 possibilités de décalage (légèrement moins si l'on soustrait les valeurs ne permettant pas de déchiffrer.)
Cependant faire une vérification des valeurs de a et b est plus couteux en ressource que bruteforce</br>
Les fonctions étant très faciles à comprendre, elles ne sont pas plus détaillées que dans le docstring.

### Vigenere

Le chiffrement de Vigenère est plus intéressant que les deux précédents.
Il s'agit d'un chiffrement polyalphabétique, c'est à dire qu'une lettre peut être chiffrée avec plusieurs décalages différents.
Il est difficile de le brute force, car il existe ENORMEMENT de possibilités.
Cependant, il est possible de faire une attaque statistique sur les textes chiffrés avec cette méthode</br>

##### Méthode opératoire : 
- On commence par déterminer la longueur de la clé en utilisant l'indice de coïncidence
- On détermine la clé en utilisant une méthode de groupe de lettres
- Déchiffrement du texte avec la clé trouvée

##### Indice de coïncidence
Formule : 
$\sum_{i=A} \frac{n_i (n_i -1)}{N(N-1)}$
avec $n_i$ le nombre d'occurence de la lettre $i$ dans le texte, et $N$ le nombre total de lettre dans le texte</br>

Il suffit alors de calculer l'indice de coincidence pour plusieurs sous-textes de longueurs différentes,
puis de choisir la valeur $I_c$ maximum.

##### Trouver la clé

Soit $k$ la longueur de la clé, et $i$ l'indice de la lettre dans le texte</br>
On sépare alors le texte en $k$ groupes de lettres, tel que k_i = {i, i + k, i + 2k, ...} $\forall i dans N$</br>
Dans la fonction : 
````python
def group_text(text: str, key_length: int) -> list:
````

Ensuite pour chaque groupe de lettre, on effectue une attaque de Caesar, et on garde le groupe avec la plus petite différence euclidienne avec la fréquence des lettres du français.</br>

On utilise ensuite la fonction afin de trouver la clé : 
````python
def find_key_frequency_vigenere(text, key_length):
````

Une fois la clé trouvée, il ne reste plus qu'à utiliser la fonction :
```python
def key_schedule(message: str, key: str)->list:
``` 
Permettant ainsi d'adapter
la clé à la longueur du texte, puis de déchiffrer le texte avec la clé trouvée en soustrayant la valeur de chaque lettre à chaque lettre du texte (modulo 26).

### Hill

Le chiffrement de Hill est également un chiffrement polyalphabétique, mais il est encore plus complexe que le chiffrement de Vigenère.
Ici dans notre cas, la clé est une matrice carrée $M_{2,2}$, ce qui limite les possibilités.
Afin d'opérer, il est nécessaire de découper le texte en bloc de 2 lettres. Si la longueur du texte est impaire, on rajoute une 
lettre au denier bloc, à l'aide de la fonction
</br>
````python
def split_text(text):
````
On transforme ensuite chaque lettre en nombre.</br>

Soit $G le groupe contenant toutes les matrices dans Z/26Z, on peux au maximum avoir $26^4 = 456 976$ matrices uniques dans $G$</br>
On génère alors la liste de toutes les matrices possibles avec la fonction : 
````python
def create_matrix_list():
    liste = np.array([[[i, j], [k, l]] for i in range(0, 26) for j in range(0, 26) for k in range(0, 26) for l in range(0, 26)])
    return liste
````
Il serait possible de tester toutes les possibilités, mais cela demanderait beaucoup trop de ressources.</br>
Une matrice peut-être utilisée pour chiffrer un texte si et seulement si elle est inversible modulo 26.</br>
CAD si et seulement si son déterminant est premier avec 26.</br>

On filtre alors toutes les matrices qui ne respectent pas cette condition : 
````python
matrix_list = [i for i in all_matrix if pgcd(determinant(i), 26) == 1]
````

Ce qui nous laisse alors 157 252 matrices inversibles (démontrable via le théorème des restes chinois)</br>

A partir de maintenant, on peut tester toutes les possibilités, et l'on garde le texte qui a la distance euclidienne entre
l'occurence de ses lettres et celle du français la plus faible.</br>

NB : Beaucoup de fonctions sont utilisées dans ce programme, et sont détaillées dans leurs docstring respectifs.
La grande majorité de ces fonctions servent uniquement à effectuer des opérations sur le texte, les listes ou à calculer un inverse modulaire.

### Substitution

Le chiffrement par substitution est lui aussi un chiffrement polyalphabétique, mais celui-ci est à la fois complexe et simple.
Car son fonctionnement repose sur le fait de changer la place des lettres de l’alphabet, c’est à dire que par exemple pour un texte normal sa clé serait : 
ABCDEFGHIJKLMNOPQRSTUVWXYZ
Alors que lorsque l’on crypte un message par substitution sa clé peut devenir par exemple :
TNICKMXQYFESZPHVOGRLJBUDWA

On peut donc se dire que : décrypter un message chiffré par substitution est plutôt simple car il suffirait d’essayer pour
chaque clé possible de traduire le texte puis de comparer les taux d’apparition des lettres dans
chaque texte et de prendre celui où le taux ressemble le plus à celui de la langue française.

Malheureusement le nombre possible de clés est énorme, il est de 26!, cela fait donc beaucoup trop. 

Nous allons ici avoir une approche différente, nous allons comparer les paterne des mots afin de comparer avec les paternes
de la langue française et pouvoir ainsi en ressortir un dictionnaire qui pour chaque lettre de l’alphabet sortira celles qui pourraient
leurs être substituées. 

Pour le moment nous avons simplement pu créer un dictionnaire qui stocke tous les paternes de la langue française.

La fonction : split_text, permet de récupérer un texte en paramètre et renvoie une liste de 20 mots aléatoires
du texte en majuscule et sans ponctuation.

La fonction get_pattern_list récupère la liste de mots précédemment créés et renvoie une liste des paternes de ces différents mots :
par exemple pour le mot CHOISIR, le paterne sera : 0.1.2.3.4.3.5

Puis la fonction compare_pattern, récupère cette liste de paternes et renvoie un dictionnaire qui,
pour chaque paterne de la liste, lui attribue les mots de la langue française avec le même paterne. 

NB : l'ensemble du code de la fonction susbtitution est trouvable dans le fichier substitution.py, et ses dépendances dans /data.
Cependant le programme ne fonctionne pas encore correctement, et nous n'avons pas eu le temps de le finir, il n'est donc pas implémenté
dans le main.py.

### Optimisation

Effectuer une attaque de Hill est très couteux en ressource, et il est donc nécessaire d'optimiser le programme.
Pour ce faire, la majorité des opérations sont effectuées un minimum de fois, et les résultats sont stockés dans des variables afin d'éviter de les recalculer.</br>
De plus numpy a été utilisé au maximum afin d'optimiser les temps de calculs.</br>
Dans la plupart des cas, les fonctions numpy sont plus rapides que les fonctions python classiques.</br>
Cependant pour certains cas, étant donné que les matrices sont des 2x2, il est plus rapide d'utiliser des fonctions en python classique (vectorisés) que des fonctions numpy.</br>
Et dans le cas ou il n'y a pas le choix, des génératrices de listes ou des map ont été utilisés afin de gagner en performance.</br>
Enfin, comme évoqué précédement certaines fonctions d'opérations sur les matrices sont vectorisées à l'aide de Numba ````@jit(nopython=True)````, ce qui permet d'optimiser encore plus les temps de calculs.</br>

**IMPORTANT** Si le programe ne se lance pas correctement (notamment à cause de numba), retirer le commentaire de la ligne 7 du fichier ``main.py`` et commenter la ligne 6. </br>
Cela permettra d'effectuer les calculs sans optimisation, mais cela sera beaucoup plus long.

### Bonus
#### Temps de calculs

Les 3 premiers algorithmes ne sont que très peu couteux en ressources, et peuvent donc être exécutés en quelques secondes.</br>
Le chiffrement de Hill est beaucoup plus couteux, et peut prendre jusqu'à 10 minutes dans le pire des cas.</br>

Chiffres obtenus sur un ordinateur portable avec la configuration suivante :
- AMD Ryzen 5 4600H 3.5 GHz
- 16 Go de RAM

Le reste de la configuration n'est pas nécessaire pour l'exécution du programme.

Mesure effectuée avec la fonction ``start = time.time()`` de python avant la fonction à mesurer, puis ``end = time.time()`` après la fonction.
Et enfin ``end - start`` </br>

Temps moyen d'exécution pour ```hill_optimised``` :
- 14.47747015953064 secondes

Temps moyen d'exécution pour ```hill_optimised``` sans vectorisation (Numba) :
- 30.21728128129817 secondes

Temps moyen d'exécution pour ```hill``` :
- 50.257126569747925 secondes

Autres temps : 
Afin d'essayer de gagner du temps de calculs, j'ai essayé de diviser la liste contenant toutes les matrices en plusieurs parties égales, puis de faire du 
multi-processing, afin de tester toutes les possibilités en parallèle.
Cependant, il faut justifier l'utilisation de plusieurs process, et dans ce cas, il y a certes un gain de temps sur l'exécution des fonctions, mais
la création des process se répercute sur le temps d'exécution total, et le gain n'est pas significatif.

Temps d'exécution pour ```hill_optimised``` avec 2 threads :
- 7.94100022315979 secondes </br>

Temps de création des process : 6.281298875808716 secondes</br>

Temps d'exécution pour ```hill_optimised``` avec 4 threads :
- 2.5492501258850098 secondes</br>

Temps de création des process : 12.76021988756021 secondes</br>

Temps d'exécution pour ```hill_optimised``` avec 8 threads :
- 2.5492501258850098 secondes</br>

Temps de création des process : 20.89210219099219 secondes</br>


## Sources : 

[1].Chris Christenses (2015).Polygraphic Substitution Cipher : The Hill Cipher, II [En ligne] Disponible : CIhttps://www.nku.edu/~christensen/1402%20Hill%20cipher%20part%20II.pdf</br>

[2].Unknown (S.D).  Math  5410 Homework Assignement 3.[En ligne] Disponible :http://math.ucdenver.edu/~wcherowi/courses/m5410/m5410hw3.html#ans1.2</br>

[3]. Proof of Concept (2020). Cryptanalysis of Vigenere cipher.[En ligne] Disponible : https://www.youtube.com/watch?v=QgHnr8-h0xI&t=2s</br>

[4]. Wikipédia. (2022). Fréquence d'apparition des lettres. [En ligne] Disponible : https://fr.wikipedia.org/wiki/Fréquence_d%27apparition_des_lettres


#Rendu 2:

## SAE CRYPTOGRAPHIE DEFI 1 - SUBSTITUTION 
### Auteurs:
- REYDET Antonin
- RONCERAY Maxime

### Description:
Ce programme permet de déchiffrer un message en utilisant la méthode de substitution.

### Utilisation:
Afin de lancer ce programme il faut executer la la commande suivante depuis le répertoire ```src```:
```bash
python3 src/substitution.py
```

### Fonctionnement:
Le programme s'articule autout de plusieurs fonctions.

Cependant celui-ci use afin de trouver le texte le plus français d'une approche probabiliste.
Tout d'abord le script du fichier ```src/creationdico``` va lire le fichier ```data/liste.de.mots.francais.frgut.txt``` et va en créer un dictionnaire.
Ce dictionnaire va contenir les mots du fichier ```data/liste.de.mots.francais.frgut.txt```  qui est un dictionnaire des mots français.

- Ensuite le script ```bigramscreator.py``` va lire un texte en français, ici le livre 'du côté de chez Swann'. De cette lecture il en ressort deux fichiers, le premier  ```data/bigrams.dat``` qui contient pour chaque lettre la probabilité d'apparition de la lettre suivante pour un texte écrit en français, donc en généralisant pour la langue française.

 
- Le second fichier lui est le fichier ```data/bigrams.png``` qui est un graphique représentant les probabilités contenues dans le fichier énoncé précédemment.


- Pour lire ce diagramme il faut comprendre que plus le carré de couleur tend vers le jaune plus la probabilité est grande. (à noté qu'ici le livre utilisé comme source à pour protagoniste une denommé 'Swann' la probabilité que la lettre 'a' suive la lettre 'w' apparait comme extrêmement probable, alors que ce n'est pas le cas dans la langue française. Cependant cela ne gênera pas les simulations.). 

L'approche utilisée pour déchiffrer le message est la suivante:
- On va lire le message chiffré caractère par caractère.
- Pour chaque caractère on va calculer la probabilité que la lettre suivante apparaisse.
- On la compare à la probabilité que la lettre suivante apparaisse dans le texte français.
- On va ensuite calculer la différence entre les deux probabilités.
- Puis on répète le processus en changeant l'échange de deux lettre dans notre clé de chiffrement hypothétique.
- Dans cet algorithme nous le faisons une première fois afin d'obtenir un premier résultat comprenant à peu près 50% de mots français.
- Puis nous le faisons une deuxième fois afin d'obtenir un résultat comprenant à peu près 80% de mots français ce qui permet de décrypter le plus souvent le message dans son intégralité, ou en tous cas dans sa grande globalité.

### Résultat:
Le résultat obtenu est le suivant:
```
Le message est: IL MIT LA RADIO UN AIR AFRO CUBAIN FUT SUIVI D UN BOSTON PUIS UN TANGO PUIS UN FOX TROT PUIS UN COTILLON MIS AU GOUT DU JOUR DUTRONC CHANTA DU LANZMANN BARBARA UN MADRIGAL D ARAGON STICH RANDALL UN AIR D AIDA 
```

### Problèmes:
- Le programme ne fonctionne pas toujours, il est possible que le message ne soit pas déchiffré correctement,
ceci est dû à la nature probabiliste de l'algorithme.

Il est possible que selon les simulations l'algorithme pense mélange l'alphabet de manière défavorable au dechiffrement du message, ce qui mène souvent à un message décrypté à seulement une cinquantaine de pourcent.

### Améliorations possibles:

- Il serait possible d'ajouter un dictionnaire de mots anglais afin de pouvoir déchiffrer des messages en anglais.
- Il serait possible de par exemple executer l'algorithme 5 fois et de proposer les 5 messages possibles et de laisser le choix à l'utilisateur pour le texte se rapportant le plus au message voulu.

### Conclusion:

- Cette méthode de chiffrement est complexe à casser en force brut, seulement via une approche probabiliste celui-ci devient tout de suite beaucoup plus abordable dans son déchiffrement.

### Sources:

- https://github.com/scienceetonnante/MCMC


## SAE CRYPTOGRAPHIE DEFI 2

### How to use 

- BSGS.py propose un code dans lequel on génère un problème de log discret puis ou l'on le casse$
Changez la ligne 30 si le programme met trop de temps a run (dépend de la puissance du pc utilisé)

- DH_Key_Exchange propose de générer 2 clés privés communes a partir d'un p,d'un n et 2 clés privés uniques
Changez la ligne 51 (remplacer le 10^200 en 10^50) si le programme met trop de temps a run (dépend de la puissance du pc utilisé)

- DLP.py met en oeuvre un processus dans lequel nous cassons et montront qu'il est possible de 
trouver les clés privés communes dans un échange de Diffie-Hellman a partir des valeurs publiques d'Alice et Bob.

- plot.py est le fichier permettant de faire les graphiques utilisés dans le raport.








