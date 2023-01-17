from convert_word import convert_all_word_to_pdf_contain_name


def main():
    file_name_to_convert = input("Enter file name to convert: ")
    convert_all_word_to_pdf_contain_name(file_name_to_convert)


if __name__ == '__main__':
    main()
