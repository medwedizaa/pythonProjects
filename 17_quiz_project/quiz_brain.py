class QuizBrain():
    def __init__(self, list):
        self.question_number = 0
        self.score = 0
        self.question_list = list

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def pop_question(self):
        current_question = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False)?: ")
        self.question_number += 1
        self.check_answer(answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print(f"That's wrong. The right answer is {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("*" * 40)
        print()

    def get_final_score(self):
        return f"{self.score}/{self.question_number}"


