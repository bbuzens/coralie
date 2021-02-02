# Application pour Coralie

## Description

Affecte des groupes définis à partir des fichiers de conf afin de pouvoir catégoriser des mesures.

L'application renvoie un fichier de sortie au format Excel avec les mesures enrichies des groupes d'appartenance.


## Installation

* Installer Python en version 3 ([lien ici](https://www.python.org/downloads/))
* Télécharger l'archive depuis le [dépôt](https://github.com/bbuzens/coralie/archive/master.zip)
* Dézipper l'archive
* [Déclarer Python en variable système](https://docs.python.org/3/using/windows.html)
* Installer les dépendances depuis une console
    * Lancer la console
    * Se placer dans le répertoire du programme
    * Exécuter la commande `python -m pip install -r requirements.txt`
    
## Utilisation

* Configurer le fichier source et le répertoire de conf dans *main.py* (édition à l'aide du *bloc note*)
* Lancer le programme en double-cliquant sur *run.bat*
* Le fichier de sortie *output_<nom_de_fichier>* est disponible dans le répertoire principal en fin de traitement


