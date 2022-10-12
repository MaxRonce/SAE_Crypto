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


**PS :** les messages sont listés dans les fichiers ``Texte1.txt ... Texte5.txt`` </br>
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
Et ainsi récupérer le texte le plus probab le d'être le texte déchiffré en français. </br>





