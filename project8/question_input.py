from project8.question_types import ObjectiveTrueFalse, ObjectiveMultipleChoice, SubjectiveLongAnswer

def get_question_from_console():
    question_text = input("Enter the question text: ")
    question_type = input("Enter question type (1 for True/False, 2 for Multiple Choice, 3 for Subjective): ")
    
    if question_type == '1':
        correct_answer = input("Enter correct answer (True/False): ")
        return ObjectiveTrueFalse(question_text, None, correct_answer)
    elif question_type == '2':
        options = []
        for i in range(4):
            option = input(f"Enter option {chr(65 + i)}: ")
            options.append(option)
        correct_answer = input("Enter correct answer (A/B/C/D): ")
        return ObjectiveMultipleChoice(question_text, None, options, correct_answer)
    elif question_type == '3':
        answer = input("Enter the answer: ")
        return SubjectiveLongAnswer(question_text, None, answer)
    else:
        print("Invalid question type")
        return None