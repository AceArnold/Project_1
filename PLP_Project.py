import mysql.connector
from datetime import datetime
from mysql.connector import Error

class Convert:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                port=3306,           # Default MySQL port
                user="root",         # Your MySQL Workbench username
                password="root",     # Your MySQL Workbench password
                database="grade_converter",
                auth_plugin='mysql_native_password'  # Authentication plugin for MySQL 8+
            )
            
            if self.connection.is_connected():
                db_info = self.connection.get_server_info()
                print(f"Connected to MySQL Server version {db_info}")
                self.cursor = self.connection.cursor(buffered=True)
                self.create_database()
                self.create_tables()
        except Error as err:
            print(f"Error connecting to MySQL Workbench: {err}")
            exit(1)
    
    def create_database(self):
        try:
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS grade_converter")
            self.cursor.execute("USE grade_converter")
            print("Database 'grade_converter' is ready!")
        except Error as err:
            print(f"Error creating database: {err}")
            exit(1)
    
    def create_tables(self):
        try:
            # Create users table
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    email VARCHAR(100) UNIQUE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                ) ENGINE=InnoDB;
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
                    ON DELETE SET NULL
                    ON UPDATE CASCADE
                ) ENGINE=InnoDB;
            """)
            
            # Create conversion_stats table
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS conversion_stats (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    conversion_type VARCHAR(50) NOT NULL UNIQUE,
                    total_conversions INT DEFAULT 0,
                    avg_from_value FLOAT DEFAULT 0,
                    avg_to_value FLOAT DEFAULT 0,
                    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
                ) ENGINE=InnoDB;
            """)
            
            self.connection.commit()
            print("All tables are ready!")
        except Error as err:
            print(f"Error creating tables: {err}")
            exit(1)
    
    def register_user(self):
        try:
            username = input("Enter your username: ")
            email = input("Enter your email (optional, press enter to skip): ").strip() or None
            
            query = "INSERT INTO users (username, email) VALUES (%s, %s)"
            self.cursor.execute(query, (username, email))
            self.connection.commit()
            user_id = self.cursor.lastrowid
            print(f"User registered successfully with ID: {user_id}")
            return user_id
        except Error as err:
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
            
            # Update statistics with UNIQUE constraint handling
            stats_query = """
                INSERT INTO conversion_stats (conversion_type, total_conversions, avg_from_value, avg_to_value)
                VALUES (%s, 1, %s, %s)
                ON DUPLICATE KEY UPDATE
                total_conversions = total_conversions + 1,
                avg_from_value = ((avg_from_value * total_conversions) + VALUES(avg_from_value)) / (total_conversions + 1),
                avg_to_value = ((avg_to_value * total_conversions) + VALUES(avg_to_value)) / (total_conversions + 1)
            """
            conversion_type = f"{from_system}_to_{to_system}"
            self.cursor.execute(stats_query, (conversion_type, from_value, to_value))
            
            self.connection.commit()
            print("Conversion saved to database!")
        except Error as err:
            print(f"Error saving conversion: {err}")
            self.connection.rollback()
    
    def show_statistics(self):
        try:
            self.cursor.execute("""
                SELECT 
                    conversion_type,
                    total_conversions,
                    ROUND(avg_from_value, 2) as avg_from,
                    ROUND(avg_to_value, 2) as avg_to,
                    last_updated
                FROM conversion_stats
                ORDER BY total_conversions DESC
            """)
            stats = self.cursor.fetchall()
            
            if not stats:
                print("\nNo conversion statistics available yet.")
                return
                
            print("\n=== Conversion Statistics ===")
            for stat in stats:
                print(f"\nConversion Type: {stat[0]}")
                print(f"Total Conversions: {stat[1]}")
                print(f"Average From Value: {stat[2]}")
                print(f"Average To Value: {stat[3]}")
                print(f"Last Updated: {stat[4]}")
            print("\n")
        except Error as err:
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
            if hasattr(self, 'cursor') and self.cursor is not None:
                self.cursor.close()
            if hasattr(self, 'connection') and self.connection.is_connected():
                self.connection.close()
                print("MySQL connection closed.")
        except Error:
            pass

# Running the conversion
def main():
    try:
        grading_system = Convert()

        while True:
            print("\nWelcome to Grade Converter!")
            print("1. Register new user")
            print("2. Continue as guest")
            print("3. View statistics")
            print("4. Exit")
            
            try:
                user_choice = int(input("Enter your choice (1-4): "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if user_choice == 4:
                print("Thank you for using Grade Converter!")
                break

            user_id = None
            if user_choice == 1:
                user_id = grading_system.register_user()
            elif user_choice == 3:
                grading_system.show_statistics()
                continue
            elif user_choice not in [1, 2, 3]:
                print("Invalid choice. Please try again.")
                continue

            print("\nChoose the grading system you want to convert from:")
            print("1. GPA")
            print("2. National")
            print("3. Percentage")
            print("4. Back to main menu")

            try:
                system_choice = int(input("Enter choice (1-4): "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if system_choice == 4:
                continue
            elif system_choice == 1:
                grading_system.gpa(user_id)
            elif system_choice == 2:
                grading_system.national(user_id)
            elif system_choice == 3:
                grading_system.percentage(user_id)
            else:
                print("Invalid choice.")

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if 'grading_system' in locals():
            del grading_system

if __name__ == "__main__":
    main()
