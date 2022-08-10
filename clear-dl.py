from os import listdir, replace, getenv, remove
from os.path import isfile, join
from pathlib import Path
import argparse
import gnupg

# Parse Arguments


# Get Download Path
mypath = str(Path.home() / "Downloads")
print(mypath)

# Get Files
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# Get JSON
onlyjson = [f for f in onlyfiles if f.split(".")[-1] == 'json']

# Get Binaries
onlyexe = [f for f in onlyfiles if f.split(".")[-1] == 'exe']

# Get Pub Key File path
# print(str(Path.home() / "jcvoo_0x511ADA8A_public.asc"))
pubkey_path = str(Path.home() / "jcvoo_0x511ADA8A_public.asc")
pubkey = open(pubkey_path, "r").read()

# Import keys
gpg = gnupg.GPG(gnupghome=str(Path.home()))
import_res = gpg.import_keys(pubkey)

# Move all files into folder - TODO

# tempfolder = getenv("APPDATA")
# for jsonfile in onlyjson:
#    replace(str(Path.home() / jsonfile), str(tempfolder+"/"+jsonfile))

# Zip files - TODO

# Encrypt Files - TODO

# Delete Original JSON Files
for jsonfile in onlyjson:
    remove(f"{mypath}/{jsonfile}")

# Delete EXE files
for exefile in onlyexe:
    remove(f"{mypath}/{exefile}")

# Move to cloud