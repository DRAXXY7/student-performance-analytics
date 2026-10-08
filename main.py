from functions import calculate_total
from functions import calculate_average
from functions import assign_grade
from functions import check_pass_fail

import pandas as pd
import numpy as np

# ---------------------------------------------------------
# Load data
# ---------------------------------------------------------
df = pd.read_csv("student.csv")

# ---------------------------------------------------------
# Per-student report (loop uses 'row', so 'df' is never overwritten)
# ---------------------------------------------------------
print("Student Report")
print("-" * 70)

for index, row in df.iterrows():
    total = calculate_total(
        row["Python"],
        row["Mathematics"],
        row["Statistics"]
    )
    average = calculate_average(total)
    grade = assign_grade(average)
    status = check_pass_fail(
        row["Python"],
        row["Mathematics"],
        row["Statistics"]
    )

    print(
        row["Name"],
        "| Total:", total,
        "| Average:", round(average, 2),
        "| Grade:", grade,
        "| Status:", status
    )

# ---------------------------------------------------------
# Add Total, Average, Grade and Status as columns
# ---------------------------------------------------------
subjects = ["Python", "Mathematics", "Statistics"]

df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df["Total"] / len(subjects)
df["Grade"] = df["Average"].apply(assign_grade)
df["Status"] = df.apply(
    lambda r: check_pass_fail(r["Python"], r["Mathematics"], r["Statistics"]),
    axis=1
)

# ---------------------------------------------------------
# Dataset overview
# ---------------------------------------------------------
print("\nFirst 5 Students:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

# ---------------------------------------------------------
# Selected columns
# ---------------------------------------------------------
print("\nResults Table:")
print(df[["Student_ID", "Name", "Department", "Total", "Average", "Grade", "Status"]])

# ---------------------------------------------------------
# Save results
# ---------------------------------------------------------
df.to_csv("student_results.csv", index=False)
print("\nResults saved to student_results.csv")

# ---------------------------------------------------------
# Performance Analysis
# ---------------------------------------------------------

# Highest-performing student
top_student = df.loc[df["Average"].idxmax()]

print("\nTop Performing Student:")
print("Name:", top_student["Name"])
print("Average:", round(top_student["Average"], 2))
print("Grade:", top_student["Grade"])


# Lowest-performing student
lowest_student = df.loc[df["Average"].idxmin()]

print("\nLowest Performing Student:")
print("Name:", lowest_student["Name"])
print("Average:", round(lowest_student["Average"], 2))
print("Grade:", lowest_student["Grade"])


# Overall class average
class_average = df["Average"].mean()

print("\nOverall Class Average:", round(class_average, 2))


# Subject averages
subject_averages = df[subjects].mean()

print("\nSubject Averages:")
print(subject_averages.round(2))


# Best-performing subject
best_subject = subject_averages.idxmax()
best_subject_average = subject_averages.max()

print("\nBest Performing Subject:")
print("Subject:", best_subject)
print("Average:", round(best_subject_average, 2))


# Pass/Fail statistics
pass_count = (df["Status"] == "Pass").sum()
fail_count = (df["Status"] == "Fail").sum()

print("\nPass/Fail Statistics:")
print("Passed:", pass_count)
print("Failed:", fail_count)


# Top 5 students
top_students = df.sort_values(
    by="Average",
    ascending=False
).head(5)

print("\nTop 5 Students:")
print(
    top_students[
        ["Student_ID", "Name", "Department", "Average", "Grade"]
    ]
)
# ---------------------------------------------------------
# NumPy Analysis
# ---------------------------------------------------------

python_marks = np.array(df["Python"])
mathematics_marks = np.array(df["Mathematics"])
statistics_marks = np.array(df["Statistics"])

# Subject averages
python_avg_numpy = np.mean(python_marks)
mathematics_avg_numpy = np.mean(mathematics_marks)
statistics_avg_numpy = np.mean(statistics_marks)

print("\nSubject Averages:")
print("Python:", round(python_avg_numpy, 2))
print("Mathematics:", round(mathematics_avg_numpy, 2))
print("Statistics:", round(statistics_avg_numpy, 2))

# Overall class average
overall_average_numpy = np.mean(df["Average"])

print(
    "\nOverall Class Average:",
    round(overall_average_numpy, 2)
)

# Highest and lowest marks
print("\nHighest and Lowest Marks:")

print(
    "Python - Highest:", np.max(python_marks),
    "| Lowest:", np.min(python_marks)
)

print(
    "Mathematics - Highest:", np.max(mathematics_marks),
    "| Lowest:", np.min(mathematics_marks)
)

print(
    "Statistics - Highest:", np.max(statistics_marks),
    "| Lowest:", np.min(statistics_marks)
)

# Standard deviation
python_std = np.std(python_marks)

print(
    "\nPython Marks Standard Deviation:",
    round(python_std, 2)
)
# ---------------------------------------------------------
# Final Performance Report
# ---------------------------------------------------------

# ---------------------------------------------------------
# Attendance Analysis
# ---------------------------------------------------------

average_attendance = df["Attendance"].mean()
highest_attendance = df["Attendance"].max()
lowest_attendance = df["Attendance"].min()

print("\nAttendance Analysis:")
print("Average Attendance:", round(average_attendance, 2), "%")
print("Highest Attendance:", highest_attendance, "%")
print("Lowest Attendance:", lowest_attendance, "%")


# ---------------------------------------------------------
# Pass/Fail Percentage
# ---------------------------------------------------------

total_students = len(df)

pass_percentage = (pass_count / total_students) * 100
fail_percentage = (fail_count / total_students) * 100

print("\nPass/Fail Percentage:")
print("Pass Percentage:", round(pass_percentage, 2), "%")
print("Fail Percentage:", round(fail_percentage, 2), "%")


# ---------------------------------------------------------
# Top 5 Students
# ---------------------------------------------------------

top_students = df.sort_values(
    by="Average",
    ascending=False
).head(5)

print("\n" + "=" * 70)
print("                    TOP 5 STUDENTS")
print("=" * 70)

print(
    top_students[
        ["Student_ID", "Name", "Department", "Average", "Grade"]
    ].to_string(index=False)
)

print("=" * 70)


# ---------------------------------------------------------
# Final Performance Summary
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("        STUDENT PERFORMANCE ANALYTICS SUMMARY")
print("=" * 70)

print("Total Students:", total_students)
print("Overall Class Average:", round(class_average, 2))
print("Best Subject:", best_subject)
print("Best Subject Average:", round(best_subject_average, 2))
print("Students Passed:", pass_count)
print("Students Failed:", fail_count)
print("Pass Percentage:", round(pass_percentage, 2), "%")
print("Fail Percentage:", round(fail_percentage, 2), "%")
print("Average Attendance:", round(average_attendance, 2), "%")

print("=" * 70)