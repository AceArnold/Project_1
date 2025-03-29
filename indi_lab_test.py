class Assignment:
    def __init__(self, name, category, weight, grade):
        self.name = name
        self.category = category
        self.weight = float(weight)
        self.grade = float(grade)

    def calculate_weighted_grade(self):
        return (self.grade / 100) * self.weight


class AssignmentProgram:
    def __init__(self):
        self.assignments = []
        self.total_formative_grade = 0
        self.total_summative_grade = 0

    def add_assignment(self, name, category, weight, grade):
        assignment = Assignment(name, category, weight, grade)
        self.assignments.append(assignment)

        if category == "FORMATIVE":
            self.total_formative_grade += grade
        elif category == "SUMMATIVE":
            self.total_summative_grade += grade

    def calculate_gpa(self):
        total_weighted_grade = sum(assignment.calculate_weighted_grade() for assignment in self.assignments)
        total_weight = sum(assignment.weight for assignment in self.assignments)
        gpa = (total_weighted_grade / total_weight) * 5
        return gpa

    def display_results(self):
        print("\nResults:")
        print("{:<20} {:<10} {:<10} {:<10} {:<10}".format("Assignment", "Category", "Grade (%)", "Weight", "Grade"))
        for assignment in self.assignments:
            print("{:<20} {:<10} {:<10} {:<10} {:<10.1f}".format(assignment.name, assignment.category,
                                                                assignment.grade, assignment.weight,
                                                                assignment.calculate_weighted_grade()))

        print("\nFormatives (60)")
        print("{:<20} {:<10} {:<10} {:<10} {:<10.1f}".format("", "", "", "", self.total_formative_grade))

        print("\nSummatives (40)")
        print("{:<20} {:<10} {:<10} {:<10} {:<10.1f}".format("", "", "", "", self.total_summative_grade))

        gpa = self.calculate_gpa()
        print("\nGPA")
        print("{:<20} {:<10} {:<10} {:<10} {:<10.3f}".format("", "", "", "", gpa))


def run_assignment_program():
    assignment_program = AssignmentProgram()

    num_assignments = int(input("Enter the number of assignments: "))

    for _ in range(num_assignments):
        print(f"\nAssignment {_ + 1}")
        name = input("Assignment name: ")
        category = input("Category (Formative/Summative): ").upper()
        weight = float(input("Weight of assignment (%): "))
        grade = float(input("Grade obtained (out of 100): "))

        while weight > 100:
            print("Error: Weight cannot exceed 100%.")
            weight = float(input("Weight of assignment (%): "))

        assignment_program.add_assignment(name, category, weight, grade)

    assignment_program.display_results()


# Example usage:
run_assignment_program()
