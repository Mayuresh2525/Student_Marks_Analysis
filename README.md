# Student Marks Analysis System

A Python-based application that reads student records from Excel files, performs statistical analysis using NumPy, and automatically generates a text report.

## Features

- Reads student records from Excel files.
- Stores student information using lists and dictionaries.
- Extracts marks into NumPy arrays.
- Calculates average and median marks.
- Finds maximum and minimum marks.
- Identifies students who passed.
- Generates an automated TXT report.

## Technologies Used

- Python
- NumPy
- Openpyxl
- File Handling

## Project Structure

```text
Student-Marks-Analysis/
├── main.py
├── calculation.py
├── requirements.txt
├── README.md
└── sample_data/
    └── students_600_records.xlsx
```

## Installation

Clone the repository:

```bash
git clone Student_Marks_Analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Excel File Format

The Excel file must contain two columns:

| Name | Marks |
|---|---|
| Rahul | 75 |
| Amit | 85 |
| Priya | 92 |

The first row should contain column headings.

## How to Run

```bash
python main.py
```

Enter the Excel file path when prompted.

The program analyses the records and generates `report.txt` in the same folder as the input Excel file.

## Learning Objectives

This project was developed to practise Python programming, NumPy operations, Excel file handling, functions, exception handling and automated report generation.
