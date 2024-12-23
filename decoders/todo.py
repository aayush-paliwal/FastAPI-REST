def decode_todo(doc):
    return {
        '_id': doc._id,
        'title': doc.todo,
        'timestamp': doc.timestamp
    }


def decode_todos(docs):
    return [
        decode_todo(doc) for doc in docs
    ]
