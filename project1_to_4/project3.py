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

reader = open_pdf(read_file_path)
numberOfPages = no_pages_in_pdf(reader)
print("No of pages in pdf : " , numberOfPages)
print("writing pdf in to the path " , write_file_path)
f = openFile(write_file_path, "w")
pg_no = get_page_num(numberOfPages)
writeToFile(f,read_page_in_pdf(reader,pg_no))
closeFile(f);












   


