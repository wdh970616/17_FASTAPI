from database import Base
from sqlalchemy import Column, Integer, String, Text, Boolean

# String => 고정된 길이(길이 제한)
# Text => 길이 제한이 없다.


class Teacher(Base):
    __tablename__ = "teachers"

    # 컬럼 설정
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    nickname = Column(String(50))
    description = Column(Text)
    is_active = Column(Boolean, default=True)


class Student(Base):
    __tablename__ = "students"

    # 컬럼 설정
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    nickname = Column(String(50))
    description = Column(Text)
    lunch_menu = Column(String(100))


# 관계 설정이 가능하다
