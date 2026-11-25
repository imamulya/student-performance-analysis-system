# Student Performance Analysis System-

A Python-based project developed for the Computational Thinking and Programming course at Bennett University.

## Problem Statement

Students often have difficulty analyzing their academic performance across multiple subjects. Calculating overall marks and averages manually can be time-consuming, and it may be difficult to identify high-performing students or subjects where improvement is needed.

This project provides a simple Python-based solution for entering and analyzing student marks and generating useful performance information.

## Objectives

- Store marks of multiple students across different subjects.
- Calculate total and average marks for each student.
- Assign grades based on student performance.
- Identify high-performing and low-performing students and subjects.
- Generate a summary of overall class performance.

## Features

- Add student records through an HTML form.
- Enter and validate marks for six subjects.
- View all student records in a table.
- Calculate individual student averages and grades.
- Search for individual student records.
- Delete student records.
- Identify the highest and lowest performers.
- Calculate class and subject-wise averages.
- Save student records using CSV file storage.

## Technologies Used

- **Python** – Application logic and calculations.
- **Flask** – Backend web framework.
- **HTML5** – Webpage structure and forms.
- **CSS3** – Basic webpage styling.
- **CSV** – Student data storage.

## How to Run

### 1. Install Python

Make sure Python is installed on your computer.

### 2. Install Dependencies

Open a terminal in the project folder and run:

```bash
pip install -r requirements.txt
```

### 3. Start the Application

Run the following command:

```bash
python app.py
```

### 4. Open the Website

Open your browser and visit:

```text
http://127.0.0.1:5000
```

The application will now be running locally on your computer.

## Data Storage

Student records are stored in a CSV file named `student_data.csv`.

The application automatically saves records when students are added or deleted, allowing existing records to be loaded when the application is started again.
