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
Pour chaque clé, nous allons déchiffrer le message et calculer la fréquence des lettres. </br>
Enfin, nous allons comparer la fréquence des lettres du message déchiffré avec la fréquence des lettres
du français. </br> 
Et ainsi récupérer le texte le plus probable d'être le texte déchiffré en français. </br>

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
Tout les résulats sont trouvables dans le dossier ``out/Text_i_decrypted``  une fois le programme lancé une première fois correctement</br>

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
Permet de retirer la ponctuation du texte en , et la retourne dans un
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

Prend un text, utilise la fonction ``calculate_percentage(text: str) -> dict:`` pour calculer la fréquence des lettres dans le texte, puis retourne la différence euclidienne entre la fréquence des lettres du texte et la fréquence des lettres du français.</br>


### file.py
Ce fichier contient des fonctions permettant de lire et écrire dans des fichiers.</br>
Notament stocker la ponctuation des différents textes dans des fichiers ``.json``</br>

### file.py

## Fonctionnement des différents déchiffrements

Les différentes méthodes de déchiffrement sont appelés dans la fonction ``main()`` du fichier ``main.py``</br>
Les méthodes de déchiffrement sont appelés dans l'order suivant : </br>
- Caesar
- Affine
- Vigenere
- Hill
- Substitution

L'ordre d'appel est défini par le temps de calcul de chaque méthode, en éliminant des méthodes a chaque texte déchiffré, les plus longues à calculer sont appliqués a un nombre de texte restant plus faible.</br>

Etant donné que les textes donnés sont plutôt cours, certains méthodes de 
déchiffrement présentent des incertitudes lors de l'utilisation d'attaque statistique 
sur ces derniers, ainsi avec des textes plus long il serait possible de déterminer automatiquement quel est le texte 
Français et chiffré avec quelle méthode.
Afin de contrer ce problème, la fonction main demande une petite intervention humaine, ou il est demandé a l'utilisateurs
de choisir entre n textes restants tirés des n fichiers restants a déchiffrer, quel est celui en Français</br>

### Caesar

Un texte chiffré par un décalage de C, est un texte où chaque lettre est décalée de C caractères dans l'alphabet.</br>
Il y a donc au maximum 26 possibilités de décalage, et donc 26 possibilités de texte déchiffré.</br>
La façon la plus rapide de forcer un chiffrement de César est de tester toutes les possibilités</br>
Puis de faire un attaque statistique sur les textes déchiffrés, en effectuant une différence euclidienne entre la fréquence des lettres du texte déchiffré et la fréquence des lettres du français.</br> 
Les fonctions étant très facile a comprendre, elles ne sont pas plus détaillées que dans le docstring
### Affine

