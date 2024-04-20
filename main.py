from fastapi import FastAPI
from typing import List
from course import CourseManager, Course
from user import UserManager
from fastapi.security import APIKeyHeader
from pydantic import BaseModel, Field

coursemanager = CourseManager()
usermanager = UserManager()
usermanager.create_a_user("John", "pwd", "studnet")
usermanager.create_a_user("Alice", "pwd", "teacher")
usermanager.create_a_user("Jimmy", "pwd", "admin")

app = FastAPI()

@app.get("/")
def welcome():
    return "Welcome to our miniCanvas!"

class CourseCreate(BaseModel):
    semester: str
    teacher_id_list: List[int] = Field(..., json_schema_extra={'example': [1, 2, 3]})

@app.post("/courses/{coursecode}")
def create_a_course(coursecode: str, course_data: CourseCreate):
    teacher_list = usermanager.find_users(course_data.teacher_id_list)
    course_id = coursemanager.create_a_course(coursecode, course_data.semester, teacher_list)
    return {"course_id": course_id}

@app.put("/courses/{courseid}/students")
def import_students(courseid: int,
                    student_id_list: List[int]) -> None:
    course = coursemanager.find_a_course(courseid)
    student_list = usermanager.find_users(student_id_list)
    course.import_students(student_list)
    
    print(course.course_id)
    print(course.student_list)
    
    return None