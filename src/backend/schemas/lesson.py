from pydantic import BaseModel, Field


class LessonData(BaseModel):
    title: str = Field(min_length=5, max_length=50)
    information: str = Field(min_length=5, max_length=10000)

    questions: list[list[str]] = Field(min_length=2)


class TestData(BaseModel):
    options: list[str] = Field(min_length=2)
    curr_answer: list[str] = Field(min_length=1)