La méthode d'attaque de l'affine est similaire à celle du César, sauf que le décalage est calculé par la formule suivante : </br>
``
x = (a * y + b) mod 26
``</br>
Il y a donc au maximum 26 * 26 possibilités de décalage (légèrement moins si l'on soustrait les valeurs ne permettant pas de déchiffre)
Cependant faire une vérification des valeurs de a et b est plus couteux en ressource que bruteforce</br>
Les fonctions étant très facile a comprendre, elles ne sont pas plus détaillées que dans le docstring

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
avec $n_i$ le nombre d'occurence de la lettre $i$ dans le texte, et $N$ le nombre total de lettre dans le texte
allant de A à Z</br>

Il suffit alors de calculer l'indice de coincidence pour plusieurs subtextes de longueur différente,
puis de choisir la valeur $I_c$ maximum

##### Trouver la clé

Soit $k$ la longueur de la clé, et $i$ l'indice de la lettre dans le texte</br>
On sépare alors le texte en $k$ groupes de lettres, tel que k_i = {i, i + k, i + 2k, ...} $\forall i dans N$</br>
Dans la fonction : 
````python
def group_text(text: str, key_length: int) -> list:
````

Ensuite pour chaque groupe de lettre, on effectue une attaque de César, et on garde le groupe avec la plus petite différence euclidienne avec la fréquence des lettres du français.</br>

On utilise ensuite la fonction afin de trouver la clé : 
````python
def find_key_frequency_vigenere(text, key_length):
````

Une fois la clé trouvée, il ne reste plus qu'a utiliser la fonction 
```python
def key_schedule(message: str, key: str)->list:
``` 
Permettant ainsi d'adapter
la clé a la longueur du texte, puis de déchiffrer le texte avec la clé trouvée en soustrayant la valeur de chaque Lettre a chaque Lettre du texte (modulo 26).

### Hill

Le chiffrement de Hill est également un chiffrement polyalphabétique, mais il est encore plus complexe que le chiffrement de Vigenère.
Ici dans notre cas, la clé est une matrice carrée $M_{2,2}$, ce qui limite les possibilités.
Afin d'opérer, il est nécéssaire de découper le texte en bloc de 2 lettres. Si la longueur du texte est impaire, on rajoute une lettre au denier bloc, a l'aide de la fonction
</br>
````python
def split_text(text):
````
On transforme ensuite chaque lettre en nombre.</br>

Soit $G le groupe contenant toutes les matrices dans Z/26Z$, on peux au maximum avoir $26^4 = 456 976$ matrices uniques dans $G$</br>
On génère alors la liste de toutes les matrices possibles avec la fonction : 
````python
def create_matrix_list():
    liste = np.array([[[i, j], [k, l]] for i in range(0, 26) for j in range(0, 26) for k in range(0, 26) for l in range(0, 26)])
    return liste
````
Il serait possible de tester toutes les possibilités, mais cela demanderait beaucoup trop de ressources.</br>
Une matrice peut etre utiliser pour chiffrer un texte si et seulement si elle est inversible modulo 26.</br>
CAD si et seulement si son déterminant est premier avec 26.</br>

On filtre alors toutes les matrices qui ne respèctent pas cette condition : 
````python
matrix_list = [i for i in all_matrix if pgcd(determinant(i), 26) == 1]
````

Ce qui nous laisse alors 157 252 matrices inversibles (démontrable via le théorème des restes Chinois)</br>

A partir de maintenant, on peut tester toutes les possibilités, et l'on garde le texte qui a la distance euclidienne entre l'occurence de ses lettres et celle du français la plus faible</br>

NB : Beaucoup de fonctions sont utilisés dans ce programme, et sont détaillées dans leurs docstring respectifs.
La grande majorité de ces fonctions servent uniquement a effectuer des opérations sur le texte, les liste, ou calculer un inverse modulaire.

#### Optimisation

Effectuer une attaque de Hill est très couteux en ressource, et il est donc nécessaire d'optimiser le programme.
Pour ce faire, la majorité des opérations sont effectués un minimum de fois, et les résultats sont stockés dans des variables afin d'éviter de les recalculer.</br>
De plus numpy a été utilisé au maximum afin d'optimiser les temps de calculs.</br>
Dans la pluspart des cas, les fonctions numpy sont plus rapide que les fonctions python classiques.</br>
Cependant pour certains cas, étant donné que les matrices sont des 2x2, il est plus rapide d'utiliser des fonctions en python classique(vectorisés) que des fonctions numpy.</br>
Et dans le cas ou il n'y avait pas le choix, des génératrices de list ou des map ont été utilisés afin de gagner en performance.</br>
Enfin, comme évoqué précédement certaines fonctions d'opérations sur les matrices sont vectorisées a l'aide de Numba ````@jit(nopython=True)````, ce qui permet d'optimiser encore plus les temps de calculs.</br>

**IMPORTANT** Si le programe ne se lance pas correctement (notamment a cause de numba), décommenter la ligne 7 du fichier ``main.py`` et commenter la ligne 6. </br>
Cela permettra d'effectuer les calculs sans optimisation, mais cela sera beaucoup plus long.

### Bonus
#### Temps de calculs

Les 3 premiers algorithmes ne sont que très peu coutueux en ressources, et peuvent donc être executés en quelques secondes.</br>
Le chiffrement de Hill est beaucoup plus couteux, et peut prendre jusqu'a 10 minutes dans le pire des cas.</br>

Chiffres obtenus sur un ordinateur portable avec la configuration suivante :
- AMD Ryzen 5 4600H 3.5 GHz
- 16 Go de RAM

Le reste de la configuration n'est pas nécessaire pour l'execution du programme.

Mesure effectuée avec la fonction ``start = time.time()`` de python avant la fonction a mesurer, ``end = time.time()`` après la fonction.
puis ``end - start`` </br>

Temps moyen d'execution pour ```hill_optimised``` :
- 14.47747015953064 secondes

Temps moyen d'execution pour ```hill_optimised``` sans vectorisation (Numba) :
- 30.21728128129817 secondes

Temps moyen d'execution pour ```hill``` :
- 50.257126569747925 secondes

Autres temps : 
Afin d'essayer de gagner du temps de calculs, j'ai essayé de diviser la liste contenant toutes les matrices en plusieurs parties égales, puis de 
multi-process, afin de tester toutes les possibilités en parallèle.
Cependant, il faut justifier l'utilisation de plusieurs process, et dans ce cas, il y a certes un gain de temps sur l'execution des fonctions, mais
la création des process se répercute sur le temps d'execution total, et le gain n'est pas significatif.

Temps d'execution pour ```hill_optimised``` avec 2 threads :
- 7.94100022315979 secondes </br>

Temps de création des process : 6.281298875808716 secondes</br>

Temps d'execution pour ```hill_optimised``` avec 4 threads :
- 2.5492501258850098 secondes</br>

Temps de création des process : 12.76021988756021 secondes</br>

Temps d'execution pour ```hill_optimised``` avec 8 threads :
- 2.5492501258850098 secondes</br>

Temps de création des process : 20.89210219099219 secondes</br>













