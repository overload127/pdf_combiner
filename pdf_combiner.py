import os

from PyPDF2 import PdfFileWriter, PdfFileReader


NAME_OUT_PDF = "combined.pdf"


def append_pdf(input_pdf, output):
    [output.addPage(input_pdf.getPage(page_num)) for page_num in range(input_pdf.numPages)]


def get_file_from_dir(dir_name):
    list_file = []
    for file in os.listdir(dir_name):
        if file.endswith(".pdf") and file != NAME_OUT_PDF:
            list_file.append(os.path.join(dir_name, file))

    return list_file

def create_from_files(list_files, dir_name):

    output = PdfFileWriter()
    
    for cur_file in list_files:
        append_pdf(PdfFileReader(open(cur_file, "rb")), output)

    output.write(open(os.path.join(dir_name, NAME_OUT_PDF),"wb"))


if __name__ == "__main__":
    all_file = []

    for file in os.listdir("."):
        if file.endswith(".pdf") and file != NAME_OUT_PDF:
            print(file)
            all_file.append(file)

    if not all_file:
        print("Не найден ни один файл")
        exit()

    output = PdfFileWriter()
    
    for file in all_file:
        append_pdf(PdfFileReader(open(file,"rb")), output)

    output.write(open(NAME_OUT_PDF,"wb"))
