# Projet : Générateur de mots de passe sécurisés

Description : Développer un script Python qui génère des mots de passe sécurisés selon les spécifications de l'utilisateur.

Fonctionnalités suggérées :

- [x] Longueur du mot de passe :
        Permettre à l'utilisateur de spécifier la longueur souhaitée pour le mot de passe (par exemple, entre 8 et 16 caractères).
- [x] Caractères spécifiques :
        Inclure la possibilité pour l'utilisateur de choisir d'inclure des caractères spéciaux, des chiffres et des lettres majuscules ou minuscules dans le mot de passe généré.
- [x] Génération aléatoire :
        Utiliser des fonctions Python pour générer aléatoirement des mots de passe sécurisés basés sur les critères spécifiés.
- [ ] Options de personnalisation :
        Offrir des options supplémentaires comme la possibilité d'exclure certains caractères spécifiques ou de garantir l'inclusion de caractères spécifiques.
- [x] Interface utilisateur simple :
        Créer une interface en ligne de commande conviviale où l'utilisateur peut interagir et obtenir rapidement des mots de passe sécurisés.

Bonus :

- [ ] Gestion de la sécurité :
        Intégrer des bonnes pratiques de sécurité, telles que la suppression des mots de passe générés après leur utilisation et l'utilisation de méthodes cryptographiques pour la génération aléatoire.
- [x] Gestion des erreurs :
        Ajouter une gestion robuste des erreurs pour les entrées utilisateur incorrectes ou inattendues.
- [x] Exportation vers un fichier :
        Offrir la possibilité d'exporter les mots de passe générés dans un fichier texte ou CSV pour une utilisation ultérieure. 

main.py | generator.py | use.py | bdd | password.csv
--- | --- | --- | --- | ---
Fichier mère gérant tout les autres | Fichier de génération des mots de passe | Récupère le mot de passe d'une ligne (peut-être choisi entre `1` et `99` | C'est la *Base de donnée* pour le mot de passe de use.py | stocke tout les mot de passe générer
