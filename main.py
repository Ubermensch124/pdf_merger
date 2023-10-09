import os

import fire
from PyPDF2 import PdfReader, PdfWriter


def parse_pdf(raw_files, changed_files):
    """
    Принимает на вход название директории с нередактированными pdf-файлами и название директории
    с подписанными титульными листами.
    
    Args:
        raw_files: путь до директории с нередактированными pdf-файлами
        changed_files: путь до директории с подписанными титульными листами
    """
    base_root = 'files/'
    
    raw_dir = os.path.join(base_root, raw_files)
    changed_dir = os.path.join(base_root, changed_files)
    result_dir = os.path.join(base_root, 'result')
    
    if not os.path.exists(result_dir):
        os.mkdir(result_dir)
    
    for filename in os.listdir(raw_dir):
        raw_path = os.path.join(raw_dir, filename)
        changed_path = os.path.join(changed_dir, filename)
        result_path = os.path.join(result_dir, filename)

        merger = PdfWriter()

        with open(raw_path, "rb") as base:
            count_of_pages = len(PdfReader(base).pages)
            merger.append(fileobj=base, pages=(1, count_of_pages))

        with open(changed_path, "rb") as first_page:
            merger.merge(position=0, fileobj=first_page, pages=(0, 1))

        with open(result_path, "wb") as output:
            merger.write(output)


if __name__ == '__main__':
    fire.Fire(parse_pdf)
