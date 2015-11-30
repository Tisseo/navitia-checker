
Lancer behave à la racine du repo

behave ./private_features/fr_npdc.feature -D environment=prod
behave ./public_features/fr_idf.feature -D environment=sim --junit
