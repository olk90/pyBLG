from pathlib import Path

from barcode import Code128
from barcode.writer import ImageWriter


class BarcodeProperties:
    print_barcode = False
    print_name = False
    barcode_format = None
    file_type = None
    output_path = None


barcodeProperties = BarcodeProperties()


def create_label(name, barcode):
    output_path = barcodeProperties.output_path
    barcode_format = barcodeProperties.barcode_format
    f_type = barcodeProperties.file_type
    path_object = Path(output_path)
    filename = "{}_{}.{}".format(name, barcode_format, f_type)
    # barcode_class = get_barcode_class(barcode_format)
    # c128 = Code128(barcode)
    # fullname = c128.save(filename, text=name)
    filepath = Path.joinpath(path_object, filename)
    with open(filepath, 'wb') as f:
        Code128(barcode, writer=ImageWriter()).write(f)
