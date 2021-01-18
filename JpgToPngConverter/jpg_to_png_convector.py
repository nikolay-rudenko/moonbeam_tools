# Run file from command with the ability to give 2 argument
# ...
# first arg = base folder with img 'Pokemon's'
# second arg = new folder with converted img 'convertedImg'
# ...
# 1. Grab first and second argument
# 2. Check if new folder exist / if not create it
# 3. Convert img to png / save them to new folder

import pathlib
from pathlib import Path

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
    else:
        if fr_dir_exist and in_dir_exist:
            print(True)


def do_twice(func):
    func(frm_folder, in_folder)
    func(frm_folder, in_folder)


do_twice(folder_creator)