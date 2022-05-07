from app.models.task import Task
from .routes_helper import error_msg

def make_task_safely(data_dict):
    try:
        task = Task.from_dict(data_dict)
    except KeyError:
        error_msg(f"Invalid data", 400)

    return task

def replace_task_safely(task, data_dict):
    try:
        task.replace_details(data_dict)
    except KeyError as err:
        error_msg(f"Missing key: {err}", 400)


def get_task_by_id(id):
    try:
        id = int(id)
    except ValueError:
        error_msg(f"Invalid id: {id}", 400)

    task = Task.query.get(id)
    if task:
        return task
    
    error_msg(f"No task with id: {id}", 404)