import pdf_water_marker

def test_watermarked_file_created():
    template = './pdf/result.pdf'
    wtr = './pdf/wtr.pdf'
    result = pdf_water_marker.watermarker(template, wtr)

    assert result == True

def test_watermarked_not_pdf():
    template = ''
    wtr = ''
    result = pdf_water_marker.watermarker(template, wtr)

    assert result == ('FileNotFoundError on', 'pdf_water_marker.py', 8)

def test_watermarked_wrong_input():
    template = None
    wtr = None
    result = pdf_water_marker.watermarker(template, wtr)

    assert result == 'enter file in string format'
