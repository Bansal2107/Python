from StudentProject.StudentScheduler import StudentScheduler
class Client:

    def showList(self):
        print("\n1.Add Student")
        print("2.Show all Students")
        print("3.Add Course")
        print("4.Show all Courses")
        print("5.Add Faculty")
        print("6.Show all Faculties")
        print("7.Add Batch Details")
        print("8.Show all Batch Details")
        print("9.Generate Reports")
        print("10. Exit\n")

    def test(self):
        while(1):
            studentScheduler = StudentScheduler()
            client = Client()
            client.showList()
            choice=input("Select your Choice---> ")

            if(choice=="1"):
                name=input("Enter Name  :")
                rollNo=input("Enter RollNo  :")
                coursesNumber=input("Enter number of Courses : ")
                coursesNumber=int(coursesNumber)
                courses = []
                for num in range(coursesNumber):
                    course=input("Enter course name  :")
                    courses.append(course)
                if(studentScheduler.getStudentById(rollNo)=="null"):
                    studentScheduler.addStudent(name,rollNo,courses)
                    print("\nStudent Details Successfully Added\n")
                else:
                    print("\nStudent ID already exists\n")


            if(choice=="2"):
                students = studentScheduler.showAllStudents()
                for student in students:
                    print("\nStudent Name: ",student.getName())
                    print("Student Roll No: ",student.getRollNo())
                    print("Student Courses: ",student.getCourses())

            if(choice=="3"):
                course=input("\nEnter course name to be added:")
                studentScheduler.addCourse(course)
                print("\nCourse Successfully Added !!!\n")

            if(choice=="4"):
                courses=studentScheduler.showAllCourses()
                print("\nCourses Available are:")
                for course in courses:
                    print(course.getCourse())

            if(choice=="5"):
                name = input("\nEnter Faculty Name  :")
                ID = input("Enter Faculty ID   :")
                coursesNumber = input("Enter number of Courses  : ")
                coursesNumber = int(coursesNumber)
                courses = []
                for num in range(coursesNumber):
                    course = input("Enter course name  :")
                    courses.append(course)
                studentScheduler.addFaculty(name, ID, courses)
                print("\nFaculty Details Successfully Added !!!\n")

            if(choice=="6"):
                faculties=studentScheduler.showAllFaculties();
                for faculty in faculties:
                    print("\nFaculty Name   : ",faculty.getName())
                    print("Faculty ID     :   ",faculty.getID())
                    courses=faculty.getCourses()
                    print("Courses are    : ")
                    for course in courses:
                        print(course)


            if(choice=="7"):
                ID=input("\nEnter Batch ID  :")
                facultyName=input("Enter Faculty Name  :")
                courseName=input("Enter Course Name  :")
                studentsNumber = input("Enter number of Students : ")
                studentsNumber = int(studentsNumber)
                students = list()
                for num in range(studentsNumber):
                    studentRollNo=input("Enter Student ID  : ")
                    student=studentScheduler.getStudentById(studentRollNo);
                    students.append(student)
                studentScheduler.addBatchDetails(ID,facultyName,courseName,students);
                print("\nBatch Details Successfully Added !!!\n")

            if(choice=="8"):
                batches=studentScheduler.showAllBatches()
                for batch in batches:
                    print("Batch ID          :",batch.getID())
                    print("Batch Faculty Name:",batch.getFacultyName())
                    print("Batch Course Name :",batch.getCourseName())
                    print("Batch Students    :")
                    students=batch.getStudent()
                    for student in students:
                        print(student.getName())

            if(choice=="9"):
                print("\n\n1. Student Details by Roll Number")
                print("2. Batch Details by Batch ID")
                print("3. Batch Details by Roll Number\n")
                reportChoice=input("Enter choice---> ")
                if(reportChoice=="1"):
                    rollNo=input("\nEnter Roll Number  :")
                    student=studentScheduler.getStudentById(rollNo)
                    print("\nName     : ",student.getName())
                    print("Roll No  :",student.getRollNo())
                    courses=student.getCourses()
                    print("Courses  : ")
                    for course in courses:
                        print(course)

                if(reportChoice=="2"):
                    batchID=input("\nEnter Batch ID   :")
                    batch=studentScheduler.getBatchById(batchID)
                    print("\nBatch ID    :",batch.getID())
                    print("Course Name   :",batch.getCourseName())
                    print("Faculty Name  :",batch.getFacultyName())
                    print("Students      :")
                    students=batch.getStudent();
                    for student in students:
                        print(student.getName())



            if (choice == "10"):
                break;

client=Client()
client.test()

"""         
    
     studentScheduler.addStudent("Akash",101)
     studentScheduler.addStudent("Karan",102)

     students=studentScheduler.showAllStudents()

     for student in students:
         print(student.getName())
         print(student.getRollNo())
         
         
         students = studentScheduler.showAllStudents()
            for student in students:
                print(student.getName())
                print(student.getRollNo())
                print(student.getCourses())
"""
