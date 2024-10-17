from fastapi import FastAPI
from typing import Union

app = FastAPI()

# 각 파라미터(사용자가 전달할 데이터)에 대해 검증과 추가정보 입력을 위한 기능을 제공한다.

# query parameter validation
from fastapi import Query

@app.get('/teachers')
async def print_teacher_name(
    name: Union[str, None] = Query(
        # name은 필수가 아니며 최대 20글자, 최소 2글자 이내로 입력해야한다.
        default = None,
        max_length = 20,
        min_length = 2
    )
):
    return f'teacher_name'