class Convert:
    def __init__(self):
        pass
    
    def gpa(self):
        gpa_score = float(input("Enter your GPA: "))
        print("Convert to:")
        print("1. Percentage")
        print("2. National")
        choice = int(input("Enter choice (1 or 2): "))
        
        if choice == 1:
            percentage = gpa_score * 25  # Example conversion
            print(f"Your GPA {gpa_score} is approximately {percentage}%.")
        elif choice == 2:
            national = (gpa_score/4)*60  # Example conversion
            print(f"Your GPA {gpa_score} is approximately {national} in the national system.")
        else:
            print("Invalid choice.")
    
    def national(self):
        national_score = float(input("Enter your National grade: "))
        print("Convert to:")
        print("1. GPA")
        print("2. Percentage")
        choice = int(input("Enter choice (1 or 2): "))
        
        if choice == 1:
            gpa = (national_score / 60)*4  # Example conversion
            print(f"Your National grade {national_score} is approximately {gpa} GPA.")
        elif choice == 2:
            percentage = (national_score / 60) * 100  # Example conversion
            print(f"Your National grade {national_score} is approximately {percentage}%.")
        else:
            print("Invalid choice.")
    
    def percentage(self):
        percentage_score = float(input("Enter your Percentage grade: "))
        print("Convert to:")
        print("1. GPA")
        print("2. National")
        choice = int(input("Enter choice (1 or 2): "))
        
        if choice == 1:
            gpa = (percentage_score / 100)*4  # Example conversion
            print(f"Your Percentage grade {percentage_score}% is approximately {gpa} GPA.")
        elif choice == 2:
            national = (percentage_score / 100) * 60  # Example conversion
            print(f"Your Percentage grade {percentage_score}% is approximately {national} in the national system.")
        else:
            print("Invalid choice.")

# Running the conversion
grading_system = Convert()
print("Choose the grading system you want to convert from:")
print("1. GPA")
print("2. National")
print("3. Percentage")

system_choice = int(input("Enter choice (1, 2, or 3): "))

if system_choice == 1:
    grading_system.gpa()
elif system_choice == 2:
    grading_system.national()
elif system_choice == 3:
    grading_system.percentage()
else:
    print("Invalid choice.")
