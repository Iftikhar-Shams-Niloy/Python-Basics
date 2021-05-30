class question :
    def __init__(self, given, ans):
        self.given = given
        self.ans = ans
print("\nLet's see how much you know about Niloy!\n")
question_prompts = [
    "1.What is the favourite color of Niloy?\n(a) Black\n(b) Red\n(c) Blue\n(d) Yellow\nAns:",
    "2.What kind of pet Niloy have?\n(a) Cat\n(b) Dog\n(c) Turtle\n(d) Birds\nAns:",
    "3.What is Niloy's favourite season?\n(a) Summer\n(b) Winter\n(c) Spring\n(d) Autumn\nAns:",
    "4.What is the zodiac sign of Niloy?\n(a) Libra\n(b) Sagittarius\n(c) Aries\n(d) Leo\nAns:",
    "5.What does Niloy love to dd the most when he is sad?\n(a) Listen Music\n(b) Working out\n(c) Drawing\n(d) Playing games\nAns:"
]
questions_given_answers =[
    question(question_prompts[0], "b"),
    question(question_prompts[1], "c"),
    question(question_prompts[2], "b"),
    question(question_prompts[3], "d"),
    question(question_prompts[4], "a")
]
def judge(QQuestions):
    score = 0
    for question in QQuestions:
        answer = input(question.given)
        if answer == question.ans:
            score = score+1
    print("\nYou got %d/5"%score)

judge(questions_given_answers)