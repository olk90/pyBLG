from pathlib import Path

from barcode import Code128
from barcode.writer import ImageWriter


class BarcodeProperties:
    print_barcode = False
    print_name = False
    output_path = ""


barcodeProperties = BarcodeProperties()


def print_barcode_img(output_path, name, barcode_format, ftype, barcode):
    path_object = Path(output_path)
    filename = "{}_{}.{}".format(name, barcode_format, ftype)
    filepath = Path.joinpath(path_object, filename)
    with open(filepath, 'wb') as f:
        Code128(barcode, writer=ImageWriter()).write(f)
