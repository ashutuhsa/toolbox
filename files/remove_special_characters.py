############################
# Python version 3.8
# @author me@mad4n7.com
############################

import os
from os import listdir
from os import path

VALID_CHARACTERS = ['-', '_']

folder_path = input('Folder path: ')

if folder_path == 'pwd':
    print('Suggested folder: ' + os.getcwd())
    folder_path = input('Sugested folder: ', )

def getModifiedPath(originalPath):
    result = ''
    file_name = originalPath.split('.')
    for c in file_name[0]:
        if c in VALID_CHARACTERS or c.isalpha():
            result += c

    result += '.' + file_name[1]
    return result
    #return ''.join(c for c in originalPath if c.isalpha())

for filename in listdir(folder_path):
    src = folder_path + filename
    dst = folder_path + getModifiedPath(filename)
    print(f" Renamed: {src} to ===> {dst}")

    os.rename(src,dst)
