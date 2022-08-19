from os import getenv
# listdir, walk, remove
# from os.path import isfile, join
from pathlib import Path
# import argparse
import gnupg
from time import sleep
# import dotenv

# Local Imports
from helpers import movefiles, check_create_folder, zipfiles, listOfFiles

# Parse Arguments - TODO

# Get appdata filepath
temp_filepath = getenv("APPDATA")+"\\"+"TEMP"

# Check Create Temp folder
check_create_folder(temp_filepath)

# List Filetypes to remove
typelist = ['json']

# Get Download Path
dlpath = str(Path.home() / "Downloads")

# Get ALL Files via helper function
file_list = {}
for filetype in typelist:
    file_list[filetype] = listOfFiles(dlpath, filetype)

# Get all relevant files
# onlyfiles = [f for f in listdir(dlpath) if isfile(join(dlpath, f))]
# file_list = {}
# for filetype in typelist:
#     file_list[filetype] = [f for f in onlyfiles if f.split(".")[-1] == filetype]

# Get Pub Key File path - default for me
pubkey_path = str(Path.home() / "0x511ADA8A_public.asc")
pubkey = open(pubkey_path, "r").read()

# Import keys for encryption
gpg = gnupg.GPG(gnupghome=str(Path.home()))
import_res = gpg.import_keys(pubkey)
public_keys = gpg.list_keys()

# Main Loop - For all filetypes
for filetype in file_list.keys():

    # Move all files into TEMP folder
    movefiles(dlpath, temp_filepath, file_list[filetype])

    # ZIP files in TEMP folder
    zipfiles(temp_filepath, filetype)

    # Sleep to make sure that we have unique filenames - TODO
    # This is because the filenames are based on the unix timestamp
    sleep(1)

# Remove temp files


# Encrypt Files - TODO

# Upload Files - TODO

# Delete Local Files - TODO
