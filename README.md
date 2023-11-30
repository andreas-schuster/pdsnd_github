_This project was created in November 2023 (2023-11-09)_

# Bikeshare Database 

## Information / Description
This project was part of the Udacity Nanodegree "Programming for Data Science with Python".
One Task was to make use of Python to explore data related to bike share systems for three major cities in the United States:

- Chicago
- New York City and 
- Washington

Target was writing code to import some sample data and answer interesting questions about it by computing descriptive statistics. 
Focus was also on writing a script that takes in raw inputs to create an interactive experience in the terminal to present these statistics.

## Installation
The main code is provided in the `bikeshare.py`-file.
The data (CSV-Files) from the available cities (mentioned in the Information section) is not part of the online Repository (github).
CSV-Files need to be placed in a subfolder called "cities", relative to the `*.py`-file OR code needs to be adapted:

Please ensure that path is correctly maintained in the very beginning of the `bikeshare.py`-file so that it can grab the files from there.

```
CITY_DATA = {'chicago': './cities/chicago.csv',
             'new york city': './cities/new_york_city.csv',
             'washington': './cities/washington.csv'}
```

Reason for the decision was the following:
I wanted to have code-file and the data-files separated from each other so that coding area looks more clean and is separated from data area.

Please ensure that pandas is installed in your environment -> if it's not yet installed, install it via terminal (there are many instructions out there :-))

## Usage
Program can be run from the terminal by typing `python .\bikeshare.py`

## Files used
- bikeshare.py (the main code-file)
- README.md (this documentation)

## Comments
...are happily welcome - feel free to leave feedback in the appropriate area - thanks