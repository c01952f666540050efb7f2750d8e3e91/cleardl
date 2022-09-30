from os import getenv
from pathlib import Path
import argparse
import gnupg
from time import sleep

# Local Imports
from helpers import movefiles, check_create_folder, zipfiles, listOfFiles, cleanTempFiles

# Parse Arguments
parser = argparse.ArgumentParser(description="Remove JSON files from specific folder")
parser.add_argument('--filepath', help="Filepath of folder to remove files from")
args = parser.parse_args()
if args.filepath and type(args.filepath) == str :
    rm_filepath = args.filepath

# Get appdata filepath - This makes it windows only - TODO - add check for mac
temp_filepath = getenv("APPDATA")+"\\"+"TEMP"

# Check Create Temp folder
check_create_folder(temp_filepath)

# List Filetypes to remove
typelist = ['json']

# Get Download Path
rmpath = str(Path.home() / "Downloads")

# Get ALL Files via helper function
file_list = {}
for filetype in typelist:
    file_list[filetype] = listOfFiles(rm_filepath, filetype)

# Main Loop - For all filetypes
for filetype in file_list.keys():

    # Move all files into TEMP folder
    movefiles(rm_filepath, temp_filepath, file_list[filetype])

    # ZIP files in TEMP folder
    zipfiles(temp_filepath, filetype)

    # Sleep to make sure that we have unique filenames - TODO
    # This is because the filenames are based on the unix timestamp
    sleep(1)

    # Remove temp files
    cleanTempFiles(temp_filepath, file_list[filetype], filetype)

# Get Pub Key File path - default for me
# pubkey_path = str(Path.home() / "0x511ADA8A_public.asc")
# pubkey = open(pubkey_path, "r").read()

# Import keys for encryption
# gpg = gnupg.GPG(gnupghome=str(Path.home()))
# import_res = gpg.import_keys(pubkey)
# public_keys = gpg.list_keys()


# print(import_res)

# Encrypt Zipped File - TODO
# testfilepath = "C:\Users\jcvoo\Documents\work\scripts\file-scripts\clear-dl\1660985753_json_archive.zip"
# with open(testfilepath, 'rb') as f:
#     status = gpg.encrypt_file(
#         f,
        
#     )

# Upload Files - TODO

# Delete Local Zipped Files - TODO
