import jpg_to_png_convector


def test_source_dir_not_exist():
    from_dir = 'source_pict'
    into_dir = 'converted'
    result = jpg_to_png_convector.Convertor(from_dir, into_dir)

    assert result.folder_creator() == False


def test_source_and_into_dir_exist():
    from_dir = 'source_pic'
    into_dir = 'converted'
    result = jpg_to_png_convector.Convertor(from_dir, into_dir)

    assert result.folder_creator() == True


def test_handling_exception():
    from_dir = [4]
    into_dir = (4)
    result = jpg_to_png_convector.Convertor(from_dir, into_dir)

    assert result.folder_creator() == 'wrong data type'


def test_img_converter_success():
    from_dir = 'source_pic'
    into_dir = 'converted'
    result = jpg_to_png_convector.Convertor(from_dir, into_dir)

    assert result.img_converter() == 'successfully converted all pictures'


def test_img_converter_negative():
    from_dir = 'source_pic'
    into_dir = 2
    result = jpg_to_png_convector.Convertor(from_dir, into_dir)

    assert result.img_converter() == 'wrong type argument given'


def test_img_converter_exceptions():
    from_dir = 'source_pic'
    into_dir = 2
    result = jpg_to_png_convector.Convertor(from_dir, into_dir, None)

    assert result.img_converter() == 'wrong type argument given'

def test_img_converter_exceptions():
    from_dir = 'source_pic'
    into_dir = 2
    result = jpg_to_png_convector.Convertor(from_dir, into_dir, None)

    assert result.img_converter() == 'wrong type argument given'

def test_img_converter_regex():
    from_dir = 'source_pic'
    into_dir = 2
    result = jpg_to_png_convector.Convertor(from_dir, into_dir, r".pgn+$")

    assert result.img_converter() == 'nasa.jpg is not .jpg file'