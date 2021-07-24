import csv

from PySide2.QtWidgets import QTableWidgetItem


def load_csv(filename, table):
    with open(filename, newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        row = 0
        count = sum(1 for _ in reader)
        table.setRowCount(count)
        csv_file.seek(0)
        reader = csv.DictReader(csv_file)
        for item in reader:
            table.setItem(row, 0, QTableWidgetItem(item["Name"]))
            table.setItem(row, 1, QTableWidgetItem(item["Barcode"]))
            row = row + 1
