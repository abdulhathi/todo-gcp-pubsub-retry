from google.cloud import firestore

db = firestore.Client(project="todo-firestore-fastapi")


def get_bulk_todos():
  ref = db.collection("todos")
  todos = ref.get()
  return todos


def save_bulk_todos(todos: list):
  batch = db.batch()
  for todo in todos:
    ref = db.collection("todos").document(todo["id"])
    batch.set(ref, todo, merge=True)
  batch.commit()
