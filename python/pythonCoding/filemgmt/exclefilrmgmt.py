from openpyxl import os Workbook, load_workbook
import os


def write_excle(filename):
    workbook = Workbook()
    sheet = workbook.active
    sheet.append(["Name", "Age"])
    sheet.append(["john doe", 30])
    sheet.append(["jane smith", 25])
    workbook.save(filename)

def read_excle