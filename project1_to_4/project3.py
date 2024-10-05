import os
from pdf_reader import *
from file_utils import *
import sys

"""
Project 3
    Read content from a particular page
Requirements
    Update project 1 and update the reading of content 
    Take a page number as an input from command prompt
    Read content of the page number provided and write to the output file
Error Handling
    Take care of case where folder is not available
    Take care of case where PDF file is not present in the content folder
    Take care of case where the output.txt file is not available   

"""

print("Current working directory :  " + os.getcwd())
base_content_path = "content"
read_file_path = base_content_path + "/" + "WEF_The_Global_Cooperation_Barometer_2024.pdf"
write_file_path = read_file_path[:read_file_path.rfind("/")] + "/output.txt";

print("project3 execution starts")


def write_pdf_into_text_file(pdf_path, txt_path):
    reader = open_pdf(pdf_path)
    numberOfPages = no_pages_in_pdf(reader)
    print("No of pages in pdf : " , numberOfPages)
    print("writing pdf in to the path " , txt_path)
    f = openFile(txt_path, "w")
    pg_no = get_page_num(numberOfPages)
    writeToFile(f,read_page_in_pdf(reader,pg_no))
    closeFile(f);

def validate_existence(dirPath,filePath):
    if(folderExists(dirPath) is False or fileExists(filePath) is False ):
        print("Either " + dirPath + " directory not exits or " + filePath + " not exists in the directory")
        exit();
    print("All validations done. Proceeding to pdf-reader logic")

def get_page_num(pagenum):
    print(f"Enter any page number from 1 to {pagenum} to read from the file.")
    input_num =  int(input()); 
    if input_num < 1 or input_num > pagenum:
        print("Invalid page number. Please retry.")
        return get_page_num(pagenum)
    else: return input_num
    


try:
    validate_paths({base_content_path : 'dir',read_file_path : 'file'})
except ValueError as e:
    print(e)  
    sys.exit(1)

write_pdf_into_text_file(read_file_path, write_file_path);












   


