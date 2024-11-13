from project1_to_4.pdf_reader import *
from project1_to_4 import file_utils
import os
import sys
import re
import io
"""
Project 5
    Store extracted questions in mysql
Requirements
    Update project   4 and add support for database
    Create a database to store the following
        Subject Name
        Question Text
        Answer options
        Chapter name
    Load a PDF containing questions
    Extract each question as per a regular expression
    Store each question in the database
Error Handling
    Take care of case where database is not available
    Take care of case where table is not available
    Take care of any error handling in DB operations

"""
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
print("Current working directory :  " + os.getcwd())
base_content_path = "content"
read_file_path = base_content_path + "/" + "Chemistry Questions.pdf"

try:
    file_utils.validate_paths({read_file_path : 'file'})
except ValueError as e:
    print(e)  
    sys.exit(1)
reader = open_pdf(read_file_path)
numberOfPages = no_pages_in_pdf(reader)


configs = file_utils.loadConfigfile('table-regex.properties');
chapter_pattern_str = configs.get('chapter_pattern').data
question_pattern_str = configs.get('question_pattern').data
options_pattern_str = configs.get('options_pattern').data
answer_pattern_str = configs.get('answer_pattern').data

print("Chapter Pattern:", chapter_pattern_str)
print("Question Pattern:", question_pattern_str)
print("Options Pattern:", options_pattern_str)
print("Answer Pattern:", answer_pattern_str)


chapter_pattern = re.compile(chapter_pattern_str)
question_pattern = re.compile(question_pattern_str)
options_pattern = re.compile(options_pattern_str)
answer_pattern = re.compile(answer_pattern_str)

text=""
for page in reader.pages:
    tmp = page.extract_text()
    #print(tmp)
    text += tmp

def clean_text(text):
    # Remove excessive newlines and join words
    return ' '.join(text.split())

def extract_content(text):
    # Clean the entire text
    text = clean_text(text)

    # Extract subject
    subject = text.split()[0]

    # Extract chapters and their content
    chapters = re.findall(r'(Chapter\s*\d+:\s*.+?)(?=Chapter|\Z)', text)

    result = {
        'subject': subject,
        'chapters': []
    }

    for chapter_content in chapters:
        # Extract chapter name and questions
        chapter_match = re.match(r'(Chapter\s*\d+:\s*.+?)\s*(1\..+)', chapter_content)
        if chapter_match:
            chapter_name = chapter_match.group(1)
            questions_text = chapter_match.group(2)

            # Extract questions and answers
            qa_pairs = re.findall(r'(\d+\..+?)\s*Answer:\s*(.+?)(?=\d+\.|\Z)', questions_text)

            chapter_data = {
                'name': chapter_name,
                'questions': []
            }

            for question_text, answer in qa_pairs:
                # Split question and options
                question_parts = re.split(r'([A-D]\))', question_text)
                question = question_parts[0].strip()
                options = [''.join(question_parts[i:i+2]).strip() for i in range(1, len(question_parts), 2)]

                chapter_data['questions'].append({
                    'question': question,
                    'options': options,
                    'answer': answer.strip()
                })

            result['chapters'].append(chapter_data)

    return result

# Extract the data
extracted_data = extract_content(text)

# Print the extracted data
print(f"Subject: {extracted_data['subject']}")
for chapter in extracted_data['chapters']:
    print(f"\nChapter: {chapter['name']}")
    for qa in chapter['questions']:
        print(f"\nQuestion: {qa['question']}")
        print("Options:")
        for option in qa['options']:
            print(f"  {option}")
        print(f"Answer: {qa['answer']}")
