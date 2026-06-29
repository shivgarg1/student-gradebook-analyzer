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

# 7. Class average across all assignments
class_average = df[assignment_cols].values.mean()
print(f"Overall class average across all assignments: {class_average:.2f}")
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
#
# This was a good way to practice basic Pandas operations like mean(),
# median(), row-wise vs column-wise aggregation with axis, and sorting
# with sort_values().
