#!/bin/bash

git_uri=("https://github.com/Roman77St" "https://github.com/budkovmm/course_go_2025" "https://github.com/AndreyASavin/course_go_2025" "https://github.com/Andzen71/course_go_2025" "https://github.com/MaximDiGoncharov/course_go_2025" "https://github.com/yuriycherepnev/course_go_2025i" "https://github.com/ViktorFree/course_go_2025" "https://github.com/ViacheslavILIN/course_go_2025.git" "https://github.com/SadovskiiAleks/course_go_2025" "tutori")
shuffled_array=( $(shuf -e "${git_uri[@]}") )

for ((i = 0; i < ${#shuffled_array[@]}; i += 2)); do
    echo "${shuffled_array[i]}"
    echo "${shuffled_array[i+1]}"
    echo
done