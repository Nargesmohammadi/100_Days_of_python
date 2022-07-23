from question_model import Question
from data import question_data

question_bank = []
for question in question_data:
    question_next = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_next, question_answer)
    question_bank.append(new_question)

print(question_bank[0].answer)
