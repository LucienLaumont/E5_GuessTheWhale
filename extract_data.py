import os
import zipfile

# Configuration du chemin
os.environ["KAGGLE_CONFIG_DIR"] = os.path.expanduser("~/.kaggle")

# Téléchargement du dataset
dataset_name = "andrewgustyjrstudent/happywhaleimagessortedbyspecies"
os.system(f"kaggle datasets download -d {dataset_name}")

# Décompression du fichier ZIP
zip_file = "happywhaleimagessortedbyspecies.zip"
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall("happywhale_images")

print("Dataset téléchargé et décompressé avec succès !")
