import shutil
import os
import json

# à lancer depuis le repertoire de navitia-checker
nav_checker_folder = os.path.join(os.getcwd(), "private_features")

params = json.load(open('steps/params.json'))
datascript_folder = params['navitia-checker']['private_features_repo']

def synchro_to_nav_checker():
    source = datascript_folder
    destination = nav_checker_folder
    synchro(source, destination)

def synchro_from_nav_checker():
    destination = datascript_folder
    source = nav_checker_folder
    synchro(source, destination)

def synchro(source, destination):
    for a_feature_file in os.listdir(source) :
        file_name, extension = os.path.splitext(a_feature_file)
        if extension == ".feature" :
            destination_file = os.path.join(destination, a_feature_file)
            source_file = os.path.join(source, a_feature_file)
            print ("copie du fichier {} de {} vers {}".format(a_feature_file, source_file, destination_file))
            shutil.copy(source_file, destination_file)

synchro_from_nav_checker()
# attention, ça "synchronise" en écrasant. Les éventuels conflits sont à régler dans l'autre dépot git.
