# Downloads Folder Cleanup Tool - BETA

I am currently testing this tool just to automate removal of specific file types in my downloads folder.
Please use at your own risk.

## How to run

Requirements (to start):
Python 3, although this is written in 3.10.2

To install python, you can download it here:
https://www.python.org/downloads/

You can first navigate to the folder directory. Then you can install the required packages.
'''cd clear-dl'''
'''pip install -r requirements.txt'''

You can then run the script via:

'''python3 -m clear-dl.py'''

If you do not have python scripts in your PATH folder. (I can show you how to do this if you'd like).

There are some specific arguments:

'''python3 -m clear-dl.py --filepath C:\Users\USERID\Downloads'''

So you can select the specific path that you want to remove from.
And that's it! You won't need to do much else.

## Current roadmap

To make this universal we will need to add some features
- We will need to add os detection
- It will have to remove the dependency on knowing the appdata folder to store the files temporarily
- Add ability to run this script at the end of day, for example
- we should add encryption and upload as a later feature once everything is working correctly.
