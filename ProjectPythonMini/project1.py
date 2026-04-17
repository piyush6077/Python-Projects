class student:
    def __init__(self,name,marks):
        self.name = name 
        self.student = student

class studentsMarksAnalyser:
    def __init__(self):
        self.student = {}

    def add_Student(self,name,marks):        
        if name in self.student:
            print("Student is in the list")
            return
        
        self.student[name] = student(name,marks)
        print("Student added successfully")

    def totalNumberStudent(self):
        if not self.student:
            print("No student available")
            return

        print(len(self.student)) 
    
annalyser = studentsMarksAnalyser()

while True:
    print("\n====Menu====")
    print("\n1. Add Student")
    print("2. Total Number of Student")
    print("3. Generate Report")
    print("4. Exit")

    choice = input("Enter your choice : ").strip()

    if choice == "1":
        name = input("Enter student name : ").strip()
        try:
            marks = int(input("Enter marks : "))
            annalyser.add_Student(name,marks)
        except:
            print("Invalid marks")

    elif choice == "2":
        annalyser.totalNumberStudent()