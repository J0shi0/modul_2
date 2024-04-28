from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid
import asyncio

# Создает экземпляр приложения FastAPI
app = FastAPI()


# Определение модели данных с именем Task с одним полем duration типа int.
# Эта модель будет использоваться для представления данных задачи, полученных из запросов.
class Task(BaseModel):
    duration: int


# Словарь, используемый для хранения задач в памяти.
tasks = {}


# Функция имитирует выполнение задачи.
# Она использует asyncio.sleep(длительность) для ожидания заданного времени.
# Во время выполнения задачи она обновляет статус задачи в словаре задач на "gotovo".
async def task_worker(task_id: str, duration: int):
    await asyncio.sleep(duration)
    tasks[task_id] = "gotovo"


# Функция асинхроного обработчика с декоратором POST для конечной точки /task. response_model=dict указывает на то, что ответом будет словарь.
# После генерирует уникальный идентификатор задачи, используя uuid.uuid4().
# Затем обновляет статус задачи в словаре задач на "soobrajaet".
# Функция использует asyncio.create_task для создания новой асинхронной задачи,
# которая вызывает функцию task_worker с task_id и task.duration.
# Возвращает словарь, содержащий сгенерированный task_id.
@app.post("/task", response_model=dict)
async def create_task(task: Task):
    task_id = str(uuid.uuid4())
    tasks[task_id] = "soobrajaet"
    await asyncio.create_task(task_worker(task_id, task.duration))
    return {"task_id": task_id}


# Функция асинхронного обработчика с декоратором GET для конечной точки /task/{task_id}. response_model=dict указывает на то, что ответом будет словарь.
# Происходит проверка на наличее task_id в tasks. Если ID не найден, то поднимается HTTPException с кодом 404.
# В противном случае возвращается словарь со статусом задачи.
@app.get("/task/{task_id}", response_model=dict)
async def get_task_status(task_id: str):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"status": tasks[task_id]}


# Функция асинхронного обработчика с декоратором GET для конечной точки /task. response_model=dict указывает на то, что ответом будет словарь.
# Возвращает словарь со состояниями всех задач.
@app.get("/tasks", response_model=dict)
async def get_all_tasks():
    return tasks
