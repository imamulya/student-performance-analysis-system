import csv

SUBJECTS = ["CSAE100", "CSAE101", "MATH102", "EECE110", "ENVS151", "FSWD100"]
DATA_FILE = "student_data.csv"

students = []
marks = []


def save_data():
    """Save all student records to a CSV file."""
    with open(DATA_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name"] + SUBJECTS)
        for name, student_marks in zip(students, marks):
            writer.writerow([name] + student_marks)
    print(f"Data saved in {DATA_FILE}.")


def load_data():
    """Load student records from the CSV file when the program starts."""
    try:
        with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader, [])
            if header != ["Name"] + SUBJECTS:
                print("The saved file has an unexpected format.")
                return

            for row in reader:
                if len(row) == len(SUBJECTS) + 1:
                    try:
                        saved_marks = [float(value) for value in row[1:]]
                        if all(0 <= mark <= 100 for mark in saved_marks):
                            students.append(row[0])
                            marks.append(saved_marks)
                    except ValueError:
                        print("Skipped a row containing invalid marks.")

        print(f"Loaded {len(students)} student record(s).")
    except FileNotFoundError:
        print("No saved data yet. Enter student data to create the file.")


def get_valid_mark(subject):
    """Get a valid mark between 0 and 100."""
    while True:
        try:
            mark = float(input(f"Enter marks in {subject} (0-100): "))
            if 0 <= mark <= 100:
                return mark
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def add_students():
    """Input student names and marks."""
    while True:
        try:
            n = int(input("Enter number of students: "))
            if n > 0:
                break
            print("Enter at least 1 student.")
        except ValueError:
            print("Please enter a whole number.")

    for i in range(n):
        print(f"\nStudent {i + 1}")
        name = input("Enter student name: ").strip()

        while name == "" or len(name) > 50:
            if name == "":
                print("Name cannot be empty.")
        else:
                print("Name cannot exceed 50 characters.")

        name = input("Enter student name: ").strip()

        student_marks = []
        for subject in SUBJECTS:
            student_marks.append(get_valid_mark(subject))

        students.append(name)
        marks.append(student_marks)

    save_data()
    print("\nStudent data added successfully.")


def calculate_average(student_marks):
    """Return the average percentage for one student."""
    return sum(student_marks) / len(student_marks)


