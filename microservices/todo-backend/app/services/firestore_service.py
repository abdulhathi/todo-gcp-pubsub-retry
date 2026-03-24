from google.cloud import firestore

db = firestore.Client(project="todo-firestore-fastapi")


def get_bulk_todos():
  docs = db.collection("todos").stream()
  return [doc.to_dict() for doc in docs]


def save_bulk_todos(todos: list):
  batch = db.batch()
  for todo in todos:
    ref = db.collection("todos").document(todo["id"])
    batch.set(ref, todo, merge=True)
  batch.commit()
