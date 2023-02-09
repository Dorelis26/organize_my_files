'''Make sure to be on the directory that needs organizing to execute this program'''

import os
from pathlib import Path

subdirectories ={
    "Documents":['.pdf','.rft','.txt',],
    "Audio":['.mpa','.mpb','.mp4'],
    "Videos":['.mov','.avi','.mp4'],
    "Images":['.jpg','.jpeg','.png']
 }

def PickDirectory(value):
    for category,suffix in subdirectories.item():
        for suffix in suffixes:
            if suffix == value:
                return category


def OrganizeDirectory():
    for items in os.scandir():
        if item.is_dir():
            continue
        file_path = Path(item)
        file_type =file_path.suffix.lower()
        directory = PickDirectory(file_type)
        directory_path =Path(directory)


        if directory_path.is_dir() != True:
            directory_path.mkdir()
        file_path.rename(directory_path.joinpath(file_path))


