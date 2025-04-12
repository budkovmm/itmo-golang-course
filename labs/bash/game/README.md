# Quiz game

## Overview
This is a simple quiz game that reads questions and answers from a specified file and allows users to answer them. The results are saved in a CSV format.

## Usage
To run the game, execute the following command in your terminal:

```bash
make run questions_file=<questions_file>
# or
./game.sh <questions_file>
```
Replace `<questions_file>` with the path to your questions file.

To clean all generated files, run:

```bash
make clean
```

## Questions File Format
The questions file should be in csv format, comma separated:

```
"Question","Correct Answer"
"Question 1","Correct Answer 1"
"Question 2","Correct Answer 2"
```