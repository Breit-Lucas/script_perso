# Guide d'installation et d'utilisation du programme de gestion d'inventaire

## Introduction
Ce document explique comment installer et utiliser le programme de gestion d'inventaire, une application en ligne de commande (CLI) pour gérer un inventaire à partir de fichiers CSV.

## Prérequis
### Python
- Assurez-vous que Python 3.6 ou une version ultérieure est installé sur votre système.
- [Téléchargez Python ici](https://www.python.org/downloads/).
- Vérifiez l'installation avec :
  ```bash
  python --version
  ```

### pip
- L'outil de gestion des paquets Python est requis pour installer les dépendances.
- Pip est généralement inclus avec Python. Vérifiez avec :
  ```bash
  pip --version
  ```

### Modules Python nécessaires
- `pandas`
- `colorama`

## Installation
### Étape 1 : Cloner ou télécharger le projet
Téléchargez le projet à partir du dépôt ou copiez les fichiers du programme dans un répertoire local.

### Étape 2 : Installer les dépendances
1. Ouvrez un terminal et naviguez vers le dossier contenant le fichier principal (`main.py`).
2. Installez les dépendances requises avec la commande suivante :
   ```bash
   pip install pandas colorama
   ```

## Utilisation
### Lancer le programme
En mode interactif :
```bash
python main.py
```

### Commandes disponibles
#### Commandes interactives
- **load** : Charger les fichiers CSV d'un dossier dans la base de données.
  - **Syntaxe** : `load <chemin_du_dossier>`
  - **Exemple** :
    ```bash
    load data/
    ```

- **search** : Rechercher un produit ou une catégorie dans l'inventaire.
  - **Syntaxe** : `search <colonne=valeur>`
  - **Exemple** :
    ```bash
    search category=electronics
    ```

- **summary** : Générer un rapport récapitulatif des quantités et des prix moyens par catégorie.
  - **Syntaxe** : `summary <chemin_du_fichier>`
  - **Exemple** :
    ```bash
    summary summary_report.csv
    ```

- **show** : Afficher les premières lignes de la base de données.
  - **Syntaxe** : `show <nombre_de_lignes>`
  - **Exemple** :
    ```bash
    show 10
    ```

- **exit** : Quitter le programme interactif.
  - **Syntaxe** : `exit`

#### Options en ligne de commande
Vous pouvez également utiliser les options suivantes sans lancer le mode interactif :

- `--load <chemin_du_dossier>` : Charger les fichiers CSV.
- `--search <colonne=valeur>` : Rechercher un produit ou une catégorie.
- `--summary <chemin_du_fichier>` : Générer un rapport récapitulatif.
- `--show <nombre>` : Afficher les premières lignes.
- `--exit` : Quitter le programme immédiatement.

**Exemple combiné** :
```bash
python main.py --load data/ --summary summary_report.csv
