"""
Author: Sukhjyot Singh Saini
"""
def average_grade(records):
    total_grade = sum(record[2] for record in records)
    return total_grade / len(records)


students = (
    ('Sukh',20, 94), ('Gurpreet',22,92), ('Divya',24,90)
    )

def main():
    avg_grade = average_grade(students)
    print("Average Grade: ", avg_grade)

main()




