import json
import random
from contextlib import contextmanager
import time


# Декоратор
def print_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__}:")
        print(result)
        return result
    return wrapper


# Контекстный менеджер для замера времени
@contextmanager
def cm_timer_1():
    start_time = time.time()
    yield
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.4f} seconds")


# Функции для обработки данных
@print_result
def f1(arg):
    return sorted(
        set(job.get('job-name', '').strip().lower() for job in arg if 'job-name' in job),
        key=str.lower
    )


@print_result
def f2(data):
    return list(filter(lambda job: job.lower().startswith("программист"), data))


@print_result
def f3(data):
    return list(map(lambda job: f"{job} с опытом Python", data))


@print_result
def f4(data):
    salaries = [random.randint(100000, 200000) for _ in range(len(data))]
    return [f"{job}, зарплата {salary} руб." for job, salary in zip(data, salaries)]



if __name__ == "__main__":
    path = "C:\\Users\\gordo\\Downloads\\data_light.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    with cm_timer_1():
        f4(f3(f2(f1(data))))
