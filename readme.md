

# Installation
* cloner le repo
* installer les dépendances : pip3 install -r requirements.txt
* créer le fichier params.json à partir du fichier default_params.json.
  * Si vous utilisez [navitia-explorer](https://github.com/CanalTP/navitia-explorer), vous pouvez reprendre le même fichier ;)
  * Sinon, obtenez une clef d'authentification navitia.io et mettez là dans le fichier
* [privé seulement :lock: ] Créer le fichier params.py qui spécifie où se trouvent les sources des tests privés
* testez (à la racine du repo) :
```shell
behave -D environnement=prod public_features/fr_idf.feature
```

Si vous ne constatez aucune erreur sur les étapes Given, c'est bon !
