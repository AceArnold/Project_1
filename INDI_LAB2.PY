class Assignment:
    def __init__(self, name, category, weight, grade):
        self.name = name
        self.category = category
        self.weight = float(weight)
        self.grade = float(grade)
        self.weighted_grade = (self.grade / 100) * self.weight

class AssigProgram:
    def __init__(self):
        self.assign = []
        self.total_form_grade = 0
        self.total_sum_grade = 0
    
    def add_assign(self, name, category, weight, grade):
        assignment = Assignment(name, category, weight, grade)
        self.assign.append(assignment)
        
        if category == "FORMATIVE" or category == "1":
            self.total_form_grade += grade
        elif category == "SUMMATIVE" or category == "2":
            self.total_sum_grade += grade
        else:
            print("\nInvalid category. \n \nPlease enter 'Formative' or 'Summative'.\nYou could also use the numerical representation of the categories. \nPlease note that category 1 is formative and category 2 is summative")
            exit()
    
    def calc_gpa(self):
        total_weighted_grade = sum(assignment.weighted_grade for assignment in self.assign)
        total_weight = sum(assignment.weight for assignment in self.assign)
        gpa = (total_weighted_grade / total_weight) * 5
        return gpa
    
    def display(self):
        print("\nResults:")
        print("{:<20} {:<10} {:<10} {:<10} {:<10}".format("Assignment", "Category", "Grade (%)", "Weight", "Grade"))
        for assignment in self.assign:
            print("{:<20} {:<10} {:<10} {:<10} {:<10.1f}".format(assignment.name, assignment.category,
                                                                assignment.grade, assignment.weight,
                                                                assignment.weighted_grade))

        print("\nFormatives (60)")
        print("{:<20} {:<10} {:<10} {:<10} {:<10.1f}".format("", "", "", "", self.total_form_grade))

        print("\nSummatives (40)")
        print("{:<20} {:<10} {:<10} {:<10} {:<10.1f}".format("", "", "", "", self.total_sum_grade))

        gpa = self.calc_gpa()
        print("\nGPA")
        print("{:<20} {:<10} {:<10} {:<10} {:<10.3f}".format("", "", "", "", gpa))

def run():
    x = AssigProgram()
    num_assignments = int(input("Enter the number of assignments: "))
    for _ in range(num_assignments):
        print(f"\nAssignment {_ + 1}")
        name = input("Assignment name: ")
        category = input("Category (Formative or number 1/Summative or number 2): ").upper() 
        weight = float(input("Weight of assignment (%): "))
        grade = float(input("Grade obtained (out of 100): "))

        while weight > 100:
            print("Error: Weight cannot exceed 100%.")
            weight = float(input("Weight of assignment (%): "))

        x.add_assign(name, category, weight, grade)
    
    x.display()

print("\n======HELLO WELCOME TO THE GRADE CONVERTER======\n")
print("THIS PROGRAM WILL HELP YOU CONVERT YOUR GRADES TO GPA\n")
print("IF YOU CHOOSE TO USE THE NUMERIAL REPRESENTATION OF THE CATEGORIES  \nPLEASE NOTE THAT CATEGORY 1 IS FORMATIVE AND CATEGORY 2 IS SUMMATIVE\n")
run()