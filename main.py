
import numpy as np
import openpyxl
from pathlib import Path
from calculation import cal_avg, med, maximum, minimum, passed_std

students=[]
std_marks=[]

file_path = input("Enter Excel file path: ")

try:
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        # data=line.strip().split(",")

        name=row[0]
        marks=float(row[1])

        students.append({"name": name, "marks":marks})

        std_marks.append(marks)

except FileNotFoundError:
    print("File not found")
    exit()

std_marks=np.array(std_marks)

average_mks=cal_avg(std_marks)
median_mks=med(std_marks)
max_mks=maximum(std_marks)
min_mks=minimum(std_marks)
passed_students=passed_std(students)

print("----- Student Analysis System -----")
print("\nAverage Marks: ", average_mks)
print("\nMedian: ", median_mks)
print("\nMaximum Marks: ", max_mks)
print("\nMinimum Marks: ", min_mks)
print("\nPassed Students (marks > 40): \n")

for std in passed_students:
    print(f'{std["name"]} | {std["marks"]}')

# Save report in the same folder as Excel file
report_path = Path(file_path).parent / "report.txt"

try:
    with open(report_path, "w") as report:
        report.write("----- Student Analysis Report -----\n")
        report.write(f"\nAverage Marks: {str(average_mks)} \n")
        report.write(f"\nMedian: {str(median_mks)}\n")
        report.write(f"\nMaximum Marks: {str(max_mks)}\n")
        report.write(f"\nMinimum Marks: {str(min_mks)}\n")
        report.write(f"\nPassed Students (marks > 40): \n")

        for std in passed_students:
            report.write(f'{std["name"]} | {str(std["marks"])} \n')

    print("\nReport generated successfully!")
    print("Report location:", report_path)

except OSError:
    print("Unable to create report")
