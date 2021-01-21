import pathlib
import re
import time
import sys

from pathlib import Path
from PIL import Image
from os import walk


input_dir = sys.argv[1]
output_dir = sys.argv[2]

# Use it in case running without parameters
# input_dir = 'source_pic'
# output_dir = 'converted'


class Convertor():
    def __init__(self, in_folder, out_folder, regex=r".jpg+$"):
        self.input_dir = in_folder
        self.output_dir = out_folder
        self.regex = regex

    def folder_creator(self):
        try:
            input_dir_exist = Path(self.input_dir).is_dir()
            output_dir_exist = Path(self.output_dir).is_dir()

            if not input_dir_exist:
                input_dir_not_found = f'\n[ {self.input_dir} directory ] does not exist\n' \
                                        f'\nPlease enter right source folder name or check if exist.' \
                                        f'\nNotice! Python script and source dir must be in one directory.\n'
                print(input_dir_not_found)
                return False

            elif input_dir_exist and not output_dir_exist:
                pathlib.Path(f'./{self.output_dir}').mkdir(parents=True, exist_ok=True)
                print(f'\n{self.output_dir} folder created')
                return 'folder created'

            if input_dir_exist and output_dir_exist:
                return True

        except TypeError:
            print('please enter the name of the folder in string format')
            return 'wrong data type'


    def img_converter(self):

        try:
            self.folder_creator()

            # getting all the file names in folder
            _, _, filenames = next(walk(f'./{self.input_dir}'))

            t0 = time.time()
            print('\n')
            for pic in filenames:
                t2 = time.time()

                # verify that picture has .jpg format
                is_jpg = re.search(self.regex, pic)

                if is_jpg is not None:
                    # converting picture
                    im = Image.open(f'./{self.input_dir}/{pic}')
                    im.save(f'./{self.output_dir}/{pic[:-4]}.png', 'png')
                else:
                    print(f'{pic} is not .jpg file')
                    return f'{pic} is not .jpg file'

                t3 = time.time()
                total_pic = '%.2f' % (t3 - t2)
                print(f'Converted... [ {pic} ] for {total_pic} seconds')


            t1 = time.time()
            total_all_pictures = '%.2f' % (t1 - t0)

            print(f'\nTotal time: {total_all_pictures} seconds')

        except (FileNotFoundError, TypeError):
            if TypeError:
                return 'wrong type argument given'
            else:
                print('please check if file exist')
                return 'file not found'


Convertor(input_dir, output_dir).img_converter()
