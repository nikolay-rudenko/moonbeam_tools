from JpgToPngConverter.jpg_to_png_convector import Convertor


def test_folder_creator():
    from_dir = 'source_pic'
    into_dir = 'converted'

    result = Convertor(from_dir, into_dir)
    result.folder_creator()

print(type(test_folder_creator()))