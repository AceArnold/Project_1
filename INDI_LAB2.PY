class Assignment: # This class represents an assignment with its details.

    def __init__(self, name, category, weight, grade):
        self.name = name
        self.category = category
        self.weight = float(weight)
        self.grade = float(grade)
        self.weighted_grade = (self.grade / 100) * self.weight  # The weighted grade is calculated as (grade / 100) * weight.

class AssigProgram: # This class manages a list of assignments and calculates the GPA.

    def __init__(self): # This method initializes the AssigProgram class.
        self.assign = []
        self.total_form_grade = 0
        self.total_sum_grade = 0
    
    def add_assign(self, name, category, weight, grade): # This method adds an assignment to the list and updates the total grades for formative and summative categories.
        assignment = Assignment(name, category, weight, grade)
        self.assign.append(assignment)
        
        if category == "FORMATIVE" or category == "1": # This condition checks if the category is formative (either by name or number).
            self.total_form_grade += grade
        elif category == "SUMMATIVE" or category == "2":
            self.total_sum_grade += grade
        else:
            print("\nInvalid category. \n \nPlease enter 'Formative' or 'Summative'.\nYou could also use the numerical representation of the categories. \nPlease note that category 1 is formative and category 2 is summative. \n")
            print("Exiting the program.")
            print("Please try again.")
            exit() # This line exits the program if an invalid category is entered.
    
    def calc_gpa(self): # This method calculates the GPA based on the weighted grades of all assignments.
        total_weighted_grade = sum(assignment.weighted_grade for assignment in self.assign)
        total_weight = sum(assignment.weight for assignment in self.assign)
        gpa = (total_weighted_grade / total_weight) * 5
        return gpa
    
    def display(self): # This method displays the results of the assignments, including the total grades for formative and summative categories and the GPA.
        print("\n======RESULTS======\n")
        print("{:<20} "
        "{:<10} "
        "{:<10} "
        "{:<10} "
        "{:<10}".format("Assignment", "Category", "Grade (%)", "Weight", "Grade"))
        for assignment in self.assign:
            print("{:<20} {:<10} {:<10} {:<10} {:<10.1f}".format(assignment.name, assignment.category,
                                                                assignment.grade, assignment.weight,
                                                                assignment.weighted_grade))

        print("\nFormatives (60)")
        print("{:<20} "
        "{:<10} "
        "{:<10} "
        "{:<10} "
        "{:<10.1f}".format("", "", "", "", self.total_form_grade))

        print("\nSummatives (40)")
        print("{:<20} "
        "{:<10} "
        "{:<10} "
        "{:<10} "
        "{:<10.1f}".format("", "", "", "", self.total_sum_grade))

        gpa = self.calc_gpa()
        print("\nGPA")
        print("{:<20} "
        "{:<10} "
        "{:<10} "
        "{:<10} "
        "{:<10.3f}".format("", "", "", "", gpa))

def run(): # This function runs the assignment program.
    x = AssigProgram() # This line creates an instance of the AssigProgram class.
    num_assignments = int(input("Enter the number of assignments: "))
    for _ in range(num_assignments):
        print(f"\nAssignment {_ + 1}")
        name = input("Assignment name: ")
        category = input("Category (Formative or number 1/Summative or number 2): ").upper() 
        weight = float(input("Weight of assignment (%): "))
        grade = float(input("Grade obtained (out of 100): "))

        while weight > 100:
            print("Error: Weight cannot exceed 100%.\n \nPlease try again.")
            exit()
            # weight = float(input("Weight of assignment (%): "))

        x.add_assign(name, category, weight, grade)
    
    x.display() # This line calls the display method to show the results.

# Main program execution
print("\n======HELLO WELCOME TO THE GRADE CONVERTER======\n")
print("THIS PROGRAM WILL HELP YOU CONVERT YOUR GRADES TO GPA\n")
print("IF YOU CHOOSE TO USE THE NUMERIAL REPRESENTATION OF THE CATEGORIES  \nPLEASE NOTE THAT CATEGORY 1 IS FORMATIVE AND CATEGORY 2 IS SUMMATIVE\n")
run()


# Programming Concepts Used in This Implementation:
# Data Structures: Lists (used to store assignments)
# Object-Oriented Programming: Classes (Assignment, AssigProgram), Objects, Encapsulation
# Loops: for loop (iterating through assignments), while loop (input validation)
# Functions/Methods: Defined methods for adding assignments, calculating GPA, and displaying results
# Conditional Statements: if-elif conditions for category checking and weight validation