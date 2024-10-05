import os
from pdf_reader import *
from file_utils import *
import sys

"""
Project 1
Requirements
    Store a PDF file in a folder called “/content”
    Read PDF file from the folder
    Write the content to a text file called “output.txt”
    Store this file under the “/content” folder
Error Handling
    Take care of case where folder is not available
    Take care of case where PDF file is not present in the content folder
    Take care of case where the output.txt file is not available   
 
"""

print("Current working directory :  " + os.getcwd())
base_content_path = "content"
read_file_path = base_content_path + "/" + "WEF_The_Global_Cooperation_Barometer_2024.pdf"
write_file_path = read_file_path[:read_file_path.rfind("/")] + "/output.txt";

print("project1 execution starts")

def write_pdf_into_text_file(pdf_path, txt_path):

    reader = open_pdf(pdf_path)
    numberOfPages = no_pages_in_pdf(reader)
    print("No of pages in pdf : " , numberOfPages)
    print("writing pdf in to the path " , txt_path)
    
    f = openFile(txt_path, "w")
    for pg_no in range(1, numberOfPages):
        writeToFile(f,read_page_in_pdf(reader,pg_no))
        writeToFile(f, "\n~~~~~~~~~~~~~page~~separator~~~~~~~~~~~~~~~~~~~~\n")
    closeFile(f);

def validate_existence(dirPath,filePath):
    if(folderExists(dirPath) is False or fileExists(filePath) is False ):
        print("Either " + dirPath + " directory not exits or " + filePath + " not exists in the directory")
        exit();
    print("All validations done. Proceeding to pdf-reader logic")
    
try:
    validate_paths({base_content_path : 'dir',read_file_path : 'file'})
except ValueError as e:
    print(e)  
    sys.exit(1)

write_pdf_into_text_file(read_file_path, write_file_path);












   


