"""
Student Gradebook Analyzer
Workshop project 2 - AIML using Python

Analyzes a class gradebook using Pandas. The dataset has 10 students and
their scores across 4 assignments. Calculates basic stats for each student
and each assignment, and figures out who the top performers are.
"""

import pandas as pd
import numpy as np

# 1. Loading the data
# I made a small CSV file with 10 students and 4 assignments (out of 100 each).
df = pd.read_csv("gradebook.csv")
print("=== Raw Gradebook ===")
print(df)
print()

# 2. Per-student statistics
# For each student, calculate average, median, max and min across their 4
# assignments. Since the assignment columns are side by side, axis=1 is
# used to calculate row-wise.
assignment_cols = ["Assignment_1", "Assignment_2", "Assignment_3", "Assignment_4"]

df["Average"] = df[assignment_cols].mean(axis=1)
df["Median"] = df[assignment_cols].median(axis=1)
df["Max_Score"] = df[assignment_cols].max(axis=1)
df["Min_Score"] = df[assignment_cols].min(axis=1)

print("=== Per-Student Stats ===")
print(df)
print()

# 3. Per-assignment statistics
# Now the other direction - for each assignment, what's the average/median/
# max/min across all students? Column-wise stats, so axis=0 (default) on
# just the assignment columns.
assignment_stats = df[assignment_cols].agg(["mean", "median", "max", "min"])
print("=== Per-Assignment Stats ===")
print(assignment_stats)
print()

# 4. Sorting students by average score
top_students = df.sort_values(by="Average", ascending=False)
print("=== Students Sorted by Average (High to Low) ===")
print(top_students[["Student_Name", "Average"]])
print()

# 5. Top 3 performers
top_3 = top_students.head(3)
print("=== Top 3 Performers ===")
print(top_3[["Student_Name", "Average"]])
print()

# 6. Who needs the most support?
# Sorting ascending to see who has the lowest average. Useful if a teacher
# wanted to know who might need extra help.
bottom_3 = df.sort_values(by="Average", ascending=True).head(3)
print("=== Bottom 3 (May Need Extra Support) ===")
print(bottom_3[["Student_Name", "Average"]])
print()

# 7. NumPy section
# Pulling the raw scores out as a NumPy array so I can use NumPy functions
# directly instead of going through Pandas for everything. Also using this
# to calculate standard deviation, which tells us how spread out the scores
# are for each assignment (Pandas can do this too, but I wanted an actual
# reason to use NumPy here instead of just importing it for no reason).
scores_array = df[assignment_cols].to_numpy()

class_average_np = np.mean(scores_array)
class_std_np = np.std(scores_array)
print(f"Overall class average (via NumPy): {class_average_np:.2f}")
print(f"Overall class standard deviation (via NumPy): {class_std_np:.2f}")
print()

# Standard deviation per assignment - higher std means scores were more
# spread out (some students did way better/worse than others on that one)
assignment_std = np.std(scores_array, axis=0)
print("=== Standard Deviation Per Assignment ===")
for col_name, std_val in zip(assignment_cols, assignment_std):
    print(f"{col_name}: {std_val:.2f}")
print()

# 8. Saving the results
# Saving the dataframe with the new stats columns to a new CSV.
df.to_csv("gradebook_with_stats.csv", index=False)
print("Saved to gradebook_with_stats.csv")

# Summary:
# - Ananya Gupta has the highest average (95.25), followed by Priya Mehta
#   (91.75) and Sneha Iyer (89.25)
# - Karan Singh has the lowest average (58.75) and might need extra support
# - Assignment_4 had the highest class average (80.2), Assignment_1 had the
#   lowest (77.0)
# - Overall class average across all assignments and students comes out to
#   be in the high 70s
# - Assignment_1 has the highest standard deviation, meaning scores were
#   more spread out on that one compared to the others
#
# This was a good way to practice basic Pandas operations like mean(),
# median(), row-wise vs column-wise aggregation with axis, and sorting
# with sort_values(). Also got to actually use NumPy for something real
# (std deviation) instead of just importing it and not touching it.