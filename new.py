class workout:
    def __init__(self, start_time, end_time, heart_rate, distance_covered):
        self.start_time=int(start_time)
        self.end_time=int(end_time)
        self.heart_rate=int(heart_rate)
        self.distance_covered=int(distance_covered)
        time_taken=int(end_time)-int(start_time)
        self.time_taken=float(time_taken)
        print(start_time, end_time, heart_rate, distance_covered)

class running(workout):
    def calculate_speed(self):
        speed = self.distance_covered / self.time_taken
        return speed
    def calculate_pace(self):
        pace = self.time_taken / self.distance_covered
        return pace
    def get_summary(self):
        print(f"Start time: {self.start_time}")
        print(f"End time: {self.end_time}")
        print(f"Heart rate: {self.heart_rate}")
        print(f"Distance covered: {self.distance_covered}")
        print(f"Time taken: {self.time_taken}")
        print(f"Speed: {self.calculate_speed()}")
        print(f"Pace: {self.calculate_pace()}")

class cycling(workout):
     
    def calculate_speed(self):
        pace = self.time_taken / self.distance_covered
        return pace
    def get_summary(self):
        print(f"Start time: {self.start_time}")
        print(f"End time: {self.end_time}")
        print(f"Heart rate: {self.heart_rate}")
        print(f"Distance covered: {self.distance_covered}")
        print(f"Time taken: {self.time_taken}")
        print(f"Speed: {self.calculate_speed()}")
        print(f"Pace: {self.calculate_pace()}")

print("Hello Please Select Your Workout")
print("1. Running") 
print("2. Cycling")
workout_type = input("Enter your choice: ")
if workout_type == "1":
    print("You have selected Running")
    print("Please enter the following details")
    a=input("Enter start time: ")
    b=input("Enter end time: ")
    c=input("Enter heart rate: ")
    d=input("Enter distance covered: ")
    x=running(a, b, c, d)
    x.calculate_speed()
    x.calculate_pace()
    x.get_summary()

elif workout_type == "2":
    print("You have selected Cycling")
    print("Please enter the following details")
    a=input("Enter start time: ")
    b=input("Enter end time: ")
    c=input("Enter heart rate: ")
    d=input("Enter distance covered: ")
    x=cycling(a, b, c, d)
    x.calculate_speed()
    x.get_summary()
else:
    print("Invalid choice")
