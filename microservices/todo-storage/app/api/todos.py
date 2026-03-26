
from fastapi import APIRouter, Depends
from app.authentication.jwtAuth import verify_token
from app.models.bulkTodoRequest import BulkTodoRequest
from app.db.dynamodb import table

router = APIRouter()


@router.post("/bulk", dependencies=[Depends(verify_token)])
def create_bulk_todos(request: BulkTodoRequest):
  with table.batch_writer() as batch:
    for todo in request.todos:
      todo_item = todo.model_dump()
      todo_item["created_at"] = todo.created_at.isoformat()
      batch.put_item(Item=todo_item)
    return {"message": "Todos saved successfully", "count": len(request.todos)}
