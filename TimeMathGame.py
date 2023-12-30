import random
import time
import pyautogui

numberOfQuestions = 10
operators = ('+', '-', '*')
times = []

# Generate a random problem
def generateProblem():
    num1 = str(random.randint(2, 12))
    operator = random.choice(operators)
    num2 = str(random.randint(2, 12))
    problem = num1 + operator + num2
    # Turns the problem string into a python expression
    answer = eval(problem)
    return problem, answer

# Ask the questions
for i in range(numberOfQuestions):
    question, answer = generateProblem()
    guess = None
    startTime = time.time()
    # Keep on asking the question until you get it right
    while guess != str(answer):
        guess = pyautogui.prompt(f'#{i+1} What is {question}?')
        if guess == None:
            exit()
    endTime = time.time()
    times.append(endTime - startTime)

# Get the average amount of seconds taken for each question
j = 0
for i in times:
    j += i
averageTime = round(j / numberOfQuestions, 2)

pyautogui.alert(f'You took an average of {averageTime} seconds for each question')
