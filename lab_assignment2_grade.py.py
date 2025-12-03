"""
gradebook.py - GradeBook Analyzer

Implements a simple CLI program to input student names and marks (manually or via CSV),
compute statistics, assign grades, and display results.


Project: Grade Book Analyzer

Name: Rudra Singh
Roll No: 2501730339
Section: C
Date: 20/11/2025

"""
def calculate_mean(scores):
    """Return the mean (average) of a list of scores."""
    if not scores:
        return 0
    return sum(scores) / len(scores)

def calculate_median(scores):
    """Return the median of a list of scores."""
    n = len(scores)
    if n == 0:
        return 0
    sorted_scores = sorted(scores)
    mid = n // 2
    if n % 2 == 0:
        # even number of scores
        return (sorted_scores[mid - 1] + sorted_scores[mid]) / 2
    else:
        # odd number of scores
        return sorted_scores[mid]

def find_max(scores):
    """Return the maximum score from the list."""
    if not scores:
        return None
    max_score = scores[0]
    for s in scores:
        if s > max_score:
            max_score = s
    return max_score

def find_min(scores):
    """Return the minimum score from the list."""
    if not scores:
        return None
    min_score = scores[0]
    for s in scores:
        if s < min_score:
            min_score = s
    return min_score

def assign_grade(score):
    """
    Assign a grade (A-F) based on the score:
    A: 90-100, B: 80-89, C: 70-79, D: 60-69, E: 40-59, F: <40
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    elif score >= 40:
        return 'E'
    else:
        return 'F'

def read_manual_input():
    """
    Read student names and marks manually from user input.
    Returns a dictionary {name: mark}.
    """
    print("Enter student data. Type 'done' to finish.")
    data = {}
    while True:
        name = input("Student Name (or 'done'): ")
        if name.lower() == 'done':
            break
        mark_str = input("Marks (0-100, or 'done'): ")
        if mark_str.lower() == 'done':
            break
        try:
            mark = float(mark_str)
        except ValueError:
            print("Invalid mark. Please enter a number.")
            continue
        data[name] = mark
    return data

def read_csv_input(file_path):
    """
    Read student names and marks from a CSV file.
    CSV format: Name,Marks per line. Returns a dictionary {name: mark}.
    """
    import csv
    data = {}
    try:
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                # Expecting at least 2 columns: name and mark
                if len(row) >= 2:
                    name = row[0].strip()
                    try:
                        mark = float(row[1])
                    except ValueError:
                        continue
                    data[name] = mark
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return data

def display_statistics(scores):
    """Calculate and display mean, median, max, and min of the given scores."""
    mean = calculate_mean(scores)
    median = calculate_median(scores)
    max_score = find_max(scores)
    min_score = find_min(scores)
    print(f"Mean score: {mean:.2f}")
    print(f"Median score: {median:.2f}")
    print(f"Max score: {max_score:.2f}")
    print(f"Min score: {min_score:.2f}")

def main():
    while True:
        print("\nGradeBook Analyzer Menu:")
        print("1. Manual input")
        print("2. CSV input")
        print("3. Exit")
        choice = input("Enter choice (1-3): ")
        if choice == '1':
            students = read_manual_input()
        elif choice == '2':
            file_path = input("Enter CSV file path: ")
            students = read_csv_input(file_path)
        elif choice == '3':
            print("Exiting GradeBook Analyzer.")
            break
        else:
            print("Invalid choice. Please try again.")
            continue

        if not students:
            print("No student data available.")
            continue

        # Extract scores for statistics
        scores = list(students.values())

        # Display statistics (mean, median, max, min)
        print("\nStatistics:")
        display_statistics(scores)

        # Assign grades and count distribution
        grade_distribution = {}
        results = {}
        for name, score in students.items():
            grade = assign_grade(score)
            results[name] = (score, grade)
            grade_distribution[grade] = grade_distribution.get(grade, 0) + 1

        # List comprehensions for passed and failed students
        passed_students = [name for name, score in students.items() if score >= 40]
        failed_students = [name for name, score in students.items() if score < 40]

        # Display grade distribution
        print("\nGrade Distribution:")
        for grade in sorted(grade_distribution.keys()):
            print(f"{grade}: {grade_distribution[grade]}")

        # Display passed/failed students
        print("\nPassed Students:", ", ".join(passed_students))
        print("Failed Students:", ", ".join(failed_students))

        # Display table of Name, Marks, Grade
        print("\nResults:")
        print(f"{'Name':<15s} {'Marks':<7s} {'Grade':<5s}")
        print("-" * 30)
        for name, (score, grade) in results.items():
            print(f"{name:<15s} {score:<7.2f} {grade:<5s}")

        # Option to repeat or exit
        cont = input("\nWould you like to perform another analysis? (y/n): ")
        if cont.lower() != 'y':
            print("Exiting GradeBook Analyzer.")
            break

if __name__ == "__main__":
    main()



