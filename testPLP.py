class GradeConverter:
    def __init__(self):
        self.scales = {
            "1": "National (Out of 60)",
            "3": "Percentage",
            "4": "A-F"
        }
        
    def get_input(self):
        print("1. National (Out of 60)\n3. Percentage\n4. A-F")
        from_sys = input("Convert from: ")
        if from_sys not in self.scales:
            return None, None
        return input("Enter your grade: "), from_sys
    
    def convert_national_to_gpa(self, grade):
        scale = {60: 4.0, 50: 3.5, 40: 3.0, 30: 2.0, 20: 1.0, 10: 0.5, 0: 0.0}
        grade = float(grade)
        return next((v for k, v in sorted(scale.items(), reverse=True) if grade >= k), "Grade not found")
    
    def convert_percentage_to_gpa(self, grade):
        scale = {90: 4.0, 80: 3.5, 70: 3.0, 60: 2.0, 50: 1.0, 0: 0.0}
        grade = float(grade)
        return next((v for k, v in sorted(scale.items(), reverse=True) if grade >= k), "Grade not found")
    
    def convert_letter_to_gpa(self, grade):
        scale = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
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
        except:
            return "Invalid input."
    
if __name__ == "__main__":
    converter = GradeConverter()
    grade, from_sys = converter.get_input()
    if grade and from_sys:
        print("Converted Grade on 4.0 Scale:", converter.convert(grade, from_sys))
