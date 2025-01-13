from project5.db_operations import DatabaseOperations
from project8.question_input import get_question_from_console
from project8.file_reader import read_questions_from_file

def get_chapter_id(db, subject_name, chapter_name):
    subject_id = db.insert_subject(subject_name)
    return db.insert_chapter(subject_id, chapter_name)

def main():
    db = DatabaseOperations(
        host='sql.freedb.tech',
        user='freedb_python-practice',
        password='uCa*ca6jaJD&xW5',
        database='freedb_python-practice',
        port=3306
    )
    
    db.connect()

    # Ensure all necessary tables exist
    if not db.table_exists('subjects'):
        db.create_table('subjects', ["subject_id INT AUTO_INCREMENT PRIMARY KEY", "subject_name VARCHAR(100) NOT NULL"])
    
    if not db.table_exists('chapters'):
        db.create_table('chapters', ["chapter_id INT AUTO_INCREMENT PRIMARY KEY", "subject_id INT", "chapter_name VARCHAR(100) NOT NULL", "FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)"])
    
    if not db.table_exists('questions'):
        db.create_table('questions', ["question_id INT AUTO_INCREMENT PRIMARY KEY", "chapter_id INT", "question_text TEXT NOT NULL", "correct_answer CHAR(1) NOT NULL", "FOREIGN KEY (chapter_id) REFERENCES chapters(chapter_id)"])
    
    if not db.table_exists('options'):
        db.create_table('options', ["option_id INT AUTO_INCREMENT PRIMARY KEY", "question_id INT", "option_letter CHAR(1) NOT NULL", "option_text TEXT NOT NULL", "FOREIGN KEY (question_id) REFERENCES questions(question_id)"])
    
    if not db.table_exists('subjective_questions'):
        db.create_table('subjective_questions', ["question_id INT AUTO_INCREMENT PRIMARY KEY", "chapter_id INT", "question_text TEXT NOT NULL", "answer TEXT NOT NULL", "FOREIGN KEY (chapter_id) REFERENCES chapters(chapter_id)"])

    input_method = input("Enter 'file' to read from file or 'console' for manual input: ")
    
    if input_method == 'file':
        file_path = input("Enter the file path: ")
        questions = read_questions_from_file(file_path)
    else:
        subject_name = input("Enter subject name: ")
        chapter_name = input("Enter chapter name: ")
        
        chapter_id = get_chapter_id(db, subject_name.strip(), chapter_name.strip())
        
        questions = []
        
        while True:
            question = get_question_from_console()
            if question:
                question.chapter_id = chapter_id
                questions.append(question)
            
            continue_input = input("Do you want to add another question? (y/n): ")
            if continue_input.lower() != 'y':
                break

    for question in questions:
        question.store(db)

    db.disconnect()
    print("Questions saved successfully!")

if __name__ == "__main__":
    main()
