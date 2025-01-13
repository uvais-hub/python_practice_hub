import re
from project8.question_types import ObjectiveTrueFalse, ObjectiveMultipleChoice, SubjectiveLongAnswer

def read_questions_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    questions = []
    question_blocks = re.split(r'\n(?=Q\d+)', content)
    
    for block in question_blocks:
        lines = block.strip().split('\n')
        question_text = lines[0].split('-', 1)[1].strip()
        
        if len(lines) == 3 and lines[1] == 'True' and lines[2] == 'False':
            questions.append(ObjectiveTrueFalse(question_text, None, lines[1]))
        elif len(lines) > 3:
            options = lines[1:-1]
            correct_answer = lines[-1]
            questions.append(ObjectiveMultipleChoice(question_text, None, options, correct_answer))
        else:
            answer = '\n'.join(lines[1:])
            questions.append(SubjectiveLongAnswer(question_text, None, answer))
    
    return questions
