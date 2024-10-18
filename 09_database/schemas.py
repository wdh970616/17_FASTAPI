from pydantic import BaseModel
from typing_extensions import Optional


# request를 받거나 response를 받을 때 사용하는 기본 모델
# 기본 형식을 만들어 놓을 수 있다.
class TeacherBase(BaseModel):
    name: str
    nickname: Optional[str] = None
    description: Optional[str] = None
    is_active: bool


# SqlAlchemy 모델 : 데이터베이스의 통신을 위한 데이터 구조 정의
# Pydantic : API 요청과 응답을 위한 데이터 구조 정의


# request 요청 모델
class TeacherCreate(TeacherBase):
    pass


# response 응답 모델
class TeacherResponse(TeacherBase):
    id: int


# 업데이트할 때
class TeacherUpdate(BaseModel):
    name: Optional[str] = None
    nickname: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None


####################################################################################

# Student로 연습하기


# request를 받거나 response를 받을 때 사용하는 기본 모델
class StudentBase(BaseModel):
    name: str
    nickname: Optional[str] = None
    description: Optional[str] = None
    lunch_menu: Optional[str] = None


# request 요청 모델
class StudentCreate(StudentBase):
    pass


# response 응답 모델
class StudentResponse(StudentBase):
    id: int


# 업데이트할 때
class StudentUpdate(BaseModel):
    name: Optional[str] = None
    nickname: Optional[str] = None
    description: Optional[str] = None
    lunch_menu: Optional[str] = None
