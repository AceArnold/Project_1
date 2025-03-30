import mysql.connector
from datetime import datetime

class Convert:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host="127.0.0.1",  # Using the IP address shown in your phpMyAdmin
                user="root",       # Default phpMyAdmin username
                password="",       # Your MySQL password (blank by default in XAMPP)
                database="grade_converter"
            )
            self.cursor = self.connection.cursor()
            self.create_tables()
            print("Successfully connected to MySQL!")
        except mysql.connector.Error as err:
            print(f"Error connecting to MySQL: {err}")
    
    def create_tables(self):
        try:
            # Create users table
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    email VARCHAR(100) UNIQUE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Create grade_conversions table with user reference
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS grade_conversions (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    user_id INT,
                    from_system VARCHAR(20) NOT NULL,
                    from_value FLOAT NOT NULL,
                    to_system VARCHAR(20) NOT NULL,
                    to_value FLOAT NOT NULL,
                    conversion_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )
            """)
            
            # Create conversion_stats table
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS conversion_stats (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    conversion_type VARCHAR(50) NOT NULL,
                    total_conversions INT DEFAULT 0,
                    avg_from_value FLOAT DEFAULT 0,
                    avg_to_value FLOAT DEFAULT 0,
                    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
                )
            """)
            
            self.connection.commit()
            print("All tables are ready!")
        except mysql.connector.Error as err:
            print(f"Error creating tables: {err}")
    
    def register_user(self):
        try:
            username = input("Enter your username: ")
            email = input("Enter your email (optional, press enter to skip): ").strip() or None
            
            query = "INSERT INTO users (username, email) VALUES (%s, %s)"
            self.cursor.execute(query, (username, email))
            self.connection.commit()
            user_id = self.cursor.lastrowid
            print(f"User registered successfully!")
            return user_id
        except mysql.connector.Error as err:
            if err.errno == 1062:  # Duplicate entry error
                print("Username or email already exists. Please try again.")
            else:
                print(f"Error registering user: {err}")
            return None
    
    def save_conversion(self, from_system, from_value, to_system, to_value, user_id=None):
        try:
            # Save the conversion
            query = """
                INSERT INTO grade_conversions (user_id, from_system, from_value, to_system, to_value)
                VALUES (%s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (user_id, from_system, from_value, to_system, to_value))
            
            # Update statistics
            stats_query = """
                INSERT INTO conversion_stats (conversion_type, total_conversions, avg_from_value, avg_to_value)
                VALUES (%s, 1, %s, %s)
                ON DUPLICATE KEY UPDATE
                total_conversions = total_conversions + 1,
                avg_from_value = (avg_from_value * total_conversions + %s) / (total_conversions + 1),
                avg_to_value = (avg_to_value * total_conversions + %s) / (total_conversions + 1)
            """
            conversion_type = f"{from_system}_to_{to_system}"
            self.cursor.execute(stats_query, (conversion_type, from_value, to_value, from_value, to_value))
            
            self.connection.commit()
            print("Conversion saved to database!")
        except mysql.connector.Error as err:
            print(f"Error saving conversion: {err}")
    
    def show_statistics(self):
        try:
            self.cursor.execute("SELECT * FROM conversion_stats")
            stats = self.cursor.fetchall()
            
            print("\n=== Conversion Statistics ===")
            for stat in stats:
                print(f"\nConversion Type: {stat[1]}")
                print(f"Total Conversions: {stat[2]}")
                print(f"Average From Value: {stat[3]:.2f}")
                print(f"Average To Value: {stat[4]:.2f}")
                print(f"Last Updated: {stat[5]}")
            print("\n")
        except mysql.connector.Error as err:
            print(f"Error fetching statistics: {err}")
    
    def gpa(self, user_id=None):
        gpa_score = float(input("Enter your GPA: "))
        print("Convert to:")
        print("1. Percentage")
        print("2. National")
        choice = int(input("Enter choice (1 or 2): "))
        
        if choice == 1:
            percentage = gpa_score * 25  # Example conversion
            print(f"Your GPA {gpa_score} is approximately {percentage}%.")
            self.save_conversion("GPA", gpa_score, "Percentage", percentage, user_id)
        elif choice == 2:
            national = (gpa_score/4)*60  # Example conversion
            print(f"Your GPA {gpa_score} is approximately {national} in the national system.")
            self.save_conversion("GPA", gpa_score, "National", national, user_id)
        else:
            print("Invalid choice.")
    
    def national(self, user_id=None):
        national_score = float(input("Enter your National grade: "))
        print("Convert to:")
        print("1. GPA")
        print("2. Percentage")
        choice = int(input("Enter choice (1 or 2): "))
        
        if choice == 1:
            gpa = (national_score / 60)*4  # Example conversion
            print(f"Your National grade {national_score} is approximately {gpa} GPA.")
            self.save_conversion("National", national_score, "GPA", gpa, user_id)
        elif choice == 2:
            percentage = (national_score / 60) * 100  # Example conversion
            print(f"Your National grade {national_score} is approximately {percentage}%.")
            self.save_conversion("National", national_score, "Percentage", percentage, user_id)
        else:
            print("Invalid choice.")
    
    def percentage(self, user_id=None):
        percentage_score = float(input("Enter your Percentage grade: "))
        print("Convert to:")
        print("1. GPA")
        print("2. National")
        choice = int(input("Enter choice (1 or 2): "))
        
        if choice == 1:
            gpa = (percentage_score / 100)*4  # Example conversion
            print(f"Your Percentage grade {percentage_score}% is approximately {gpa} GPA.")
            self.save_conversion("Percentage", percentage_score, "GPA", gpa, user_id)
        elif choice == 2:
            national = (percentage_score / 100) * 60  # Example conversion
            print(f"Your Percentage grade {percentage_score}% is approximately {national} in the national system.")
            self.save_conversion("Percentage", percentage_score, "National", national, user_id)
        else:
            print("Invalid choice.")
    
    def __del__(self):
        try:
            if hasattr(self, 'connection') and self.connection.is_connected():
                self.cursor.close()
                self.connection.close()
                print("MySQL connection closed.")
        except Exception:
            pass

# Running the conversion
grading_system = Convert()

print("Welcome to Grade Converter!")
print("1. Register new user")
print("2. Continue as guest")
print("3. View statistics")
user_choice = int(input("Enter your choice (1-3): "))

user_id = None
if user_choice == 1:
    user_id = grading_system.register_user()
elif user_choice == 3:
    grading_system.show_statistics()
    exit()

print("\nChoose the grading system you want to convert from:")
print("1. GPA")
print("2. National")
print("3. Percentage")

system_choice = int(input("Enter choice (1, 2, or 3): "))

if system_choice == 1:
    grading_system.gpa(user_id)
elif system_choice == 2:
    grading_system.national(user_id)
elif system_choice == 3:
    grading_system.percentage(user_id)
else:
    print("Invalid choice.")
