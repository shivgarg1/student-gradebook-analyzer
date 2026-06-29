# Student Gradebook Analyzer

Project 2 for the AIML using Python workshop. Analyzes student scores across multiple assignments using Pandas and NumPy.

## What it does

- Loads student names and scores (4 assignments) from a CSV into a Pandas DataFrame
- Calculates average, median, max, and min for each student (row-wise)
- Calculates the same stats for each assignment across all students (column-wise)
- Sorts students by average score to find top performers and students who might need extra support
- Uses NumPy to calculate standard deviation (how spread out scores are) per assignment and overall
- Saves the final data with calculated stats to a new CSV

## Files

- `gradebook.csv` - the raw input data (10 students, 4 assignments, made up by me for this project)
- `gradebook_analyzer.py` - main script, run this directly in PyCharm
- `Student_Gradebook_Analyzer.ipynb` - notebook version with step by step explanations and outputs
- `sample_output.txt` - example of what the script prints when run, in case you want to see the output without running it
- `gradebook_with_stats.csv` - output file generated after running the script/notebook (includes the calculated Average/Median/Max/Min columns)
- `requirements.txt` - dependencies needed to run this

## How to run (PyCharm) - script version

1. Clone the repo and open the folder in PyCharm
2. Set up a virtual environment if you don't have one already: `python -m venv venv`, then activate it
3. Install dependencies: `pip install -r requirements.txt`
4. Right-click `gradebook_analyzer.py` → Run
5. `gradebook_with_stats.csv` will be generated in the same folder

## How to run - notebook version

1. Make sure `pandas`, `numpy` and `jupyter` are installed
2. Open `Student_Gradebook_Analyzer.ipynb` in Jupyter or in PyCharm's notebook viewer
3. Run all cells in order

## Notes / Limitations

- The dataset is dummy data I made up for this project, not real student records
- Only handles numeric scores, no missing value handling (every student has all 4 scores filled in)
- Assumes equal weight for every assignment, doesn't account for assignments being worth different amounts

## What I learned

Mainly got comfortable with `axis=0` vs `axis=1` in Pandas aggregations - row-wise stats need `axis=1` since the assignments are along the columns, while per-assignment stats use the default `axis=0`. Used `sort_values()` to rank students and `.agg()` to compute multiple stats in one line. Also actually used NumPy for something real this time - converting the score columns to a NumPy array with `.to_numpy()` and using `np.std()` to check how spread out the scores were on each assignment, instead of just importing numpy and not touching it.