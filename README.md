Guide d’installation
Prérequis
Python 3.8+ doit être installé sur votre machine. Téléchargez-le ici : Python Downloads.
Les bibliothèques nécessaires sont :
pandas (pour la manipulation des données CSV).
colorama (pour l'affichage coloré dans le terminal).
Étapes d'installation
Clonez ce dépôt Git ou téléchargez le fichier main.py :

bash
Copier le code
git clone <URL_DU_DEPOT>
cd inventory_manager
Installez les dépendances nécessaires en utilisant le fichier requirements.txt :

bash
Copier le code
pip install -r requirements.txt
Si le fichier requirements.txt n'est pas disponible, installez manuellement les bibliothèques :

bash
Copier le code
pip install pandas colorama
Testez l'installation en lançant le script :

bash
Copier le code
python main.py
Exemples d’utilisation
Une fois l’application lancée, utilisez les commandes suivantes pour manipuler votre inventaire.

1. Charger des fichiers CSV
Consolidez plusieurs fichiers CSV situés dans un même dossier en une base unique :

bash
Copier le code
load <chemin_du_dossier>
Exemple :

bash
Copier le code
load ./stocks
Cela charge tous les fichiers CSV du dossier stocks.

2. Rechercher dans l’inventaire
Effectuez une recherche dans une colonne spécifique. La syntaxe est :

bash
Copier le code
search <colonne=valeur>
Exemple :

bash
Copier le code
search category=Electronics
Recherche tous les produits de la catégorie Electronics.

3. Afficher les premières lignes de la base
Affichez les premières lignes pour vérifier les données consolidées :

bash
Copier le code
show <nombre_de_lignes>
Exemple :

bash
Copier le code
show 10
Affiche les 10 premières lignes.

4. Générer un rapport récapitulatif
Créez un rapport résumant les quantités et le prix moyen par catégorie. La commande est :

bash
Copier le code
summary <chemin_du_fichier_exporté>
Exemple :

bash
Copier le code
summary ./rapport_inventaire.csv
Génère un fichier rapport_inventaire.csv contenant le résumé.

5. Quitter l’application
Pour quitter l’application, utilisez :

bash
Copier le code
exit
