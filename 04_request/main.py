from fastapi import FastAPI, Request

app = FastAPI()

@app.get('/items')
async def read_items(request : Request):
    # 클라이언트 ip
    host = request.client.host
    # Request 객체로 확인 가능한 것
    # body() : 본문
    # headers : 헤더
    return {'clienthost' : host}

# request Body
# 클래스 타입으로 만들고, BaseModel을 상속받아 구현한다.
from pydantic import BaseModel

class Teacher(BaseModel):
    is_working: bool
    name: str
    nickname: str | None = None # 선택적 항목으로 설정
    
@app.post('/teachers')
async def teacher_info(teacher: Teacher):
    if teacher.nickname:
        return f'안녕하세요 제 이름은 {teacher.name}, 닉네임은 {teacher.nickname}이고 현재 일하는 상태는 {teacher.is_working}입니다.'
    return f'안녕하세요 제 이름은 {teacher.name}이고, 현재 일하는 상태는 {teacher.is_working}입니다.'

# path_parameter
# query_parameter
# requestBody

# student_no : path_parameter로 받고 int
# Student : requestBody (이름, 나이)
# lecture_name : query_parameter

# student no, name, age, lecture_name을 전부 출력하는 문자열로 return 해주는 api 작성해보기

class Student(BaseModel):
    name: str
    age: int
    
@app.post('/students/{student_no}')
async def student_info(
    student_no: int,
    name: str,
    age: int,
    lecture_name: str
    ):
    return {
        '학번': student_no,
        '이름': name,
        '나이': age,
        '수강중인 과목': lecture_name
    }