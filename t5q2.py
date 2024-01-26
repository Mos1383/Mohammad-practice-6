class Course:
    def init(self, course_id, course_name, capacity):
        self.course_id = course_id
        self.course_name = course_name
        self.capacity = capacity
        self.students = 0

    def enroll_student(self):
        if self.students < self.capacity:
            self.students += 1
            print("course added successfully!")
        else:
            print("course is full")

class EduSystem:
    def init(self):
        self.courses = []

    def add_course(self, course_id, course_name, capacity):
        for course in self.courses:
            if course.course_id == course_id:
                print("course id already exists")
                return
        new_course = Course(course_id, course_name, capacity)
        self.courses.append(new_course)
        print("course added successfully!")

    def get_course(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                if course.students == 0:
                    course.enroll_student()
                else:
                    print("you already have this course")
                return
        print("incorrect course id")

edu_system = EduSystem()
edu_system.add_course(1, "Math", 50)
edu_system.add_course(2, "Physics", 40)
edu_system.get_course(1)  
edu_system.get_course(1)  