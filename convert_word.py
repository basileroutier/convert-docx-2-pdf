import pydocx
from docx2pdf import convert
import os


def __find_file_contain_name(name):
    list_of_files = []
    for file in os.listdir(os.getcwd()):
        if (file.lower().find(name) != -1 or name == "") and file.lower().endswith(".docx"):
            list_of_files.append(file)

    return list_of_files


def convert_all_word_to_pdf_contain_name(name):
    list_of_files = __find_file_contain_name(name)
    if len(list_of_files) == 0:
        print(f"No file found with name: {name}")
        return

    print("Converting files...")
    for index, file_name in enumerate(list_of_files):
        __docx_to_pdf(file_name)
        print(f"Converted {index + 1} of {len(list_of_files)}")


def __docx_to_pdf(docx_file_name):
    convert(docx_file_name, f"{docx_file_name.replace('.docx', '.pdf')}")
