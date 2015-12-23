

# Installation
* cloner le repo
* installer les dépendances : pip3 install -r requirements.txt
* créer le fichier params.json à partir du fichier default_params.json.
  * Si vous utilisez [navitia-explorer](https://github.com/CanalTP/navitia-explorer), vous pouvez reprendre le même fichier ;)
  * Sinon, obtenez une clef d'authentification navitia.io et mettez là dans le fichier
* tester (à la racine du répertoire) :
```shell
behave -D environnement=prod public_features/fr_idf.feature
```

Si vous ne constatez aucune erreur sur les étapes Given, c'est bon !

# Configuration avancée :lock:
Pour effectuer des tests sur des données non publiques, vous pouvez utiliser le répertoire private_features : les tests qui y sont ne sont pas suivis par git.

Afin d'avoir tout de même un suivi git de ces tests (dans un autre dépôt git non public), nous avons choisi un système de synchronisation de répertoires :
* les tests non publics sont dans le répertoire private_features
* un script de synchronisation permet de dupliquer les fichiers vers un autre répertoire (associé à un autre dépôt git)
* une étape (steps) de test est ajoutée pour vérifier que les deux fichiers (source et dupliqué) sont bien identiques

Pour cela :
* créer votre répertoire de tests privé, où vous voulez
* indiquer le chemin de ce répertoire dans le fichier params.json. C'est un chemin relatif par rapport à la racine du répertoire de navitia-checker
* dans les tests privés, ajouter l'étape "Given je teste un coverage privé"
* synchroniser les tests privés de votre autre répertoire avec le répertoire private_features de navitia-checker
* tester (à la racine du répertoire) :
```shell
behave -D environnement=mine private_features/my_very_own_private_data.feature
```

Si vous ne constatez aucune erreur sur les étapes Given, c'est bon !
