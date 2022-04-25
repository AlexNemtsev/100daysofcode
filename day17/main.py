from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


def convert_question_data(question):
    return Question(question['text'], question['answer'])


question_bank = list(map(convert_question_data, question_data))
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(quiz.question_list)}")