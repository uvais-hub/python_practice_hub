from pypdf import PdfReader
from file_utils import *

"""
PDF Reader Utility Script

This script provides utility functions for reading PDF files using the PyPDF library.
It includes functionalities to open a PDF, check the number of pages, and extract text from a specific page.
"""

def open_pdf(pdf_path):
     return PdfReader(pdf_path);
def no_pages_in_pdf(reader):
     return len(reader.pages);
def read_page_in_pdf(reader, pageNo):
    return reader.pages[pageNo].extract_text();












   


