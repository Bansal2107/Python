from StudentProject.Student import Student
from StudentProject.Course import Course
from StudentProject.Faculty import Faculty
from StudentProject.Batch import Batch

class StudentScheduler:

    students=list()
    courses=list()
    faculties=list()
    batches=list()

    def addStudent(self,name,rollNo,courses):
        student=Student()
        student.setName(name)
        student.setRollNo(rollNo)
        student.setCourses(courses)
        self.students.append(student)

    def showAllStudents(self):
        return self.students

    def addCourse(self,course):
        courseObj=Course()
        courseObj.setCourse(course)
        self.courses.append(courseObj)
        for courseLoop in self.courses:
            print(courseLoop.getCourse())

    def showAllCourses(self):
        return self.courses

    def addFaculty(self,ID,name,courses):
        faculty=Faculty()
        faculty.setName(name)
        faculty.setCourses(courses)
        faculty.setID(ID)
        self.faculties.append(faculty)

    def showAllFaculties(self):
        return self.faculties

    def addBatchDetails(self,ID,facultyName,courseName,batchStudents):
        batch=Batch()
        batch.setID(ID)
        batch.setCourseName(courseName)
        batch.setFacultyName(facultyName)
        batch.setStudent(batchStudents)
        self.batches.append(batch)

    def getStudentById(self,ID):
        flag=0
        for student in self.students:
            if(student.getRollNo()==ID):
                flag=1
                tempStudent=student
        if(flag==1):
            return tempStudent
        return "null"

    def showAllBatches(self):
        return self.batches

    def getBatchById(self,ID):
        for batch in self.batches:
            if(batch.getID()==ID):
                return batch

