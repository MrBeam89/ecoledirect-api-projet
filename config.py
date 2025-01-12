#    EcoleDirecte Bot (config.py)
#    Copyright 2023-2024 MrBeam89_
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

import re
from os.path import basename

import configparser

ECOLEDIRECTE_DIR = __file__.rstrip(basename(__file__))
CONFIG_FILENAME = f"config.ini"

def get_config():
    # Vérification fichier de configuration
    try:
        config = configparser.ConfigParser()
        config.read(f"{ECOLEDIRECTE_DIR}{CONFIG_FILENAME}")

        print(f'Ouverture du fichier "{ECOLEDIRECTE_DIR}{CONFIG_FILENAME}" réussie!')
        BOT_TOKEN_FILENAME = config["Files"]["BOT_TOKEN_FILENAME"]
        DB_KEY_FILENAME = config["Files"]['DB_KEY_FILENAME']
        DB_FILENAME = config["Files"]["DB_FILENAME"]
        BOT_COMMAND_PREFIX = config["Bot"]["BOT_COMMAND_PREFIX"]
        LOGGING_LEVEL = config["Bot"]["LOGGING_LEVEL"]
        COOLDOWN = config["Bot"]["COOLDOWN"]
        EMBED_COLOR = config["Bot"]["EMBED_COLOR"]
        ZIP_SOURCE_CODE_FILENAME = config["Files"]["ZIP_SOURCE_CODE_FILENAME"]

    except FileNotFoundError:
        print(f'"{CONFIG_FILENAME}" est introuvable!')
        input("Appuyez sur Entree pour quitter...")
        exit()

    # Vérification du fichier de token
    try:
        token_file = open(f"{ECOLEDIRECTE_DIR}{BOT_TOKEN_FILENAME}", "r")
        print(f'Ouverture du fichier "{ECOLEDIRECTE_DIR}{BOT_TOKEN_FILENAME}" réussie!')
        token_file.close()
    except FileNotFoundError:
        print(f'Fichier introuvable! Placez le token dans le fichier "{ECOLEDIRECTE_DIR}{BOT_TOKEN_FILENAME}"')
        input("Appuyez sur Entree pour quitter...")
        exit()

    # Vérification du fichier de clé pour la base de données
    try:
        db_key_file = open(f"{ECOLEDIRECTE_DIR}{DB_KEY_FILENAME}", "r")
        print(f'Ouverture du fichier "{ECOLEDIRECTE_DIR}{DB_KEY_FILENAME}", réussie!')
        db_key_file.close()

    except FileNotFoundError:
        from keygen import getkey
        print(f'Fichier introuvable! Création d\'une nouvelle clé dans le fichier "{ECOLEDIRECTE_DIR}{DB_KEY_FILENAME}"...')
        getkey()
        print(f'Création d\'une nouvelle clé dans le fichier "{ECOLEDIRECTE_DIR}{DB_KEY_FILENAME}" réussie!')
        print(r"/!\ ATTENTION /!\ La base de données (si non vide) ne fonctionnera pas correctement avec la nouvelle clé.")

    # Vérification du fichier de la base de données
    try:
        db_key_file = open(f"{ECOLEDIRECTE_DIR}{DB_FILENAME}", "r")
        print(f'Ouverture du fichier "{ECOLEDIRECTE_DIR}{DB_FILENAME}" réussie!')
        db_key_file.close()

    except FileNotFoundError:
        print(f'Fichier introuvable! Création de la base de données "{ECOLEDIRECTE_DIR}{DB_FILENAME}"...')

    # Vérification du préfixe du bot
    if not isinstance(BOT_COMMAND_PREFIX, str):
        print("Préfixe de commande de bot invalide!")
        input("Appuyez sur Entree pour quitter...")
        exit()
    else:
        print("Préfixe de commande de bot valide!")

    # Vérification du niveau de journalisation
    try:
        LOGGING_LEVEL = int(LOGGING_LEVEL)
    except ValueError:
        print("Niveau de journalisation invalide!")
        input("Appuyez sur Entree pour quitter...")
        exit()
    print("Niveau de journalisation valide!")

    # Vérification du cooldown
    try:
        COOLDOWN = int(COOLDOWN)
    except ValueError:
        print("Cooldown invalide!")
        input("Appuyez sur Entree pour quitter...")
        exit()
    print("Cooldown valide!")

    # Vérification de la couleur de l'embed
    try:
        int(EMBED_COLOR, 16)
    except ValueError:
        print("Couleur de l'embed invalide!")
        input("Appuyez sur Entree pour quitter...")
        exit()

    color_pattern = re.compile("^0x[0-9a-fA-F]{6}$")
    if not color_pattern.match(EMBED_COLOR):
        print("Couleur de l'embed invalide!")
        input("Appuyez sur Entree pour quitter...")
        exit()
    else:
        print("Couleur de l'embed valide!")

    # Vérification du nom de fichier du ZIP du code source
    if not isinstance(ZIP_SOURCE_CODE_FILENAME, str):
        print("Nom du fichier du ZIP du code source invalide!")
        input("Appuyez sur Entree pour quitter...")
        exit()
    else:
        print("Nom du fichier du ZIP du code source valide!")

    # Renvoie la configuration
    print("Configuration valide!")
    
    return {
        "ECOLEDIRECTE_DIR": ECOLEDIRECTE_DIR,
        "BOT_TOKEN_FILENAME": BOT_TOKEN_FILENAME,
        "DB_KEY_FILENAME": DB_KEY_FILENAME,
        "DB_FILENAME": DB_FILENAME,
        "CONFIG_FILENAME": CONFIG_FILENAME,
        "BOT_COMMAND_PREFIX": BOT_COMMAND_PREFIX,
        "LOGGING_LEVEL": LOGGING_LEVEL,
        "COOLDOWN": COOLDOWN,
        "EMBED_COLOR": int(EMBED_COLOR, 16),
        "ZIP_SOURCE_CODE_FILENAME": ZIP_SOURCE_CODE_FILENAME
    }
