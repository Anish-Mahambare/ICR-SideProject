import csv
import random

def load_questions(filename):
    questions = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 2:  # Ensure each row has exactly two columns
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

def print_question(question, choices):
    print(f"Question: {question}")
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")
    return choices.index(choices[0]) + 1

def main():
    filename = './Datasets/trivia_questions.csv'
    questions = load_questions(filename)
    
    while True:
        random.shuffle(questions)
        for question in questions:
            choices = generate_choices(questions, question['answer'])
            correct_choice_index = print_question(question['question'], choices)
            user_choice = None
            while user_choice not in ['1', '2', '3', '4']:
                user_choice = input("Enter your choice (1-4): ")
            user_choice = int(user_choice)
            if user_choice == correct_choice_index:
                print("Correct!")
            else:
                print(f"Wrong! The correct answer was: {correct_choice_index}. {question['answer']}")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
