from fastapi import FastAPI
from routes.todo import todo_route

app = FastAPI()
app.include_router(todo_route)



# To start the server run: fastapi dev main.py
