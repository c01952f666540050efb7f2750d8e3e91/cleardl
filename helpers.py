# from os import listdir, replace, getenv, remove
import os
from os.path import isfile, join
from pathlib import Path
import gnupg
import shutil
import time

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

    # Make Archive
    shutil.make_archive(f"{time_str}_{iden}_archive", "zip", folderpath)



def uploadfile(frompath, func, **kwargs) -> None:
    # Move Files
    print("Uploading files")

