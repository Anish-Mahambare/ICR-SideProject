from flask import Flask, render_template, request, session
import csv
import random
import os
import sys

try:
    dataset = sys.argv[1]
except:
    print('YOU have not ran the program correclty, run it with a dataset from the Datasets folder\n the correct syntax for running the program is: python3 LearnLet.py ./Datasets/FILE NAME HERE\nCTRL-C to exit and try again\n ----------------------------')
    
app = Flask(__name__)
app.secret_key = os.urandom(24)

def load_questions(filename):
    questions = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 2:
                questions.append({
                    'question': row[0],
                    'answer': row[1]
                })
    return questions

def generate_choices(questions, correct_answer):
    choices = [correct_answer]
    while len(choices) < 4:
        random_question = random.choice(questions)
        random_answer = random_question['answer']
        if random_answer != correct_answer and random_answer not in choices:
            choices.append(random_answer)
    random.shuffle(choices)
    return choices

@app.route('/', methods=['GET', 'POST'])
def quiz():
    if 'questions' not in session:
        session['questions'] = load_questions(dataset)
        session['current_question'] = 0
        session['incorrect_answers'] = []
        session['total_questions'] = 0

    if request.method == 'POST':
        user_choice = request.form.get('choice', False)
        correct_answer = session['current_choices'][int(user_choice)]
        if correct_answer == session['questions'][session['current_question']]['answer']:
            result = "Correct!"
        else:
            result = f"Wrong! The correct answer was: {session['questions'][session['current_question']]['answer']}"
            session['incorrect_answers'].append(session['questions'][session['current_question']])

        session['current_question'] += 1
        session['total_questions'] += 1

        if session['total_questions'] % 10 == 0 and session['incorrect_answers']:
            return render_template('review.html', questions=session['incorrect_answers'])

        if session['current_question'] >= len(session['questions']):
            session['current_question'] = 0
            random.shuffle(session['questions'])

        session.modified = True
        return render_template('result.html', result=result)

    question = session['questions'][session['current_question']]
    choices = generate_choices(session['questions'], question['answer'])
    session['current_choices'] = choices
    return render_template('quiz.html', question=question['question'], choices=choices)

@app.route('/review', methods=['POST'])
def review():
    print('1')
    session['incorrect_answers'] = []
    print('2')
    session.modified = True
    print('3')
    return quiz() 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
