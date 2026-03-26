import boto3
from fastapi import FastAPI
from dotenv import load_dotenv
import os
from app.api.todos import router as todos_router
from app.api.login import router as login_router

load_dotenv()

app = FastAPI(title="Todo storage api")

app.include_router(todos_router, prefix="/todos", tags=["Todos"])
app.include_router(login_router, prefix="/auth", tags=["auth"])


@app.get("/health")
def check_health():
  return {"status": "Ok"}


@app.get("/health/dynamodb")
def check_dynamoDB_health():
  client = boto3.client('dynamodb', region_name="us-east-1", aws_access_key_id=os.getenv(
      'AWS_ACCESS_KEY'), aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))

  response = client.list_backups()
  return {"status": "healthy",
          "items_checked": len(response.get("TableNames", []))}
