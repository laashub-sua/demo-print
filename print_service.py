import convert_pdf_2_jpg
import printer


def do_print(file_path):
    if file_path.endswith('.pdf'):
        file_path = convert_pdf_2_jpg.do_convert(file_path)
    printer.do_print(file_path)
