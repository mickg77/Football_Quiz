# Object Oriented Quiz
# Simple True/False quiz based on facts

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []  # creates array

for question in question_data:  # for all the questions in the question data dictionary

    question_text = question["text"]  # assigns text to the question text variable
    question_answer = question["answer"]  # assigns answer to the question answer variable
    # creates a new_question from the Question class and passes in the text and answer
    new_question = Question(question_text, question_answer)
    # the new question is appended to the bank of questions
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)  # quiz is created by passing the entire question bank into it
while quiz.still_has_questions():
    print(f"You scored  {quiz.show_score()} out of {quiz.show_question()}")
    quiz.next_question()

