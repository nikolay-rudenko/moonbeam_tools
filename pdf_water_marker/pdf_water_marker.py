import PyPDF2
from pathlib import Path
import sys, os

def watermarker(template_pdf, watermart_pdf):

  try:
    template = PyPDF2.PdfFileReader(open(template_pdf, 'rb'))
    watermark = PyPDF2.PdfFileReader(open(watermart_pdf, 'rb'))
    output = PyPDF2.PdfFileWriter()

    for i in range(template.getNumPages()):
      page = template.getPage(i)
      page.mergePage(watermark.getPage(0))
      output.addPage(page)

      with open('./pdf/watermarked_output.pdf', 'wb') as file:
        output.write(file)

      my_file = Path('./pdf/watermarked_output.pdf')
      return my_file.is_file()
  except FileNotFoundError:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    return 'FileNotFoundError on',fname, exc_tb.tb_lineno
  except TypeError:
    return 'enter file in string format'



