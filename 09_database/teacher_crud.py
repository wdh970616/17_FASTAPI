from sqlalchemy.orm import Session
from fastapi import HTTPException
import schemas, models


# teacher를 저장하는 서비스로직
def create_teacher(db: Session, teacher=schemas.TeacherCreate):
    db_teacher = models.Teacher(
        name=teacher.name,
        nickname=teacher.nickname,
        description=teacher.description,
        is_active=teacher.is_active,
    )

    db.add(db_teacher)

    db.commit()

    return db_teacher


# ID로 teacher 찾기
def get_teacher_by_id(db: Session, teacher_id: int):
    found_teacher = (
        db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()
    )

    if found_teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")

    return found_teacher


# 모든 teacher 찾기
def get_all_teachers(db: Session):
    all_teacher = db.query(models.Teacher).all()
    return all_teacher


# teacher 정보 수정
def update_teacher(db: Session, teacher_id: int, teacher: schemas.TeacherUpdate):

    found_teacher = (
        db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()
    )

    if found_teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")

    if teacher.name is not None:
        found_teacher.name = teacher.name
    if teacher.nickname is not None:
        found_teacher.nickname = teacher.nickname
    if teacher.description is not None:
        found_teacher.description = teacher.description
    if teacher.is_active is not None:
        found_teacher.is_active = teacher.is_active

    db.commit()

    return found_teacher


# teacher 삭제
def delete_teacher(db: Session, teacher_id: int):

    found_teacher = (
        db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()
    )

    if found_teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")

    db.delete(found_teacher)

    db.commit()
