import os
from jproperties import Properties 

"""
File and Directory Utility Functions

This script provides utility functions for handling file and directory operations.
The functions included allow for checking the existence of folders and files,
writing to files, opening and closing files, validating paths and loading config path based on specified criteria.
"""

def folderExists(path):
    return os.path.exists(path) and os.path.isdir(path)
def fileExists(path):
    return os.path.exists(path) and os.path.isfile(path)
def writeToFile(f,text):
    f.write(text)
def openFile(path, mode):
    if 'b' in mode: # this check is required to avoid ValueError: binary mode doesn't take an encoding argument
         return open(path , mode)
    else:
        return open(path , mode, encoding="utf-8")
def closeFile(f):
    f.close
def validate_paths(path_map):
    if not path_map:
        raise ValueError("The path map must contain at least one entry.")
    for path, expected_type in path_map.items():
        if expected_type == 'dir':
            if not os.path.isdir(path):
                raise ValueError(f"The path '{path}' is not a valid directory.")
        elif expected_type == 'file':
            if not os.path.isfile(path):
                raise ValueError(f"The file '{path}' does not exist.")
        else:
            raise ValueError(f"Invalid type '{expected_type}' for path '{path}'. Use 'dir' or 'file'.")
    print("All validations done.")
def loadConfigfile(configfile):
    configs = Properties() 
    configs.load(openFile(configfile, 'rb')) 
    return configs;