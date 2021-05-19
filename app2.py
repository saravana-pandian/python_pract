from ques import ques


ques_prompt = [
    "What color are apples?\n(a) Red\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are straberry?\n(a) Yellow\n(b) Red\n(c)Blue\n\n"
]
questions = [
    ques(ques_prompt[0], "a"),
    ques(ques_prompt[1], "c"),
    ques(ques_prompt[2], "b"),
]

def runtest(ques):
    score = 0
    for ques in questions:
        answer = input(ques.prompt)
        if answer == ques.answer:
            score += 1
    print("you got" + str(score) + "/" + str(len(questions)) + "correct")
runtest(questions)