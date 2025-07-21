from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for d in question_data:
    question_bank.append(Question(d['text'], d['answer']))

print(question_bank)
brain = QuizBrain(question_bank)
while brain.still_has_questions():
    brain.pop_question()

print("You've completed the quiz")
print(f"Your final score was: {brain.get_final_score()}")