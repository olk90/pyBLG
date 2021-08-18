from pathlib import Path

from barcode import codex, ean, isxn
from barcode.writer import ImageWriter


class BarcodeProperties:
    print_barcode = False
    print_name = False
    barcode_format = None
    file_type = None
    output_path = ""


barcodeProperties = BarcodeProperties()


def create_label(name, barcode):
    output_path = barcodeProperties.output_path
    barcode_format = barcodeProperties.barcode_format
    f_type = barcodeProperties.file_type
    path_object = Path(output_path)
    filename = "{}_{}.{}".format(name, barcode_format, f_type)
    filepath = Path.joinpath(path_object, filename)
    with open(filepath, 'wb') as f:
        if barcode_format.startswith("code"):
            __handle_code_format(f, barcode_format, barcode)
        elif barcode_format.startswith("ean"):
            __handle_ean_format(f, barcode_format, barcode)
        else:
            raise ValueError("Unknown barcode format: {}".format(barcode_format))


def __handle_code_format(f, barcode_format, barcode):
    if barcode_format == "code128":
        codex.Code128(barcode, writer=ImageWriter()).write(f)
    elif barcode_format == "code39":
        codex.Code39(barcode, writer=ImageWriter()).write(f)
    else:
        raise ValueError("Unknown barcode format: {}".format(barcode_format))


def __handle_ean_format(f, barcode_format, barcode):
    if barcode_format == "ean8":
        ean.EuropeanArticleNumber8(barcode, writer=ImageWriter()).write(f)
    elif barcode_format == "ean13":
        ean.EuropeanArticleNumber13(barcode, writer=ImageWriter()).write(f)
    elif barcode_format == "ean14":
        ean.EuropeanArticleNumber14(barcode, writer=ImageWriter()).write(f)
    elif barcode_format == "jan":
        ean.JapanArticleNumber(barcode, writer=ImageWriter()).write(f)
    else:
        raise ValueError("Unknown barcode format: {}".format(barcode_format))


def __handle_isbn_format(f, barcode_format, barcode):
    if barcode_format == "isbn10":
        isxn.InternationalStandardBookNumber10(barcode, writer=ImageWriter()).write(f)
    elif barcode_format == "isbn13":
        isxn.InternationalStandardBookNumber13(barcode, writer=ImageWriter()).write(f)
    elif barcode_format == "issn":
        isxn.InternationalStandardSerialNumber(barcode, writer=ImageWriter()).write(f)
    else:
        raise ValueError("Unknown barcode format: {}".format(barcode_format))

