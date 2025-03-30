class GradeConverter:
    def __init__(self):
        self.scales = {
            "1": "National (Out of 60)",
            "3": "Percentage",
            "4": "A-F"
        }

    def get_input(self):
        print("Select the grading system you are converting from:")
        print("1. National (Out of 60)")
        print("3. Percentage")
        print("4. A-F")

        from_sys = input("Enter the number corresponding to your grading system: ")
        if from_sys not in self.scales:
            print("Invalid selection.")
            return None, None

        grade = input("Enter your grade: ")
        return grade, from_sys

    def convert_national_to_gpa(self, grade):
        scale = {60: 4.0, 55: 3.7, 50: 3.5, 45: 3.2, 40: 3.0, 35: 2.5, 30: 2.0, 25: 1.5, 20: 1.0, 15: 0.5, 10: 0.2, 0: 0.0}
        grade = float(grade)
        for k in sorted(scale.keys(), reverse=True):
            if grade >= k:
                return scale[k]
        return "Grade not found"

    def convert_percentage_to_gpa(self, grade):
        scale = {100: 4.0, 90: 3.7, 80: 3.5, 75: 3.2, 70: 3.0, 65: 2.5, 60: 2.0, 55: 1.5, 50: 1.0, 45: 0.5, 0: 0.0}
        grade = float(grade)
        for k in sorted(scale.keys(), reverse=True):
            if grade >= k:
                return scale[k]
        return "Grade not found"

    def convert_letter_to_gpa(self, grade):
        scale = {"A+": 4.0, "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "C+": 2.3, "C": 2.0, "C-": 1.7, "D+": 1.3, "D": 1.0, "F": 0.0}
        return scale.get(grade.upper(), "Grade not found")

    def convert(self, grade, from_sys):
        try:
            if from_sys == "1":
                return self.convert_national_to_gpa(grade)
            elif from_sys == "3":
                return self.convert_percentage_to_gpa(grade)
            elif from_sys == "4":
                return self.convert_letter_to_gpa(grade)
            else:
                return "Invalid system."
        except ValueError:
            return "Invalid input. Please enter a valid grade."

if __name__ == "__main__":
    converter = GradeConverter()
    grade, from_sys = converter.get_input()
    if grade and from_sys:
        print("Converted Grade on 4.0 Scale:", converter.convert(grade, from_sys))
