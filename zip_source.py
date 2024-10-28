#    EcoleDirecte Bot (zip_source.py)
#    Copyright (C) 2023-2024 MrBeam89_
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <https://www.gnu.org/licenses/>.

import os
import tempfile
import git
import zipfile
import subprocess

from config import ECOLEDIRECTE_DIR

TEMP_DIR = tempfile.gettempdir() # Chemin d'accès du répertoire temporaire pour stocker l'archive


# Supprimer l'archive ZIP du code source
def delete_zip_source(zip_filename):
    if os.path.exists(zip_filename):
        try:
            os.remove(zip_filename)
        except:
            print(f'Erreur lors de la supression du fichier {zip_filename}')


# Créer l'archive ZIP du code source
def create_zip_source(zip_filename):
    # Obtenir les fichiers à inclure dans l'archive (sans ceux spécifiés dans le fichier .gitignore)
    files_to_zip = subprocess.check_output(['git', '-C', ECOLEDIRECTE_DIR, 'ls-files'], text=True).splitlines()

    # Chemin d'accès à l'archive (stockée dans le répertoire temporaire)
    temp_zip_filepath = os.path.join(TEMP_DIR, zip_filename)

    # Ajouter les fichiers à l'archive
    with zipfile.ZipFile(temp_zip_filepath, 'w') as zip_file:
        for file in files_to_zip:
            zip_file.write(file)

    # Retourner le chemin d'accès à l'archive
    return temp_zip_filepath