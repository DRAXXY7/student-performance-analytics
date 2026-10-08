# Student Performance Analytics System

## 1. Project Title

**Student Performance Analytics System**

A Python-based system for analyzing student academic performance using **Python, NumPy, and Pandas**.

---

## 2. Project Objective

The objective of this project is to develop a Python-based Student Performance Analytics System that can process student academic data and generate useful performance insights.

The system calculates student totals and averages, assigns grades, determines Pass/Fail status, performs subject-wise analysis, identifies top-performing students, and analyzes attendance.

---

## 3. Technologies Used

* Python
* NumPy
* Pandas
* CSV Dataset

---

## 4. Dataset Description

The project uses a CSV dataset containing **20 student records**.

The dataset contains the following columns:

| Column      | Description                          |
| ----------- | ------------------------------------ |
| Student_ID  | Unique student identification number |
| Name        | Student name                         |
| Department  | Student department                   |
| Python      | Python subject marks                 |
| Mathematics | Mathematics subject marks            |
| Statistics  | Statistics subject marks             |
| Attendance  | Student attendance percentage        |

---

## 5. Project Structure

```text
student-performance-analytics/
│
├── main.py
├── functions.py
├── student.csv
├── student_results.csv
└── README.md
```

### File Description

**main.py**
Contains the main program, data loading, calculations, analysis, and final report.

**functions.py**
Contains reusable functions for calculating total marks, average marks, grades, and Pass/Fail status.

**student.csv**
Contains the original student dataset.

**student_results.csv**
Contains the processed student data with calculated Total, Average, Grade, and Status columns.

**README.md**
Contains project documentation.

---

## 6. Main Features

The system provides the following features:

1. Loads student data using Pandas.
2. Displays the first five student records.
3. Calculates total marks for each student.
4. Calculates average marks.
5. Assigns grades based on average marks.
6. Determines Pass/Fail status.
7. Finds the highest-performing student.
8. Finds the lowest-performing student.
9. Calculates the overall class average.
10. Calculates subject-wise averages.
11. Identifies the best-performing subject.
12. Calculates Pass/Fail statistics.
13. Displays the Top 5 students.
14. Performs attendance analysis.
15. Performs numerical calculations using NumPy.
16. Saves the processed results to a CSV file.

---

## 7. Grade System

The project uses the following grading system:

| Average Marks | Grade |
| ------------: | :---- |
|  90 and above | A+    |
|      80–89.99 | A     |
|      70–79.99 | B     |
|      60–69.99 | C     |
|      50–59.99 | D     |
|      Below 50 | F     |

### Pass Condition

A student is considered **Pass** when the student scores at least **40 marks in every subject**.

---

## 8. Implementation

### Pandas

Pandas is used for:

* Reading the CSV dataset
* Creating and working with the DataFrame
* Selecting columns
* Calculating results
* Sorting students
* Performing data analysis
* Saving the final results

### NumPy

NumPy is used for numerical calculations such as:

* Mean
* Maximum
* Minimum
* Standard deviation

### Functions

Reusable functions are created for:

* Total marks calculation
* Average calculation
* Grade assignment
* Pass/Fail checking

### Loops

A loop is used to process each student record and generate an individual student performance report.

---

## 9. Analysis Performed

The system performs the following analysis:

### Student Performance

* Total marks
* Average marks
* Grade
* Pass/Fail status

### Class Performance

* Overall class average
* Highest-performing student
* Lowest-performing student

### Subject Performance

* Python average
* Mathematics average
* Statistics average
* Best-performing subject
* Highest and lowest marks

### Attendance

* Average attendance
* Highest attendance
* Lowest attendance

### Top Performers

The system sorts students according to their average marks and displays the **Top 5 students**.

---

## 10. Output

The program generates:

* Individual student performance reports
* Dataset information
* Statistical summary
* Subject-wise performance
* Pass/Fail statistics
* Attendance analysis
* Top 5 students
* Final performance summary

The processed results are also saved in:

```text
student_results.csv
```

---

## 11. Learning Outcomes

Through this project, the following concepts were practiced:

* Python variables and data types
* Conditional statements
* Loops
* Functions
* Pandas DataFrames
* Reading and writing CSV files
* Data analysis
* NumPy numerical calculations
* Sorting and filtering data
* Basic project organization

---

## 12. Challenges and Learning

One of the main challenges was organizing the project into reusable functions and integrating Python, Pandas, and NumPy into a single working system.

The project helped in understanding how Python programming concepts can be applied to a practical data analysis problem.

---

## 13. Final Outcome

The Student Performance Analytics System successfully processes student academic data and generates meaningful performance information.

The system can identify individual performance, analyze class and subject performance, determine Pass/Fail statistics, analyze attendance, and identify the top-performing students.

---

## 14. GitHub Repository

GitHub Repository:

**[Add your GitHub repository link here]**

---

## 15. Project Status

**Completed**
