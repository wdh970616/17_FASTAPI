from fastapi import FastAPI

app = FastAPI()

# 쿼리 파라미터
# url 뒤에 ? 키=밸류 쌍으로 들어가는 파라미터


@app.get("/teachers/")
async def print_teacher_num(num: int, name: str):
    return {f"num: {num}, name: {name}"}


# 쿼리 매개변수를 필수로 만들려면 기본값을 설정하지 않으면 된다.
# 다양한 매개변수를 작성할 때, 매개변수는 이름으로 찾아지기 때문에 순서는 상관없다.

# 선택적 매개변수
from typing import Union


@app.get("/teachers/{teacher_id}")
async def print_teacher(
    teacher_id: int, name: Union[str, None] = None  # path parameter  # query parameter
):
    if name:
        return {f"teacher_id : {teacher_id}, teacher_name : {name}"}
    return {f"teacher_id : {teacher_id}"}
