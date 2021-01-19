import pathlib
import re
import time
import sys

from pathlib import Path
from PIL import Image
from os import walk

# frm_folder = sys.argv[1]
# in_folder = sys.argv[2]

from_dir = 'pic'
into_dir = 'new_folder'


class Convertor:
    def __init__(self, frm_folder, in_folder):
        self.from_dir = frm_folder
        self.into_dir = in_folder

    def folder_creator(self):
        fr_dir_exist = Path(self.from_dir).is_dir()
        in_dir_exist = Path(self.into_dir).is_dir()

        if not fr_dir_exist:
            fr_dir_message = 'please enter right from_folder name or check if exist'
            print(fr_dir_message)
            return fr_dir_message

        elif fr_dir_exist and not in_dir_exist:
            pathlib.Path(f'./{self.into_dir}').mkdir(parents=True, exist_ok=True)
            print(f'{self.into_dir} created')

            return 'folder created'
        if fr_dir_exist and in_dir_exist:
            return True

    @staticmethod
    def imgConverter():
        # getting all the file names in folder
        _, _, filenames = next(walk(f'./{from_dir}'))

        t0 = time.time()
        for pic in filenames:
            t2 = time.time()

            # checking them for .jpg format
            regex = r".jpg+$"
            is_jpg = re.search(regex, pic)

            if is_jpg is not None:
                # print(f'\nconverting... {pic}')
                im = Image.open(f'./{from_dir}/{pic}')
                im.save(f'./{into_dir}/{pic[:-4]}.png')
            else:
                print(f'{pic} is not .jpg file')
            t3 = time.time()
            total = '%.2f' % (t3 - t2)
            print(f'{pic} converted time: {total} seconds')

        t1 = time.time()
        total = '%.2f' % (t1 - t0)

        print(f'\ntotal converted for: {total} seconds')


c = Convertor(from_dir, into_dir)
c.folder_creator()
c.imgConverter()
