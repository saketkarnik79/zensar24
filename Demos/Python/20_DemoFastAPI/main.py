from fastapi import FastAPI;
from pydantic import BaseModel;

app = FastAPI();

class Student(BaseModel):
    id: int;
    name: str;
    age: int;
    course: str;

students = {
    1: {
        "id": 101,
        "name": "John Doe",
        "age": 22,
        "course": "Python"
    }
};

@app.post("/students")
def create_student(student: Student):

    students[student.id] = student.model_dump()

    return {
        "message": "Student Created",
        "data": student
    }

@app.get("/students")
def get_students():
    return students

@app.get("/students/{student_id}")
def get_student(student_id: int):
    return students.get(student_id)

@app.put("/students/{student_id}")
def update_student(
    student_id: int,
    student: Student
):
    students[student_id] = student.model_dump()
    return {
        "message": "Updated Successfully",
        "data": student
    }

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    deleted = students.pop(student_id)
    return {
        "message": "Deleted",
        "data": deleted
    }