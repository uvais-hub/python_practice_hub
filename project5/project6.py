import sys
from project5.db_operations import DatabaseOperations

def load_chapter_questions(chapter_name):
    db = DatabaseOperations(
        host='sql.freedb.tech',
        user='freedb_python-practice',
        password='uCa*ca6jaJD&xW5',
        database='freedb_python-practice',
        port=3306
    )
    
    db.connect()
    
    query = """
    SELECT q.question_text, q.correct_answer, o.option_letter, o.option_text
    FROM chapters c
    JOIN questions q ON c.chapter_id = q.chapter_id
    JOIN options o ON q.question_id = o.question_id
    WHERE c.chapter_name = %s
    ORDER BY q.question_id, o.option_letter
    """
    
    results = db.execute_query(query, (chapter_name,))
    
    if not results:
        print(f"No questions found for chapter: {chapter_name}")
        return
    
    current_question = None
    for row in results:
        if current_question != row[0]:
            if current_question:
                print(f"Correct Answer: {current_answer}\n")
            current_question = row[0]
            current_answer = row[1]
            print(f"Question: {current_question}")
            print("Options:")
        print(f"  {row[2]}) {row[3]}")
    
    if current_question:
        print(f"Correct Answer: {current_answer}\n")
    
    db.disconnect()

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].strip():
        print("Usage: python script_name.py <chapter_name>")
        print("Error: Please provide a non-empty chapter name.")
        sys.exit(1)
    
    chapter_name = sys.argv[1].strip()
    load_chapter_questions(chapter_name)
