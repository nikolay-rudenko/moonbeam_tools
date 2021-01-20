import pathlib
import re
import time
import sys
import os

from pathlib import Path
from PIL import Image
from os import walk

# from_dir = sys.argv[1]
# into_dir = sys.argv[2]

# Use it in case running without parameters
# from_dir = 'source_pic'
# into_dir = 'converted'


class Convertor():
    def __init__(self, frm_folder, in_folder):
        self.from_dir = frm_folder
        self.into_dir = in_folder

    def folder_creator(self):
        source_dir_exist = Path(self.from_dir).is_dir()
        converted_dir_exist = Path(self.into_dir).is_dir()

        if not source_dir_exist:
            dir_not_found_message = f'\n[ {self.from_dir} directory ] does not exist\n' \
                                    f'\nPlease enter right source folder name or check if exist.' \
                                    f'\nNotice! Python script and source dir must be in on directory.\n'
            print(dir_not_found_message)

            return dir_not_found_message

        elif source_dir_exist and not converted_dir_exist:
            pathlib.Path(f'./{self.into_dir}').mkdir(parents=True, exist_ok=True)
            print(f'\n{self.into_dir} folder created')
            return 'folder created'

        if source_dir_exist and converted_dir_exist:
            return True


    def imgConverter(self):
        self.folder_creator()

        # getting all the file names in folder
        _, _, filenames = next(walk(f'./{from_dir}'))

        t0 = time.time()
        for pic in filenames:
            t2 = time.time()

            # verify that picture has .jpg format
            regex = r".jpg+$"
            is_jpg = re.search(regex, pic)

            if is_jpg is not None:
                # converting picture
                im = Image.open(f'./{from_dir}/{pic}')
                im.save(f'./{into_dir}/{pic[:-4]}.png')
            else:
                print(f'{pic} is not .jpg file')
            t3 = time.time()
            total_pic = '%.2f' % (t3 - t2)
            print(f'{pic} converted time: {total_pic} seconds')

        t1 = time.time()
        total_all_pictures = '%.2f' % (t1 - t0)

        print(f'\ntotal converted time {total_all_pictures} seconds')

#
# Convertor(from_dir, into_dir).imgConverter()
