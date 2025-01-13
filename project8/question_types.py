from abc import ABC, abstractmethod

class Question(ABC):
    def __init__(self, question_text, chapter_id):
        self.question_text = question_text
        self.chapter_id = chapter_id

    @abstractmethod
    def store(self, db):
        pass

class ObjectiveTrueFalse(Question):
    def __init__(self, question_text, chapter_id, correct_answer):
        super().__init__(question_text, chapter_id)
        self.correct_answer = correct_answer

    def store(self, db):
        question_id = db.insert_question(self.chapter_id, self.question_text, self.correct_answer)
        db.insert_option(question_id, 'A', 'True')
        db.insert_option(question_id, 'B', 'False')

class ObjectiveMultipleChoice(Question):
    def __init__(self, question_text, chapter_id, options, correct_answer):
        super().__init__(question_text, chapter_id)
        self.options = options
        self.correct_answer = correct_answer

    def store(self, db):
        question_id = db.insert_question(self.chapter_id, self.question_text, self.correct_answer)
        for i, option in enumerate(self.options):
            db.insert_option(question_id, chr(65 + i), option)

class SubjectiveLongAnswer(Question):
    def __init__(self, question_text, chapter_id, answer):
        super().__init__(question_text, chapter_id)
        self.answer = answer

    def store(self, db):
        db.insert_subjective_question(self.chapter_id, self.question_text, self.answer)
