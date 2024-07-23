from flask import Flask, render_template, request, session, jsonify
import csv
import random
import os
import sys

try:
    dataset = sys.argv[1]
except IndexError:
    print('You have not run the program correctly. Run it with a dataset from the Datasets folder.')
    print('The correct syntax for running the program is: python3 MatchingGame.py ./Datasets/FILE_NAME_HERE')
    print('CTRL-C to exit and try again\n ----------------------------')
    sys.exit(1)

app = Flask(__name__)
app.secret_key = os.urandom(24)

def load_pairs(filename):
    pairs = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 2:
                pairs.append({
                    'question': row[0],
                    'answer': row[1]
                })
    return pairs

@app.route('/')
def index():
    if 'pairs' not in session:
        session['pairs'] = load_pairs(dataset)
    return render_template('matching_game.html')

@app.route('/get_cards')
def get_cards():
    num_cards = 16  # Number of cards to display (must be even)
    pairs = random.sample(session['pairs'], num_cards // 2)
    cards = []
    for pair in pairs:
        cards.extend([
            {'id': len(cards), 'content': pair['question'], 'type': 'question'},
            {'id': len(cards) + 1, 'content': pair['answer'], 'type': 'answer'}
        ])
    random.shuffle(cards)
    return jsonify(cards)

@app.route('/check_match', methods=['POST'])
def check_match():
    data = request.json
    card1 = data['card1']
    card2 = data['card2']
    
    for pair in session['pairs']:
        if (card1['content'] == pair['question'] and card2['content'] == pair['answer']) or \
           (card2['content'] == pair['question'] and card1['content'] == pair['answer']):
            return jsonify({'match': True})
    
    return jsonify({'match': False})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
