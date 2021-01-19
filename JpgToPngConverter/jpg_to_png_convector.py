import pathlib
import re

from pathlib import Path
from PIL import Image
from os import walk

# frm_folder = sys.argv[1]
# in_folder = sys.argv[2]

frm_folder = 'pokemons'
in_folder = '2'


def folder_creator(from_dir, into_dir):
    fr_dir_exist = Path(from_dir).is_dir()
    in_dir_exist = Path(into_dir).is_dir()

    if not fr_dir_exist:
        print('please enter right from_folder name or check if exist')
    elif fr_dir_exist and not in_dir_exist:
        pathlib.Path(f'./{into_dir}').mkdir(parents=True, exist_ok=True)
    if fr_dir_exist and in_dir_exist:
        return True

folder_creator(frm_folder, in_folder)


def imgConverter():

    # getting all the file names in folder
    _, _, filenames = next(walk(f'./{frm_folder}'))
    regex = r".jpg+$"
    isJpg = re.search(regex, filenames[0])

    for pic in filenames:
        im = Image.open(f'./{frm_folder}/{pic}')
        im.save(f'./{in_folder}/{pic[:-4]}.png')

    # for pic in range(len(filenames)):
    #     im = Image.open(f'./{frm_folder}/{pic}')
    #     yield im.save(f'./{in_folder}/{pic[:-4]}.png')

    # checking them for .jpg format
    if isJpg != None:
        print('converting [0] img')
    else:
        print('[0] is not .jpg')





imgConverter()

