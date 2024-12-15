# Guide d’installation

## Prérequis
- **Python 3.8+** doit être installé sur votre machine. [Téléchargez-le ici](https://www.python.org/downloads/).
- Les bibliothèques nécessaires sont :
  - `pandas` (pour la manipulation des données CSV).
  - `colorama` (pour l'affichage coloré dans le terminal).

## Étapes d'installation
1. **Clonez ce dépôt Git ou téléchargez le fichier `main.py`** :
   ```bash
   git clone <URL_DU_DEPOT>
   cd inventory_manager
   ```

2. **Installez les dépendances nécessaires en utilisant le fichier `requirements.txt`** :
   ```bash
   pip install -r requirements.txt
   ```
   Si le fichier `requirements.txt` n'est pas disponible, installez manuellement les bibliothèques :
   ```bash
   pip install pandas colorama
   ```

3. **Testez l'installation en lançant le script** :
   ```bash
   python main.py
   ```

## Exemples d’utilisation
Une fois l’application lancée, utilisez les commandes suivantes pour manipuler votre inventaire.

### 1. Charger des fichiers CSV
Consolidez plusieurs fichiers CSV situés dans un même dossier en une base unique :
```bash
load <chemin_du_dossier>
```
**Exemple** :
```bash
load ./stocks
```
Cela charge tous les fichiers CSV du dossier `stocks`.

### 2. Rechercher dans l’inventaire
Effectuez une recherche dans une colonne spécifique. La syntaxe est :
```bash
search <colonne=valeur>
```
**Exemple** :
```bash
search category=Electronics
```
Recherche tous les produits de la catégorie `Electronics`.

### 3. Afficher les premières lignes de la base
Affichez les premières lignes pour vérifier les données consolidées :
```bash
show <nombre_de_lignes>
```
**Exemple** :
```bash
show 10
```
Affiche les 10 premières lignes.

### 4. Générer un rapport récapitulatif
Créez un rapport résumant les quantités et le prix moyen par catégorie. La commande est :
```bash
summary <chemin_du_fichier_exporté>
```
**Exemple** :
```bash
summary ./rapport_inventaire.csv
```
Génère un fichier `rapport_inventaire.csv` contenant le résumé.

### 5. Quitter l’application
Pour quitter l’application, utilisez :
```bash
exit
```

### Options en ligne de commande
Vous pouvez également utiliser les options suivantes sans lancer le mode interactif :

- `--load <chemin_du_dossier>` : Charger les fichiers CSV.
- `--search <colonne=valeur>` : Rechercher un produit ou une catégorie.
- `--summary <chemin_du_fichier>` : Générer un rapport récapitulatif.
- `--show <nombre>` : Afficher les premières lignes.
- `--exit` : Quitter le programme immédiatement.

**Exemple combiné** :
```bash
python main.py --load data/ --summary summary_report.csv
```
