# Student Gradebook Analyzer

Project 2 for the AIML using Python workshop. Analyzes student scores across multiple assignments using Pandas.

## What it does

- Loads student names and scores (4 assignments) from a CSV into a Pandas DataFrame
- Calculates average, median, max, and min for each student (row-wise)
- Calculates the same stats for each assignment across all students (column-wise)
- Sorts students by average score to find top performers and students who might need extra support
- Saves the final data with calculated stats to a new CSV

## Files

- `gradebook.csv` - the raw input data (10 students, 4 assignments)
- `gradebook_analyzer.py` - main script, run this directly in PyCharm
- `gradebook_with_stats.csv` - output file generated after running the script (includes the calculated Average/Median/Max/Min columns)

## How to run (PyCharm)

1. Clone the repo and open the folder in PyCharm
2. Set up a virtual environment if you don't have one already: `python -m venv venv`, then activate it
3. Install dependencies: `pip install -r requirements.txt`
4. Right-click `gradebook_analyzer.py` → Run
5. `gradebook_with_stats.csv` will be generated in the same folder

## Notes / Limitations

- The dataset is dummy data I made up for this project, not real student records
- Only handles numeric scores, no missing value handling (every student has all 4 scores filled in)
- Assumes equal weight for every assignment, doesn't account for assignments being worth different amounts

## What I learned

Mainly got comfortable with `axis=0` vs `axis=1` in Pandas aggregations - row-wise stats need `axis=1` since the assignments are along the columns, while per-assignment stats use the default `axis=0`. Also used `sort_values()` to rank students and `.agg()` to compute multiple stats in one line instead of calling `.mean()`, `.median()` etc separately.