# Projet 1 : Zorglangue
---
## Description

Implémentation d’un encodeur/décodeur pour la Zorglangue, langage fictif inventé par Zorglub (Spirou et Fantasio).
Règle principale :
Inverser l’ordre des lettres dans chaque mot sans changer l’ordre des mots ni la position de la ponctuation.
Les majuscules restent majuscules après inversion.

### Exemples :

- Bonjour → ruojnoB

- Vive Zorglub ! → eviV bulgroZ !

- Ceci est un message secret → iceC tse un egassam terces

### Fonctionnalités

- Encodage d’un texte en Zorglangue

- Décodage (identique à l’encodage, opération involutive)

- Gestion correcte de la ponctuation

- Conservation des majuscules/minuscules

- Interface CLI simple (optionnel)

- Tests automatisés avec pytest