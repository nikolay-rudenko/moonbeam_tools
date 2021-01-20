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
    def __init__(self, frm_folder, in_folder, regex=r".jpg+$"):
        self.from_dir = frm_folder
        self.into_dir = in_folder
        self.regex = regex

    def folder_creator(self):
        try:
            source_dir_exist = Path(self.from_dir).is_dir()
            converted_dir_exist = Path(self.into_dir).is_dir()

            if not source_dir_exist:
                dir_not_found_message = f'\n[ {self.from_dir} directory ] does not exist\n' \
                                        f'\nPlease enter right source folder name or check if exist.' \
                                        f'\nNotice! Python script and source dir must be in on directory.\n'
                print(dir_not_found_message)
                return False

            elif source_dir_exist and not converted_dir_exist:
                pathlib.Path(f'./{self.into_dir}').mkdir(parents=True, exist_ok=True)
                print(f'\n{self.into_dir} folder created')
                return 'folder created'

            if source_dir_exist and converted_dir_exist:
                return True

        except TypeError:
            print('please enter the name of the folder in string format')
            return 'wrong data type'


    def img_converter(self):

        try:
            self.folder_creator()

            # getting all the file names in folder
            _, _, filenames = next(walk(f'./{self.from_dir}'))

            t0 = time.time()
            for pic in filenames:
                t2 = time.time()

                # verify that picture has .jpg format
                regex = r".jpg+$"
                is_jpg = re.search(regex, pic)
                is_jpg_test = re.search(self.regex, pic)

                if is_jpg_test is not None:
                    # converting picture
                    im = Image.open(f'./{self.from_dir}/{pic}')
                    im.save(f'./{self.into_dir}/{pic[:-4]}.png')
                else:
                    print(f'{pic} is not .jpg file')
                    return f'{pic} is not .jpg file'

                t3 = time.time()
                total_pic = '%.2f' % (t3 - t2)
                print(f'{pic} converted time: {total_pic} seconds')
                return 'successfully converted all pictures'


            t1 = time.time()
            total_all_pictures = '%.2f' % (t1 - t0)

            print(f'\ntotal converted time {total_all_pictures} seconds')

        except (FileNotFoundError, TypeError):
            if TypeError:
                return 'wrong type argument given'
            else:
                print('please check if file exist')
                return 'file not found'



# Convertor(from_dir, into_dir).img_converter()
