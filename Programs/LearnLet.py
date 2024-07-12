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
    choices = [correct_answer]  # Start with the correct answer
    
    # Select three other random answers from questions
    while len(choices) < 4:
        random_question = random.choice(questions)
        random_answer = random_question['answer']
        if random_answer != correct_answer and random_answer not in choices:
            choices.append(random_answer)
    
    # Shuffle the choices
    random.shuffle(choices)
    return choices

def print_question(question, choices):
    print(f"Question: {question}")
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")

def main():
    filename = './Datasets/trivia_questions.csv'
    questions = load_questions(filename)
    incorrect_answers = []
    
    while True:
        random.shuffle(questions)
        for index, question in enumerate(questions, start=1):
            correct_answer = question['answer']
            choices = generate_choices(questions, correct_answer)
            print_question(question['question'], choices)
            
            user_choice = None
            while user_choice not in ['1', '2', '3', '4']:
                user_choice = input("Enter your choice (1-4): ")
            user_choice = int(user_choice)
            
            if choices[user_choice - 1] == correct_answer:
                print("Correct!")
            else:
                print(f"Wrong! The correct answer was: {correct_answer}")
                incorrect_answers.append(question)  # Record the incorrect question
            
            if index % 10 == 0:
                # Every 10 questions, revisit incorrect answers
                if incorrect_answers:
                    input("You've completed 10 questions. Press Enter to revisit the questions you got wrong.")
                    for wrong_question in incorrect_answers:
                        correct_answer = wrong_question['answer']
                        choices = generate_choices(questions, correct_answer)
                        print_question(wrong_question['question'], choices)
                        
                        user_choice = None
                        while user_choice not in ['1', '2', '3', '4']:
                            user_choice = input("Enter your choice (1-4): ")
                            user_choice = int(user_choice)
                        
                            if choices[user_choice - 1] == correct_answer:
                                print("Correct!")
                            else:
                                print(f"Wrong! The correct answer was: {correct_answer}")
                        
                                input("Press Enter to continue...")
                                incorrect_answers = []  # Clear the list after revisiting
            
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
