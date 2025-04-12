#!/bin/bash

# Define colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

output_dir="./out"
questions_file="$1"

# Check output folder and create it if not exists
if [ ! -d "$output_dir" ]; then
    mkdir "$output_dir"
fi

# Check that required argument is passed
if [ -z "$questions_file" ]; then
    echo -e "${RED}Error: you do not pass file with questions${NC}"
    echo -e "Usage: $0 <questions_file>${NC}"
    exit 1
fi

# Check that file with questions exists
if [ ! -f "$questions_file" ]; then
    echo "Questions file ($questions_file) not found!"
    exit 1
fi

# Read username
echo -en "${CYAN}Enter your name: ${NC}"
read username
clear

# Create results file
results_file="$output_dir/results_${username}_$(date +"%Y%m%d%H%M").csv"

# Define line counter
line_number=0

# Reading questions file line by line, checking that questions and correct answers are not empty and writing result to the file
while IFS="/n" read -r line
do  
    if [ $line_number -eq 0 ]; then
        # Write title to the file
        echo '"Question","User answer","Correct answer"' >> "$results_file"
        ((line_number++))
        continue
    fi
    
    # Parse question and answer from the line
    question=$(echo "$line" | awk -F'",' '{print $1}' | sed 's/^"//;s/"$//')
    answer=$(echo "$line" | awk -F'",' '{print $2}' | sed 's/^"//;s/"$//')

    if [ -z "$question" ]; then
        echo -e "${RED}Invalid line, question shouldn't be empty.${NC}"
        continue
    elif [ -z "$answer" ]; then
        echo -e "${RED}Invalid line, correct answer shouldn't be empty.${NC}"
        continue
    else
        # Asking a question
        echo -e "${YELLOW}$line_number question: $question${NC}"
        echo -en "${CYAN}Enter your answer: ${NC}"
        read user_answer < /dev/tty
        echo $user_answer

        # Write result to the results file
        echo "\"$question\",\"$user_answer\",\"$answer\"" >> "$results_file"
        clear
    fi

    ((line_number++))
    
done < "$questions_file"

# Write the results summary
echo -e "${GREEN}You answered $((line_number - 1)) questions.${NC}"
echo -e "${GREEN}Results have been saved to the $results_file.${NC}"