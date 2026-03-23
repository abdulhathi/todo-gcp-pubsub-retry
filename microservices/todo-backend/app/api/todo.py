
from fastapi import APIRouter
from app.services.firestore_service import save_bulk_todos, get_bulk_todos
from app.services.pubsub_service import publish_todos


router = APIRouter()


@router.get("/")
def get_todos():
  todos = get_bulk_todos()
  return {"status": "Ok", "todos": todos}


@router.post("/save")
def save_todos(payload: dict):
  todos = payload["todos"]
  save_bulk_todos(todos)
  return {"status": "saved"}


@router.post("/submit")
def submit_todos(payload: dict):
  todos = payload["todos"]

  # Step 1: Save
  save_todos(todos)

  # Step 2: Publish for async processing
  publish_todos(todos)

  return {"status": "submitted"}
