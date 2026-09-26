# Automated Multi-Format Report Generator

A zero-dependency Python automation project that reads messy startup registration data, cleans and structures the records, and generates a formatted JSON report.

## Project Overview

This project demonstrates how raw and inconsistent text data can be processed using pure Python.

The program:

- Reads raw startup registration data from a `.txt` file
- Removes unnecessary spaces and blank lines
- Splits comma-separated records
- Standardizes text using Python string methods
- Converts records into structured dictionaries
- Generates a formatted JSON report
- Creates a summary of the processed dataset
- Handles missing files and unexpected errors safely

## Project Structure

'''text
automated-report-generator/
│
├── main.py
├── raw_data.txt
├── report.json
└── README.md
'''

## Technologies Used

- Python 3
- JSON
- File Handling
- String Methods
- Lists
- Dictionaries
- Sets
- Exception Handling

No external Python libraries are required.

## How It Works

## How It Works

```text
Raw TXT File
     ↓
Read File
     ↓
Remove Blank Lines
     ↓
Split Records
     ↓
Clean Individual Fields
     ↓
Standardize Text
     ↓
Create Dictionaries
     ↓
Generate Summary
     ↓
Create report.json
```

## How to Run

Make sure Python 3 is installed.

Run the following command:
python main.py

After successful execution, the program generates:
report.json

## Report Output

The generated report contains:

- Total number of startups
- Number of unique cities
- Number of unique industries
- Structured startup records

-Example 

```json
{
    "report_summary": {
        "total_startups": 8,
        "unique_cities": 7,
        "unique_industries": 8
    },
    "startups": [
        {
            "id": "ST001",
            "company": "Novabyte Technologies",
            "industry": "ai & machine learning",
            "city": "Lucknow"
        }
    ]
}
```

## Internship Challenge

This project was developed as part of a Python Programming Internship Week 1 challenge focused on:

File handling
Data cleaning
String sanitization
Dictionary-based data structuring
JSON serialization
Defensive programming

## Author

Mohammad Amaan

B.Tech CSE — Data Science & AI  