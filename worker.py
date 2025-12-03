import os
import time

from celery import Celery
from openai import BaseModel, OpenAI

client = OpenAI()

app = Celery(
    "random_number",
    broker=os.getenv("CELERY_BROKER_URL"),
    backend=os.getenv("CELERY_BACKEND_URL"),
)


# class Movie(BaseModel):
#     title: str
#     release_year: int
#     director: str
#     genre: str


class MoviePartA(BaseModel):
    title: str
    release_year: int


class MoviePartB(BaseModel):
    director: str
    genre: str


class MoviePartC(BaseModel):
    actors: list[str]


@app.task
def movie_info_a(prompt):
    # response = client.beta.chat.completions.parse(
    #     model="gpt-4o-mini",
    #     messages=[
    #         {
    #             "role": "system",
    #             "content": "You are an assistant that provides movie information in a structured way.",
    #         },
    #         {"role": "user", "content": prompt},
    #     ],
    #     response_format=MoviePartA,
    # )

    # content = response.choices[0].message.content
    # if not content:
    #     raise ValueError("No content returned from OpenAI")

    # movie_part_a = MoviePartA.model_validate_json(content)
    time.sleep(5)

    movie_part_a = MoviePartA(
        title="Shutter Island",
        release_year=2010,
    )

    return movie_part_a.model_dump()


@app.task
def movie_info_b(prompt):
    # response = client.beta.chat.completions.parse(
    #     model="gpt-4o-mini",
    #     messages=[
    #         {
    #             "role": "system",
    #             "content": "You are an assistant that provides movie information in a structured way.",
    #         },
    #         {"role": "user", "content": prompt},
    #     ],
    #     response_format=MoviePartB,
    # )

    # content = response.choices[0].message.content
    # if not content:
    #     raise ValueError("No content returned from OpenAI")

    # movie_part_b = MoviePartB.model_validate_json(content)
    time.sleep(5)
    movie_part_b = MoviePartB(
        director="Martin Scorsese",
        genre="Drama",
    )

    time.sleep(5)
    return movie_part_b.model_dump()


@app.task
def movie_info_c(prompt):
    # response = client.beta.chat.completions.parse(
    #     model="gpt-4o-mini",
    #     messages=[
    #         {
    #             "role": "system",
    #             "content": "You are an assistant that provides movie information in a structured way.",
    #         },
    #         {"role": "user", "content": prompt},
    #     ],
    #     response_format=MoviePartC,
    # )

    # content = response.choices[0].message.content
    # if not content:
    #     raise ValueError("No content returned from OpenAI")

    # movie_part_c = MoviePartC.model_validate_json(content)

    time.sleep(5)
    movie_part_c = MoviePartC(
        actors=["Leonardo DiCaprio", "Mark Wahlberg", "Max von Sydow"],
    )

    return movie_part_c.model_dump()


# @app.task
# def movie_info(prompt):
#     response = client.beta.chat.completions.parse(
#         model="gpt-4o-mini",
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are an assistant that provides movie information in a structured way.",
#             },
#             {"role": "user", "content": prompt},
#         ],
#         response_format=Movie,
#     )

#     content = response.choices[0].message.content
#     if not content:
#         raise ValueError("No content returned from OpenAI")

#     movie = Movie.model_validate_json(content)

#     return movie.model_dump()


# @app.task
# def random_number(max_value):
#     time.sleep(5)
#     return random.randint(1, max_value)


@app.task
def combine_parts(parts):
    merged = {}

    for part in parts:
        merged |= part

    return merged