def get_grade(average):
    """Return the project grade based on the average."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"


def display_students():
    """Display all stored student marks."""
    if not students:
        print("\nNo student data available. Add students first.")
        return

    print("\n" + "=" * 75)
    print("STUDENT RECORDS")
    print("=" * 75)
    print(f"{'Name':<20}" + "".join(f"{subject:>12}" for subject in SUBJECTS))
    print("-" * (20 + 12 * len(SUBJECTS)))

    for name, student_marks in zip(students, marks):
        print(
            f"{name:<20}"
            + "".join(f"{mark:>12.1f}" for mark in student_marks)
        )


def display_individual_results():
    """Display average and grade for every student."""
    if not students:
        print("\nNo student data available. Add students first.")
        return

    print("\n" + "=" * 65)
    print("INDIVIDUAL PERFORMANCE")
    print("=" * 65)

    for name, student_marks in zip(students, marks):
        average = calculate_average(student_marks)
        grade = get_grade(average)
        print(f"{name:<20} Average: {average:>6.2f}%   Grade: {grade}")


def find_highest_lowest():
    """Find students with highest and lowest averages."""
    if not students:
        print("\nNo student data available. Add students first.")
        return

    averages = [calculate_average(student_marks) for student_marks in marks]
    highest_index = averages.index(max(averages))
    lowest_index = averages.index(min(averages))

    print("\n" + "=" * 55)
    print("PERFORMANCE RANGE")
    print("=" * 55)
    print(
        f"Highest Performer: {students[highest_index]} "
        f"({averages[highest_index]:.2f}%)"
    )
    print(
        f"Lowest Performer:  {students[lowest_index]} "
        f"({averages[lowest_index]:.2f}%)"
    )


def subject_averages():
    """Calculate and display the average for each subject."""
    if not students:
        print("\nNo student data available. Add students first.")
        return

    print("\n" + "=" * 55)
    print("SUBJECT ANALYSIS")
    print("=" * 55)

    subject_totals = [0] * len(SUBJECTS)

    for student_marks in marks:
        for i, mark in enumerate(student_marks):
            subject_totals[i] += mark

    for i, subject in enumerate(SUBJECTS):
        average = subject_totals[i] / len(students)
        status = "Needs improvement" if average < 40 else "Normal"
        print(f"{subject:<20} Average: {average:>6.2f}%   {status}")


def class_summary():
    """Display the overall class average and grade distribution."""
    if not students:
        print("\nNo student data available. Add students first.")
        return

    averages = [calculate_average(student_marks) for student_marks in marks]
    class_average = sum(averages) / len(averages)

    grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}
    for average in averages:
        grade_counts[get_grade(average)] += 1

    print("\n" + "=" * 55)
    print("CLASS SUMMARY")
    print("=" * 55)
    print(f"Number of students : {len(students)}")
    print(f"Class average      : {class_average:.2f}%")
    print("\nGrade distribution:")
    for grade in grade_counts:
        print(f"Grade {grade}: {grade_counts[grade]}")


def search_student():
    """Search for a student by name."""
    if not students:
        print("\nNo student data available. Add students first.")
        return

    query = input("Enter student name to search: ").strip().lower()
    found = False

    for i, name in enumerate(students):
        if name.lower() == query:
            average = calculate_average(marks[i])
            print("\nStudent found")
            print("-" * 35)
            print(f"Name: {name}")
            for subject, mark in zip(SUBJECTS, marks[i]):
                print(f"{subject}: {mark:.1f}")
            print(f"Average: {average:.2f}%")
            print(f"Grade: {get_grade(average)}")
            found = True
            break

    if not found:
        print("Student not found.")



def delete_student():
    """Delete one student's record after confirmation."""
    if not students:
        print("\nNo student records available to delete.")
        return

    name_to_delete = input("Enter the student name to delete: ").strip().lower()
    found_index = -1

    for i, name in enumerate(students):
        if name.lower() == name_to_delete:
            found_index = i
            break

    if found_index == -1:
        print("Student not found. No records were deleted.")
        return

    confirmation = input(
        f"Are you sure you want to delete {students[found_index]}? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":
        deleted_name = students.pop(found_index)
        marks.pop(found_index)
        save_data()
        print(f"{deleted_name}'s record deleted successfully.")
    else:
        print("Deletion cancelled.")


def delete_all_students():
    """Delete all student records after confirmation."""
    if not students:
        print("\nThere are no student records to delete.")
        return

    confirmation = input(
        "WARNING: This will delete ALL student records. Type yes to confirm: "
    ).strip().lower()

    if confirmation == "yes":
        students.clear()
        marks.clear()
        save_data()
        print("All student records deleted successfully.")
    else:
        print("Deletion cancelled.")


def show_menu():
    """Display the main menu."""
    print("\n" + "=" * 65)
    print("       STUDENT PERFORMANCE ANALYSIS SYSTEM")
    print("=" * 65)
    print("1. Enter student data")
    print("2. Display student records")
    print("3. Display individual averages and grades")
    print("4. Find highest and lowest performers")
    print("5. Display subject averages")
    print("6. Display class summary")
    print("7. Search for a student")
    print("8. Save data")
    print("9. Delete a student record")
    print("10. Delete all student records")
    print("11. Exit")


def main():
    """Load saved records and run the project menu."""
    load_data()
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_students()
        elif choice == "2":
            display_students()
        elif choice == "3":
            display_individual_results()
        elif choice == "4":
            find_highest_lowest()
        elif choice == "5":
            subject_averages()
        elif choice == "6":
            class_summary()
        elif choice == "7":
            search_student()
        elif choice == "8":
            save_data()
        elif choice == "9":
            delete_student()
        elif choice == "10":
            delete_all_students()
        elif choice == "11":
            save_data()
            print("Thank you for using the Student Performance Analysis System.")
            break
        else:
            print("Invalid choice. Please select 1-11.")


if __name__ == "__main__":
    main()
