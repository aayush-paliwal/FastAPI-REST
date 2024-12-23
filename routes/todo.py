from fastapi import APIRouter
from model.pydantic_model import Todo
import all_routes
import operations.to_do as db


todo_route = APIRouter()


# Create a new Todo
@todo_route.post(all_routes.todo_create)
def new_todo(doc: Todo):
    doc = dict(doc)
    todo: str = doc['todo']
    res = db.create_todo(todo)
    return res


# Get all todos
@todo_route.get(all_routes.todo_all)
def all_todos():
    res = db.get_all_todos()
    return res


# Get one todo
@todo_route.get(all_routes.todo_one)
def one_todo(_id: int):
    res = db.get_todo(_id)
    return res


# Update todo
@todo_route.patch(all_routes.todo_update)
def update_todo(_id: int, doc: Todo):
    doc = dict(doc)
    title: str = doc['todo']
    res = db.update_todo(_id, title)
    return res


# Delete todo
@todo_route.delete(all_routes.todo_delete)
def one_todo(_id: int):
    res = db.delete_todo(_id)
    return res