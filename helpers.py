# from os import listdir, replace, getenv, remove
import os
from os.path import isfile, join, exists
from pathlib import Path
import gnupg
import shutil
import time

# Get File List
def listOfFiles(path, filetype=None) -> list:

    # Get FULL file list
    filelist = [f for f in os.listdir(path) if isfile(join(path, f))]

    # If no filetype specified
    if not filetype:

        # Return Filelist
        return filelist

    # Otherwise return for specific filetype
    else:

        # Sanitise input (string only)
        if type(filetype) == str:

            # Return filelist for specific filetype
            return [f for f in filelist if f.split(".")[-1] == filetype]

# Check if folder exists, if not create
def check_create_folder(folderpath) -> None:

    # If folder does not exist
    if not os.path.exists(folderpath):
        
        # Create folder
        os.makedirs(folderpath)

        # Test Print
        print(f"Folder Created!: {folderpath}")

# Move Files function
def movefiles(frompath = None, topath = None, filelist = None) -> None:
    
    # Test Print
    print("-- Moving files --")
    
    # Check inputs
    if frompath and topath and filelist:

        # Iterate filenames
        for filename in filelist:

            # Test Print
            print(f"Moving {filename}")

            # Move files
            os.replace(frompath+"\\"+filename, topath+"\\"+filename)

# Zip Files in Folder function
def zipfiles(folderpath, iden) -> None:
    
    # Test Print
    print("Compressing files")

    # Getting unix timestamp for unique filename
    time_str = int(time.time())

    # Check Create folder
    check_create_folder(folderpath)

    # Make Archive
    shutil.make_archive(f"{time_str}_{iden}_archive", "zip", folderpath)

# Remove any all files from the TEMP folder
def cleanTempFiles(filepath, filelist, filetype):
    print(f"Removing filetype:{filetype} from junk!")

    # For all files
    for files in filelist:

        # Remove the files
        os.remove(filepath+"\\"+files)


def uploadfile(frompath, func, **kwargs) -> None:
    # Move Files
    print("Uploading files")

