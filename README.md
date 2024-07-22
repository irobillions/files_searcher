
# File Searcher

## Description

File Searcher est un outil de recherche de fichiers avancé développé en Python. Il permet aux utilisateurs de rechercher des fichiers dans un répertoire en fonction de divers critères tels que le nom du fichier, le type de fichier, le contenu et les métadonnées. Les résultats de la recherche peuvent être exportés dans un fichier Excel (`.xlsx`) et l'application conserve des journaux des recherches effectuées et des résultats produits. De plus, l'application peut suivre et stocker l'historique des recherches dans une base de données SQLite.

## Fonctionnalités

- **Recherche par Nom de Fichier** : Trouvez des fichiers en spécifiant un nom de fichier partiel ou complet.
- **Recherche par Type de Fichier** : Filtrez les fichiers en fonction de leur extension (par exemple, `.txt`, `.pdf`).
- **Recherche par Contenu de Fichier** : Recherchez des fichiers contenant des mots-clés spécifiques dans leur contenu.
- **Recherche par Métadonnées** : Filtrez les fichiers en fonction des métadonnées telles que la date de création, la date de modification et la taille du fichier.
- **Exportation vers Excel** : Enregistrez les résultats de la recherche dans un fichier Excel avec des détails tels que le nom du fichier, le chemin et une brève description du contenu.
- **Journalisation** : Conservez des journaux des recherches effectuées et des fichiers de résultats produits.
- **Base de Données** : Stockez l'historique des recherches et des fichiers de résultats dans une base de données SQLite.

## Installation

### Prérequis

- Python 3.6 ou supérieur
- Pip (gestionnaire de packages Python)

### Étapes d'installation

1. Clonez le dépôt :

    ```bash
    git clone https://github.com/votre-utilisateur/file_searcher.git
    cd file_searcher
    ```

2. Installez les dépendances :

    ```bash
    pip install -r requirements.txt
    ```

### Dépendances

- `openpyxl` : Pour créer et manipuler des fichiers Excel
- `sqlite3` : Pour la gestion de la base de données SQLite

## Utilisation

### Interface en Ligne de Commande (CLI)

Pour exécuter une recherche par nom de fichier et exporter les résultats vers un fichier Excel :

```bash
python src/ui/cli.py <répertoire> <nom_du_fichier> <fichier_de_sortie.xlsx> [--log <fichier_de_log>] [--db <fichier_de_base_de_données>]
```

#### Arguments

- `<répertoire>` : Répertoire à rechercher
- `<nom_du_fichier>` : Nom du fichier à rechercher
- `<fichier_de_sortie.xlsx>` : Fichier Excel de sortie
- `--log` : Fichier de log (optionnel, par défaut `search_log.log`)
- `--db` : Fichier de base de données (optionnel, par défaut `searches.db`)

### Exemple

```bash
python src/ui/cli.py /chemin/à/rechercher exemple resultat.xlsx --log mon_log.log --db ma_base_de_données.db
```

## Architecture du Projet

```
file_searcher/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── search/
│   │   ├── __init__.py
│   │   ├── search_base.py
│   │   ├── search_by_name.py
│   │   ├── search_by_type.py
│   │   ├── search_by_content.py
│   │   ├── search_by_metadata.py
│   ├── index/
│   │   ├── __init__.py
│   │   ├── indexer.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── file_utils.py
│   │   ├── threading_utils.py
│   │   ├── excel_utils.py
│   │   ├── logging_utils.py
│   │   ├── db_utils.py
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── cli.py
│   │   ├── gui.py
│
├── tests/
│   ├── __init__.py
│   ├── test_search.py
│   ├── test_index.py
│   ├── test_utils.py
│
├── requirements.txt
├── README.md
└── setup.py
```

## Contribuer

Les contributions sont les bienvenues ! Veuillez créer une "issue" pour discuter de ce que vous aimeriez changer. Vous pouvez également faire un fork du projet et soumettre une "pull request".

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
