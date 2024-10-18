from sqlalchemy.orm import Session
from fastapi import HTTPException
import schemas, models


# ID로 student 찾기
def get_student_by_id(db: Session, student_id: int):

    found_student = (
        db.query(models.Student).filter(models.Student.id == student_id).first()
    )

    if found_student is None:
        raise HTTPException(status_code=404, detail="Student is not found")

    return found_student


# 모든 student 조회
def get_all_students(db: Session):
    all_students = db.query(models.Student).all()
    return all_students


# student 등록
def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(
        name=student.name,
        nickname=student.nickname,
        description=student.description,
        lunch_menu=student.lunch_menu,
    )

    db.add(db_student)

    db.commit()

    return db_student


# student 정보 수정
def update_student(db: Session, student_id: int, student: schemas.StudentUpdate):

    found_student = (
        db.query(models.Student).filter(models.Student.id == student_id).first()
    )

    if found_student is None:
        raise HTTPException(status_code=404, detail="Student is not found")

    if student.name is not None:
        found_student.name = student.name
    if student.nickname is not None:
        found_student.nickname = student.nickname
    if student.description is not None:
        found_student.description = student.description
    if student.lunch_menu is not None:
        found_student.lunch_menu = student.lunch_menu

    db.commit()

    return found_student


# student 삭제
def delete_student(db: Session, student_id: int):

    found_student = (
        db.query(models.Student).filter(models.Student.id == student_id).first()
    )

    if found_student is None:
        raise HTTPException(status_code=404, detail="Student is not found")

    db.delete(found_student)

    db.commit()
