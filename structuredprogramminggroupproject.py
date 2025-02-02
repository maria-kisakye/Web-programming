"""Calculates the grade and grade point average (GPA) based on the given score.

    Args:
        score: The student's score.

    Returns:
        A tuple containing the grade and GPA.
    """

def grade_calculator(score):
    
    if 80 <= score <= 100:
        grade = 'A'
        gpa = 5.0
    elif 75 <= score <= 79:
        grade = 'B+'
        gpa = 4.5
    elif 70 <= score <= 74:
        grade = 'B'
        gpa = 4.0
    elif 65 <= score <= 69:
        grade = 'C+'
        gpa = 3.5
    elif 60 <= score <= 64:
        grade = 'C'
        gpa = 3.0
    elif 55 <= score <= 59:
        grade = 'D+'
        gpa = 2.5
    elif 50 <= score <= 54:
        grade = 'D'
        gpa = 2.0
    else:
        grade = 'F'
        gpa = 0.0

    return grade, gpa

score = int(input('enter the score: '))  
grade, gpa = grade_calculator(score)
print(f"Grade: {grade}, GPA: {gpa}")


### qn 1:
def calculate_average(grades):
    """Calculate the average of a list of grades."""
    if not grades:
        return 0
    return sum(grades) / len(grades)

def assign_letter_grade(average):
    """Assign a letter grade based on the average score."""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def main():
    """Main function to run the student grading system."""
    students = []  # List to store student data57l

    continue_input = True
    while continue_input:
        # Input student name
        name = input("Enter student name (or type 'exit' to finish): ")
        if name.lower() == 'exit':
            continue_input = False
            break
        
        grades = []
        for i in range(1, 4):  # Allow input for 3 papers
            while True:
                try:
                    grade = float(input(f"Enter grade for paper {i} for {name}: "))
                    if 0 <= grade <= 100:  # Validate that the grade is between 0 and 100
                        grades.append(grade)
                        break
                    else:
                        print("Please enter a grade between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a numeric grade.")

        # Store student data as a list: [name, grades]
        students.append([name, grades])

    # Calculate averages and assign letter grades
    if students:
        print("\nStudent Grades and Averages:")
        for student in students:
            name = student[0]
            grades = student[1]
            average = calculate_average(grades)
            letter_grade = assign_letter_grade(average)
            print(f"{name}: Grades: {grades}, Average: {average:.2f}, Letter Grade: {letter_grade}")
    else:
        print("No student data entered.")

if __name__ == "__main__":
    main()


    # Student Grading System README.

#The Student Grading System is a command-line interface (CLI) application written in Python that allows users to input student names 
# and their grades for three papers. The program calculates the average grade for each student 
# and assigns a corresponding letter grade based on the average.

## Features

#- Input student names and grades for three papers.
#- Calculate the average grade for each student.
#- Assign letter grades based on average scores.
#- Display a summary of all students with their grades, averages, and letter grades.
#- Input validation for grades to ensure they are between 0 and 100.

## Requirements

#- Python 3.x installed on your system.
