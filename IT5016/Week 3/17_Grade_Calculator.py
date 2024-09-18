"""
Week 3 Lab 
Question 4. The program inputs the assessment grade and the exam grade from a student and calculates the final grade.
Author: Sukhjyot Singh
"""

def grade():
    assessment_grade = float(input("Enter your assessment grade: "))
    exam_grade = float(input("Enter yopu exam grade: "))

    average_grade = (assessment_grade + exam_grade) * 0.5
    print(f"Your average grade is {average_grade}")

    if(average_grade == 90 or average_grade >90):
        print("Your final grade is A.")

    elif(average_grade == 80 or average_grade >80):
        print("Your final grade is B.")

    elif(average_grade == 70 or average_grade > 70):
        print("Your final grade is C.")

    elif(average_grade == 60 or average_grade > 60):
        print("Your final grade is D.")

    else:
        print("FAIL")

grade()
