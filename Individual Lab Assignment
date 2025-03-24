class Assignment:
    def __init__(self, name, category, weight, grade):
        self.name = name
        self.category = category
        self.weight = float(weight)
        self.grade = float(grade)

def calculate_gpa(assignments):
    total_weighted_grade = 0
    total_weight = 0

    for assignment in assignments:
        total_weighted_grade += (assignment.grade / 100) * assignment.weight
        total_weight += assignment.weight

    gpa = (total_weighted_grade / total_weight) * 5
    return gpa

def main():
    assignments = []
    total_formative_grade = 0
    total_summative_grade = 0

    num_assignments = int(input("Enter the number of assignments: "))

    for _ in range(num_assignments):
        print(f"\nAssignment {_ + 1}")
        name = input("Assignment name: ")
        category = input("Category (Formative/Summative): ").lower()
        weight = float(input("Weight of assignment (%): "))
        grade = float(input("Grade obtained (out of 100): "))

        while weight > 100:
            print("Error: Weight cannot exceed 100%.")
            weight = float(input("Weight of assignment (%): "))

        assignment = Assignment(name, category, weight, grade)
        assignments.append(assignment)

        if category == "formative":
            total_formative_grade += grade
        elif category == "summative":
            total_summative_grade += grade

    gpa = calculate_gpa(assignments)
    avg_formative_grade = total_formative_grade / num_assignments
    avg_summative_grade = total_summative_grade / num_assignments

    print("\nResults:")
    print(f"Total grade in Formative category: {total_formative_grade}")
    print(f"Total grade in Summative category: {total_summative_grade}")
    print(f"GPA: {gpa:.2f}")

    if gpa >= (avg_formative_grade + avg_summative_grade) / 2:
        print("Result: Pass")
    else:
        print("Result: Fail and Repeat")

if __name__ == "__main__":
    main()
