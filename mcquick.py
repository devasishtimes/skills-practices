class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    "What is the capital of France?\n(a) Paris\n(b) London\n(c) Berlin\n(d) Madrid\n\n",
    "What is the largest planet in our solar system?\n(a) Earth\n(b) Mars\n(c) Jupiter\n(d) Saturn\n\n",
    "What is the chemical symbol for gold?\n(a) Au\n(b) Ag\n(c) Fe\n(d) Hg\n\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower().strip() == question.answer:
            score += 1
    print(f"You got {score}/{len(questions)} correct.")


run_test(questions)