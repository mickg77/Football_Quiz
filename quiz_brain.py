class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer= input(f"Q.{self.question_number}: {current_question.text}(True/False)")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return(self.question_number < len(self.question_list))

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower()==correct_answer.lower():
            print("Well done")
            self.score += 1
        else:
            print("Wrong")
        print(f"The correct answer is {correct_answer}")

    def show_score(self):
        return self.score

    def show_question(self):
        return self.question_number




