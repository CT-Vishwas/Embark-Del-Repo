#!/usr/bin/env python3
# Script for Data aggregation using dictionary comprehension

students_info = [
    {"name": "vishwas", "scores":{"math":90, "science":94, "history":80}},
    {"name": "John", "scores":{"math":70, "science":98, "history":56}},
    {"name": "Jane", "scores":{"math":67, "science":100, "history":73}}
]

# Usual Approach
average_scores_loop = {}
for student in students_info:
    name = student["name"]
    scores = student["scores"].values()
    average_score = sum(scores) / len(scores)
    average_scores_loop[name] = average_score

print("Average Score: ", average_scores_loop)

average_scores_comp = {
    student["name"]: sum(student["scores"].values()) / len(student["scores"])
    for student in students_info
}

print("Average Score: ", average_scores_comp)