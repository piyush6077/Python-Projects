"""

Challenge: Student Marks Analyzer

Create a Python program that allows a user to input student names along with their marks and then calculates useful statistics.
Your program should:
1. Let the user input multiple students with their marks (name + integer score).
2. After input is complete, display:
   - Average marks
   - Highest marks and student(s) who scored it
   - Lowest marks and student(s) who scored it
   - Total number of students

Bonus:
- Allow the user to enter all data first, then view the report
- Format output clearly in a report-style layout
- Prevent duplicate student names

"""





class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


class StudentAnalyzer:
    def __init__(self):
        self.students = {}

    def add_student(self, name, marks):
        if name in self.students:
            print("⚠️ Student already exists!")
            return
        self.students[name] = Student(name, marks)
        print("Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No students available.")
            return
        
        print("\n Student List:")
        for student in self.students.values():
            print(f"{student.name} → {student.marks}")

    def calculate_average(self):
        total = sum(s.marks for s in self.students.values())
        return total / len(self.students)

    def get_highest(self):
        max_marks = max(s.marks for s in self.students.values())
        toppers = [s.name for s in self.students.values() if s.marks == max_marks]
        return max_marks, toppers

    def get_lowest(self):
        min_marks = min(s.marks for s in self.students.values())
        low_scorers = [s.name for s in self.students.values() if s.marks == min_marks]
        return min_marks, low_scorers

    def generate_report(self):
        if not self.students:
            print("No student data available.")
            return

        print("\n" + "-"*30)
        print("STUDENT REPORT")
        print("-"*30)

        avg = self.calculate_average()
        highest, toppers = self.get_highest()
        lowest, low_scorers = self.get_lowest()

        print(f"Total Students : {len(self.students)}")
        print(f"Average Marks  : {avg:.2f}")

        print(f"\nHighest Marks  : {highest}")
        print("Topper(s)      : " + ", ".join(toppers))

        print(f"\nLowest Marks   : {lowest}")
        print("Lowest Scorer(s): " + ", ".join(low_scorers))

        print("-"*30)


# -------- MENU-DRIVEN APP --------
analyzer = StudentAnalyzer()

while True:
    print("\n===== MENU =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Generate Report")
    print("4. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        name = input("Enter student name: ").strip()
        try:
            marks = int(input("Enter marks: "))
            analyzer.add_student(name, marks)
        except ValueError:
            print("Invalid marks!")

    elif choice == "2":
        analyzer.view_students()

    elif choice == "3":
        analyzer.generate_report()

    elif choice == "4":
        print("Exiting program... ")
        break

    else:
        print("Invalid choice! Try again.")


################################

s = "abbcd"
d = {} 

for i in s:
    d[i] = d.get(i,0) + 1
    # if i not in d:
    #     d[i] = 1
    #     {a:1,b:1,c:1}
    # else:
    #     d[i] = d[i] + 1
    
    
print(d)

#{a:1,b:2,c:1,d:1}
