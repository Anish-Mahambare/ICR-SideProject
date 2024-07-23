
███████████████████████████████████████████████████
█▄─▄███▄─▄▄─██▀▄─██▄─▄▄▀█▄─▀█▄─▄█▄─▄███▄─▄▄─█─▄─▄─█
██─██▀██─▄█▀██─▀─███─▄─▄██─█▄▀─███─██▀██─▄█▀███─███
▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀

### Open Source version of a popular quiz  style learning website done while interning @ Institue of Computing in Research 

## Usage - Linux/Mac
### Cloning the project
```
git clone https://github.com/Anish-Mahambare/LearnLet.git
```
### Package installation
Install the following dependencies to get started
```
pip install flask
pip install csv
pip install random
```
### Creating your Learning Set
There are two ways to create your learning set that you will practice through learn let.
- Option 1
1. Go to your text editor and make a file InsertName.csv
2. Write your questions and anwsers in the following format
```
question,anwser
question,anwser
question,anwser
```
3. Save the csv file in the LearnLet/Programs/Datasets/ directory
- Option 2
1. Go to the set you wish to study on quizlet
2. Open up web console through inspect
3. Copy the JS script(QuizletTOcsv.js) from the Programs directory and run it in the web console
4. Copy the output and save it in your text editor
5. Save the file as InsertName.csv in the  ```LearnLet/Programs/Datasets/``` directory
### Running the application
1. Navigate into the programs directory and run the following: (switch InsertName with the set you want to study)
```
python3 LearnLet.py ./Datasets/InsertName.csv
```
2. Open the link that the terminal outputs and start studying!

## Usage - Windows
### Cloning the project
```
git clone https://github.com/Anish-Mahambare/LearnLet.git
```
### Package installation
Install the following dependencies to get started
```
!pip install flask
!pip install csv
!pip install random
```
### Creating your Learning Set
There are two ways to create your learning set that you will practice through learn let.
- Option 1
1. Go to your text editor and make a file InsertName.csv
2. Write your questions and anwsers in the following format
```
question,anwser
question,anwser
question,anwser
```
3. Save the csv file in the LearnLet/Programs/Datasets/ directory
- Option 2
1. Go to the set you wish to study on quizlet
2. Open up web console through inspect
3. Copy the JS script(QuizletTOcsv.js) from the Programs directory and run it in the web console
4. Copy the output and save it in your text editor
5. Save the file as InsertName.csv in the  ```LearnLet/Programs/Datasets/``` directory
### Running the application
1. Navigate into the programs directory and run the following: (switch InsertName with the set you want to study)
```
python LearnLet.py ./Datasets/InsertName.csv
```
2. Open the link that the terminal outputs and start studying!