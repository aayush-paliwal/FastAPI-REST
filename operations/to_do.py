import sys
sys.path.append('./')

from connection import db_session
from model.sql_model import Todo
import decoders.todo as decode


# Create a todo
def create_todo(todo: str) -> dict:
    try:
        req = Todo(todo)
        db_session.add(req)
        db_session.commit()

        return {
            "status": "ok",
            "message": "New todo added"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
        

# Get all todos
def get_all_todos():
    try:
        res = db_session.query(Todo).all()
        docs = decode.decode_todos(res)
        return {
            'status': "ok",
            'data': docs
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


# Get one todo
def get_todo(_id: int):
    try:
        res = db_session.query(Todo).filter(Todo._id == _id).one_or_none()

        if res is not None:
            record = decode.decode_todo(res)
            
            return {
                'status': "ok",
                'data': record
            }
        else:
            return {
                'status': 'error',
                'message': f'Record with id {_id} do not exist'
            }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

# Update a todo
def update_todo(_id: int, title: str):
    try:
        res = db_session.query(Todo).filter(Todo._id == _id).one_or_none()

        if res is not None:
            res.todo = title
            db_session.commit()
            
            return {
                'status': "ok",
                'message': 'Record updated success'
            }
        else:
            return {
                'status': 'error',
                'message': f'Record with id {_id} do not exist'
            }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


# Delete a todo
def delete_todo(_id: int):
    try:
        res = db_session.query(Todo).filter(Todo._id == _id).one_or_none()

        if res is not None:
            db_session.delete(res)
            db_session.commit()
            
            return {
                'status': "ok",
                'message': 'Record deleted success'
            }
        else:
            return {
                'status': 'error',
                'message': f'Record with id {_id} do not exist'
            }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }




# res = create_todo("Learn Fast")
# res = get_all_todos()
# res = get_todo(2)
# res = update_todo(1, "Go Slow")
# res = delete_todo(1)
# print(res);