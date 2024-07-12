
███████████████████████████████████████████████████
█▄─▄███▄─▄▄─██▀▄─██▄─▄▄▀█▄─▀█▄─▄█▄─▄███▄─▄▄─█─▄─▄─█
██─██▀██─▄█▀██─▀─███─▄─▄██─█▄▀─███─██▀██─▄█▀███─███
▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀

### Open Source version of a popular flashcard style learning website done while interning @ Institue of Computing in Research 

- Update: July 12 *As of now, the app only has a Learn Mode(it currenlty errors out in the review function)*
## Usage 
**FOLLOWING DIRECTIONS ASSUME YOU USING LINUX OPERATING SYSTEM** (Windows and MacOS directions will be publised later)
### Package installation

## Independent File READMEs

### LearnLet.py
Will contain the code for the main app
- for now it has the learn function which will later be put in a class or a seperate file for organaztion
### QuizletTOcsv.js
A js script that downloads quizlet sets in csv format to be used in LearnLet
- Directions
  1) copy the script by running `cat QuizletTOcsv.js` in the programs directory and then copy it by selecting the text and running `CTRL-SHIFT-C`
  2) go to the quizlet set you desire, go to its home page. Then open up the web console(right click, inspect, web console tab), and paste the script
  3) once downloaded copy the file from downloads by running (in the programs directory of the repo) `cp ~/Downloads/terms.csv ./Datasets/NAMEyourSEThere.csv | rm ~/Downloads/terms.csv`
