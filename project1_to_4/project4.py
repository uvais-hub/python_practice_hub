import os
import re
from pypdf import PdfReader
from jproperties import Properties 
from pdf_reader import *
from file_utils import *
import sys

"""
Project 4
    Read regular expression from a config file and extract content
Requirements
    Update project 3
    Add support for a configuration file 
    In the configuration file set a config with key “regex” and value some regular expression that will match a part of the content in the PDF
    Update code to extract only the content matching the regular expression 
    Write to the output file
Error Handling
    Take care of case where folder is not available
    Take care of case where PDF file is not present in a sub-folder
    Take care of case where the output.txt file is not available in a sub-folder
    Take care of case where no configuration file is available
    Take care of the case where configuration file does not have the regular expression
"""

print("Current working directory :  " + os.getcwd())
base_content_path = "content"
read_file_path = base_content_path + "/" + "WEF_The_Global_Cooperation_Barometer_2024.pdf"
write_file_path = read_file_path[:read_file_path.rfind("/")] + "/output.txt";

print("project4 execution starts")

try:
    validate_paths({base_content_path : 'dir',read_file_path : 'file'})
except ValueError as e:
    print(e)  
    sys.exit(1)

configs = loadConfigfile('./project1_to_4/config.properties');
regex_pattern=configs.get('regex').data
print('loaded property file : ' , regex_pattern)
reader = open_pdf(read_file_path)
f = openFile(write_file_path, "w")
matched_content = []
for page_number, page in enumerate(reader.pages, start=1):
    text = page.extract_text()
    matches = re.findall(regex_pattern, text)
    for match in matches:
        matched_content.append((match, page_number)) 
for match, page_number in matched_content:
    writeToFile(f,'Page ' + str(page_number) + ' ' +  match)


    













   


